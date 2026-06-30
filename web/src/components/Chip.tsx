import type { ReactNode } from "react";

const CONF: Record<string, string> = {
  baixa: "var(--color-conf-baixa)",
  media: "var(--color-conf-media)",
  alta: "var(--color-conf-alta)",
};

const STATUS: Record<string, string> = {
  stub: "var(--color-muted-foreground)",
  rascunho: "oklch(0.72 0.15 85)",
  revisado: "oklch(0.6 0.13 240)",
  consolidado: "var(--color-conf-alta)",
};

export function confColor(conf: string): string {
  return CONF[conf] ?? "var(--color-muted-foreground)";
}

export function statusColor(status: string): string {
  return STATUS[status] ?? "var(--color-muted-foreground)";
}

// Conceitos (origem contextual) ganham destaque com a cor primária; demais
// tipos (verbete literal) não recebem chip — o card é o estado default.
export function tipoColor(tipo: string): string {
  return tipo === "conceito" ? "var(--color-primary)" : "var(--color-muted-foreground)";
}

export const VERPON_COLOR = "var(--color-verpon)";

export function Chip({
  children,
  color = "var(--color-muted-foreground)",
  title,
}: {
  children: ReactNode;
  color?: string;
  title?: string;
}) {
  return (
    <span
      title={title}
      className="inline-flex items-center rounded-full border px-2 py-0.5 text-[10px]
                 font-semibold uppercase tracking-wide leading-none"
      style={{
        color,
        borderColor: `color-mix(in oklch, ${color} 35%, transparent)`,
        backgroundColor: `color-mix(in oklch, ${color} 12%, transparent)`,
      }}
    >
      {children}
    </span>
  );
}
