import { useCallback, useEffect, useMemo, useState } from "react";
import { toast } from "sonner";
import { getMeta, getVerbete, listVerbetes, saveVerbete } from "../lib/api";
import type { Editable, Meta, VerbeteListItem } from "../lib/types";
import { changedFields, clone, isDirty } from "../lib/editable";
import { VerbeteList } from "../components/VerbeteList";
import { VerbeteForm } from "../components/VerbeteForm";
import { PendingPanel } from "../components/PendingPanel";

export function Editor() {
  const [list, setList] = useState<VerbeteListItem[]>([]);
  const [meta, setMeta] = useState<Meta | null>(null);
  const [sel, setSel] = useState<string | null>(null);
  const [originals, setOriginals] = useState<Record<string, Editable>>({});
  const [edits, setEdits] = useState<Record<string, Editable>>({});
  const [loadingSlug, setLoadingSlug] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);

  const loadList = useCallback(() => {
    listVerbetes()
      .then(setList)
      .catch((e) => toast.error(`Falha ao listar verbetes: ${e}`));
  }, []);

  useEffect(() => {
    loadList();
    getMeta().then(setMeta).catch((e) => toast.error(`Falha ao carregar metadados: ${e}`));
  }, [loadList]);

  const ensureLoaded = useCallback(
    async (slug: string) => {
      if (originals[slug]) return;
      setLoadingSlug(slug);
      try {
        const d = await getVerbete(slug);
        setOriginals((o) => ({ ...o, [slug]: d.editable }));
        setEdits((e) => (e[slug] ? e : { ...e, [slug]: clone(d.editable) }));
      } catch (e) {
        toast.error(`Erro ao abrir ${slug}: ${e}`);
      } finally {
        setLoadingSlug((s) => (s === slug ? null : s));
      }
    },
    [originals]
  );

  const select = useCallback(
    (slug: string) => {
      setSel(slug);
      void ensureLoaded(slug);
    },
    [ensureLoaded]
  );

  const patch = (p: Partial<Editable>) => {
    if (!sel) return;
    setEdits((e) => ({ ...e, [sel]: { ...e[sel], ...p } }));
  };

  const discard = (slug: string) => {
    if (originals[slug]) setEdits((e) => ({ ...e, [slug]: clone(originals[slug]) }));
  };

  const dirtySlugs = useMemo(
    () => Object.keys(edits).filter((s) => originals[s] && isDirty(edits[s], originals[s])),
    [edits, originals]
  );
  const dirtySet = useMemo(() => new Set(dirtySlugs), [dirtySlugs]);

  const pendingItems = useMemo(
    () =>
      dirtySlugs.map((s) => ({
        slug: s,
        titulo: originals[s].titulo,
        fields: changedFields(edits[s], originals[s]),
      })),
    [dirtySlugs, edits, originals]
  );

  const save = async () => {
    if (!dirtySlugs.length) return;
    setSaving(true);
    let ok = 0;
    for (const s of dirtySlugs) {
      try {
        const res = await saveVerbete(s, edits[s]);
        ok++;
        const saved = clone(edits[s]);
        setOriginals((o) => ({ ...o, [s]: saved }));
        if (res.renamed) {
          toast.success(`Renomeado → ${saved.titulo}`, {
            description: res.log ? res.log.split("\n").slice(0, 3).join(" · ") : "rename + sync aplicados",
          });
        } else {
          toast.success(`Gravado: ${saved.titulo}`);
        }
      } catch (e) {
        toast.error(`Erro ao gravar ${s}`, { description: String(e).slice(0, 300) });
      }
    }
    setSaving(false);
    if (ok) loadList(); // títulos/contagens podem ter mudado
  };

  return (
    <div className="grid h-[calc(100vh-104px)] grid-cols-1 gap-4 lg:grid-cols-[260px_minmax(0,1fr)_280px]">
      <aside className="min-h-0">
        <VerbeteList
          items={list}
          meta={meta}
          sel={sel}
          dirty={dirtySet}
          onSelect={select}
          onRefresh={() => {
            setOriginals({});
            setEdits({});
            loadList();
            toast.info("Recarregado do disco.");
          }}
        />
      </aside>

      <main className="min-h-0 overflow-y-auto rounded-2xl border border-border bg-card/40 p-5">
        {!sel ? (
          <p className="text-sm text-muted-foreground">Selecione um verbete na lista para editar.</p>
        ) : !edits[sel] ? (
          <p className="text-sm text-muted-foreground">
            {loadingSlug === sel ? "Carregando verbete…" : "—"}
          </p>
        ) : (
          <VerbeteForm
            slug={sel}
            ed={edits[sel]}
            original={originals[sel]}
            meta={meta}
            onChange={patch}
            onOpenSlug={select}
          />
        )}
      </main>

      <aside className="min-h-0">
        <PendingPanel
          items={pendingItems}
          saving={saving}
          onSelect={select}
          onDiscard={discard}
          onSave={save}
        />
      </aside>
    </div>
  );
}
