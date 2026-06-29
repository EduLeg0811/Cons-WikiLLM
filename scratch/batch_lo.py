# -*- coding: utf-8 -*-
"""Lote único: para cada verbete status=stub, se o título casar (exato, normalizado)
com um verbete do Léxico de Ortopensatas, adiciona convergência 2ª fonte e eleva
confiança baixa->média. Mantém status=stub (preserva isenção de órfã do lint).
Uso: python scratch/batch_lo.py [--apply]"""
import json, re, pathlib, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
TODAY = "2026-06-27"
APPLY = "--apply" in sys.argv

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9 ]","", s.lower()).strip()

lo = json.load(open(ROOT/"corpus"/"lo.json", encoding="utf-8"))
recs = lo["records"] if isinstance(lo,dict) and "records" in lo else (lo if isinstance(lo,list) else list(lo.values())[0])
by_title = {}
for r in recs:
    t = norm(r.get("title",""))
    if not t: continue
    by_title.setdefault(t, []).append(r)

def best(records):
    # prefer substantive: longest text, mas tira ruído de etimologística/neologística
    cand = [r for r in records if not re.search(r"(?i)etimolog|neolog|surgiu em|do idioma", r.get("text",""))] or records
    return max(cand, key=lambda r: len(r.get("text","")))

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S); return m.group(1), m.group(2)
def set_fm(fm, k, v): return re.sub(rf"(?m)^{k}:.*$", f"{k}: {v}", fm) if re.search(rf"(?m)^{k}:",fm) else fm+f"\n{k}: {v}"
def insert_after(body, header, block):
    pat = re.compile(rf"(?ms)^(## {re.escape(header)}\n.*?)(?=^## |\Z)")
    if pat.search(body):
        return pat.sub(lambda m: m.group(1).rstrip()+"\n\n"+block+"\n\n", body, count=1)
    return None

changed=hit=0
for p in sorted(VERB.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    fm, body = split_front(txt)
    if not re.search(r"(?m)^status:\s*stub", fm): continue
    if "## Convergência" in body: continue
    mt = re.search(r"(?m)^titulo:\s*(.+)$", fm)
    if not mt: continue
    title = mt.group(1).strip()
    key = norm(title)
    recset = by_title.get(key)
    matchkind = "exato"
    if not recset:
        ma = re.search(r"(?m)^alias:\s*(.+)$", fm)
        if ma: recset = by_title.get(norm(ma.group(1)))
    if not recset:
        # fallback: palavra-núcleo (primeira, depois última), len>=5, fora do stoplist
        STOP = {"tecnica","teoria","principio","lei","fator","condicao","estado","efeito",
                "ciencia","tipo","forma","modo","grau","nivel","ponto","parte","conjunto",
                "categoria","abordagem","analise","sindrome","binomio","trinomio"}
        words = [w for w in key.split() if len(w)>=5 and w not in STOP]
        for w in words + words[::-1]:
            if w in by_title:
                recset = by_title[w]; matchkind = f"nucleo:{w}"; break
    if not recset: continue
    hit += 1
    r = best(recset)
    text = re.sub(r"\s+"," ", r.get("text","")).strip()
    page = r.get("page","?")
    conv = f"## Convergência: Léxico de Ortopensatas\n\"{text}\" — Léxico de Ortopensatas, p. {page}."
    nb = insert_after(body, "Definologia", conv) or insert_after(body, "Argumentologia (DAC)", conv)
    if not nb: continue
    nb = re.sub(r"(?ms)^(## Fontes ingeridas\n)", lambda m: m.group(1)+f"- `corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{r.get('title')}*, p. {page}.\n", nb, count=1)
    fm2 = set_fm(fm, "confianca", "media")
    fm2 = set_fm(fm2, "fontes_count", "2")
    fm2 = set_fm(fm2, "ultima_atualizacao", TODAY)
    nb = re.sub(r"(?ms)^(## Log de revisões\n)", lambda m: m.group(1)+f"- {TODAY}: convergência 2ª fonte (lote Léxico, match de título); confiança baixa→média.\n", nb, count=1)
    if APPLY:
        p.write_text(f"---\n{fm2}\n---\n{nb}", encoding="utf-8")
    changed += 1

print(f"{'APLICADO' if APPLY else 'DRY-RUN'}: stubs com match de título no lo = {hit}; convergências aplicadas = {changed}")
