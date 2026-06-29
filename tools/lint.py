"""Health-check estrutural do wiki (parte algorítmica do lint do AGENTS §5.3).

Verifica, sem LLM: links [[...]] quebrados, páginas órfãs (sem inbound links),
frontmatter obrigatório ausente, slug divergente do nome do arquivo, slugs
duplicados, e estatísticas de status/confiança. Gera relatório em
wiki/lint-reports/YYYY-MM-DD.md.

Uso: python tools/lint.py            # imprime + grava relatório
     python tools/lint.py --no-write # só imprime
"""
from __future__ import annotations
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
REQUIRED = ["tipo", "slug", "titulo", "status", "confianca", "fontes_count"]
LINK = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
# tipos cujas páginas naturalmente têm poucos/zero inbound links (não são "órfãs problema")
ORPHAN_EXEMPT = {"obra"}


def frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def main():
    pages = {}  # slug(basename) -> {path, fm, links, body}
    for f in WIKI.rglob("*.md"):
        if f.name in ("index.md", "log.md") or f.name.startswith("catalogo") \
                or "lint-reports" in f.parts:
            continue
        text = f.read_text(encoding="utf-8")
        base = f.stem
        pages[base] = {
            "path": f.relative_to(WIKI.parent),
            "fm": frontmatter(text),
            "links": {m.group(1).strip() for m in LINK.finditer(text)},
        }

    slugs = set(pages)
    broken, orphans, fm_missing, slug_mismatch = [], [], [], []
    dup = defaultdict(list)
    inbound = Counter()

    for base, p in pages.items():
        dup[base].append(str(p["path"]))
        for l in p["links"]:
            if l in slugs:
                inbound[l] += 1
            else:
                broken.append((base, l))
        miss = [k for k in REQUIRED if k not in p["fm"]]
        if miss:
            fm_missing.append((base, miss))
        fmslug = p["fm"].get("slug")
        if fmslug and fmslug != base:
            slug_mismatch.append((base, fmslug))

    for base, p in pages.items():
        if inbound[base] == 0 and p["fm"].get("tipo") not in ORPHAN_EXEMPT \
                and p["fm"].get("status") != "stub":
            orphans.append(base)

    status = Counter(p["fm"].get("status", "?") for p in pages.values())
    conf = Counter(p["fm"].get("confianca", "?") for p in pages.values())
    tipo = Counter(p["fm"].get("tipo", "?") for p in pages.values())

    L = []
    w = L.append
    w(f"# Lint-report — {date.today().isoformat()}")
    w(f"\n**Páginas de conteúdo:** {len(pages)}  ·  "
      f"tipos: {dict(tipo)}")
    w(f"\n**Status:** {dict(status)}  ·  **Confiança:** {dict(conf)}")

    w(f"\n## Links quebrados ({len(broken)})")
    w("\n".join(f"- `{a}` → `[[{b}]]`" for a, b in broken) or "_nenhum_ ✓")

    w(f"\n## Páginas órfãs — sem inbound links ({len(orphans)})")
    w("\n".join(f"- [[{o}]] ({pages[o]['fm'].get('tipo','?')})" for o in sorted(orphans)) or "_nenhuma_ ✓")

    w(f"\n## Frontmatter incompleto ({len(fm_missing)})")
    w("\n".join(f"- `{a}`: faltam {m}" for a, m in fm_missing) or "_nenhum_ ✓")

    w(f"\n## Slug ≠ nome do arquivo ({len(slug_mismatch)})")
    w("\n".join(f"- `{a}`: slug=`{s}`" for a, s in slug_mismatch) or "_nenhum_ ✓")

    dups = {k: v for k, v in dup.items() if len(v) > 1}
    w(f"\n## Slugs duplicados ({len(dups)})")
    w("\n".join(f"- `{k}`: {v}" for k, v in dups.items()) or "_nenhum_ ✓")

    rascunhos = sorted(b for b, p in pages.items() if p["fm"].get("status") == "rascunho")
    w(f"\n## Páginas em rascunho ({len(rascunhos)})")
    w(", ".join(f"[[{r}]]" for r in rascunhos) or "_nenhuma_")

    report = "\n".join(L) + "\n"
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(report)
    if "--no-write" not in sys.argv:
        out = WIKI / "lint-reports" / f"{date.today().isoformat()}.md"
        out.parent.mkdir(exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"[gravado em {out.relative_to(WIKI.parent)}]")


if __name__ == "__main__":
    main()
