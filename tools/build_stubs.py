"""Gera páginas-stub em massa a partir de uma fonte-dicionário (EC ou DAC).

Separa COBERTURA (mecânica, barata) de PROFUNDIDADE (LLM, cara): cada verbete tem
texto citável, então a página-stub é gerável por Python. O LLM enriquece depois.

- Não sobrescreve páginas já existentes (curadas) — só cria o que falta.
- Marca `status: stub` + `gerado: auto` no frontmatter (distinguível do curado).
- Gera `wiki/catalogo-<book>.md` (dá inbound aos stubs → não viram órfãos).

Especificidades por fonte:
- **EC**: 1 registro = 1 verbete com Definologia limpa → stub direto.
- **DAC**: verbete-argumentologia (-logia) com vários registros; o stub usa o
  argumento-líder e detecta o **conceito-núcleo recorrente** (n-grama mais
  frequente cuja raiz bate com o título), registrado como `alias` pesquisável
  (ex.: verbete *Inacabamentologia* → alias *Inacabamento a Maior*).

Uso:
    python tools/build_stubs.py --book ec       # stubs da Enciclopédia
    python tools/build_stubs.py --book dac      # stubs do DAC
    python tools/build_stubs.py --book dac --dry-run
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

WIKI = Path(__file__).resolve().parent.parent / "wiki"
VERB = WIKI / "verbetes"
TODAY = date.today().isoformat()

BOOK_NAME = {"ec": "Enciclopédia da Conscienciologia",
             "dac": "Dicionário de Argumentos da Conscienciologia"}
# títulos estruturais do DAC que não são conceitos
SKIP_TITLES = {"introducao", "apresentacao", "bibliografia", "sumario", "indice",
               "agradecimentos", "prefacio", "posfacio"}
STOP = {"para", "com", "que", "dos", "das", "uma", "por", "sem", "nao", "seu",
        "sua", "como", "mais", "dela", "dele", "aos", "nas", "nos", "essa",
        "esse", "esta", "este", "isto", "ainda", "toda", "todo"}


def existing_slugs() -> set[str]:
    return {f.stem for f in WIKI.rglob("*.md")
            if f.name not in ("index.md", "log.md") and "lint-reports" not in f.parts}


def clean_def(text: str) -> str:
    return re.sub(r"^\**\s*Definologia\s*:?\**\.?\s*", "", text).strip()


# ---------------------------------------------------------------- detecção DAC
def core_concept(blob: str, title: str) -> str:
    """N-grama recorrente (freq>=3) cuja raiz bate com o título → conceito-núcleo."""
    root = re.sub(r"o?logia$", "", norm(title))[:6]
    words = re.findall(r"[a-zA-Zà-ÿ]+", re.sub(r"\*+", "", blob))
    nw = [norm(w) for w in words]
    cnt = Counter()
    for k in (4, 3, 2):
        for i in range(len(nw) - k + 1):
            g = nw[i:i + k]
            if g[0] in STOP or g[-1] in STOP or not any(len(x) >= 6 for x in g):
                continue
            cnt[tuple(g)] += 1
    best, bestn = None, 0
    for g, n in cnt.items():
        if n < 3 or (root and root not in " ".join(g)):
            continue
        # prefere o mais frequente; em empate, o mais longo
        if n > bestn or (n == bestn and best and len(g) > len(best)):
            best, bestn = g, n
    if not best:
        return ""
    phrase = " ".join(best).strip()
    phrase = re.sub(r"^(o|a|os|as)\s+", "", phrase)        # tira artigo inicial
    small = {"a", "o", "e", "de", "da", "do", "das", "dos", "ao", "aos"}
    return " ".join(w if w in small else w.capitalize() for w in phrase.split())


# ---------------------------------------------------------------- conceitos
def concepts_ec():
    for r in iter_records(["ec"]):
        if not r.title:
            continue
        yield dict(title=r.title, area=r.area, aliases=[],
                   body=(f'## Definologia\n"{clean_def(r.text)}" — Extraído da '
                         f'*{BOOK_NAME["ec"]}*, verbete *{r.title}* (Waldo Vieira).'),
                   fonte=f"- `corpus/ec.json` — {BOOK_NAME['ec']}, verbete *{r.title}*.")


def concepts_dac():
    groups = defaultdict(list)
    for r in iter_records(["dac"]):
        if r.title:
            groups[r.title].append(r)
    for title, rs in groups.items():
        if norm(title) in SKIP_TITLES:
            continue
        blob = " ".join(x.text for x in rs)
        lead = max(rs[:3], key=lambda x: len(x.text))   # registro-líder
        page = lead.page or rs[0].page
        core = core_concept(blob, title)
        aliases = [core] if core and norm(core) not in norm(title) else []
        body = (f"## Definologia\n"
                f"> Verbete argumentológico do DAC (não-definicional); "
                f"definologia direta a consolidar da melhor fonte do corpus.\n\n"
                f"## Argumentologia (DAC)\n"
                f'"{lead.text.strip()}" — Extraído do *{BOOK_NAME["dac"]}*, '
                f"verbete *{title}*"
                + (f", p. {page}" if page else "") + " (Waldo Vieira).")
        fonte = (f"- `corpus/dac.json` — {BOOK_NAME['dac']}, verbete *{title}*"
                 + (f", p. {page}" if page else "") + ".")
        yield dict(title=title, area="", aliases=aliases, body=body, fonte=fonte)


# ---------------------------------------------------------------- stub render
def render(c: dict) -> str:
    slug = slugify(c["title"])
    al = f"\naliases: [{', '.join(c['aliases'])}]" if c["aliases"] else ""
    return f"""---
