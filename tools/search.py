"""Busca BM25 sobre o corpus — a ferramenta que o LLM chama no ingest/query.

Uso:
    python tools/search.py "holopensene domiciliar"
    python tools/search.py "estado vibracional" --book ec,tnp -n 8
    python tools/search.py "proexis" --full        # texto integral dos trechos

O índice tokenizado é cacheado em tools/.search_cache.pkl e reconstruído
automaticamente quando algum JSON do corpus muda (assinatura por mtime).
BM25 implementado em Python puro — sem dependências externas.
"""
from __future__ import annotations
import argparse
import math
import pickle
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

from corpus import CORPUS_DIR, iter_records

CACHE = Path(__file__).resolve().parent / ".search_cache.pkl"
_TOKEN = re.compile(r"[0-9a-zà-ÿ]+")


def tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return _TOKEN.findall(text)


def _signature() -> dict[str, float]:
    return {p.name: p.stat().st_mtime for p in CORPUS_DIR.glob("*.json")}


def build_index():
    recs, docs = [], []
    for r in iter_records():
        recs.append(r)
        docs.append(tokens(f"{r.title} {r.text}"))
    df: Counter = Counter()
    for d in docs:
        df.update(set(d))
    n = len(docs)
    idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
    avgdl = sum(len(d) for d in docs) / max(n, 1)
    tfs = [Counter(d) for d in docs]
    lens = [len(d) for d in docs]
    index = {"recs": recs, "tfs": tfs, "lens": lens, "idf": idf,
             "avgdl": avgdl, "sig": _signature()}
    CACHE.write_bytes(pickle.dumps(index))
    return index


def load_index():
    if CACHE.exists():
        idx = pickle.loads(CACHE.read_bytes())
        if idx.get("sig") == _signature():
            return idx
    return build_index()


def search(query: str, books: list[str] | None, n: int, k1=1.5, b=0.75):
    idx = load_index()
    idf, tfs, lens, avgdl = idx["idf"], idx["tfs"], idx["lens"], idx["avgdl"]
    q = [t for t in tokens(query) if t in idf]
    scored = []
    for i, rec in enumerate(idx["recs"]):
        if books and rec.book not in books:
            continue
        tf, dl = tfs[i], lens[i]
        s = sum(idf[t] * (tf[t] * (k1 + 1)) /
                (tf[t] + k1 * (1 - b + b * dl / avgdl)) for t in q if tf[t])
        if s > 0:
            scored.append((s, rec))
    scored.sort(key=lambda x: -x[0])
    return scored[:n]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Busca BM25 no corpus de Conscienciologia.")
    ap.add_argument("query")
    ap.add_argument("--book", help="filtra por index_id, separado por vírgula (ex. ec,tnp)")
    ap.add_argument("-n", type=int, default=10, help="nº de resultados")
    ap.add_argument("--full", action="store_true", help="mostra o trecho integral")
    a = ap.parse_args()
    books = a.book.split(",") if a.book else None
    hits = search(a.query, books, a.n)
    if not hits:
        print("(sem resultados)")
        return
    for score, r in hits:
        txt = r.text if a.full else (r.text[:280] + ("…" if len(r.text) > 280 else ""))
        print(f"\n[{score:5.1f}] {r.cite()}")
        print(txt)


if __name__ == "__main__":
    sys.exit(main())
