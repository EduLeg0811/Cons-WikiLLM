"""Índice de busca BM25 sobre os VERBETES da wiki (não o corpus-fonte).

Complementa search.py (que indexa as obras brutas): aqui o alvo são os
~2.700 verbetes curados em wiki/verbetes/*.md, com seus campos estruturados
(definologia, convergências, conexões, fontes) e facetas (especialidade,
confiança, fonte, status, verpon). BM25 puro-Python, cache por mtime.

Uso CLI:
    python tools/verbetes_index.py "estado vibracional"
    python tools/verbetes_index.py "assedio" --esp Parapatologia -n 8
"""
from __future__ import annotations
import argparse
import math
import pickle
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
# Pastas de conteúdo indexadas pela busca unificada: verbetes literais +
# conceitos de origem contextual (verpons/originais, ver tipo: conceito).
ROOTS = [WIKI / "verbetes", WIKI / "conceitos"]
VERB = ROOTS[0]   # mantido por compat. com importadores externos
CACHE = Path(__file__).resolve().parent / ".verbete_cache.pkl"
_TOKEN = re.compile(r"[0-9a-zà-ÿ]+")


def _iter_md():
    for root in ROOTS:
        if root.exists():
            yield from sorted(root.glob("*.md"))


def tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return _TOKEN.findall(text)


@dataclass
class VRecord:
    slug: str
    titulo: str
    tipo: str = "verbete"
    derivado_de: str = ""
    aliases: list[str] = field(default_factory=list)
    especialidade: str = ""
    area: str = ""
    status: str = "stub"
    confianca: str = "baixa"
    fontes_count: int = 0
    verpon: bool = False
    definologia: str = ""
    convergencias: list[str] = field(default_factory=list)
    fontes: list[str] = field(default_factory=list)   # index_ids citados (ec, lo, dac…)
    links: list[str] = field(default_factory=list)    # [[slugs]] referenciados
    corpo: str = ""


def _fm_get(fm: str, key: str, default: str = "") -> str:
    m = re.search(rf"(?m)^{key}:[ \t]*(.*)$", fm)
    return m.group(1).strip() if m else default


def _as_list(v: str) -> list[str]:
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip() for x in v[1:-1].split(",") if x.strip()]
    return [v] if v else []


def parse(path: Path) -> VRecord:
    t = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", t)
    defm = re.search(r"(?ms)^## Definologia\s*\n+>?\s*\"?(.+?)(?:\"|\n##|\Z)", body)
    convs = re.findall(r"(?ms)^## Convergência:[^\n]*\n+\"?(.+?)(?:\n##|\Z)", body)
    links = re.findall(r"\[\[([^\]|]+)", body)
    fontes = sorted(set(re.findall(r"corpus/(\w+)\.json", body)))
    return VRecord(
        slug=_fm_get(fm, "slug", path.stem),
        titulo=_fm_get(fm, "titulo", path.stem),
        tipo=_fm_get(fm, "tipo", "verbete"),
        derivado_de=_fm_get(fm, "derivado_de"),
        aliases=_as_list(_fm_get(fm, "aliases")),
        especialidade=_fm_get(fm, "especialidade"),
        area=_fm_get(fm, "area"),
        status=_fm_get(fm, "status", "stub"),
        confianca=_fm_get(fm, "confianca", "baixa"),
        fontes_count=int(re.sub(r"\D", "", _fm_get(fm, "fontes_count", "0")) or 0),
        verpon=_fm_get(fm, "verpon", "false").lower() == "true",
        definologia=re.sub(r"\s+", " ", (defm.group(1) if defm else "")).strip(),
        convergencias=[re.sub(r"\s+", " ", c).strip() for c in convs],
        fontes=fontes,
        links=[s.strip() for s in links],
        corpo=re.sub(r"\s+", " ", re.sub(r"^#.*", "", body)).strip(),
    )


def _signature() -> dict[str, float]:
    return {str(p): p.stat().st_mtime for p in _iter_md()}


