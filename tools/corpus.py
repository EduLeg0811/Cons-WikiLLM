"""Camada de acesso ao corpus JSON (fonte canônica de ingest).

Normaliza os schemas heterogêneos dos arquivos em /corpus numa interface
única. Use `iter_records()` para varrer; cada registro é um Record.

Os JSONs variam (alguns com `metadata` aninhado, headers diferentes), mas
todos expõem `records[].data` como o registro plano completo — é o que usamos.
"""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

CORPUS_DIR = Path(__file__).resolve().parent.parent / "corpus"


@dataclass
class Record:
    book: str        # index_id, ex. "ec"
    book_name: str   # ex. "Enciclopedia da Conscienciologia"
    row: int
    text: str
    title: str = ""
    page: str = ""   # pagina, ou number como fallback
    area: str = ""
    theme: str = ""
    author: str = ""

    def cite(self) -> str:
        loc = f", p. {self.page}" if self.page else ""
        ttl = f" — {self.title}" if self.title else ""
        return f"[{self.book_name}{ttl}{loc}]"


def books() -> dict[str, dict]:
    """Mapa index_id -> metadados da obra (de corpus/index.json)."""
    idx = json.loads((CORPUS_DIR / "index.json").read_text(encoding="utf-8"))
    return {s["index_id"]: s for s in idx["sources"]}


def _record(book: str, book_name: str, raw: dict) -> Record:
    d = raw.get("data", raw)
    return Record(
        book=book,
        book_name=book_name,
        row=raw.get("row", 0),
        text=(d.get("text") or "").strip(),
        title=str(d.get("title") or "").strip(),
        page=str(d.get("pagina") or d.get("number") or d.get("page") or "").strip(),
        area=str(d.get("area") or "").strip(),
        theme=str(d.get("theme") or "").strip(),
        author=str(d.get("author") or "").strip(),
    )


def iter_records(only: list[str] | None = None) -> Iterator[Record]:
    """Varre o corpus. `only` filtra por index_id (ex. ['ec','dac'])."""
    meta = books()
    ids = only or list(meta)
    for bid in ids:
        # o nome do arquivo pode diferir do index_id (ex. ec -> ecwv.json);
        # o índice carrega o mapeamento em `file`, com fallback para <id>.json.
        fname = meta.get(bid, {}).get("file", f"{bid}.json")
        path = CORPUS_DIR / fname
        if not path.exists():
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        name = meta.get(bid, {}).get("book_name", bid)
        for raw in doc.get("records", []):
            rec = _record(bid, name, raw)
            if rec.text:
                yield rec


if __name__ == "__main__":
    from collections import Counter
    c = Counter()
    for r in iter_records():
        c[r.book] += 1
    for bid, n in sorted(c.items(), key=lambda x: -x[1]):
        print(f"{n:>7}  {bid:<14} {books().get(bid, {}).get('book_name','')}")
    print(f"{sum(c.values()):>7}  TOTAL")
