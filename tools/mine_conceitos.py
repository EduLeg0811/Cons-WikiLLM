"""Minera CONCEITOS contextuais embutidos em verbetes argumentológicos (DAC).

Conceitos relevantes/originais (frequentemente verpons) aparecem na prosa do DAC
sem headword próprio — caem no vão entre o regime-dicionário (enumerar-primeiro)
e o regime-discursivo (AGENTS §5.1). Hoje o `build_stubs.py` detecta o conceito-
núcleo (`core_concept`) mas o rebaixa a `alias` do verbete-`-logia`. Esta ferramenta
o **promove a candidato**: emite um backlog para o curador/LLM decidir o que vira
página própria em `wiki/conceitos/` (tipo: conceito, definicao: contextual).

Separa COBERTURA (detecção barata, Python) de PROFUNDIDADE/RELEVÂNCIA (julgamento):
por padrão só sugere; `--emit-stubs` gera stubs em `conceitos/` (usar com parcimônia,
senão recria o problema de massa de stubs irrelevantes que esta camada quer evitar).

Uso:
    python tools/mine_conceitos.py                 # backlog -> wiki/lacunas-conceitos.md
    python tools/mine_conceitos.py --emit-stubs    # também cria stubs em conceitos/
"""
from __future__ import annotations
import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from corpus import iter_records
from inventory import norm, slugify, wiki_titles
from build_stubs import BOOK_NAME, SKIP_TITLES, core_concept

WIKI = Path(__file__).resolve().parent.parent / "wiki"
CONCEITOS = WIKI / "conceitos"
BACKLOG = WIKI / "lacunas-conceitos.md"
TODAY = date.today().isoformat()

# Palavras-função: se um termo em itálico COMEÇA ou TERMINA com uma delas, é
# quase sempre fragmento de prosa em ênfase, não conceito ("O ato de", "Segundo a").
_EDGE_STOP = {"a", "o", "os", "as", "e", "de", "da", "do", "das", "dos", "ao", "aos",
              "na", "no", "nas", "nos", "em", "com", "por", "para", "sem", "sob",
              "ate", "entre", "que", "se", "ou", "the", "of", "segundo", "quanto",
              "conforme", "tal", "tao", "como", "mais", "menos", "muito"}
_ITAL = re.compile(r"\*([^*]{4,60}?)\*")


def existing_slugs() -> set[str]:
    return {f.stem for f in WIKI.rglob("*.md")
            if f.name not in ("index.md", "log.md") and "lint-reports" not in f.parts}


def find_passage(records, core: str):
    """Registro (argumento) mais focado que contém o conceito-núcleo."""
    nc = norm(core)
    hits = [r for r in records if nc in norm(r.text)]
    return min(hits, key=lambda x: len(x.text)) if hits else None


# prefixos que denunciam fragmento de prosa, não conceito (artigos/preposições)
_PREP = {"da", "do", "de", "das", "dos", "e", "a", "o", "os", "as", "ao", "aos",
         "na", "no", "nas", "nos", "em", "com", "por", "para"}


def candidates(book: str = "dac"):
    """Gera (conceito, slug, logia_title, logia_slug, page, passagem).

    Filtros baratos contra ruído do heurístico (o julgamento fino fica p/ curadoria):
    descarta o conceito-núcleo que (i) repete o título, (ii) é outra `-logia`
    (vira headword próprio, não conceito contextual), (iii) começa por preposição.
    """
    groups = defaultdict(list)
    for r in iter_records([book]):
        if r.title:
            groups[r.title].append(r)
    for title, rs in groups.items():
        if norm(title) in SKIP_TITLES:
            continue
        blob = " ".join(x.text for x in rs)
        core = core_concept(blob, title)
        if not core or norm(core) in norm(title):
            continue
        nc = norm(core)
        if nc.endswith("logia") or nc.split()[0] in _PREP:
            continue
        psg = find_passage(rs, core)
        page = (psg.page if psg else "") or (rs[0].page if rs else "")
        yield dict(conceito=core, slug=slugify(core), logia_title=title,
                   logia_slug=slugify(title), page=page,
                   passagem=(psg.text.strip() if psg else ""))


