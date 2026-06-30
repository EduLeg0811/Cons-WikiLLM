import { useEffect, useState } from "react";
import { AnimatePresence } from "motion/react";
import { toast } from "sonner";
import { getVerbete } from "../lib/api";
import type { VerbeteDetail } from "../lib/types";
import { useVerbeteSearch } from "../lib/useVerbeteSearch";
import { SearchToolbar } from "../components/SearchToolbar";
import { ResultCard } from "../components/ResultCard";
import { Reader } from "../components/Reader";

export function Consulta() {
  const s = useVerbeteSearch();

  const [openSlug, setOpenSlug] = useState<string | null>(null);
  const [detail, setDetail] = useState<VerbeteDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  // Auto-abre o 1º resultado sempre que a lista de hits mudar.
  useEffect(() => {
    setOpenSlug((prev) => {
      if (prev && s.hits.some((h) => h.slug === prev)) return prev;
      return s.hits[0]?.slug ?? null;
    });
  }, [s.hits]);

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

  const hasSearched = s.dq.trim().length > 0;

  const countLabel = s.searching
    ? "buscando…"
    : `${s.hits.length} resultado(s)` + (!s.q && s.meta ? ` · de ${s.meta.total} verbetes` : "");

  return (
    <div>
      <SearchToolbar
        showHero={!hasSearched}
        meta={s.meta}
        q={s.q}
        setQ={s.setQ}
        n={s.n}
        setN={s.setN}
        esp={s.esp}
        setEsp={s.setEsp}
        conf={s.conf}
        setConf={s.setConf}
        fonte={s.fonte}
        setFonte={s.setFonte}
        status={s.status}
        setStatus={s.setStatus}
        verpon={s.verpon}
        setVerpon={s.setVerpon}
        tipo={s.tipo}
        setTipo={s.setTipo}
        showFacets={s.showFacets}
        setShowFacets={s.setShowFacets}
        countLabel={countLabel}
      />

      {/* Resultados + Leitor — aparecem após a barra/facetas compartilhadas */}
      <div className="mt-4 grid grid-cols-1 gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.25fr)]">
        <section>
          <div className="flex max-h-[calc(100vh-220px)] flex-col gap-2 overflow-y-auto pr-1">
            <AnimatePresence mode="popLayout">
              {s.hits.map((h) => (
                <ResultCard
                  key={h.slug}
                  hit={h}
                  active={h.slug === openSlug}
                  onOpen={() => open(h.slug)}
                />
              ))}
            </AnimatePresence>
            {!s.searching && s.hits.length === 0 && (
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
