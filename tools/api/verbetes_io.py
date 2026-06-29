"""Leitura/escrita canônica dos verbetes — núcleo compartilhado pela API.

Unifica o parse/serialize que antes vivia (duplicado) em `wiki_app.py`. Mantém
o **slug imutável**: alterações de título são gravadas com o título ANTIGO no
frontmatter/H1 e a transição é feita por `rename.py` (que protege os `[[links]]`
e as citações ipsis litteris). Pós-escrita, sincroniza as contagens do index.

Sem dependência de Streamlit — só stdlib. Pode ser importado por qualquer camada.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import threading
from datetime import date
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
ROOT = TOOLS.parent
VERB = ROOT / "wiki" / "verbetes"
CORPUS_INDEX = ROOT / "corpus" / "index.json"

EDITABLE = ["titulo", "especialidade", "area", "status", "confianca",
            "fontes_count", "verpon", "tags", "aliases"]
STATUS_OPTS = ["rascunho", "revisado", "consolidado"]
CONF_OPTS = ["baixa", "media", "alta"]
AREA_OPTS = ["Autoconscienciologia", "Conscienciologia", "Intraconscienciologia",
             "Extraconscienciologia", "Paraconscienciologia", "Interconscienciologia",
             "Policonscienciologia"]

# Serializa escritas concorrentes (edição é single-user local, mas dois PUT
# simultâneos não podem corromper o arquivo nem cruzar com o rename/sync).
_WRITE_LOCK = threading.Lock()


def book_names() -> dict[str, str]:
    """index_id -> rótulo de exibição da obra (corpus/index.json)."""
    if CORPUS_INDEX.exists():
        idx = json.loads(CORPUS_INDEX.read_text(encoding="utf-8"))
        return {s["index_id"]: s["index_label"] for s in idx["sources"]}
    return {}


def path_for(slug: str) -> Path:
    """Caminho do verbete a partir do slug, com guarda contra path traversal."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug or ""):
        raise ValueError(f"slug inválido: {slug!r}")
    return VERB / f"{slug}.md"


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    fm_lines = m.group(1).splitlines() if m else []
    body = m.group(2) if m else text
    fm: dict[str, str] = {}
    for ln in fm_lines:
        km = re.match(r"^([a-z_]+):\s*(.*)$", ln)
        if km:
            fm[km.group(1)] = km.group(2).strip()
    # H1 fora do corpo editável
    body = body.lstrip("\n")
    bm = re.match(r"#\s+[^\n]*\n+", body)
    body_rest = body[bm.end():] if bm else body
    sources = sorted(set(re.findall(r"corpus/(\w+)\.json", text)))

    def as_list(v):
        v = (v or "").strip()
        if v.startswith("[") and v.endswith("]"):
            return [x.strip() for x in v[1:-1].split(",") if x.strip()]
        return [x for x in [v] if x]

    return {
        "slug": fm.get("slug", path.stem),
        "tipo": fm.get("tipo", "verbete"),
        "path": path,
        "fm_order": [re.match(r"^([a-z_]+):", l).group(1)
                     for l in fm_lines if re.match(r"^([a-z_]+):", l)],
        "raw_fm": fm,
        "editable": {
            "titulo": fm.get("titulo", path.stem),
            "especialidade": fm.get("especialidade", ""),
            "area": fm.get("area", ""),
            "status": fm.get("status", "rascunho"),
            "confianca": fm.get("confianca", "baixa"),
            "fontes_count": int(fm.get("fontes_count", "0") or 0),
            "verpon": str(fm.get("verpon", "false")).lower() == "true",
            "tags": ", ".join(as_list(fm.get("tags"))),
            "aliases": ", ".join(as_list(fm.get("aliases"))),
            "body": body_rest.rstrip() + "\n",
        },
        "sources": sources,
    }


def serialize(rec: dict, ed: dict) -> str:
    """Reconstrói o arquivo a partir do frontmatter original + edições.
    titulo/H1 recebem `_title_for_fm` (permite gravar com título antigo p/ rename.py)."""
    title = ed["_title_for_fm"]
    vals = dict(rec["raw_fm"])
    vals.update({
        "titulo": title,
        "especialidade": ed["especialidade"],
        "area": ed["area"],
        "status": ed["status"],
        "confianca": ed["confianca"],
        "fontes_count": str(ed["fontes_count"]),
        "verpon": "true" if ed["verpon"] else "false",
        "tags": "[" + ", ".join(s.strip() for s in ed["tags"].split(",") if s.strip()) + "]",
        "ultima_atualizacao": date.today().isoformat(),
    })
    al = [s.strip() for s in ed["aliases"].split(",") if s.strip()]
    if al:
        vals["aliases"] = "[" + ", ".join(al) + "]"
    order = list(rec["fm_order"])
    if al and "aliases" not in order:
        order.insert(order.index("titulo") + 1, "aliases")
    if "ultima_atualizacao" not in order:
        order.append("ultima_atualizacao")
    fm = "\n".join(f"{k}: {vals[k]}" for k in order if k in vals)
    return f"---\n{fm}\n---\n\n# {title}\n\n{ed['body'].strip()}\n"


def apply_one(rec: dict, ed: dict) -> str:
    """Grava as edições; renomeia via rename.py se o título mudou; sincroniza o index.

    Retorna o log textual de rename/sync (string vazia se nada a reportar).
    """
    path = rec["path"]
    old_title = rec["editable"]["titulo"]
    new_title = ed["titulo"]
    changed_title = new_title != old_title
    ed_for_write = {**ed, "_title_for_fm": old_title if changed_title else new_title}

    with _WRITE_LOCK:
        path.write_text(serialize(rec, ed_for_write), encoding="utf-8")
        out = ""
        if changed_title:
            r = subprocess.run(
                [sys.executable, str(TOOLS / "rename.py"), rec["slug"],
                 "--titulo", new_title, "--add-alias", "--apply-prose"],
                cwd=TOOLS, capture_output=True, text=True, encoding="utf-8")
            out = (r.stdout or "") + (r.stderr or "")
            if r.returncode != 0:
                out = f"[ERRO RENAME (código {r.returncode})]\n" + out
        r_sync = subprocess.run(
            [sys.executable, str(TOOLS / "sync_index_counts.py")],
            cwd=TOOLS, capture_output=True, text=True, encoding="utf-8")
        if r_sync.returncode != 0:
            out = (out or "") + f"\n[ERRO SYNC_INDEX_COUNTS (código {r_sync.returncode})]\n" + (r_sync.stderr or "")
    return out