def stub(c: dict) -> str:
    return f"""---
tipo: conceito
slug: {c['slug']}
titulo: {c['conceito']}
especialidade: {c['logia_title']}
area:
derivado_de: {c['logia_slug']}
definicao: contextual
status: stub
confianca: baixa
fontes_count: 1
ultima_atualizacao: {TODAY}
tags: []
verpon: false
gerado: auto
---

# {c['conceito']}

## Definologia
> Conceito de **origem contextual** (sem Definologia *ipsis litteris* no headword);
> síntese a redigir a partir da *Passagem-fonte*.

## Passagem-fonte
"{c['passagem']}" — Extraído do *{BOOK_NAME['dac']}*, verbete *{c['logia_title']}*\
{f', p. {c["page"]}' if c['page'] else ''} (Waldo Vieira).

## Conexões internas
- [[{c['logia_slug']}]] — especialidade de origem (verbete-hub)

## Fontes ingeridas
- `corpus/dac.json` — {BOOK_NAME['dac']}, verbete *{c['logia_title']}*\
{f', p. {c["page"]}' if c['page'] else ''}.

## Log de revisões
- {TODAY}: stub de conceito contextual minerado de `corpus/dac.json` (candidato a verpon/original).
"""


def _good_term(words: list[str]) -> bool:
    if not (2 <= len(words) <= 5):
        return False
    if words[0] in _EDGE_STOP or words[-1] in _EDGE_STOP:   # fragmento de prosa
        return False
    if not any(len(w) >= 6 for w in words):                # exige 1 palavra "densa"
        return False
    return True


def neologism_candidates(min_freq: int = 3, min_sources: int = 2):
    """Neologismos em itálico (*termo*) recorrentes em ≥N fontes, sem página.

    Sinal tipográfico que o autor usa p/ conceitos cunhados — generaliza a TODAS
    as fontes (vs. o n-grama do `core_concept`, preso à estrutura -logia do DAC).
    Ranking por convergência (nº de fontes) e frequência.
    """
    freq: Counter = Counter()
    books: dict[str, set] = defaultdict(set)
    disp: dict[str, str] = {}
    psg: dict[str, tuple] = {}      # k -> (len_texto, excerpt, book_name, book_id, page)
    for r in iter_records():
        for m in _ITAL.finditer(r.text):
            raw = m.group(1).strip(" ,.;:")
            if not re.fullmatch(r"[A-Za-zà-ÿ ]+", raw):
                continue
            words = [norm(w) for w in raw.split()]
            if not _good_term(words):
                continue
            k = norm(raw)
            if len(k) < 8:
                continue
            freq[k] += 1
            books[k].add(r.book)
            disp.setdefault(k, raw)
            cur = psg.get(k)
            if cur is None or len(r.text) < cur[0]:
                psg[k] = (len(r.text), r.text.strip(), r.book_name, r.book, r.page)
    out = []
    for k, n in freq.items():
        if n < min_freq or len(books[k]) < min_sources:
            continue
        _, excerpt, bname, bid, page = psg[k]
        out.append(dict(conceito=disp[k], slug=slugify(disp[k]), freq=n,
                        n_fontes=len(books[k]), fontes=sorted(books[k]),
                        book_name=bname, book_id=bid, page=page, passagem=excerpt))
    out.sort(key=lambda c: (-c["n_fontes"], -c["freq"]))
    return out


