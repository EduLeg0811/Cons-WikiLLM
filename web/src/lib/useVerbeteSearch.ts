// Estado + busca compartilhados entre Consulta e Editor — mesmos controles
// (texto, facetas, quantidade) alimentam a mesma chamada de API em ambas as
// páginas, garantindo que a barra de busca/filtros se comporte de forma
// idêntica nos dois modos.
import { useEffect, useRef, useState } from "react";
import { toast } from "sonner";
import { getMeta, search } from "./api";
import type { Meta, SearchHit } from "./types";
import { useDebounce } from "./useDebounce";

export const N_OPTS = [15, 30, 60, 120];
export const N_ALL = 0; // sentinela "Todos" — resolvido para meta.total antes de buscar

export function useVerbeteSearch(initialN: number = 30) {
  const [meta, setMeta] = useState<Meta | null>(null);

  const [q, setQ] = useState("");
  const [n, setN] = useState(initialN);
  const [esp, setEsp] = useState("");
  const [conf, setConf] = useState("");
  const [fonte, setFonte] = useState("");
  const [status, setStatus] = useState("");
  const [verpon, setVerpon] = useState("");
  const [tipo, setTipo] = useState("");
  const [showFacets, setShowFacets] = useState(false);

  const [hits, setHits] = useState<SearchHit[]>([]);
  const [searching, setSearching] = useState(false);
  const [refreshTick, setRefreshTick] = useState(0);

  const dq = useDebounce(q, 250);

  useEffect(() => {
    getMeta().then(setMeta).catch((e) => toast.error(`Falha ao carregar metadados: ${e}`));
  }, []);

  const reqId = useRef(0);
  useEffect(() => {
    const id = ++reqId.current;
    setSearching(true);
    const effectiveN = n === N_ALL ? Math.max(meta?.total ?? 0, 1) : n;
    search({ q: dq, esp, conf, fonte, status, verpon, tipo, n: effectiveN })
      .then((res) => {
        if (id !== reqId.current) return; // resposta obsoleta
        setHits(res);
      })
      .catch((e) => {
        if (id === reqId.current) toast.error(`Erro na busca: ${e}`);
      })
      .finally(() => {
        if (id === reqId.current) setSearching(false);
      });
  }, [dq, esp, conf, fonte, status, verpon, tipo, n, meta, refreshTick]);

  return {
    meta,
    q, setQ, dq,
    n, setN,
    esp, setEsp,
    conf, setConf,
    fonte, setFonte,
    status, setStatus,
    verpon, setVerpon,
    tipo, setTipo,
    showFacets, setShowFacets,
    hits, searching,
    refresh: () => setRefreshTick((t) => t + 1),
  };
}
