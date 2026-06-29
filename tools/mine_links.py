"""Mineração de relações por co-ocorrência (densifica a malha [[...]]).

Varre a Definologia de cada página-stub e detecta menções a outros conceitos
já existentes na base (por título/slug, com fronteira de palavra). Preenche a
seção `## Conexões internas` dos stubs — que nasceram sem relações.

Conservador por design: só toca páginas `status: stub` cuja seção de conexões
ainda é o placeholder; nunca altera páginas curadas nem cria conceitos.

Uso:
    python tools/mine_links.py --dry-run   # estatísticas, não grava
    python tools/mine_links.py             # aplica nos stubs
    python tools/mine_links.py -n 12        # cap de links por página (def. 10)
"""
from __future__ import annotations
import argparse
import re
import sys
import unicodedata
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
PLACEHOLDER = "<!-- stub: relações a extrair -->"
MIN_LEN = 6          # ignora surfaces curtas/genéricas (soma, vida…)
MAX_FREQ = 200       # alvo que casaria em >200 stubs é genérico demais → descartado
STOP = {"conscienciologia", "consciencia", "conscienciologica", "evolucao",
        "pessoal", "humana", "cosmoetica", "qualidade", "condicao", "estado",
        "verbete", "efeito", "conhecimento", "analise", "interesse", "palavra",
        "conceito", "vida-humana", "vida humana", "autovivencia", "pararrealidade",
        "exemplo", "natureza", "realidade", "pessoa", "tecnica", "conscin",
        "momento-evolutivo", "momento evolutivo", "definologia"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def load_pages():
    pages = {}
    for f in WIKI.rglob("*.md"):
        if f.name in ("index.md", "log.md") or f.name.startswith("catalogo") \
                or "lint-reports" in f.parts:
            continue
        t = f.read_text(encoding="utf-8")
        fm = {}
        m = re.search(r"^titulo:\s*(.+)$", t, re.M)
        fm["titulo"] = m.group(1).strip() if m else f.stem
        s = re.search(r"^status:\s*(\S+)", t, re.M)
        fm["status"] = s.group(1) if s else "?"
        pages[f.stem] = {"path": f, "text": t, **fm}
    return pages


def build_matcher(pages):
    """Regex única de todas as surfaces -> slug. Surfaces: título e slug-words."""
    surf = {}  # surface normalizada -> slug
    for slug, p in pages.items():
        cands = {norm(re.sub(r"\(.*", "", p["titulo"])), norm(slug.replace("-", " "))}
        for c in cands:
            c = c.strip()
            if len(c) >= MIN_LEN and c not in STOP:
                surf.setdefault(c, slug)
    # surfaces mais longas primeiro (evita match parcial)
    keys = sorted(surf, key=len, reverse=True)
    rx = re.compile(r"\b(" + "|".join(re.escape(k) for k in keys) + r")\b")
    return rx, surf


def definologia(text: str) -> str:
    """Texto minerável: seções Definologia + Argumentologia (DAC), sem a citação."""
    parts = re.findall(r"## (?:Definologia|Argumentologia[^\n]*)\n(.+?)(?=\n## |\Z)",
                       text, re.S)
    out = []
    for p in parts:
        p = re.sub(r"^>.*$", "", p, flags=re.M)             # tira nota boilerplate
        out.append(re.split(r"—\s*Extra[íi]do", p)[0])      # tira a citação
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("-n", type=int, default=10, help="cap de links por página")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    pages = load_pages()
    rx, surf = build_matcher(pages)
    targets = [s for s, p in pages.items()
               if p["status"] == "stub" and PLACEHOLDER in p["text"]]

    # passagem 1: matches crus por stub + frequência global de cada alvo
    from collections import Counter
    raw = {}
    freq = Counter()
    for slug in targets:
        seen = []
        for m in rx.finditer(norm(definologia(pages[slug]["text"]))):
            tgt = surf[m.group(1)]
            if tgt != slug and tgt not in seen:
                seen.append(tgt)
        raw[slug] = seen
        freq.update(seen)
    generic = {t for t, n in freq.items() if n > MAX_FREQ}

    # passagem 2: aplica, descartando alvos genéricos demais, com cap
    changed = total_links = zero = 0
    dist = []
    for slug in targets:
        p = pages[slug]
        found = [t for t in raw[slug] if t not in generic][:a.n]
        dist.append(len(found))
        if not found:
            zero += 1
            continue
        bullets = "\n".join(f"- [[{t}]] — {pages[t]['titulo']}" for t in found)
        new = p["text"].replace(PLACEHOLDER, bullets)
        total_links += len(found)
        changed += 1
        if not a.dry_run:
            p["path"].write_text(new, encoding="utf-8")

    n = len(targets)
    print(f"stubs alvo: {n}")
    print(f"com ≥1 relação: {changed}  ·  sem relação: {zero}")
    print(f"links criados: {total_links}  ·  média/stub: {total_links/max(n,1):.1f}")
    if a.dry_run and dist:
        from collections import Counter
        print("distribuição (nº de links -> nº de stubs):",
              dict(sorted(Counter(dist).items())))


if __name__ == "__main__":
    main()
