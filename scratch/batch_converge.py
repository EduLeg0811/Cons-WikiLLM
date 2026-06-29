# -*- coding: utf-8 -*-
"""Lote final: para cada verbete status=stub + confianca baixa, roda BM25 (search),
exclui a obra de origem e ruído, e auto-aplica o melhor candidato (score>=THRESH)
como Convergência de 2ª fonte. Eleva baixa->média; mantém status=stub. Idempotente."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "tools"))
from search import search
from converge import info, is_noise

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
TODAY = "2026-06-27"
THRESH = 12.0
APPLY = "--apply" in sys.argv

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S); return m.group(1), m.group(2)
def set_fm(fm,k,v): return re.sub(rf"(?m)^{k}:.*$", f"{k}: {v}", fm)
def insert_after(body, header, block):
    pat = re.compile(rf"(?ms)^(## {re.escape(header)}\n.*?)(?=^## |\Z)")
    return pat.sub(lambda m: m.group(1).rstrip()+"\n\n"+block+"\n\n", body, count=1) if pat.search(body) else None

changed = scanned = 0
for p in sorted(VERB.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    fm, body = split_front(txt)
    if not re.search(r"(?m)^confianca:\s*baixa", fm): continue
    if "## Convergência" in body: continue
    scanned += 1
    d = info(p)
    hits = [h for h in search(d["query"], None, 12)
            if h[1].book not in d["src"] and not is_noise(h[1])]
    if not hits: continue
    score, r = hits[0]
    if score < THRESH: continue
    text = re.sub(r"\s+"," ", (r.text or "")).strip()
    if len(text) < 25: continue
    pg = f", p. {r.page}" if r.page else ""
    titpart = f", verbete *{r.title}*" if r.book == "lo" else (f", {r.title}" if r.title else "")
    conv = f"## Convergência: {r.book_name}\n\"{text}\" — {r.book_name}{titpart}{pg}."
    nb = insert_after(body, "Argumentologia (DAC)", conv) or insert_after(body, "Definologia", conv)
    if not nb: continue
    fonte = f"- `corpus/{r.book}.json` — {r.book_name}{titpart}{pg}."
    nb = re.sub(r"(?ms)^(## Fontes ingeridas\n)", lambda m: m.group(1)+fonte+"\n", nb, count=1)
    fm2 = set_fm(set_fm(set_fm(fm,"confianca","media"),"fontes_count","2"),"ultima_atualizacao",TODAY)
    nb = re.sub(r"(?ms)^(## Log de revisões\n)", lambda m: m.group(1)+f"- {TODAY}: convergência 2ª fonte (lote BM25, score {score:.1f}); confiança baixa→média.\n", nb, count=1)
    if APPLY: p.write_text(f"---\n{fm2}\n---\n{nb}", encoding="utf-8")
    changed += 1

print(f"{'APLICADO' if APPLY else 'DRY-RUN'}: escaneados={scanned} convergências(score>={THRESH})={changed}")
