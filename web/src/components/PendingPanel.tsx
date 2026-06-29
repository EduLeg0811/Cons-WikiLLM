interface PendingItem {
  slug: string;
  titulo: string;
  fields: string[];
}

export function PendingPanel({
  items,
  saving,
  onSelect,
  onDiscard,
  onSave,
}: {
  items: PendingItem[];
  saving: boolean;
  onSelect: (slug: string) => void;
  onDiscard: (slug: string) => void;
  onSave: () => void;
}) {
  return (
    <div className="flex h-full flex-col">
      <h2 className="text-subtitle mb-2">Pendentes</h2>

      {items.length === 0 ? (
        <p className="rounded-lg border border-border bg-card p-3 text-sm text-muted-foreground">
          Nada pendente.
        </p>
      ) : (
        <>
          <div className="flex-1 space-y-2 overflow-y-auto">
            {items.map((it) => (
              <div key={it.slug} className="rounded-lg border border-border bg-card p-2.5">
                <div className="flex items-start justify-between gap-2">
                  <button onClick={() => onSelect(it.slug)} className="text-left text-sm font-medium hover:text-primary">
                    {it.titulo}
                  </button>
                  <button
                    onClick={() => onDiscard(it.slug)}
                    title="Descartar alterações"
                    className="shrink-0 text-muted-foreground hover:text-conf-baixa"
                  >
                    🗑️
                  </button>
                </div>
                <p className="mt-0.5 text-[11px] text-muted-foreground">{it.fields.join(", ")}</p>
              </div>
            ))}
          </div>

          <button
            onClick={onSave}
            disabled={saving}
            className="mt-3 w-full rounded-lg bg-primary px-3 py-2.5 text-sm font-semibold text-primary-foreground
                       transition-opacity hover:opacity-90 disabled:opacity-50"
          >
            {saving ? "Gravando…" : `💾 Gravar (${items.length})`}
          </button>
        </>
      )}
    </div>
  );
}
