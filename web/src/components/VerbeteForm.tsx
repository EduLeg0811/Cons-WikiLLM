import { useState } from "react";
import type { Editable, Meta } from "../lib/types";
import { changedFields } from "../lib/editable";
import { Chip, confColor, statusColor, VERPON_COLOR } from "./Chip";
import { MarkdownReader } from "../lib/markdown";

const inputCls =
  "w-full rounded-lg border border-border bg-card px-2.5 py-1.5 text-sm outline-none focus:border-primary";

function uniqueOpts(base: string[], current: string): string[] {
  return base.includes(current) || !current ? base : [current, ...base];
}

export function VerbeteForm({
  slug,
  ed,
  original,
  meta,
  onChange,
  onOpenSlug,
}: {
  slug: string;
  ed: Editable;
  original: Editable;
  meta: Meta | null;
  onChange: (patch: Partial<Editable>) => void;
  onOpenSlug: (slug: string) => void;
}) {
  const [tab, setTab] = useState<"edit" | "preview">("edit");
  const changed = changedFields(ed, original);

  return (
    <div>
      <div className="flex items-baseline justify-between gap-2">
        <h2 className="text-section-title">Editando</h2>
        <code className="text-xs text-muted-foreground">{slug}</code>
      </div>

      {/* Badges reativos */}
      <div className="mt-2 flex flex-wrap items-center gap-1.5">
        <Chip color={statusColor(ed.status)}>{ed.status}</Chip>
        <Chip color={confColor(ed.confianca)}>{ed.confianca}</Chip>
        {ed.verpon && <Chip color={VERPON_COLOR}>verpon</Chip>}
      </div>

      <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Título
          <input className={inputCls} value={ed.titulo} onChange={(e) => onChange({ titulo: e.target.value })} />
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Especialidade
          <input
            className={inputCls}
            value={ed.especialidade}
            onChange={(e) => onChange({ especialidade: e.target.value })}
          />
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Área
          <select className={inputCls} value={ed.area} onChange={(e) => onChange({ area: e.target.value })}>
            <option value="">—</option>
            {(meta?.area_opts ?? []).map((a) => (
              <option key={a} value={a}>
                {a}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Status
          <select className={inputCls} value={ed.status} onChange={(e) => onChange({ status: e.target.value })}>
            {uniqueOpts(["stub", ...(meta?.status_opts ?? [])], ed.status).map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Confiança
          <select
            className={inputCls}
            value={ed.confianca}
            onChange={(e) => onChange({ confianca: e.target.value })}
          >
            {uniqueOpts([...(meta?.conf_opts ?? [])], ed.confianca).map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Fontes (count)
          <input
            type="number"
            min={0}
            className={inputCls}
            value={ed.fontes_count}
            onChange={(e) => onChange({ fontes_count: Math.max(0, Number(e.target.value) || 0) })}
          />
        </label>
        <label className="col-span-full flex items-center gap-2 text-sm">
          <input
            type="checkbox"
            checked={ed.verpon}
            onChange={(e) => onChange({ verpon: e.target.checked })}
            className="size-4 accent-[var(--color-primary)]"
          />
          Verpon (verdade relativa de ponta)
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Tags (separadas por vírgula)
          <input
            className={inputCls}
            value={ed.tags.join(", ")}
            onChange={(e) => onChange({ tags: e.target.value.split(",").map((s) => s.trim()).filter(Boolean) })}
          />
        </label>
        <label className="flex flex-col gap-1 text-xs text-muted-foreground">
          Aliases (separados por vírgula)
          <input
            className={inputCls}
            value={ed.aliases.join(", ")}
            onChange={(e) =>
              onChange({ aliases: e.target.value.split(",").map((s) => s.trim()).filter(Boolean) })
            }
          />
        </label>
      </div>

      {/* Corpo: editar / preview */}
      <div className="mt-4">
        <div className="mb-2 flex gap-1">
          {(["edit", "preview"] as const).map((t) => (
            <button
              key={t}
              onClick={() => setTab(t)}
              className={[
                "rounded-lg px-3 py-1 text-xs font-medium transition-colors",
                tab === t ? "bg-primary text-primary-foreground" : "text-muted-foreground hover:bg-muted",
              ].join(" ")}
            >
              {t === "edit" ? "📝 Editar" : "👁️ Pré-visualização"}
            </button>
          ))}
        </div>
        {tab === "edit" ? (
          <textarea
            value={ed.body}
            onChange={(e) => onChange({ body: e.target.value })}
            spellCheck={false}
            className="h-[360px] w-full resize-y rounded-lg border border-border bg-card p-3
                       font-mono text-[13px] leading-relaxed outline-none focus:border-primary"
          />
        ) : (
          <div className="min-h-[360px] rounded-lg border border-border bg-card p-4">
            <MarkdownReader body={ed.body} onOpenSlug={onOpenSlug} />
          </div>
        )}
      </div>

      {changed.length > 0 && (
        <p className="mt-3 rounded-lg border border-primary/40 bg-primary/10 px-3 py-2 text-xs text-primary">
          Alterações não gravadas: {changed.join(", ")}
        </p>
      )}
    </div>
  );
}
