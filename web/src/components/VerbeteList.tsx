import { useMemo, useState } from "react";
import type { Meta, VerbeteListItem } from "../lib/types";

export function VerbeteList({
  items,
  meta,
  sel,
  dirty,
  onSelect,
  onRefresh,
}: {
  items: VerbeteListItem[];
  meta: Meta | null;
  sel: string | null;
  dirty: Set<string>;
  onSelect: (slug: string) => void;
  onRefresh: () => void;
}) {
  const [fSrc, setFSrc] = useState("");
  const [fStatus, setFStatus] = useState("");
  const [fConf, setFConf] = useState("");
  const [fEsp, setFEsp] = useState("");
  const [fVerpon, setFVerpon] = useState("");
  const [fText, setFText] = useState("");
  const [more, setMore] = useState(false);

  const filtered = useMemo(() => {
    const t = fText.trim().toLowerCase();
    return items.filter((r) => {
      if (fSrc && !r.fontes.includes(fSrc)) return false;
      if (fStatus && r.status !== fStatus) return false;
      if (fConf && r.confianca !== fConf) return false;
      if (fEsp && r.especialidade !== fEsp) return false;
      if (fVerpon && r.verpon !== (fVerpon === "sim")) return false;
      if (t && !r.titulo.toLowerCase().includes(t)) return false;
      return true;
    });
  }, [items, fSrc, fStatus, fConf, fEsp, fVerpon, fText]);

  const esps = useMemo(
    () => Array.from(new Set(items.map((r) => r.especialidade).filter(Boolean))).sort(),
    [items]
  );

  const inputCls =
    "w-full rounded-lg border border-border bg-card px-2.5 py-1.5 text-sm outline-none focus:border-primary";

  return (
    <div className="flex h-full flex-col">
      <div className="mb-2 flex items-center justify-between">
        <h2 className="text-subtitle">Verbetes</h2>
        <button
          onClick={onRefresh}
          title="Recarregar do disco"
          className="grid size-7 place-items-center rounded-lg border border-border text-xs hover:bg-muted"
        >
          ↻
        </button>
      </div>

      <select value={fSrc} onChange={(e) => setFSrc(e.target.value)} className={inputCls}>
        <option value="">Fonte (corpus) — todas</option>
        {(meta?.fontes ?? []).map((f) => (
          <option key={f.id} value={f.id}>
            {f.label}
          </option>
        ))}
      </select>

      <button
        onClick={() => setMore((m) => !m)}
        className="mt-2 self-start text-xs text-muted-foreground hover:text-foreground"
      >
        {more ? "▾ menos filtros" : "▸ mais filtros"}
      </button>

      {more && (
        <div className="mt-2 grid grid-cols-2 gap-2">
          <select value={fStatus} onChange={(e) => setFStatus(e.target.value)} className={inputCls}>
            <option value="">status — todos</option>
            <option value="stub">stub</option>
            {(meta?.status_opts ?? []).map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
          <select value={fConf} onChange={(e) => setFConf(e.target.value)} className={inputCls}>
            <option value="">confiança — todas</option>
            {(meta?.conf_opts ?? []).map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
          <select value={fEsp} onChange={(e) => setFEsp(e.target.value)} className={`${inputCls} col-span-2`}>
            <option value="">especialidade — todas</option>
            {esps.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
          <select value={fVerpon} onChange={(e) => setFVerpon(e.target.value)} className={inputCls}>
            <option value="">verpon — todos</option>
            <option value="sim">sim</option>
            <option value="não">não</option>
          </select>
          <input
            value={fText}
            onChange={(e) => setFText(e.target.value)}
            placeholder="busca no título"
            className={inputCls}
          />
        </div>
      )}

      <p className="mt-2 text-xs text-muted-foreground">
        {filtered.length} de {items.length} verbetes
      </p>

      <div className="mt-1 flex-1 overflow-y-auto rounded-lg border border-border">
        {filtered.map((r) => {
          const active = r.slug === sel;
          return (
            <button
              key={r.slug}
              onClick={() => onSelect(r.slug)}
              className={[
                "flex w-full items-center gap-2 border-b border-border/60 px-2.5 py-1.5 text-left text-sm last:border-0",
                active ? "bg-primary/10 text-primary" : "hover:bg-muted",
              ].join(" ")}
            >
              {dirty.has(r.slug) && <span className="text-primary">●</span>}
              <span className="truncate">{r.titulo}</span>
            </button>
          );
        })}
        {filtered.length === 0 && (
          <p className="p-3 text-sm text-muted-foreground">Nenhum verbete no filtro atual.</p>
        )}
      </div>
    </div>
  );
}
