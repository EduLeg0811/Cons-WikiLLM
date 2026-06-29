# API da Wiki (FastAPI) — Fase 0

Backend fino que reaproveita os módulos Python já testados (`verbetes_index` para
BM25, `rename.py` para renomear título preservando o slug, `sync_index_counts.py`
para o index). A SPA React (Fase 1+) consome este JSON; nunca toca disco direto.

## Rodar

```powershell
pip install -r tools/requirements.txt
cd tools
python -m uvicorn api.main:app --reload --port 8000
```

Docs interativas: http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Faz |
|---|---|---|
| `GET` | `/api/meta` | especialidades, fontes (id+label), opções de status/confiança/área, total |
| `GET` | `/api/search?q&esp&conf&fonte&status&verpon&n` | busca BM25 + filtros → lista de hits |
| `GET` | `/api/verbete/{slug}` | campos editáveis + corpo + definologia + conceitos ligados |
| `PUT` | `/api/verbete/{slug}` | grava edições; se `titulo` mudou roda `rename.py`; depois `sync` |

`PUT` recebe `tags`/`aliases` como **listas**; `verpon` como bool; `fontes_count` int.
O slug é imutável (validado contra path traversal). Escritas são serializadas por lock.
