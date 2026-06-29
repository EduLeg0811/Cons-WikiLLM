"""Sincroniza as contagens de fontes `(N)` do wiki/index.md com o `fontes_count`
real de cada página (lido do frontmatter). Preserva descrições e ordem.

Uso: python tools/sync_index_counts.py        # aplica
     python tools/sync_index_counts.py --check # só relata divergências
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
INDEX = WIKI / "index.md"
_FC = re.compile(r"^fontes_count:\s*(\d+)", re.M)
_SLUG = re.compile(r"\[\[([^\]|]+?)\]\]")
_COUNT = re.compile(r"\((\d+)\)\s*$")


def fontes_count(slug: str) -> int | None:
    for f in WIKI.rglob(f"{slug}.md"):
        m = _FC.search(f.read_text(encoding="utf-8"))
        return int(m.group(1)) if m else None
    return None


def main():
    check = "--check" in sys.argv
    out, changed = [], 0
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        ms, mc = _SLUG.search(line), _COUNT.search(line)
        if ms and mc:
            real = fontes_count(ms.group(1).strip())
            if real is not None and real != int(mc.group(1)):
                changed += 1
                print(f"{'~' if check else '*'} {ms.group(1)}: ({mc.group(1)}) -> ({real})")
                if not check:
                    line = line[:mc.start()] + f"({real})"
        out.append(line)
    if not check and changed:
        INDEX.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{changed} linha(s) {'divergente(s)' if check else 'atualizada(s)'}.")


if __name__ == "__main__":
    main()