def build_index() -> dict:
    recs = [parse(p) for p in _iter_md()]
    docs = []
    for r in recs:
        # boost de campos: título/aliases pesam mais que o corpo
        blob = " ".join([(r.titulo + " ") * 3, (" ".join(r.aliases) + " ") * 2,
                         r.especialidade, r.definologia,
                         " ".join(r.convergencias), r.corpo])
        docs.append(tokens(blob))
    df: Counter = Counter()
    for d in docs:
        df.update(set(d))
    n = len(docs)
    idf = {w: math.log(1 + (n - f + 0.5) / (f + 0.5)) for w, f in df.items()}
    idx = {"recs": recs, "tfs": [Counter(d) for d in docs],
           "lens": [len(d) for d in docs], "idf": idf,
           "avgdl": sum(len(d) for d in docs) / max(n, 1), "sig": _signature()}
    CACHE.write_bytes(pickle.dumps(idx))
    return idx


def load_index() -> dict:
    if CACHE.exists():
        try:
            idx = pickle.loads(CACHE.read_bytes())
            if idx.get("sig") == _signature():
                return idx
        except Exception:
            pass  # cache corrompido/incompatível → reconstrói
    return build_index()


def vsearch(query: str, n: int = 20, *, especialidade=None, confianca=None,
            fonte=None, status=None, verpon=None, tipo=None, k1=1.5, b=0.75):
    """BM25 sobre verbetes com facetas. Filtros None = não aplica.
    Sem query (vazia) → devolve os que casam só pelos filtros, por confiança."""
    idx = load_index()
    idf, tfs, lens, avgdl = idx["idf"], idx["tfs"], idx["lens"], idx["avgdl"]
    q = [t for t in tokens(query or "") if t in idf]

    def passes(r: VRecord) -> bool:
        if especialidade and r.especialidade != especialidade:
            return False
        if confianca and r.confianca != confianca:
            return False
        if status and r.status != status:
            return False
        if fonte and fonte not in r.fontes:
            return False
        if verpon is not None and r.verpon != verpon:
            return False
        if tipo and r.tipo != tipo:
            return False
        return True

    out = []
    conf_rank = {"alta": 2, "media": 1, "baixa": 0}
    for i, r in enumerate(idx["recs"]):
        if not passes(r):
            continue
        if q:
            tf, dl = tfs[i], lens[i]
            s = sum(idf[t] * (tf[t] * (k1 + 1)) /
                    (tf[t] + k1 * (1 - b + b * dl / avgdl)) for t in q if tf[t])
            if s <= 0:
                continue
            out.append((s, r))
        else:
            out.append((float(conf_rank.get(r.confianca, 0)), r))
    out.sort(key=lambda x: -x[0])
    return out[:n]


def especialidades() -> list[str]:
    return sorted({r.especialidade for r in load_index()["recs"] if r.especialidade})


def tipos() -> list[str]:
    return sorted({r.tipo for r in load_index()["recs"] if r.tipo})


def fontes_disp() -> list[str]:
    return sorted({f for r in load_index()["recs"] for f in r.fontes})


def by_slug(slug: str) -> VRecord | None:
    return next((r for r in load_index()["recs"] if r.slug == slug), None)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Busca BM25 sobre os verbetes da wiki.")
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--esp", help="filtra por especialidade")
    ap.add_argument("--conf", help="filtra por confiança (baixa/media/alta)")
    ap.add_argument("-n", type=int, default=12)
    a = ap.parse_args()
    hits = vsearch(a.query, a.n, especialidade=a.esp, confianca=a.conf)
    if not hits:
        print("(sem resultados)")
        return
    for s, r in hits:
        flags = f"{r.confianca}" + (" · verpon" if r.verpon else "")
        print(f"\n[{s:5.1f}] {r.titulo}  ·  {r.especialidade or '—'}  ({flags})")
        if r.definologia:
            print("   " + r.definologia[:200] + ("…" if len(r.definologia) > 200 else ""))


if __name__ == "__main__":
    main()
