import type { Editable } from "./types";

export const FIELDS: (keyof Editable)[] = [
  "titulo",
  "especialidade",
  "area",
  "status",
  "confianca",
  "fontes_count",
  "verpon",
  "tags",
  "aliases",
  "body",
];

function eqValue(a: unknown, b: unknown): boolean {
  if (Array.isArray(a) && Array.isArray(b)) {
    return a.length === b.length && a.every((v, i) => v === b[i]);
  }
  return a === b;
}

export function changedFields(a: Editable, b: Editable): (keyof Editable)[] {
  return FIELDS.filter((f) => !eqValue(a[f], b[f]));
}

export function isDirty(a: Editable, b: Editable): boolean {
  return changedFields(a, b).length > 0;
}

export function clone(e: Editable): Editable {
  return { ...e, tags: [...e.tags], aliases: [...e.aliases] };
}