def write_neologisms(a, have: set[str], used: set[str]):
    novos, ja, seen = [], 0, set()
    for c in neologism_candidates(a.min_freq, a.min_fontes):
        k = norm(c["conceito"])
        if k in seen:
            continue
        seen.add(k)
        if k in have or c["slug"] in used:    # já é página/alias -> vira nota, não candidato
            ja += 1
            continue
        novos.append(c)

    L = ["# Backlog de conceitos — neologismos em itálico (todas as fontes)",
         f"\n> Gerado por `tools/mine_conceitos.py --neologisms` em {TODAY}. "
         f"{len(novos)} candidatos (freq≥{a.min_freq}, ≥{a.min_fontes} fontes; já cobertos/aliases: {ja}).",
         "> Sinal: termos *em itálico* recorrentes **sem página própria**, ordenados por "
         "convergência (nº de fontes) e frequência.",
         "> Promova os relevantes para `wiki/conceitos/` (`tipo: conceito`). "
         "**Atenção:** alguns já existem sob outro nome → viram **alias**, não página nova.\n"]
    for c in novos:
        page = f", p. {c['page']}" if c["page"] else ""
        L.append(f"- **{c['conceito']}**  `{c['slug']}` — {c['n_fontes']} fontes · {c['freq']} ocorr.")
        if c["passagem"]:
            ex = c["passagem"][:280] + ("…" if len(c["passagem"]) > 280 else "")
            L.append(f"  > \"{ex}\" — {c['book_name']}{page}.")
    BACKLOG.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[neologisms] candidatos: {len(novos)}  ·  já cobertos/aliases: {ja}  ·  "
          f"backlog: {BACKLOG.relative_to(WIKI.parent)}")


def write_dac(a, have: set[str], used: set[str]):
    novos, ja, emitidos, seen = [], 0, 0, set()
    for c in candidates("dac"):
        k = norm(c["conceito"])
        if k in seen:
            continue
        seen.add(k)
        if k in have or c["slug"] in used:    # já é página/alias (ex.: inacabamento-a-maior)
            ja += 1
            continue
        novos.append(c)
        if a.emit_stubs:
            CONCEITOS.mkdir(exist_ok=True)
            (CONCEITOS / f"{c['slug']}.md").write_text(stub(c), encoding="utf-8")
            used.add(c["slug"])
            emitidos += 1

    novos.sort(key=lambda c: c["logia_title"].lower())
    L = ["# Backlog de conceitos contextuais — embutidos no DAC (core_concept)",
         f"\n> Gerado por `tools/mine_conceitos.py` em {TODAY}. {len(novos)} candidatos "
         f"(já promovidos/cobertos: {ja}).",
         "> Conceitos-núcleo embutidos em verbetes argumentológicos, **sem página própria**. "
         "Promova os relevantes para `wiki/conceitos/` (`tipo: conceito`, `definicao: contextual`).\n"]
    for c in novos:
        page = f", p. {c['page']}" if c["page"] else ""
        L.append(f"- **{c['conceito']}**  `{c['slug']}` — de [[{c['logia_slug']}]] "
                 f"(*{c['logia_title']}*{page})")
        if c["passagem"]:
            ex = c["passagem"][:300] + ("…" if len(c["passagem"]) > 300 else "")
            L.append(f"  > \"{ex}\"")
    BACKLOG.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[dac] candidatos novos: {len(novos)}  ·  já cobertos: {ja}  ·  "
          f"stubs emitidos: {emitidos}  ·  backlog: {BACKLOG.relative_to(WIKI.parent)}")


def main():
    ap = argparse.ArgumentParser(description="Minera conceitos contextuais (verpons/originais).")
    ap.add_argument("--neologisms", action="store_true",
                    help="modo neologismos em itálico, TODAS as fontes (recomendado)")
    ap.add_argument("--book", default="dac", choices=["dac"],
                    help="modo DAC: conceito-núcleo embutido via core_concept")
    ap.add_argument("--min-freq", type=int, default=3, help="freq mínima (modo neologisms)")
    ap.add_argument("--min-fontes", type=int, default=2, help="nº mínimo de fontes (modo neologisms)")
    ap.add_argument("--emit-stubs", action="store_true",
                    help="modo DAC: cria stubs em wiki/conceitos/ (usar com parcimônia)")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    have = wiki_titles()           # títulos/slugs/aliases já cobertos
    used = existing_slugs()
    if a.neologisms:
        write_neologisms(a, have, used)
    else:
        write_dac(a, have, used)


if __name__ == "__main__":
    main()
