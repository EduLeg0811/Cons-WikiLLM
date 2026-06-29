"""Busca automática de convergência (2ª fonte) por conceito — acelera o tier.

Para cada página-stub de uma especialidade (ou lista de slugs), roda BM25 no
corpus, **exclui a fonte de origem** (a obra que já cita o verbete) e devolve os
melhores candidatos a 2ª fonte, com citação pronta e marca de força. O LLM então
só escolhe a melhor e redige — sem buscar concept a concept.

Uso:
    python tools/converge.py --esp Recexologia          # todos os stubs da esp.
    python tools/converge.py --slug melex,desperto       # conceitos avulsos
    python tools/converge.py --esp Proexologia -o cand.txt
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

from search import search

WIKI = Path(__file__).resolve().parent.parent / "wiki"
STRONG = 14.0   # score acima do qual o candidato é provavelmente bom
# trechos não-definicionais (listas, taxonomias, enumerações) — baixo valor de convergência
NOISE = re.compile(r"taxolog|taxonom|^\s*\**\s*(sinon[íi]mia|anton[íi]mia|"
                   r"enumeraciologia|casu[íi]stica|antonimologia)\b", re.I)


def is_noise(r) -> bool:
    return bool(NOISE.search(r.title or "")) or bool(NOISE.match(r.text or ""))


def pages_by_esp(esp: str) -> list[Path]:
    out = []
    for f in WIKI.rglob("*.md"):
        if "lint-reports" in f.parts:
            continue
        t = f.read_text(encoding="utf-8")
        if re.search(r"^status:\s*stub", t, re.M) and \
           re.search(rf"^especialidade:\s*{re.escape(esp)}\s*$", t, re.M):
            out.append(f)
    return out


def info(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    g = lambda k: (re.search(rf"^{k}:\s*(.+)$", t, re.M) or [None, ""])[1].strip()
    src = set(re.findall(r"corpus/(\w+)\.json", t))   # obras já citadas (excluir)
    al = re.search(r"^aliases:\s*\[(.*?)\]", t, re.M)
    defin = (re.search(r"## Definologia\n\"?(.+?)[\"\n]", t, re.S) or [None, ""])[1]
    return {"slug": g("slug"), "titulo": g("titulo"),
            "query": g("titulo") + (" " + al.group(1) if al else ""),
            "src": src, "defin": defin.strip()[:110]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--esp", help="especialidade (filtra stubs)")
    ap.add_argument("--slug", help="slugs avulsos, separados por vírgula")
    ap.add_argument("-n", type=int, default=2, help="candidatos por conceito")
    ap.add_argument("-o", help="grava num arquivo (UTF-8) em vez do stdout")
    a = ap.parse_args()

    if a.slug:
        paths = []
        for s in a.slug.split(","):
            hit = list(WIKI.rglob(f"{s.strip()}.md"))
            paths += hit
    else:
        paths = pages_by_esp(a.esp)

    L = []
    strong = 0
    for p in sorted(paths):
        d = info(p)
        hits = [h for h in search(d["query"], None, 12)
                if h[1].book not in d["src"] and not is_noise(h[1])][:a.n]
        L.append(f"\n### {d['slug']}  ·  {d['titulo']}")
        L.append(f"def: {d['defin']}")
        if not hits:
            L.append("  (sem candidato fora da fonte de origem)")
            continue
        for i, (score, r) in enumerate(hits):
            star = "★" if score >= STRONG else " "
            if i == 0 and score >= STRONG:
                strong += 1
            pg = f", p. {r.page}" if r.page else ""
            L.append(f"  {star} [{score:5.1f}] {r.book_name} — {r.title or '—'}{pg}")
            L.append(f"      {r.text[:240]}")

    head = (f"# Candidatos a convergência — {a.esp or a.slug}\n"
            f"{len(paths)} conceitos · {strong} com candidato forte (★, score≥{STRONG})\n")
    out = head + "\n".join(L) + "\n"
    if a.o:
        Path(a.o).write_text(out, encoding="utf-8")
        print(f"[gravado em {a.o}] {len(paths)} conceitos, {strong} fortes")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
