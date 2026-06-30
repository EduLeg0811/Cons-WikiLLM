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
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from corpus import iter_records
from inventory import norm, slugify, wiki_titles
from build_stubs import BOOK_NAME, SKIP_TITLES, core_concept

WIKI = Path(__file__).resolve().parent.parent / "wiki"
CONCEITOS = WIKI / "conceitos"
BACKLOG = WIKI / "lacunas-conceitos.md"
TODAY = date.today().isoformat()


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


def main():
    ap = argparse.ArgumentParser(description="Minera conceitos contextuais (DAC).")
    ap.add_argument("--book", default="dac", choices=["dac"])
    ap.add_argument("--emit-stubs", action="store_true",
                    help="cria stubs em wiki/conceitos/ (usar com parcimônia)")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    have = wiki_titles()           # títulos/slugs/aliases já cobertos
    used = existing_slugs()
    novos, ja, emitidos = [], 0, 0
    seen = set()

    for c in candidates(a.book):
        k = norm(c["conceito"])
        if k in seen:
            continue
        seen.add(k)
        # já é página/alias? (ex.: inacabamento-a-maior, já promovido) -> não sugere
        if k in have or c["slug"] in used:
            ja += 1
            continue
        novos.append(c)
        if a.emit_stubs:
            CONCEITOS.mkdir(exist_ok=True)
            (CONCEITOS / f"{c['slug']}.md").write_text(stub(c), encoding="utf-8")
            used.add(c["slug"])
            emitidos += 1

    novos.sort(key=lambda c: c["logia_title"].lower())
    L = [f"# Backlog de conceitos contextuais — candidatos ({a.book.upper()})",
         f"\n> Gerado por `tools/mine_conceitos.py` em {TODAY}. {len(novos)} candidatos "
         f"(já promovidos/cobertos: {ja}).",
         "> Conceitos-núcleo embutidos em verbetes argumentológicos, **sem página própria**. "
         "Promova os relevantes para `wiki/conceitos/` (`tipo: conceito`, `definicao: contextual`).\n"]
    for c in novos:
        page = f", p. {c['page']}" if c["page"] else ""
        L.append(f"- **{c['conceito']}**  `{c['slug']}` — de [[{c['logia_slug']}]] "
                 f"(*{c['logia_title']}*{page})")
        if c["passagem"]:
            excerpt = c["passagem"][:300] + ("…" if len(c["passagem"]) > 300 else "")
            L.append(f"  > \"{excerpt}\"")
    BACKLOG.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"[{a.book}] candidatos novos: {len(novos)}  ·  já cobertos: {ja}  ·  "
          f"stubs emitidos: {emitidos}  ·  backlog: {BACKLOG.relative_to(WIKI.parent)}")


if __name__ == "__main__":
    main()
