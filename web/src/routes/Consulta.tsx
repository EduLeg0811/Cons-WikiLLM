import { useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence } from "motion/react";
import { Search } from "lucide-react";
import { toast } from "sonner";
import { getMeta, getVerbete, search } from "../lib/api";
import type { Meta, SearchHit, VerbeteDetail } from "../lib/types";
import { useDebounce } from "../lib/useDebounce";
import { Select } from "../components/Select";
import { ResultCard } from "../components/ResultCard";
import { Reader } from "../components/Reader";

const N_OPTS = [15, 30, 60, 120];
const N_ALL = 0; // sentinela "Todos" — resolvido para meta.total antes de buscar

export function Consulta() {
  const [meta, setMeta] = useState<Meta | null>(null);

  const [q, setQ] = useState("");
  const [n, setN] = useState(30);
  const [esp, setEsp] = useState("");
  const [conf, setConf] = useState("");
  const [fonte, setFonte] = useState("");
  const [status, setStatus] = useState("");
  const [verpon, setVerpon] = useState("");
  const [tipo, setTipo] = useState("");
  const [showFacets, setShowFacets] = useState(false);

  const [hits, setHits] = useState<SearchHit[]>([]);
  const [searching, setSearching] = useState(false);

  const [openSlug, setOpenSlug] = useState<string | null>(null);
  const [detail, setDetail] = useState<VerbeteDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  const dq = useDebounce(q, 250);

  useEffect(() => {
    getMeta().then(setMeta).catch((e) => toast.error(`Falha ao carregar metadados: ${e}`));
  }, []);

  // Busca reativa (query debounced + facetas). Auto-abre o 1º resultado.
  const reqId = useRef(0);
  useEffect(() => {
    const id = ++reqId.current;
    setSearching(true);
    const effectiveN = n === N_ALL ? Math.max(meta?.total ?? 0, 1) : n;
    search({ q: dq, esp, conf, fonte, status, verpon, tipo, n: effectiveN })
      .then((res) => {
        if (id !== reqId.current) return; // resposta obsoleta
        setHits(res);
        setOpenSlug((prev) => {
          if (prev && res.some((h) => h.slug === prev)) return prev;
          return res[0]?.slug ?? null;
        });
      })
      .catch((e) => {
        if (id === reqId.current) toast.error(`Erro na busca: ${e}`);
      })
      .finally(() => {
        if (id === reqId.current) setSearching(false);
      });
  }, [dq, esp, conf, fonte, status, verpon, tipo, n, meta]);

  // Carrega o verbete aberto.
  useEffect(() => {
    if (!openSlug) {
      setDetail(null);
      return;
    }
    let alive = true;
    setDetailLoading(true);
    getVerbete(openSlug)
      .then((d) => alive && setDetail(d))
      .catch((e) => alive && toast.error(`Erro ao abrir verbete: ${e}`))
      .finally(() => alive && setDetailLoading(false));
    return () => {
      alive = false;
    };
  }, [openSlug]);

  const open = (slug: string) => setOpenSlug(slug);

  const hasSearched = dq.trim().length > 0;

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
      {/* Hero — só antes da 1ª busca por texto (ver .agents/SKILL.md §2) */}
      {!hasSearched && (
        <div className="mb-12 text-center">
          <h2 className="font-display text-5xl leading-[1.05] text-foreground sm:text-6xl">
            Conscienciologia estruturada,
            <br />
            <span className="italic text-primary/80">second brain ontológico.</span>
          </h2>
          <p className="mx-auto mt-5 max-w-2xl text-base leading-relaxed text-muted-foreground">
            Verbetes • Técnicas • Fenômenos • Obras • Conceitos
          </p>
        </div>
      )}

      {/* Caixa de pesquisa (ver .agents/SKILL.md §3) */}
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
          onClick={() => setShowFacets((s) => !s)}
          className={[
            "rounded-xl border px-4 py-2.5 text-sm font-medium transition-colors",
            showFacets ? "border-primary text-primary" : "border-border text-muted-foreground hover:bg-muted",
          ].join(" ")}
        >
          Filtros
        </button>
      </div>

      {/* Filtros */}
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

      {/* Resultados + Leitor */}
      <div className="mt-4 grid grid-cols-1 gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.25fr)]">
        <section>
          <p className="mb-2 text-xs text-muted-foreground">
            {searching ? "buscando…" : `${hits.length} resultado(s)`}
            {!q && meta ? ` · de ${meta.total} verbetes` : ""}
          </p>
          <div className="flex max-h-[calc(100vh-220px)] flex-col gap-2 overflow-y-auto pr-1">
            <AnimatePresence mode="popLayout">
              {hits.map((h) => (
                <ResultCard
                  key={h.slug}
                  hit={h}
                  active={h.slug === openSlug}
                  query={dq}
                  onOpen={() => open(h.slug)}
                />
              ))}
            </AnimatePresence>
            {!searching && hits.length === 0 && (
              <p className="rounded-xl border border-border bg-card p-4 text-sm text-muted-foreground">
                Nenhum verbete encontrado para os critérios atuais.
              </p>
            )}
          </div>
        </section>

        <section className="lg:sticky lg:top-[76px] lg:max-h-[calc(100vh-92px)] lg:overflow-y-auto">
          <div className="rounded-2xl border border-border bg-card p-5">
            <Reader detail={detail} loading={detailLoading} onOpenSlug={open} />
          </div>
        </section>
      </div>
    </div>
  );
}
