// Cliente da API. A SPA nunca toca disco nem reimplementa BM25/rename —
// só consome o JSON servido pelo FastAPI.
//
// Em dev, o Vite faz proxy de /api -> localhost:8000 (vite.config.ts), então
// VITE_API_URL fica vazio e as chamadas usam caminho relativo.
// Em produção com API e SPA em serviços/domínios separados (ex.: Render),
// defina VITE_API_URL com a URL completa da API (sem barra final) no build.
import type {
  Meta,
  SearchHit,
  VerbeteDetail,
  VerbeteListItem,
  Editable,
  SaveResult,
} from "./types";

const API_BASE = import.meta.env.VITE_API_URL ?? "";

async function getJSON<T>(url: string): Promise<T> {
  const res = await fetch(`${API_BASE}${url}`);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json() as Promise<T>;
}

export const getMeta = () => getJSON<Meta>("/api/meta");

export const listVerbetes = () => getJSON<VerbeteListItem[]>("/api/verbetes");

export interface SearchParams {
  q?: string;
  esp?: string;
  conf?: string;
  fonte?: string;
  status?: string;
  verpon?: string; // "", "sim", "não"/"nao"
  tipo?: string;
  n?: number;
}

export function search(p: SearchParams): Promise<SearchHit[]> {
  const qs = new URLSearchParams();
  if (p.q) qs.set("q", p.q);
  if (p.esp) qs.set("esp", p.esp);
  if (p.conf) qs.set("conf", p.conf);
  if (p.fonte) qs.set("fonte", p.fonte);
  if (p.status) qs.set("status", p.status);
  if (p.verpon) qs.set("verpon", p.verpon === "não" ? "nao" : p.verpon);
  if (p.tipo) qs.set("tipo", p.tipo);
  if (p.n) qs.set("n", String(p.n));
  return getJSON<SearchHit[]>(`/api/search?${qs.toString()}`);
}

export const getVerbete = (slug: string) =>
  getJSON<VerbeteDetail>(`/api/verbete/${encodeURIComponent(slug)}`);

export async function saveVerbete(slug: string, ed: Editable): Promise<SaveResult> {
  const res = await fetch(`${API_BASE}/api/verbete/${encodeURIComponent(slug)}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(ed),
  });
  if (!res.ok) {
    let detail = `${res.status} ${res.statusText}`;
    try {
      const j = await res.json();
      if (j?.detail) detail = typeof j.detail === "string" ? j.detail : JSON.stringify(j.detail);
    } catch {
      /* corpo não-JSON */
    }
    throw new Error(detail);
  }
  return res.json() as Promise<SaveResult>;
}
