// Lista de verbetes do Editor — apenas exibição/seleção; a busca e os
// filtros vêm da SearchToolbar compartilhada com a Consulta (mesma barra
// de busca/facetas no topo das duas páginas).
export function VerbeteList({
  items,
  sel,
  dirty,
  onSelect,
  onRefresh,
}: {
  items: { slug: string; titulo: string; tipo: string }[];
  sel: string | null;
  dirty: Set<string>;
  onSelect: (slug: string) => void;
  onRefresh: () => void;
}) {
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

      <div className="flex-1 overflow-y-auto rounded-lg border border-border">
        {items.map((r) => {
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
              {r.tipo === "conceito" && (
                <span className="ml-auto shrink-0 rounded bg-primary/15 px-1 text-[9px] font-semibold uppercase text-primary">
                  conceito
                </span>
              )}
            </button>
          );
        })}
        {items.length === 0 && (
          <p className="p-3 text-sm text-muted-foreground">Nenhum verbete encontrado para os critérios atuais.</p>
        )}
      </div>
    </div>
  );
}
