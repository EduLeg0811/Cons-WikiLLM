"""API FastAPI da Wiki de Conscienciologia.

Camada fina sobre os módulos Python já testados — não reimplementa BM25 nem
o rename seguro de títulos. Expõe o necessário para a SPA React:

    GET  /api/meta              facetas + rótulos das obras + opções de campos
    GET  /api/search           busca BM25 (verbetes_index.vsearch) + filtros
    GET  /api/verbete/{slug}    record completo (campos editáveis + corpo + links)
    PUT  /api/verbete/{slug}    grava edições (rename.py se o título mudar; sync)

Rodar:  uvicorn api.main:app --reload --port 8000   (a partir de tools/)
"""
from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import verbetes_index as vi          # noqa: E402  (BM25 sobre os verbetes)
from api import verbetes_io as vio   # noqa: E402

app = FastAPI(title="ConsIA ● Wiki LLM", version="0.1.0")

# Vite dev server (porta padrão 5173); ajustar/estender conforme necessário.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "PUT", "OPTIONS"],
    allow_headers=["*"],
)


# ---------------- modelos de resposta/entrada ----------------
class SearchHit(BaseModel):
    score: float
    slug: str
    titulo: str
    tipo: str = "verbete"
    especialidade: str = ""
    confianca: str = "baixa"
    status: str = "stub"
    verpon: bool = False
    fontes: list[str] = []
    definologia: str = ""


class LinkRef(BaseModel):
    slug: str
    titulo: str


class VerbeteListItem(BaseModel):
    slug: str
    titulo: str
    tipo: str = "verbete"
    especialidade: str = ""
    area: str = ""
    status: str = "stub"
    confianca: str = "baixa"
    verpon: bool = False
    fontes_count: int = 0
    fontes: list[str] = []      # index_ids citados (= "fonte/corpus" para filtro)


class Editable(BaseModel):
    titulo: str
    especialidade: str = ""
    area: str = ""
    status: str = "rascunho"
    confianca: str = "baixa"
    fontes_count: int = 0
    verpon: bool = False
    tags: list[str] = []
    aliases: list[str] = []
    body: str = ""


class VerbeteDetail(BaseModel):
    slug: str
    tipo: str
    derivado_de: str = ""           # especialidade-hub de origem (tipo: conceito)
    sources: list[LinkRef]          # {slug: index_id, titulo: rótulo da obra}
    editable: Editable
    definologia: str = ""
    links: list[LinkRef] = []       # conceitos relacionados existentes


class SaveResult(BaseModel):
    ok: bool
    renamed: bool
    log: str = ""


def _split(csv: str) -> list[str]:
    return [s.strip() for s in (csv or "").split(",") if s.strip()]


# ---------------- rotas ----------------
@app.get("/api/meta")
def meta():
    labels = vio.book_names()
    return {
        "especialidades": vi.especialidades(),
        "fontes": [{"id": f, "label": labels.get(f, f)} for f in vi.fontes_disp()],
        "tipos": vi.tipos(),
        "status_opts": vio.STATUS_OPTS,
        "conf_opts": vio.CONF_OPTS,
        "area_opts": vio.AREA_OPTS,
        "total": len(vi.load_index()["recs"]),
    }


@app.get("/api/verbetes", response_model=list[VerbeteListItem])
def list_verbetes():
    """Lista leve de TODOS os verbetes (ordenada por título) para o Editor
    filtrar no cliente — espelha o load_all() do wiki_app."""
    recs = vi.load_index()["recs"]
    items = [
        VerbeteListItem(
            slug=r.slug, titulo=r.titulo, tipo=r.tipo, especialidade=r.especialidade,
            area=r.area, status=r.status, confianca=r.confianca, verpon=r.verpon,
            fontes_count=r.fontes_count, fontes=r.fontes,
        )
        for r in recs
    ]
    items.sort(key=lambda x: x.titulo.lower())
    return items


@app.get("/api/search", response_model=list[SearchHit])
def search(q: str = "", esp: str = "", conf: str = "", fonte: str = "",
           status: str = "", verpon: str = "", tipo: str = "", n: int = 30):
    vp = None if verpon in ("", "todos") else (verpon in ("sim", "true", "1"))
    hits = vi.vsearch(q, n, especialidade=esp or None, confianca=conf or None,
                      fonte=fonte or None, status=status or None, verpon=vp,
                      tipo=tipo or None)
    return [
        SearchHit(
            score=round(s, 1), slug=r.slug, titulo=r.titulo, tipo=r.tipo,
            especialidade=r.especialidade, confianca=r.confianca,
            status=r.status, verpon=r.verpon, fontes=r.fontes,
            definologia=r.definologia,
        )
        for s, r in hits
    ]


@app.get("/api/verbete/{slug}", response_model=VerbeteDetail)
def get_verbete(slug: str):
    try:
        path = vio.path_for(slug)
    except ValueError:
        raise HTTPException(400, "slug inválido")
    if not path.exists():
        raise HTTPException(404, "verbete não encontrado")

    rec = vio.parse(path)
    e = rec["editable"]
    labels = vio.book_names()

    by_slug = {r.slug: r for r in vi.load_index()["recs"]}
    vrec = by_slug.get(slug)
    definologia = vrec.definologia if vrec else ""
    links: list[LinkRef] = []
    if vrec:
        seen: dict[str, None] = {}
        for s in vrec.links:
            if s in by_slug and s not in seen and s != slug:
                seen[s] = None
                links.append(LinkRef(slug=s, titulo=by_slug[s].titulo))
        links = links[:24]

    return VerbeteDetail(
        slug=rec["slug"],
        tipo=rec["tipo"],
        derivado_de=vrec.derivado_de if vrec else "",
        sources=[LinkRef(slug=s, titulo=labels.get(s, s)) for s in rec["sources"]],
        editable=Editable(
            titulo=e["titulo"], especialidade=e["especialidade"], area=e["area"],
            status=e["status"], confianca=e["confianca"],
            fontes_count=e["fontes_count"], verpon=e["verpon"],
            tags=_split(e["tags"]), aliases=_split(e["aliases"]), body=e["body"],
        ),
        definologia=definologia,
        links=links,
    )


@app.put("/api/verbete/{slug}", response_model=SaveResult)
def save_verbete(slug: str, ed: Editable):
    try:
        path = vio.path_for(slug)
    except ValueError:
        raise HTTPException(400, "slug inválido")
    if not path.exists():
        raise HTTPException(404, "verbete não encontrado")

    rec = vio.parse(path)
    renamed = ed.titulo != rec["editable"]["titulo"]
    ed_dict = {
        "titulo": ed.titulo,
        "especialidade": ed.especialidade,
        "area": ed.area,
        "status": ed.status,
        "confianca": ed.confianca,
        "fontes_count": ed.fontes_count,
        "verpon": ed.verpon,
        "tags": ", ".join(ed.tags),
        "aliases": ", ".join(ed.aliases),
        "body": ed.body,
    }
    log = vio.apply_one(rec, ed_dict)
    if "[ERRO" in log:
        raise HTTPException(500, log)
    return SaveResult(ok=True, renamed=renamed, log=log.strip())
