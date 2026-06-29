"""Inventário de conceitos das fontes-dicionário vs. cobertura do wiki.

Enumera os verbetes/títulos das fontes estruturadas (Enciclopédia, DAC, …) —
que já são dicionários de conceitos pré-segmentados — e cruza com os slugs já
existentes no wiki, produzindo um backlog medível de cobertura/lacunas.

Doutrina (AGENTS §5.1, revisada): para fontes-dicionário o ingest é
*enumerar-primeiro*; a curadoria decide profundidade (tier), não inclusão.

Uso:
    python tools/inventory.py              # resumo de cobertura por fonte
    python tools/inventory.py --book ec    # lista lacunas de uma fonte
    python tools/inventory.py --gaps ec    # só os títulos ainda SEM página
"""
from __future__ import annotations
import argparse
import re
import sys
import unicodedata
from pathlib import Path

from corpus import CORPUS_DIR, books, iter_records

WIKI = Path(__file__).resolve().parent.parent / "wiki"
# fontes-dicionário: 1 título = 1 conceito segmentado
DICT_BOOKS = ["ec", "dac"]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\(.*", "", s).strip()


def slugify(title: str) -> str:
    s = unicodedata.normalize("NFKD", title.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def wiki_titles() -> set[str]:
    """Conjunto de títulos+slugs normalizados já presentes no wiki."""
    have = set()
    for f in WIKI.rglob("*.md"):
        if f.name in ("index.md", "log.md") or "lint-reports" in f.parts:
            continue
        t = f.read_text(encoding="utf-8")
        have.add(norm(f.stem))
        m = re.search(r"^titulo:\s*(.+)$", t, re.M)
        if m:
            have.add(norm(m.group(1)))
        for a in re.findall(r"^aliases:\s*\[(.*?)\]", t, re.M):
            for al in a.split(","):
                have.add(norm(al))
    return have


def inventory(book: str, have: set[str]):
    rows = []
    for r in iter_records([book]):
        if not r.title:
            continue
        rows.append((r.title, r.area, norm(r.title) in have))
    # dedup por título normalizado preservando ordem
    seen, uniq = set(), []
    for ti, area, cov in rows:
        k = norm(ti)
        if k in seen:
            continue
        seen.add(k)
        uniq.append((ti, area, cov))
    return uniq


def main():
    ap = argparse.ArgumentParser(description="Inventário de cobertura conceitual.")
    ap.add_argument("--book", help="detalhar uma fonte (lista verbetes + cobertura)")
    ap.add_argument("--gaps", help="listar só os títulos SEM página de uma fonte")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    have = wiki_titles()
    meta = books()

    target = a.gaps or a.book
    if target:
        inv = inventory(target, have)
        cov = sum(1 for _, _, c in inv if c)
        name = meta.get(target, {}).get("book_name", target)
        print(f"# {name} — {cov}/{len(inv)} cobertos ({100*cov/max(len(inv),1):.1f}%)\n")
        for ti, area, c in inv:
            if a.gaps and c:
                continue
            mark = "✓" if c else " "
            print(f"[{mark}] {slugify(ti):<40} {ti}  ·  {area}")
        return

    print("# Inventário de cobertura (fontes-dicionário)\n")
    print(f"{'fonte':6} {'conceitos':>10} {'no wiki':>8} {'cobertura':>10}")
    for b in DICT_BOOKS:
        inv = inventory(b, have)
        cov = sum(1 for _, _, c in inv if c)
        print(f"{b:6} {len(inv):>10} {cov:>8} {100*cov/max(len(inv),1):>9.1f}%")


if __name__ == "__main__":
    main()
