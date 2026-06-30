import { AnimatePresence } from "motion/react";
import { Search } from "lucide-react";
import { useMemo } from "react";
import { Select } from "./Select";
import { RouteTabs } from "./RouteTabs";
import { N_ALL, N_OPTS } from "../lib/useVerbeteSearch";
import type { Meta } from "../lib/types";

// Barra de busca + facetas + botões Consulta/Editor, compartilhada pelas
// duas páginas (ver .agents/SKILL.md §3) para manter a parte superior
// idêntica nos dois modos.
export function SearchToolbar(props: {
  meta: Meta | null;
  q: string;
  setQ: (v: string) => void;
  n: number;
  setN: (v: number) => void;
  esp: string;
  setEsp: (v: string) => void;
  conf: string;
  setConf: (v: string) => void;
  fonte: string;
  setFonte: (v: string) => void;
  status: string;
  setStatus: (v: string) => void;
  verpon: string;
  setVerpon: (v: string) => void;
  tipo: string;
  setTipo: (v: string) => void;
  showFacets: boolean;
  setShowFacets: (v: boolean) => void;
  countLabel: string;
}) {
  const {
    meta, q, setQ, n, setN, esp, setEsp, conf, setConf, fonte, setFonte,
    status, setStatus, verpon, setVerpon, tipo, setTipo, showFacets, setShowFacets, countLabel,
  } = props;

  const espOpts = useMemo(
    () => [{ value: "", label: "Especialidade — todas" }, ...(meta?.especialidades ?? []).map((s) => ({ value: s, label: s }))],
    [meta]
  );
  const fonteOpts = useMemo(
    () => [{ value: "", label: "Fonte — todas" }, ...(meta?.fontes ?? []).map((f) => ({ value: f.id, label: f.label }))],
    [meta]
  );

  return (
    <div>
      <div className="flex flex-wrap items-center gap-2">
        <div
          className="flex w-full min-w-[280px] flex-1 items-center gap-1.5 rounded-2xl border
                     border-border/70 bg-card/80 p-1.5 shadow-[0_4px_24px_-12px_rgba(80,70,120,0.25)]
                     backdrop-blur sm:gap-2 sm:p-2"
        >
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="Busca por conteúdo — ex.: estado vibracional, autassédio, recin grupal…"
            className="min-w-0 flex-1 rounded-xl bg-transparent px-3 py-2 font-display text-base
                       text-foreground outline-none placeholder:text-muted-foreground/50 sm:px-4 sm:py-3 sm:text-lg"
          />
          <button
            type="button"
            aria-label="Pesquisar"
            title="Pesquisar"
            className="flex shrink-0 items-center justify-center rounded-xl bg-primary px-5 py-2.5
                       text-primary-foreground transition hover:opacity-90 sm:px-6 sm:py-3"
          >
            <Search className="h-6 w-6" strokeWidth={2} />
          </button>
        </div>
        <select
          value={n}
          onChange={(e) => setN(Number(e.target.value))}
          className="rounded-xl border border-border bg-card px-3 py-2.5 text-sm outline-none focus:border-primary"
        >
          {N_OPTS.map((v) => (
            <option key={v} value={v}>
              {v} resultados
            </option>
          ))}
          <option value={N_ALL}>Todos</option>
        </select>
        <button
          onClick={() => setShowFacets(!showFacets)}
          className={[
            "rounded-xl border px-4 py-2.5 text-sm font-medium transition-colors",
            showFacets ? "border-primary text-primary" : "border-border text-muted-foreground hover:bg-muted",
          ].join(" ")}
        >
          Filtros
        </button>
        <RouteTabs />
      </div>

      <AnimatePresence>
        {showFacets && (
          <div className="mt-3 grid grid-cols-2 gap-3 rounded-xl border border-border bg-card/50 p-4 sm:grid-cols-3 lg:grid-cols-6">
            <Select
              label="Tipo"
              value={tipo}
              onChange={setTipo}
              options={[
                { value: "", label: "todos" },
                ...(meta?.tipos ?? []).map((t) => ({ value: t, label: t })),
              ]}
            />
            <Select label="Especialidade" value={esp} onChange={setEsp} options={espOpts} />
            <Select
              label="Confiança"
              value={conf}
              onChange={setConf}
              options={[{ value: "", label: "todas" }, ...(meta?.conf_opts ?? []).map((c) => ({ value: c, label: c }))]}
            />
            <Select label="Fonte (obra citada)" value={fonte} onChange={setFonte} options={fonteOpts} />
            <Select
              label="Status"
              value={status}
              onChange={setStatus}
              options={[
                { value: "", label: "todos" },
                { value: "stub", label: "stub" },
                ...(meta?.status_opts ?? []).map((s) => ({ value: s, label: s })),
              ]}
            />
            <Select
              label="Verpon"
              value={verpon}
              onChange={setVerpon}
              options={[
                { value: "", label: "todos" },
                { value: "sim", label: "sim" },
                { value: "não", label: "não" },
              ]}
            />
          </div>
        )}
      </AnimatePresence>

      <p className="mt-3 text-xs text-muted-foreground">{countLabel}</p>
    </div>
  );
}
