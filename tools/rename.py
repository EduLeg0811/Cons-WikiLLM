"""Renomeia o título de um conceito a partir de um único ponto de edição.

O `slug` (ID) é imutável e preserva todos os links [[slug]]. Só o nome de
exibição (`titulo:` + `# H1`) muda. O script:
  1. atualiza `titulo:` no frontmatter e o cabeçalho `# H1` da página;
  2. (opcional) guarda o nome antigo em `aliases:` para não se perder;
  3. varre a wiki por menções LITERAIS do nome antigo em prosa e as lista
     para revisão manual — NÃO substitui sozinho, porque citações entre
     aspas são ipsis litteris (regra do AGENTS.md §2.7) e não podem mudar;
  4. roda o lint estrutural ao final.

Uso:
    python tools/rename.py <slug> --titulo "Novo Nome" [--add-alias]
    python tools/rename.py <slug> --titulo "Novo Nome" --apply-prose  # também troca na prosa não-citada
"""
from __future__ import annotations
import argparse
import re
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
WIKI = TOOLS.parent / "wiki"


def find_page(slug: str) -> Path | None:
    for f in WIKI.rglob(f"{slug}.md"):
        if "lint-reports" not in f.parts:
            return f
    return None


def get_field(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.*)$", text[: text.find("\n---", 3)], re.M)
    return m.group(1).strip() if m else None


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Renomeia o título de um conceito (slug imutável).")
    ap.add_argument("slug")
    ap.add_argument("--titulo", required=True, help="Novo nome de exibição")
    ap.add_argument("--add-alias", action="store_true", help="Guarda o nome antigo em aliases:")
    ap.add_argument("--apply-prose", action="store_true",
                    help="Também substitui o nome antigo na prosa NÃO-citada (linhas sem aspas)")
    a = ap.parse_args()

    page = find_page(a.slug)
    if not page:
        sys.exit(f"[erro] página não encontrada para slug '{a.slug}'")

    text = page.read_text(encoding="utf-8")
    old = get_field(text, "titulo")
    if old is None:
        sys.exit(f"[erro] '{a.slug}' não tem campo 'titulo:' no frontmatter")
    if old == a.titulo:
        sys.exit(f"[nada a fazer] título já é '{a.titulo}'")

    # 1. frontmatter titulo: + 2. H1
    new = re.sub(r"^titulo:[^\n]*$", f"titulo: {a.titulo}", text, count=1, flags=re.M)
    new = re.sub(rf"^#\s+{re.escape(old)}[ \t]*$", f"# {a.titulo}", new, count=1, flags=re.M)
    if new == text:
        print("[aviso] titulo/H1 não casaram exatamente — verifique a página manualmente.")

    # 3. aliases
    if a.add_alias:
        m = re.search(r"^aliases:\s*\[(.*)\]\s*$", new, re.M)
        if m:
            items = [x.strip() for x in m.group(1).split(",") if x.strip()]
            if old not in items:
                items.append(old)
                new = new[: m.start()] + f"aliases: [{', '.join(items)}]" + new[m.end():]
        else:  # cria o campo logo após titulo:
            new = re.sub(r"^(titulo:.*)$", rf"\1\naliases: [{old}]", new, count=1, flags=re.M)

    page.write_text(new, encoding="utf-8")
    print(f"✓ {page.relative_to(WIKI.parent)}: '{old}' → '{a.titulo}'" + (" (+alias)" if a.add_alias else ""))

    # 4. varredura de prosa em toda a wiki
    print(f"\nMenções literais de '{old}' na prosa (revisão manual):")
    hits = 0
    for f in WIKI.rglob("*.md"):
        if "lint-reports" in f.parts:
            continue
        lines = f.read_text(encoding="utf-8").splitlines()
        changed = False
        for i, line in enumerate(lines, 1):
            if old not in line or line.strip().startswith(("titulo:", "aliases:", "#", "- [[")):
                continue
            quoted = '"' in line or "Extraído de" in line
            tag = " [CITAÇÃO — não alterar]" if quoted else ""
            print(f"  {f.relative_to(WIKI.parent)}:{i}{tag}")
            print(f"      {line.strip()[:110]}")
            hits += 1
            if a.apply_prose and not quoted:
                lines[i - 1] = line.replace(old, a.titulo)
                changed = True
        if changed:
            f.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"    → prosa substituída em {f.relative_to(WIKI.parent)}")
    if not hits:
        print("  (nenhuma)")
    elif not a.apply_prose:
        print("\n  Use --apply-prose para substituir automaticamente as linhas SEM citação.")

    # 5. lint
    print("\n--- lint ---")
    sys.stdout.flush()
    subprocess.run([sys.executable, str(TOOLS / "lint.py"), "--no-write"], cwd=TOOLS)


if __name__ == "__main__":
    main()
