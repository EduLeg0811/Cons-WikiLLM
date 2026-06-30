import { motion } from "motion/react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { SearchHit } from "../lib/types";
import { Chip, confColor, tipoColor, VERPON_COLOR } from "./Chip";

// Componentes que achatam elementos de bloco para inline, adequado para
// o preview line-clamp-2 dos cards.
const MD_COMPONENTS = {
  p: ({ children }: { children?: React.ReactNode }) => <>{children}</>,
  h1: ({ children }: { children?: React.ReactNode }) => <strong>{children} </strong>,
  h2: ({ children }: { children?: React.ReactNode }) => <strong>{children} </strong>,
  h3: ({ children }: { children?: React.ReactNode }) => <em>{children} </em>,
  h4: ({ children }: { children?: React.ReactNode }) => <em>{children} </em>,
  ul: ({ children }: { children?: React.ReactNode }) => <>{children}</>,
  ol: ({ children }: { children?: React.ReactNode }) => <>{children}</>,
  li: ({ children }: { children?: React.ReactNode }) => <span>{children} </span>,
  blockquote: ({ children }: { children?: React.ReactNode }) => <em className="text-foreground/70">{children}</em>,
  code: ({ children }: { children?: React.ReactNode }) => (
    <code className="rounded bg-muted px-0.5 font-mono text-[0.9em]">{children}</code>
  ),
};

export function ResultCard({
  hit,
  active,
  query,
  onOpen,
}: {
  hit: SearchHit;
  active: boolean;
  query: string;
  onOpen: () => void;
}) {
  return (
    <motion.button
      layout
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.18 }}
      onClick={onOpen}
      className={[
        "w-full rounded-xl border bg-card p-3.5 text-left transition-colors",
        active
          ? "border-primary ring-1 ring-primary/40"
          : "border-border hover:border-primary/40 hover:bg-muted/40",
      ].join(" ")}
    >
      <div className="flex items-start justify-between gap-3">
        <h3 className="text-card-title">{hit.titulo}</h3>
        <span className="text-card-body shrink-0 text-xs font-semibold text-muted-foreground">
          score {hit.score}
        </span>
      </div>

      <div className="mt-1.5 flex flex-wrap items-center gap-1.5">
        {hit.tipo === "conceito" && <Chip color={tipoColor("conceito")}>conceito</Chip>}
        {hit.especialidade && (
          <span className="text-card-body text-xs uppercase tracking-[0.14em] text-muted-foreground">
            {hit.especialidade}
          </span>
        )}
        <Chip color={confColor(hit.confianca)}>{hit.confianca}</Chip>
        {hit.verpon && <Chip color={VERPON_COLOR}>verpon</Chip>}
      </div>

      {hit.definologia && (
        <div className="text-card-body mt-2 line-clamp-2 text-sm leading-relaxed text-muted-foreground">
          <ReactMarkdown remarkPlugins={[remarkGfm]} components={MD_COMPONENTS}>
            {hit.definologia}
          </ReactMarkdown>
        </div>
      )}

      {hit.fontes.length > 0 && (
        <p className="text-card-body mt-1.5 text-xs uppercase tracking-[0.14em] text-muted-foreground/60">
          {hit.fontes.join(" · ")}
        </p>
      )}
    </motion.button>
  );
}
