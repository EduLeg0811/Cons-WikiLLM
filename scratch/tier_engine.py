# -*- coding: utf-8 -*-
"""Motor genérico de enriquecimento por tier. Uso:
   python scratch/tier_engine.py <esp_tag> <data_module>
O módulo de dados expõe: ESP (str), REL (dict), CONV (dict). Ver tier_autodisc estilo.
"""
import re, pathlib, sys, importlib.util
ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
TODAY = "2026-06-27"

def load(modpath):
    spec = importlib.util.spec_from_file_location("tierdata", modpath)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def split_front(txt):
    mt = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    return mt.group(1), mt.group(2)

def set_fm(fm, key, val):
    if re.search(rf"(?m)^{key}:", fm):
        return re.sub(rf"(?m)^{key}:.*$", f"{key}: {val}", fm)
    return fm + f"\n{key}: {val}"

def replace_section(body, header, new_content):
    pat = re.compile(rf"(?ms)^## {re.escape(header)}\n.*?(?=^## |\Z)")
    repl = f"## {header}\n{new_content}\n\n"
    return pat.sub(repl, body, count=1) if pat.search(body) else body

def insert_after(body, after_header, block):
    pat = re.compile(rf"(?ms)^(## {re.escape(after_header)}\n.*?)(?=^## |\Z)")
    return pat.sub(lambda m: m.group(1).rstrip() + "\n\n" + block + "\n\n", body, count=1)

def run(ESP, REL, CONV):
    changed = conv_n = 0
    for slug, rels in REL.items():
        p = VERB / f"{slug}.md"
        if not p.exists():
            print("FALTA", slug); continue
        txt = p.read_text(encoding="utf-8")
        fm, body = split_front(txt)
        tag = f"tier {ESP}"
        if tag in body:
            continue
        rel_block = "\n".join(f"- {r}" for r in rels) if rels else "- relações a curar"
        body = replace_section(body, "Conexões internas", rel_block)
        has_conv = slug in CONV
        if has_conv:
            titulo, texto, cit, fonte_line = CONV[slug]
            body = insert_after(body, "Definologia", f"## Convergência: {titulo}\n\"{texto}\" — {cit}")
            body = re.sub(r"(?ms)^(## Fontes ingeridas\n)", lambda m: m.group(1) + "- " + fonte_line + "\n", body, count=1)
            conv_n += 1
        fm = set_fm(fm, "status", "revisado")
        fm = set_fm(fm, "ultima_atualizacao", TODAY)
        if has_conv:
            fm = set_fm(fm, "confianca", "media"); fm = set_fm(fm, "fontes_count", "2")
        note = "relações semânticas" + ("; convergência 2ª fonte; baixa→média" if has_conv else "")
        logline = f"- {TODAY}: enriquecido (tier {ESP}): {note}; stub→revisado."
        body = re.sub(r"(?ms)^(## Log de revisões\n)", lambda m: m.group(1) + logline + "\n", body, count=1)
        p.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")
        changed += 1
    print(f"[{ESP}] alterados={changed} convergencias={conv_n}")

if __name__ == "__main__":
    m = load(sys.argv[1])
    run(m.ESP, m.REL, m.CONV)
