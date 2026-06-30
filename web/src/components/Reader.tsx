import { motion } from "motion/react";
import type { VerbeteDetail } from "../lib/types";
import { Chip, confColor, statusColor, tipoColor, VERPON_COLOR } from "./Chip";
import { MarkdownReader } from "../lib/markdown";

export function Reader({
  detail,
  loading,
  onOpenSlug,
}: {
  detail: VerbeteDetail | null;
  loading: boolean;
  onOpenSlug: (slug: string) => void;
}) {
  if (loading) {
    return <p className="text-sm text-muted-foreground">Carregando verbete…</p>;
  }
  if (!detail) {
    return (
      <p className="text-sm text-muted-foreground">
        Selecione um verbete para ler o conteúdo completo e navegar pelos conceitos ligados.
      </p>
    );
  }

  const e = detail.editable;
  return (
    <motion.article
      key={detail.slug}
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.2 }}
    >
      <h2 className="text-page-title">{e.titulo}</h2>

      <div className="mt-2 flex flex-wrap items-center gap-1.5">
        {detail.tipo === "conceito" && <Chip color={tipoColor("conceito")}>conceito</Chip>}
        <Chip color={statusColor(e.status)}>{e.status}</Chip>
        <Chip color={confColor(e.confianca)}>{e.confianca}</Chip>
        {e.verpon && <Chip color={VERPON_COLOR}>verpon</Chip>}
        {e.especialidade && (
          <span className="ml-1 text-xs uppercase tracking-[0.14em] text-muted-foreground">
            {e.especialidade}
          </span>
        )}
      </div>

      {detail.derivado_de && (
        <p className="mt-1.5 text-xs text-muted-foreground">
          Conceito derivado da especialidade{" "}
          <button
            onClick={() => onOpenSlug(detail.derivado_de)}
            className="font-medium text-primary hover:underline"
          >
            {detail.derivado_de}
          </button>
        </p>
      )}

      {detail.sources.length > 0 && (
        <p className="mt-1.5 text-xs uppercase tracking-[0.14em] text-muted-foreground/70">
          Fontes: {detail.sources.map((s) => s.titulo).join(" · ")}
        </p>
      )}

      <div className="mt-3 border-t border-border pt-3">
        <MarkdownReader body={e.body} onOpenSlug={onOpenSlug} />
      </div>

      {detail.links.length > 0 && (
        <div className="mt-6 border-t border-border pt-4">
          <p className="text-subtitle mb-2">Conceitos relacionados</p>
          <div className="flex flex-wrap gap-2">
            {detail.links.map((l) => (
              <button
                key={l.slug}
                onClick={() => onOpenSlug(l.slug)}
                className="rounded-lg border border-border px-2.5 py-1 text-xs font-semibold
                           uppercase tracking-[0.14em] transition-colors
                           hover:border-primary/50 hover:bg-muted"
              >
                {l.titulo}
              </button>
            ))}
          </div>
        </div>
      )}
    </motion.article>
  );
}
