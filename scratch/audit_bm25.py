# -*- coding: utf-8 -*-
"""Audita convergências do lote BM25: separa fortes de fracas.
Heurística de FRACO: fonte = Léxico de Ortopensatas E o verbete-fonte não
compartilha palavra-núcleo (>=4 letras) com o título/alias do conceito.
(matches de obras-capítulo são por corpo BM25 -> mantidos)
Uso: python scratch/audit_bm25.py [--revert]"""
import re, sys, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
REVERT = "--revert" in sys.argv
sys.stdout.reconfigure(encoding="utf-8")

def words(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return set(w for w in re.sub(r"[^a-z0-9 ]"," ", s.lower()).split() if len(w) >= 4)

def substrs(w, n=4):
    return set(w[i:i+n] for i in range(len(w)-n+1)) if len(w) >= n else {w}

def related(cw, sw):
    """há raiz comum (substring >=4) entre palavras do conceito e da fonte?"""
    csub = set().union(*[substrs(w) for w in cw]) if cw else set()
    ssub = set().union(*[substrs(w) for w in sw]) if sw else set()
    return bool(csub & ssub)

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S); return m.group(1), m.group(2)
def set_fm(fm,k,v): return re.sub(rf"(?m)^{k}:.*$", f"{k}: {v}", fm)

total=lo_n=other=weak=0; weaklist=[]; stronglist=[]
for p in sorted(VERB.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    mlog = re.search(r"(?m)^- .*lote BM25, score [\d.]+.*$", t)
    if not mlog: continue
    total += 1
    tit = re.search(r"(?m)^titulo:\s*(.+)$", t).group(1)
    al = re.search(r"(?m)^aliases?:\s*\[(.*?)\]", t)
    cw = words(tit) | (words(al.group(1)) if al else set())
    hdr = re.search(r"(?m)^## Convergência:\s*(.+)$", t).group(1).strip()
    mlo = re.search(r"`corpus/lo\.json`[^\n]*verbete \*([^*]+)\*", t)
    islo = bool(mlo)
    is_weak = False
    if islo:
        lo_n += 1
        src = mlo.group(1)
        if not related(cw, words(src)):
            is_weak = True; weak += 1; weaklist.append((p, tit, src))
        else:
            stronglist.append((tit, "lo:"+src))
    else:
        other += 1
        stronglist.append((tit, hdr[:24]))

print(f"BM25 total={total} | lo={lo_n} (fracas={weak}) | obras-capítulo={other}")
print("\n=== FRACAS (lo sem overlap) — candidatas a reverter ===")
for _,tit,src in weaklist: print(f"  {tit[:36]:36} <- lo '{src}'")

if REVERT:
    rev=0
    for p,tit,src in weaklist:
        t = p.read_text(encoding="utf-8")
        fm, body = split_front(t)
        # remove seção Convergência (até próximo ##)
        body = re.sub(r"(?ms)^## Convergência:.*?(?=^## )", "", body, count=1)
        # remove linha de fonte do lo
        body = re.sub(r"(?m)^- `corpus/lo\.json`.*\n", "", body, count=1)
        # remove linha de log do lote BM25
        body = re.sub(r"(?m)^- .*lote BM25, score [\d.]+.*\n", "", body, count=1)
        fm = set_fm(set_fm(fm,"confianca","baixa"),"fontes_count","1")
        p.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")
        rev += 1
    print(f"\nREVERTIDAS: {rev}")
else:
    print("\n(dry-run; use --revert para limpar)")
