// Tipos espelhando os modelos da API (tools/api/main.py).

export interface Fonte {
  id: string;
  label: string;
}

export interface Meta {
  especialidades: string[];
  fontes: Fonte[];
  tipos: string[];
  status_opts: string[];
  conf_opts: string[];
  area_opts: string[];
  total: number;
}

export interface SearchHit {
  score: number;
  slug: string;
  titulo: string;
  tipo: string;
  especialidade: string;
  confianca: string;
  status: string;
  verpon: boolean;
  fontes: string[];
  definologia: string;
}

export interface LinkRef {
  slug: string;
  titulo: string;
}

export interface VerbeteListItem {
  slug: string;
  titulo: string;
  tipo: string;
  especialidade: string;
  area: string;
  status: string;
  confianca: string;
  verpon: boolean;
  fontes_count: number;
  fontes: string[];
}

export interface Editable {
  titulo: string;
  especialidade: string;
  area: string;
  status: string;
  confianca: string;
  fontes_count: number;
  verpon: boolean;
  tags: string[];
  aliases: string[];
  body: string;
}

export interface VerbeteDetail {
  slug: string;
  tipo: string;
  derivado_de: string;
  sources: LinkRef[];
  editable: Editable;
  definologia: string;
  links: LinkRef[];
}

export interface SaveResult {
  ok: boolean;
  renamed: boolean;
  log: string;
}
