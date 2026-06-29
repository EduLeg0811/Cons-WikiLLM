# -*- coding: utf-8 -*-
"""Lote v2: stubs do DAC (-logia) restantes em baixa. Gera raiz do conceito a partir
do título -logia e/ou do alias, com variantes morfológicas, e casa (exato) no lo.json.
Insere Convergência após '## Argumentologia (DAC)'. Mantém status=stub."""
import json, re, pathlib, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
TODAY = "2026-06-27"
APPLY = "--apply" in sys.argv

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9 ]","", s.lower()).strip()

lo = json.load(open(ROOT/"corpus"/"lo.json", encoding="utf-8"))
recs = lo["records"] if isinstance(lo,dict) and "records" in lo else lo
by = {}
for r in recs:
    by.setdefault(norm(r.get("title","")), []).append(r)

def roots(title, aliases):
    """gera candidatos de raiz (normalizados) para um título -logia + aliases."""
    out = []
    # alias: núcleo (cada palavra >=5)
    for a in aliases:
        for w in norm(a).split():
            if len(w) >= 5: out.append(w)
        out.append(norm(a))
    t = norm(title).replace(" ","")
    for suf in ("ologia","logia"):
        if t.endswith(suf):
            r = t[:-len(suf)]
            # variantes morfológicas
            cands = {r, r+"o", r+"a", r+"e"}
            if r.endswith("ci"): cands |= {r[:-2]+"cao", r[:-2]+"ciao", r[:-2]+"co"}
            if r.endswith("c"):  cands |= {r+"ao", r+"a"}
            if r.endswith("i"):  cands |= {r[:-1]+"e", r[:-1]+"ia"}
            if r.endswith("t"):  cands |= {r+"o", r+"e"}
            if r.endswith("ic"): cands |= {r+"a", r+"o"}
            if r.endswith("idad"): cands |= {r+"e"}
            if r.endswith("ist"): cands |= {r+"a", r+"ico"}
            # strip de prefixos conscienciológicos -> raiz nua + vogais
            PREF = ("autorr","auto","aut","parar","para","anti","neo","megar","mega","maxi",
                    "mini","omni","cripto","inter","intra","hetero","multi","retro","super",
                    "sub","trans","pseudo","semi","contra")
            base = set(cands)
            for c in list(base):
                for pre in PREF:
                    if c.startswith(pre) and len(c)-len(pre) >= 5:
                        rr = c[len(pre):]
                        cands |= {rr, rr+"o", rr+"a", rr+"e"}
                        if rr.endswith("c"): cands |= {rr+"ao"}
            out += [c for c in cands if len(c) >= 5]
            break
    # dedup preservando ordem
    seen=set(); res=[]
    for c in out:
        if c and c not in seen: seen.add(c); res.append(c)
    return res

def best(rs):
    c = [r for r in rs if not re.search(r"(?i)etimolog|neolog|surgiu em|do idioma", r.get("text",""))] or rs
    return max(c, key=lambda r: len(r.get("text","")))

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S); return m.group(1), m.group(2)
def set_fm(fm,k,v): return re.sub(rf"(?m)^{k}:.*$", f"{k}: {v}", fm)
def insert_after(body, header, block):
    pat = re.compile(rf"(?ms)^(## {re.escape(header)}\n.*?)(?=^## |\Z)")
    return pat.sub(lambda m: m.group(1).rstrip()+"\n\n"+block+"\n\n", body, count=1) if pat.search(body) else None

changed=0; sample=[]
for p in sorted(VERB.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    fm, body = split_front(txt)
    if not re.search(r"(?m)^status:\s*stub", fm): continue
    if not re.search(r"(?m)^confianca:\s*baixa", fm): continue
    if "## Convergência" in body: continue
    mt = re.search(r"(?m)^titulo:\s*(.+)$", fm)
    if not mt: continue
    title = mt.group(1).strip()
    ma = re.search(r"(?m)^aliases?:\s*\[(.*)\]", fm)
    aliases = [a.strip() for a in ma.group(1).split(",")] if ma else []
    rec=None; matched=None
    for cand in roots(title, aliases):
        if cand in by and len(cand)>=5:
            rec = best(by[cand]); matched=cand; break
    if not rec: continue
    text = re.sub(r"\s+"," ", rec.get("text","")).strip()
    page = rec.get("page","?")
    conv = f"## Convergência: Léxico de Ortopensatas\n\"{text}\" — Léxico de Ortopensatas, p. {page}."
    nb = insert_after(body, "Argumentologia (DAC)", conv) or insert_after(body, "Definologia", conv)
    if not nb: continue
    nb = re.sub(r"(?ms)^(## Fontes ingeridas\n)", lambda m: m.group(1)+f"- `corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{rec.get('title')}*, p. {page}.\n", nb, count=1)
    fm2 = set_fm(set_fm(set_fm(fm,"confianca","media"),"fontes_count","2"),"ultima_atualizacao",TODAY)
    nb = re.sub(r"(?ms)^(## Log de revisões\n)", lambda m: m.group(1)+f"- {TODAY}: convergência 2ª fonte (lote DAC→Léxico, raiz '{matched}'); confiança baixa→média.\n", nb, count=1)
    if APPLY: p.write_text(f"---\n{fm2}\n---\n{nb}", encoding="utf-8")
    changed += 1
    if len(sample)<20: sample.append((title, matched, rec.get('title')))

print(f"{'APLICADO' if APPLY else 'DRY-RUN'}: convergências = {changed}")
for t,m,lt in sample: print(f"  {t[:34]:34} raiz='{m}' -> lo '{lt}'")