tipo: verbete
slug: {slug}
titulo: {c['title']}
especialidade: {c['area']}
area:{al}
status: stub
confianca: baixa
fontes_count: 1
ultima_atualizacao: {TODAY}
tags: []
verpon: false
gerado: auto
---

# {c['title']}

{c['body']}

## Conexões internas
<!-- stub: relações a extrair -->

## Fontes ingeridas
{c['fonte']}

## Log de revisões
- {TODAY}: stub gerado automaticamente a partir de `corpus/{c.get('book','')}.json`.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", choices=["ec", "dac"], default="ec")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    have = wiki_titles()
    used = existing_slugs()
    gen = concepts_ec() if a.book == "ec" else concepts_dac()
    catalog = []      # (slug, title, is_stub, aliases)
    created = skipped = aliased = 0
    seen = set()

    for c in (dict(x, book=a.book) for x in gen):
        k = norm(c["title"])
        if k in seen:
            continue
        seen.add(k)
        slug = slugify(c["title"])
        # cobertura: por título OU por algum alias já existente no wiki
        already = (k in have) or (slug in used) or any(norm(x) in have for x in c["aliases"])
        catalog.append((slug, c["title"], not already, c["aliases"]))
        if already:
            skipped += 1
            continue
        s, n = slug, 2
        while s in used:
            s, n = f"{slug}-{n}", n + 1
        used.add(s)
        c["title_slug"] = s
        if c["aliases"]:
            aliased += 1
        if not a.dry_run:
            body = render(c).replace(f"slug: {slug}\n", f"slug: {s}\n", 1)
            (VERB / f"{s}.md").write_text(body, encoding="utf-8")
        created += 1

    if not a.dry_run:
        L = [f"# Catálogo — {BOOK_NAME[a.book]}",
             f"\n> Gerado por `tools/build_stubs.py --book {a.book}` em {TODAY}. "
             f"{len(catalog)} verbetes. **(stub)** = gerado automaticamente.\n"]
        for slug, title, is_stub, al in sorted(catalog, key=lambda x: x[1]):
            tag = " **(stub)**" if is_stub else ""
            alt = f"  · _{', '.join(al)}_" if al else ""
            L.append(f"- [[{slug}]] — {title}{tag}{alt}")
        (WIKI / f"catalogo-{a.book}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"[{a.book}] stubs criados: {created}  ·  já existentes: {skipped}  ·  "
          f"com alias-conceito: {aliased}  ·  catálogo: wiki/catalogo-{a.book}.md")


if __name__ == "__main__":
    main()
