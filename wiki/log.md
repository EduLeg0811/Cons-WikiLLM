# Log — Wiki de Conscienciologia

> Linha do tempo orientada a tempo. Cabeçalho grep-ável: `## [YYYY-MM-DD HH:MM] <tipo> | <descrição>`.
> `grep "^## \[" log.md | tail -10` → últimos 10 eventos.

## [2026-06-24 00:00] setup | reinício da ingestão a partir do corpus
- Wiki anterior (gerada a partir dos PDFs de `/raw`) apagada por completo.
- Nova ingestão padronizada pela camada algorítmica `/tools` e citando o corpus em `/corpus`.
- Ordem planejada: obras menores primeiro (tnp → proexis → temas → dupla → …).

## [2026-06-24 00:30] ingest | Manual da Tenepes (`corpus/tnp.json`, 340 registros)
- Obra catalogada: [[manual-da-tenepes]].
- Verbetes criados (5): [[tenepes]] (verpon), [[tacon]], [[tares]], [[ofiex]], [[epicon]] — todos citando o corpus (obra + página).
- Pares conjugados cruzados: tacon↔tares↔tenepes (trinômio assistencial); tenepes↔ofiex; tenepes↔epicon.
- Verpon registrada: teoria da fartura de energia consciencial (cap. 32).
- Lacunas (mencionadas sem página): [[amparador]], [[maximecanismo]], [[energia-consciencial]], [[assistencialidade]] — virão de outras obras.
- Contradições: nenhuma (primeira obra do corpus reiniciado).
- Confiança: tenepes média (definição direta + verpon); demais baixa (fonte única).

## [2026-06-24 01:00] ingest | Manual da Proéxis (`corpus/proexis.json`, 750 registros)
- Calibração: usuário escolheu modo "mais completo" + os 4 grupos (núcleo / compléxis-moréxis / apoio / técnicas).
- Obra catalogada: [[manual-da-proexis]].
- Verbetes criados (15): [[proexis]], [[miniproexis]], [[maxiproexis]], [[antiproexis]], [[complexis]], [[incomplexis]], [[multicomplexis]], [[morexis]], [[minimorexis]], [[maximorexis]], [[energia-consciencial]], [[tridotacao-consciencial]], [[ectopia-consciencial]], [[macrossoma]], [[desperto]].
- Técnicas criadas (2): [[tecnica-execucao-proexis]], [[tecnica-ainda-nao-e]].
- Lacuna do tnp preenchida: [[energia-consciencial]] (cap. 25).
- Pares conjugados: miniproexis↔maxiproexis · complexis↔incomplexis · morexis(mini/maxi) · proexis↔antiproexis · ec↔energia-imanente.
- Definições diretas (ipsis litteris) em: proexis, miniproexis, maxiproexis, antiproexis, morexis, minimorexis, tridotacao, energia-consciencial, desperto.
- Lacunas abertas: [[energia-imanente]], [[holocarmalidade]], [[seriexis]], [[soma]], [[mentalsoma]], [[holochacra]], [[dupla-evolutiva]], [[holomaturidade]], [[amparador]], [[maximecanismo]], [[assistencialidade]], [[ressoma]] — virão das próximas obras.
- Contradições: nenhuma.

## [2026-06-24 01:30] ingest | Temas da Conscienciologia (`corpus/temas.json`, 721 registros)
- Calibração: modo "mais completo" + os 4 grupos (núcleo / holossomática-chacras / invéxis / fenômenos-técnicas).
- Natureza: coletânea panorâmica — ilustra mais do que define; pgs. marcadas "definição direta pendente (reforçar com EC)" onde Temas não traz definição formal.
- Obra catalogada: [[temas-da-conscienciologia]].
- Verbetes criados (12): [[teatica]] (def. direta), [[cosmoetica]], [[multidimensionalidade]], [[holocarmalidade]], [[holomaturidade]], [[verpon]], [[holossomatica]], [[laringochacra]], [[subcerebro-abdominal]] (def. direta), [[inversora-existencial]], [[conscienciometria]], [[consciencioterapia]].
- Fenômenos criados (2): [[projecao-consciente]], [[eqm]] (def. direta).
- Técnicas criadas (2): [[tecnica-respiracao-ritmica]] (def. direta), [[tecnica-abertura-da-porta]].
- Pares conjugados: conscienciometria↔consciencioterapia · projecao-consciente↔eqm · teatica↔cosmoetica.
- Controvérsia anotada: localização da EQM no lobo temporal (ciência) vs. parafenômeno (cap. 88) — em [[eqm]].
- Pendências para EC: definições formais de cosmoetica, multidimensionalidade, holocarmalidade, holomaturidade, holossomatica, verpon, laringochacra, inversora-existencial, conscienciometria, consciencioterapia.
- Contradições entre fontes do corpus: nenhuma.

## [2026-06-24 02:00] ingest | Manual da Dupla Evolutiva (`corpus/dupla.json`, 783 registros)
- Calibração: criar dupla-evolutiva (rico) + sexossomatica + primener.
- Obra catalogada: [[manual-da-dupla-evolutiva]] (monografia que cruza o conceito com 40 especialidades).
- Verbetes criados (3): [[dupla-evolutiva]] (def. direta, cap. 1; confiança média), [[sexossomatica]] (def. direta, cap. 39), [[primener]] (def. direta, cap. 14).
- Pares conjugados: dupla-evolutiva↔primener · dupla-evolutiva↔sexossomatica · 3 etapas a dois (proexis→complexis→morexis).
- Cross-refs adicionados em páginas existentes via links: proexis/complexis/morexis (etapas a dois), tares, homo-sapiens-serenissimus (pendente).
- Lacunas: [[homo-sapiens-serenissimus]] (Serenão; par ideal), Conviviologia como especialidade.
- Contradições: nenhuma.

## [2026-06-24 02:45] ingest | 200 Teáticas da Conscienciologia (`corpus/200teat.json`, 1.945 registros) — 1º lote
- Calibração: usuário fixou regra "sempre o mais completo, todos os grupos" (registrada em memória).
- Obra catalogada: [[200-teaticas-da-conscienciologia]] (glossário de 200 verbetes; ~180 restam como cauda longa).
- Lacunas centrais criadas (6): [[holopensene]], [[amparador]], [[assistencialidade]], [[estado-vibracional]], [[assim-desassim]], [[acoplamento-aurico]].
- Família pensene criada (8): [[pensene]], [[autopensene]], [[contrapensene]], [[materpensene]], [[primopensene]], [[xenopensene]], [[fitopensene]], [[assinatura-pensenica]].
- Cluster projeciologia criado (5): [[curso-intermissivo]], [[holomemoria]], [[descoincidencia-vigil]], [[base-fisica-do-projetor]], [[clarividencia-viajora]].
- Defs diretas fortes: holopensene, estado-vibracional, assim/desassim, autopensene, primopensene, holomemoria, amparador, assistencialidade, assinatura-pensenica.
- Lacunas do tnp/proexis preenchidas: [[amparador]], [[assistencialidade]], [[estado-vibracional]], [[holopensene]].
- Pares conjugados: pensene↔holopensene · assim↔desassim · materpensene→holopensene · base-fisica→ofiex · curso-intermissivo↔intermissao.
- Contradições: nenhuma.

## [2026-06-24 03:15] convergência | 200 Teáticas → 20 páginas existentes
- Reforço por convergência (fontes_count 1→2; seção `## Convergência: 200 Teáticas` com citação direta): [[energia-consciencial]] (71), [[ofiex]] (123), [[epicon]] (73), [[complexis]] (37), [[proexis]] (153), [[morexis]] (122), [[cosmoetica]] (53), [[ectopia-consciencial]] (68), [[macrossoma]] (111), [[tridotacao-consciencial]] (194), [[dupla-evolutiva]] (67), [[conscienciometria]] (47/167), [[consciencioterapia]] (48), [[holossomatica]] (99/132), [[subcerebro-abdominal]] (183), [[inversora-existencial]] (109), [[tenepes]] (187), [[tacon]] (185), [[tares]] (186), [[sexossomatica]] (177).
- Confiança elevada baixa→média em 16 páginas; mantida média (2 fontes) nas que já estavam.
- [[cosmoetica]]: definição formal direta do 200teat (cap. 53) substituiu a síntese provisória — pendência de definição resolvida.
- Ferramenta nova: `tools/sync_index_counts.py` sincroniza as contagens `(N)` do index.md com o `fontes_count` real (rodada após a convergência; 0 divergências restantes).
- Sem novas páginas. Contradições: nenhuma.

## [2026-06-24 04:00] ingest | Enciclopédia + fechamento das lacunas (multi-fonte)
- Achado: a Enciclopédia (`ec`) cataloga neologismos específicos; termos-base (holossoma, holochacra, psicossoma, consciex, projeciologia…) **não** têm verbete próprio nela → definidos a partir da melhor fonte do corpus para cada um.
- Obra catalogada: [[enciclopedia-da-conscienciologia]] (`ec.json`).
- 20 verbetes criados, fechando TODAS as lacunas de links: [[soma]] (ec), [[intermissao]] (ec), [[holossoma]] (200teat+proj), [[holochacra]] (hsp), [[psicossoma]] (proj), [[mentalsoma]] (200teat), [[consciex]] (hsr), [[conscin]] (hsr), [[energia-imanente]] (700exp+200teat), [[ressoma]] (200teat), [[seriexis]] (200teat+hsp), [[holorgasmo]] (200teat+700exp), [[homo-sapiens-serenissimus]] (hsp), [[maximecanismo]] (dac+hsp), [[projeciologia]] (200teat), [[pensenologia]] (200teat), [[patopensene]] (hsp), [[mentalsomatica]] (proexis+200teat), [[evoluciologia]] (200teat), [[sociex]] (200teat).
- Lint de links: **0 links internos quebrados** (eram 17). Wiki internamente fechada.
- Fontes novas usadas como referência de definição (a catalogar em ingest dedicado): `proj`, `hsp`, `hsr`, `700exp`, `dac`.
- `sync_index_counts.py` rodado: index consistente.
- Contradições: nenhuma.

## [2026-06-24 05:00] ingest | 700 Experimentos da Conscienciologia (`corpus/700exp.json`, 4.019 registros) — fundamentos
- Obra catalogada: [[700-experimentos-da-conscienciologia]] (tratado experimental/metodológico, 700 caps.).
- Verbetes fundamentais criados (6): [[conscienciologia]] (def. da própria ciência, cap. 24), [[paradigma-consciencial]] (cap. 28 + proj cap. 2), [[conscienciometrologia]] (cap. 3), [[universalismo]] (cap. 573), [[cosmoconsciencia]] (ec, Comunicologia), [[autoconscientizacao-multidimensional]] (ec + 700exp cap. 628).
- Técnica criada (1): [[autodefesa-energetica]] (cap. 55).
- Convergência (700exp como fonte adicional): [[energia-consciencial]] (2→3), [[tenepes]] (2→3), [[inversora-existencial]] (2→3), [[cosmoetica]] (2→3), [[primener]] (1→2). [[holorgasmo]] e [[energia-imanente]] já citavam 700exp.
- Pares conjugados: conscienciologia↔paradigma-consciencial · conscienciometria↔conscienciometrologia · universalismo↔cosmoconsciencia.
- Lint: 0 links internos quebrados; `sync_index_counts.py` aplicado (5 contagens elevadas). 42 páginas em confiança média.
- Fontes a catalogar ainda: proj, hsp, hsr, dac.
- Contradições: nenhuma.

## [2026-06-24 05:45] ingest | Projeciologia (`corpus/proj.json`, 8.985 registros) — cluster projetivo
- Obra catalogada: [[projeciologia-obra]] (slug distinto do verbete [[projeciologia]] para evitar colisão).
- Verbete criado (1): [[exteriorizacao-de-energias]] (cap. 291).
- Fenômenos criados (5): [[visao-panoramica-projetiva]] (cap. 55), [[autobilocacao-consciencial]] (cap. 39), [[catalepsia-projetiva]] (cap. 44), [[intuicao-extrafisica]] (cap. 51), [[estado-de-animacao-suspensa]] (cap. 65).
- [[projecao-consciente]]: definição consolidada (caps. 29–30) — **pendência resolvida**; 2ª fonte (baixa→média).
- Convergência (proj como fonte adicional): [[projeciologia]] (1→2), [[clarividencia-viajora]] (1→2), [[cosmoconsciencia]] (1→2), [[eqm]] (1→2).
- Lint: 0 links quebrados, 0 slugs duplicados; `sync_index_counts.py` aplicado. 48 páginas em confiança média.
- Cauda longa: ~500 seções da Projeciologia (centenas de fenômenos projetivos específicos) a ingerir gradualmente.
- Fontes a catalogar ainda: hsp, hsr, dac.
- Contradições: nenhuma.

## [2026-06-24 06:30] ingest | Dicionário de Argumentos da Conscienciologia (`corpus/dac.json`, 4.804 registros) — conceitos avançados
- Natureza distinta: 651 verbetes-**argumentologia** (formato argumentativo/aforístico, com campo `argumento`), não definicional. Estratégia: *definologia* da melhor fonte do corpus + seção "## Argumentologia (DAC)" com o argumento-tese citado.
- Obra catalogada: [[dicionario-de-argumentos-da-conscienciologia]].
- Verbetes criados (8): [[reciclagem-intraconsciencial]] (recin; hsr+dac), [[neoverpon]] (ec+dac), [[auto-revezamento]] (200teat+dac), [[autopesquisa]] (hsr+dac), [[interassistencialidade]] (lo+dac), [[megafraternidade]] (200teat+dac), [[grupocarma]] (lo+dac), [[conviviologia]] (dac).
- Curadoria: escolhidos conceitos avançados e centrais; descartada a maioria dos 651 (muitos hiperespecíficos/lúdicos: Banheirologia, Gargalologia, Antibaboseirologia…).
- Pares conjugados: recin↔recéxis · neoverpon↔verpon · auto-revezamento↔seriexis · interassistencialidade↔assistencialidade · megafraternidade↔cosmoetica.
- Lint: 0 links quebrados, 0 slugs duplicados; `sync_index_counts.py` consistente. 54 páginas em confiança média.
- Lacunas abertas: recéxis/recexologia, policarmalidade, interprisão-grupocármica.
- Fontes a catalogar ainda: hsp, hsr, lo.
- Contradições: nenhuma.

## [2026-06-24 07:00] ingest | Fechamento de lacunas do DAC (multi-fonte)
- Verbetes criados (3): [[recexis]] (hsr cap. 328), [[policarmalidade]] (hsp cap. 333 + 200teat cap. 144), [[interprisao-grupocarmica]] (hsr cap. 164 + lo).
- Restaurados os links em [[grupocarma]] e [[reciclagem-intraconsciencial]] (antes desfeitos para evitar quebra).
- Trinômios completados: recéxis↔recin↔Grecex; ego↔grupo↔policarma (holocarmalidade); grupocarma↔interprisão↔policarmalidade.
- Lint: 0 links quebrados; `sync_index_counts.py` consistente. 57 páginas em confiança média.
- Contradições: nenhuma.

## [2026-06-24 07:30] ingest | Homo sapiens reurbanisatus (`corpus/hsr.json`, 8.407 registros) — núcleo da reurbanização
- Obra catalogada: [[homo-sapiens-reurbanisatus]] (extensa/taxonômica; ingestão curada nos conceitos próprios).
- Verbetes criados (5): [[reurbex]] (tese da obra, caps. 25/86), [[consreu]] (cap. 44/304), [[baratrosfera]] (ec + hsr), [[transmigracao-consciencial]] (cap. 304), [[semiconsciex]] (cap. 65).
- Curadoria: descartadas centenas de seções pontuais (tecnologia, taxonomias, neologística, variáveis da Enciclopédia).
- Pares conjugados: reurbex↔baratrosfera · reurbex↔consreu · consreu↔transmigracao · semiconsciex↔desperto (escala evolutiva).
- Lint: 0 links quebrados; index consistente. 62 páginas em confiança média.
- Fontes a catalogar ainda: hsp, lo.
- Contradições: nenhuma.

## [2026-06-24 08:00] ingest | Homo sapiens pacificus (`corpus/hsp.json`, 6.965 registros) — SEA e correlatos
- Obra catalogada: [[homo-sapiens-pacificus]] (antibelicismo/pacificação; ingestão curada).
- Verbetes criados (5): [[sindrome-da-ectopia-afetiva]] (SEA, conceito-tese, cap. 8), [[trafor-trafar]] (par traço-força/traço-fardo, cap. 208), [[egocarma]] (cap. 52 — fecha o trinômio ego/grupo/poli), [[dessoma]] (cap. 51), [[porao-consciencial]] (200teat cap. 145 — fecha link de trafor-trafar).
- Curadoria: descartadas as extensas casuísticas da SEA (cinologia, maternidade, pedofilia, tabagismo…) e taxonomias.
- Trinômio holocármico agora completo: [[egocarma]] ↔ [[grupocarma]] ↔ [[policarmalidade]].
- Pares conjugados: trafor↔trafar · dessoma↔ressoma · SEA↔patopensene · porão↔subcérebro-abdominal.
- Lint: 0 links quebrados; index consistente. 65 páginas em confiança média.
- Fontes a catalogar ainda: lo (Léxico de Ortopensatas).
- Contradições: nenhuma.

## [2026-06-24 08:30] lint | health-check completo da base (126 páginas)
- Ferramenta nova: `tools/lint.py` (links quebrados, órfãs, frontmatter, slug≠arquivo, duplicados, status/confiança). Relatório: `wiki/lint-reports/2026-06-24.md`.
- Mecânico: **0 links quebrados, 0 órfãs, 0 frontmatter inválido, 0 slug≠arquivo, 0 slugs duplicados**.
- Corrigidos nesta passada: órfã [[base-fisica-do-projetor]] (inbound de [[ofiex]]); bug do lint contando o próprio relatório (exclusão de `lint-reports/`).
- Lacuna textual fechada: [[ortopensene]] (par de [[patopensene]]). Pendentes menores: cognópolis, holodiscernimento, conscienciês, hiperacuidade, neopensene, grecex.
- Contradições não-anotadas: nenhuma (autor único, corpus consistente).
- Backlog: 57 páginas em rascunho (fonte única) aguardam convergência (via `lo` e cauda longa do 200teat).

## [2026-06-27 00:00] fix | reparo do corpus/index.json e atualização da lista de fontes
- **Bloqueio resolvido:** `corpus/index.json` não existia → todas as ferramentas (`corpus.py`, `search.py`, `lint.py`) quebravam com `FileNotFoundError`. Regenerado a partir dos metadados internos (`index_id`/`book_name`) de cada JSON. Nenhum dado perdido.
- **Lista de fontes atualizada:** o corpus agora tem **13 fontes** (66.905 registros). Foram retiradas propositalmente 4 fontes que existiam antes: `mini_arlindo`, `proj1986`, `quest`, `zefiro`. O índice reflete só as 13 atuais.
- **Bug corrigido em `corpus.py`:** o arquivo da Enciclopédia é `ecwv.json` mas seu `index_id` é `ec`; `iter_records` procurava `ec.json` (inexistente) e pulava a obra. Agora o índice carrega o mapeamento `index_id→file` (campo `file`) e o `corpus.py` o utiliza (fallback `<id>.json`). Enciclopédia voltou a ser indexável.
- Lint de baseline (`tools/lint.py --no-write`): 126 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter inválido, 0 slug≠arquivo, 0 duplicados**. Status: 69 revisado / 57 rascunho. Confiança: 11 alta / 65 média / 50 baixa.
- **Pendências de ingest reavaliadas:** das 13 fontes, faltam catalogar/ingerir apenas `ccg` (Conscienciograma, 1.980 reg., intocada) e `lo` (Léxico de Ortopensatas, 25.187 reg., usada só incidentalmente). As outras 11 já são obras catalogadas.

## [2026-06-27 01:00] ingest | Fechamento das 6 lacunas textuais pendentes (multi-fonte)
- Verbetes criados (6), fechando as lacunas listadas no lint de 24/06: [[cognopolis]] (ec+lo), [[holodiscernimento]] (hsp cap. 333 + hsr cap. 316 + dac), [[consciencies]] (proj caps. 269/329), [[hiperacuidade]] (ec, def. direta), [[neopensene]] (ec, def. direta + lo), [[grecex]] (proexis cap. 12 + 700exp cap. 655).
- Backlinks adicionados (§5.1.7) para evitar órfãs: [[conviviologia]]→cognópolis, [[policarmalidade]]→holodiscernimento, [[universalismo]]→conscienciês, [[primener]]→hiperacuidade, [[neoverpon]]→neopensene, [[recexis]]→grecex.
- Pares/cadeias: neopensene↔neoverpon · hiperacuidade↔holodiscernimento (cadeia da autopancognição) · grecex↔recéxis (e análogo grinvex↔invéxis) · conscienciês↔mentalsoma.
- Lint: 132 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter inválido, 0 slug≠arquivo, 0 duplicados**. Relatório: `wiki/lint-reports/2026-06-27.md`.
- Pendências de ingest restantes: catalogação formal das obras [[conscienciograma]] e [[lexico-de-ortopensatas]]; convergência via `lo` das ~56 páginas em confiança baixa (não solicitada nesta passada).

## [2026-06-27 01:30] ingest | Catalogação do Léxico de Ortopensatas (`corpus/lo.json`, 25.187 reg.)
- Obra catalogada: [[lexico-de-ortopensatas]] — maior fonte do corpus (~7.508 temas de ortopensatas; estrutura aforística title+text+page). Natureza não-definicional: entra como camada de convergência/reforço, não de definologia (mesma filosofia do DAC).
- Inbound garantido (anti-órfã): link [[lexico-de-ortopensatas]] adicionado nas 5 páginas que já a citam como fonte — [[cognopolis]], [[neopensene]], [[grupocarma]], [[interassistencialidade]], [[interprisao-grupocarmica]].
- index.md: Obras 11→12; nota de pendências reduzida a apenas `ccg` (Conscienciograma, deixado de fora a pedido).
- Lint: 133 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter inválido, 0 slug≠arquivo, 0 duplicados**.
- Pendência restante: convergência sistemática via `lo` das ~56 páginas em confiança baixa (não solicitada nesta passada); catalogação do `ccg` (adiada).

## [2026-06-27 02:00] ingest | Convergência via Léxico de Ortopensatas (lote 1) — 32 páginas baixa→média
- Estratégia: para cada conceito com cobertura direta no `lo`, adicionada seção `## Convergência: Léxico de Ortopensatas` com 1 ortopensata substantiva citada (obra + página), elevando confiança baixa→média e status rascunho→revisado.
- Aplicação mecânica via script Python (julgamento LLM = escolha da ortopensata; aplicação determinística = inserção/frontmatter/log), descartado após uso.
- Páginas convergidas (30): amparador, antiproexis, assistencialidade, autopensene, consciencies, conscienciometrologia, conscin, conviviologia, desperto, egocarma, hiperacuidade, holomaturidade, incomplexis, laringochacra, materpensene, maximecanismo, maximorexis, maxiproexis, miniproexis, multidimensionalidade, neopensene, patopensene, pensene, primopensene, psicossoma, teatica, universalismo, verpon, cognopolis, ortopensene.
- Correção de fontes_count subcontado na criação (sem nova seção lo): holodiscernimento (3), grecex (2).
- Resultado global: **revisado 101 / rascunho 32**; **confiança alta 12 / média 96 / baixa 25** (antes: média 65 / baixa 56).
- Lint: 133 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**. `sync_index_counts.py` consistente.
- Restam baixa (25): conceitos sem verbete-título direto no `lo` (acoplamento-aurico, assim-desassim, contrapensene, xenopensene, fitopensene, sociex, holocarmalidade, soma, holochacra, mentalsoma, consciex, intermissao, ressoma, multicomplexis, minimorexis, etc.) — convergência exige busca temática (lote 2, não nesta passada).

## [2026-06-27 02:30] ingest | Convergência lote 2 (busca temática) — 18 páginas baixa→média
- Para conceitos sem verbete-título direto no Léxico, a convergência veio de menção temática (a máxima sob outro verbete do `lo`) ou de 2ª fonte em outra obra.
- Via Léxico (10): descoincidencia-vigil, intuicao-extrafisica, autodefesa-energetica, assim-desassim, assinatura-pensenica (Grafopensene), base-fisica-do-projetor (Base), porao-consciencial (Porão), xenopensene (Lateropensene), estado-de-animacao-suspensa (Animação), holocarmalidade (Tenepes), curso-intermissivo (verbete *CI*, p. 402).
- Via outra obra (5): contrapensene (200teat cap. 52), fitopensene (200teat cap. 89), acoplamento-aurico (hsr cap. 317 — acoplamento energético), minimorexis (ec, verbete Minimoréxis), sociex (700exp cap. 154).
- Flag corrigida (já tinham 2 fontes): grupocarma, paradigma-consciencial.
- Resultado global: **revisado 120 / rascunho 13**; **confiança alta 12 / média 115 / baixa 6**.
- Baixa restantes (6) — fonte única legítima: catalepsia-projetiva (só Projeciologia), multicomplexis (só Manual da Proéxis), e as 4 técnicas procedimentais (tecnica-abertura-da-porta, tecnica-ainda-nao-e, tecnica-execucao-proexis, tecnica-respiracao-ritmica).
- Lint: 133 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.

## [2026-06-27 03:00] método | Virada de doutrina: enumerar-primeiro + cobertura em massa da Enciclopédia
- **Diagnóstico:** cobertura conceitual real era ínfima — EC 31/2.019 (1,5%), DAC 3/652 (0,5%). Causa: ingest "search-driven + curadoria que descarta a maioria" tem baixo recall por design, não falha de leitura.
- **Doutrina nova (AGENTS §5.1):** dois regimes. (A) Fontes-dicionário (EC, DAC) = *enumerar-primeiro*: separar COBERTURA (mecânica, Python) de PROFUNDIDADE (LLM). (B) Fontes discursivas = busca, como antes.
- **Tools novas:** `tools/inventory.py` (mede cobertura/lacunas) e `tools/build_stubs.py` (gera stubs + catálogo).
- **Execução:** gerados **1.988 verbetes-stub** da EC (`status: stub`, `gerado: auto`, Definologia ipsis litteris + citação, classificados por especialidade). Cobertura EC: 1,5% → **100%**. Páginas curadas (107) intactas, não sobrescritas.
- Catálogo `wiki/catalogo-ec.md` (2.019 verbetes por área) dá inbound a cada stub → 0 órfãs.
- `lint.py` ajustado: exclui `catalogo*.md`; isenta `status: stub` da checagem de órfãs.
- Lint: **2.121 páginas** (verbete 2.095, obra 12, técnica 5, fenômeno 9); status revisado 120 / rascunho 13 / stub 1.988; **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 slug≠arquivo, 0 duplicados**.
- Próximo: enriquecimento por tier (stub→rascunho→revisado) das especialidades prioritárias; mesmo tratamento para DAC (652).

## [2026-06-27 03:30] método | Mineração de relações por co-ocorrência nos stubs
- Tool nova: `tools/mine_links.py` — varre a Definologia de cada stub, detecta menções a conceitos existentes (match por título/slug com fronteira de palavra) e preenche `## Conexões internas`. Conservador: só toca `status: stub` com placeholder; não altera páginas curadas.
- Anti-ruído: (a) remove a linha de citação ("— Extraído da…") antes de minerar (senão todo stub linkava para a obra/"verbete"); (b) filtro automático de frequência (alvo que casaria em >200 stubs = genérico, descartado) + stoplist (conscin, efeito, conhecimento…).
- Resultado: **1.639 relações** criadas em **982 stubs** (avg 0,8/stub); 1.006 stubs sem relação (definição curta sem menção nominal a outro conceito — não forçado).
- Lint: 2.121 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto**. Malha interna densificada sem custo de LLM.
- Próximo: enriquecimento por tier (stub→revisado) das especialidades prioritárias; relações dos 1.006 stubs restantes dependem de leitura semântica (LLM), não de match léxico.

## [2026-06-27 04:00] método | build_stubs generalizado para o DAC + conceitos-núcleo embutidos
- `tools/build_stubs.py` agora aceita `--book ec|dac`. Para o DAC (verbetes-argumentologia): 1 stub por verbete (-logia) com o argumento-líder citado em `## Argumentologia (DAC)`.
- **Detecção de conceito embutido** (pedido do usuário): o conceito-núcleo do verbete (n-grama recorrente, freq≥3, cuja raiz bate com o título) é capturado como `alias` pesquisável. Ex.: verbete *Inacabamentologia* → alias *Inacabamento a Maior* (p. 787). 76 verbetes ganharam alias-conceito.
- Correções de suporte: `corpus.py` passou a ler também a chave `page` (DAC usa `page`, não `pagina`/`number`) — citações do DAC agora trazem página; title-case de alias preserva artigos minúsculos.
- `mine_links.py` estendido para minerar também a seção `## Argumentologia (DAC)` (antes só `## Definologia`); bug do delimitador `\n## ` consumido corrigido (lookahead); descarte de notas boilerplate (`>`).
- **Execução:** 614 stubs do DAC criados; mineração adicionou 1.557 relações (542 stubs com ≥1 link; ex.: grupocarmologia → grupocarma, inseparabilidade-grupocarmica).
- Cobertura (inventory.py): **EC 100% (2.019/2.019), DAC 98,5% (642/652)** — os 10 ausentes são títulos estruturais (Introdução, Apresentação…) deliberadamente pulados.
- Catálogo `wiki/catalogo-dac.md` (dá inbound aos stubs; lista aliases).
- Lint: **2.735 páginas** (verbete 2.709); **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 slug≠arquivo, 0 duplicados**.

## [2026-06-27 04:30] enriquecimento | Tier 1 — especialidade Intermissiologia (18 stubs → revisado)
- Primeiro lote de enriquecimento por tier (stub → revisado): a especialidade Intermissiologia inteira (18 verbetes do ciclo intermissão↔vida).
- **Relações semânticas curadas** (o que o match léxico do `mine_links` não pega): cada verbete recebeu Conexões internas com glosa, tecendo a teia da especialidade (tipos de intermissão · o intermissivista · processos do CI · pós-dessoma).
- **Convergência (2ª fonte)** em 5: [[melex]] (lo p.1273 — "melancolia sem soma"), [[intermissao-prolongada]] (lo p.1090), [[intermissivista]] (lo p.1093 — "nouveau riche evolutivo"), [[comite-de-pararrecepcao]] (lo p.1487), [[bagagem-pre-ressomatica]] (hsr p.210) → confiança baixa→média.
- **Hub da especialidade**: [[intermissao]] ganhou seção "Verbetes da Intermissiologia" linkando o cluster — dá inbound a todos (necessário porque, ao promover stub→revisado, perde-se a isenção de órfã do lint; o catálogo não conta como inbound). **Padrão reutilizável para os próximos tiers.**
- Global: revisado 120→**138**; confiança média 115→**120**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 duplicados**.
- Próximas especialidades candidatas (centrais, tratáveis): Recexologia (19), Proexologia (24), Cosmoeticologia (37), Energossomatologia (27).

## [2026-06-27 05:00] tooling | Automação da busca de convergência (acelera os tiers)
- Tool nova: `tools/converge.py` — para cada stub de uma especialidade, roda BM25 excluindo a(s) fonte(s) de origem já citada(s) e devolve os melhores candidatos a 2ª fonte (citação pronta, score, marca ★ de força), filtrando trechos não-definicionais (taxonomias, sinonímia, enumerações).
- Elimina a busca manual concept-a-concept do tier: `python tools/converge.py --esp <X> -o cand.txt` gera a tabela de candidatos pronta para o julgamento do LLM.
- Validação: `--esp Recexologia` → 19 conceitos, 6 com candidato forte; ruído de taxonomia removido pelo filtro.
- Doutrina §5.1-A atualizada com o fluxo do tier (converge → escolher/redigir → seção-hub anti-órfã) e tabela de tools §8 atualizada.

## [2026-06-27 05:30] enriquecimento | Tier 2 — especialidade Recexologia (19 verbetes → revisado) via converge.py
- Primeiro tier usando `converge.py`: `--esp Recexologia` levantou candidatos a 2ª fonte de 19 conceitos (6 fortes) numa só passada — eliminou a busca manual concept-a-concept do tier anterior.
- **Relações semânticas curadas** nos 18 stubs + relação da teia (núcleo · mecanismos · disposição · resultados · patologias).
- **Convergência (2ª fonte)** em 5: [[descarte-dos-resquicios]] (proj cap.148 — 2ª dessoma), [[autoprontidao]] (dac, Recinologia), [[retificacao]] (Temas cap.58), [[retomador-de-tarefa]] (lo p.1746), [[autofagia]] (hsr cap.223) → baixa→média.
- **Deduplicação:** o stub [[recin]] (EC) duplicava a canônica [[reciclagem-intraconsciencial]]. Resolvido: alias *Recin* + convergência lo (p.1703) absorvidos na canônica (fontes 2→3); o stub virou página-companheira com cross-ref explícito (preserva a Definologia própria da EC sobre neossinapses). Inventory futuro já marca o conceito coberto via alias.
- **Hub**: [[recexis]] (eponym da Recexologia) ganhou seção "Verbetes da Recexologia" linkando o cluster → 0 órfãs.
- Global: revisado 138→**157**; confiança média 120→**126**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 duplicados**.
- Ganho de velocidade confirmado: o gargalo do tier passou a ser só o julgamento/redação; o levantamento de fontes é automático.

## [2026-06-27 06:00] enriquecimento | Tier 3 — especialidade Proexologia (24 verbetes → revisado)
- `converge.py --esp Proexologia`: 24 conceitos, 13 fortes (especialidade central, bem coberta no corpus).
- **Relações semânticas curadas** nos 24, organizadas em planejamento · execução/produção · recursos · desafio/desfecho · desvios.
- **Convergência (2ª fonte) em 12**: abstencionismo-consciencial (200teat cap.2), alavancagem-da-proexis (lo), amplitude-autopensenica (dac, Megarrecexologia), atitude-antiproexis (proexis cap.17), autodesempenho-proexologico (lo p.1638), autodestravamento (lo), clausula-petrea (lo, Codigologia), desafio-da-proexis (proexis cap.32), desviacionismo (lo), gescon (lo), inventariologia (lo), priorizacao-da-proexis (proexis cap.24) → baixa→média.
- **Hub**: [[proexis]] ganhou seção "Verbetes da Proexologia" linkando o cluster → 0 órfãs.
- Global: revisado 157→**181**; confiança média 126→**138**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 duplicados**.
- Três especialidades centrais concluídas (Intermissiologia, Recexologia, Proexologia); padrão converge→julgar→hub estável e rápido.

## [2026-06-27 06:30] enriquecimento | Tier 4 — especialidade Cosmoeticologia (37 verbetes → revisado)
- `converge.py --esp Cosmoeticologia`: 37 conceitos, 23 fortes (especialidade ampla, núcleo ético).
- **Relações semânticas curadas** nos 37, ancoradas em [[cosmoetica]] e organizadas em fundamentos · virtudes/condutas · técnicas/processos · atributos · desvios/patologias.
- **Convergência (2ª fonte) em 28** — maior rendimento de um tier até aqui: autossacrificio, autexemplificacao, principio-do-exemplarismo-pessoal (hsp), catarse-cosmoetica (700exp), senso-universalista (hsr), paradever/paradireito/limite-cosmoetico/lisura/gratuidade-cosmoetica/concessao-cosmoetica/calculismo-cosmoetico/codigo-pessoal-de-cosmoetica/ortopensenidade (lo), megaexplicitacao-cosmoetica (dac), vacuo-cosmoetico (proj), entre outros → baixa→média.
- **Hub**: [[cosmoetica]] ganhou seção "Verbetes da Cosmoeticologia" linkando o cluster → 0 órfãs.
- Global: revisado 181→**218**; confiança média 138→**166**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 duplicados**.
- Quatro especialidades concluídas (Intermissiologia, Recexologia, Proexologia, Cosmoeticologia). 218 páginas revisadas; 166 em confiança média.

## [2026-06-27 07:00] enriquecimento | Tier 5 — especialidade Energossomatologia (27 verbetes → revisado)
- `converge.py --esp Energossomatologia`: 27 conceitos, 10 fortes (energossoma/bioenergética).
- **Relações semânticas curadas** nos 27, ancoradas em [[holochacra]] (=energossoma)/[[energia-consciencial]]/[[estado-vibracional]], organizadas em ECs e estados · técnicas/manobras · estado vibracional · primener/ciclos · acoplamento/papéis · desvios.
- **Convergência (2ª fonte) em 14**: acoplador-energetico/abuso-das-ECs (hsr cap.318), agente-antiprimener (hsp), assim (700exp cap.273), balonamento (tnp), banho-energetico (proj), energia-consciencial-gasta (700exp), qualificacao/usina-consciencial (200teat), cipriene/dimener/encapsulamento/evolucao-energossomatica/mimo-energetico (lo) → baixa→média.
- Nota: [[assim]] (stub EC) cross-linkado ao par canônico [[assim-desassim]]; descartado o ruído de etimologística nos candidatos.
- **Hub**: [[holochacra]] ganhou seção "Verbetes da Energossomatologia" → 0 órfãs.
- Global: revisado 218→**245**; confiança média 166→**180**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 duplicados**.
- Cinco especialidades concluídas (Intermissiologia, Recexologia, Proexologia, Cosmoeticologia, Energossomatologia).

## [2026-06-27 08:00] enriquecimento | Tier 6 — especialidade Autodiscernimentologia (58 verbetes → revisado)
- `converge.py --esp Autodiscernimentologia`: 58 conceitos, 16 fortes — primeiro tier "grande" (lote ~2x os anteriores).
- **Relações semânticas curadas** nos 58, ancoradas em [[autodiscernimento]] e organizadas em razão/análise · percepção/crítica · priorização/escolha · conduta/atributos · antagonismos (subcluster) · desvios.
- **Convergência (2ª fonte) em 24**: adorno-consciencial, ajuizamento-pessoal, autesforco-convergente, autodespriorizacao, autorresolucao, detalhe-irretocavel, douta-ignorancia, pertinencia-evolutiva, primeira-impressao, pseudobem (lo); amor-doador (700exp), autodiscernimento-dinamico (hsr), antagonismo/antagonismo-midiatico (hsp), objetivo-prioritario (dupla), visao (proj); antagonismologia-patologica, criteriologia, fatofilia, megarrecexologia, olho-clinico, preferenciologia, principiologia, refem-da-autocognicao, rigor-racionalistico (dac) → baixa→média.
- **Hub**: [[autodiscernimento]] ganhou seção "Verbetes da Autodiscernimentologia" linkando os 58 → 0 órfãs (o hub é eponym de Holomaturologia, mas é o âncora natural do cluster).
- Global: revisado 245→**303**; confiança média 180→**205**.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 frontmatter incompleto, 0 slug≠arquivo, 0 duplicados**.
- Seis especialidades concluídas (Intermissiologia, Recexologia, Proexologia, Cosmoeticologia, Energossomatologia, Autodiscernimentologia). Padrão converge→julgar→hub mantém-se estável mesmo no lote grande.

## [2026-06-27 08:30] enriquecimento | Tier 7 — especialidade Conviviologia (67 verbetes → revisado)
- `converge.py --esp Conviviologia`: 67 conceitos, 23 fortes. Motor genérico de aplicação criado (`scratch/tier_engine.py` + módulo de dados por especialidade) para acelerar os tiers grandes.
- **Relações semânticas curadas** nos 67, ancoradas em [[conviviologia]] e organizadas em amizade/companhia · relações/vínculos · convivialidade/plenitude · casal/dupla · convívio patológico · binômios/posicionamentos · exposição social · conduta/processos.
- **Convergência (2ª fonte) em 46** (maior rendimento absoluto de um tier): destaque para casal-incompleto e binomio-admiracao-discordancia (200teat), companhia-eletiva/fusao-social/comunidade-CCCI (dac), amizade-rarissima/anticonscienciologista/aglutinacao (lo), dependencia-indireta/elenco (hsr), entrevista-evolutiva (hsp), intersubjetividade (proj) → baixa→média.
- **Hub**: [[conviviologia]] ganhou seção "Verbetes da Conviviologia" linkando os 67 → 0 órfãs.
- Global: revisado 303→**370**; confiança média 251 / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Sete especialidades concluídas. Engine reutilizável reduz o tier ao julgamento (relações + escolha da convergência).

## [2026-06-27 09:00] enriquecimento | Tier 8 — especialidade Mentalsomatologia (70 verbetes → revisado)
- `converge.py --esp Mentalsomatologia`: 70 conceitos, 26 fortes. Maior tier até aqui.
- **Relações curadas** nos 70, ancoradas em [[mentalsoma]]: atenção/cognição · ideias/criatividade · técnicas/ritmo · autorado/produção · livros/saber · epistemologia · estados diversos.
- **Convergência (2ª fonte) em 61** (recorde absoluto): neologismos da Mentalsomática no hsr (aperitivo-intelectual, aquecimento-neuronal, cosmossíntese), princípio-da-descrença/princípio-organizador-dos-saberes/paradoxo-da-conscienciologia (lo), ciclo-mentalsomático/confor (200teat), ideia-original (700exp), bibliologia/topico-intelectivo/intraconscienciologia (dac) → baixa→média.
- **Hub**: [[mentalsoma]] ganhou seção "Verbetes da Mentalsomatologia" linkando os 70 → 0 órfãs.
- Global: revisado 370→**440**; confiança média **312** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Oito especialidades concluídas.

## [2026-06-27 09:45] enriquecimento | Tier 9 — especialidade Evoluciologia (93 verbetes → revisado)
- `converge.py --esp Evoluciologia`: 93 conceitos, 32 fortes. Maior tier executado.
- **Relações curadas** nos 93, ancoradas em [[evoluciologia]]: autevolução/processos · tempo/ciclo · escalas/níveis · agentes evolutivos · escala serenológica (pré-serenão→CL) · desafios/crises · hipóteses/teoria · desvios.
- **Convergência (2ª fonte) em 52**: escala-da-consciência-contínua (700exp, 7 estágios), continuísmo/gestação/consciência-podálica (200teat), antissubumanidade/holomaturologia/epicon-lúcido/teleguiado-autocrítico/microminoria (hsr,hsp), autopotencialização/epiconscienciologia/maximologia/negocinho-evolutivo (dac), dezenas no lo → baixa→média.
- **Hub**: [[evoluciologia]] ganhou seção "Verbetes da Evoluciologia" linkando os 93 → 0 órfãs.
- Global: revisado 440→**533**; confiança média **364** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Nove especialidades concluídas; ~533/2.735 revisadas (19,5%).

## [2026-06-27 10:30] enriquecimento | Tier 10 — especialidade Holomaturologia (64 verbetes → revisado)
- `converge.py --esp Holomaturologia`: 64 conceitos, 21 fortes.
- **Relações curadas** nos 64, ancoradas em [[holomaturidade]]: autolucidez/autoconsciência · cosmoética/intenção · orientação/bússola · filosofia/coerência · picos/amplitude · verdade/valor · desvios.
- **Convergência (2ª fonte) em 41**: amplificador-da-consciencialidade (200teat), holanálise-da-conscin/redutor-do-autodiscernimento/bússola-intraconsciencial/princípio-filosófico (hsp,hsr), lei-do-maior-esforço/inutilogia/coerenciologia (dac), trinômio-da-holomaturidade (proexis), otimização-dos-desempenhos (700exp), dezenas no lo → baixa→média.
- Nota: [[autodiscernimento]] (especialidade Holomaturologia) foi enriquecido neste tier E mantém a seção-hub "Verbetes da Autodiscernimentologia" do tier 6 — duplo papel, ambas seções coexistem.
- **Hub**: [[holomaturidade]] ganhou seção "Verbetes da Holomaturologia" linkando os 64 → 0 órfãs.
- Global: revisado 533→**597**; confiança média **405** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Dez especialidades concluídas; ~597/2.735 revisadas (21,8%).

## [2026-06-27 11:00] enriquecimento | Tier 11 — especialidade Comunicologia (58 verbetes → revisado)
- `converge.py --esp Comunicologia`: 58 conceitos, 24 fortes. Sem página eponym "comunicologia"; hub ancorado em [[tares]] (a Comunicologia serve à tarefa do esclarecimento).
- **Relações curadas** nos 58: palavra/léxico · linguagem/expressão · técnicas redacionais · escrita/verbetes · argumentação/esclarecimento · desvios.
- **Convergência (2ª fonte) em 41**: informação-conscienciológica/modelo-mentalsomático (200teat), frase-enfática/conformática/jornalismo-marrom (hsr,hsp), linguagem-mentalsomática/nomadismo/via-expressa/alexitimia (proj), enumerologia/citaciologia/holotecologia (dac), consciência-gráfica/matematização (700exp), dezenas no lo → baixa→média.
- **Hub**: [[tares]] ganhou seção "Verbetes da Comunicologia" linkando os 58 → 0 órfãs.
- Global: revisado 597→**655**; confiança média **446** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Onze especialidades concluídas; 655/2.735 revisadas (23,9%).

## [2026-06-27 11:30] enriquecimento | Tier 12 — especialidade Interassistenciologia (50 verbetes → revisado)
- `converge.py --esp Interassistenciologia`: 50 conceitos, 20 fortes.
- **Relações curadas** nos 50, ancoradas em [[interassistencialidade]]: assistência/tipos · esclarecimento/tares · amparador/consciex · minipeça/maximecanismo · assistido/condições · holopensene.
- **Convergência (2ª fonte) em 39**: evolução-tacon-tares/minipeça/ataque-paraterapêutico/amparador (lo), inversão-interassistencial (700exp), entrevista/minitares/atitude-pró-amparador/ranque (hsp,hsr), perfil-assistencial/abridor-de-caminho (dac) → baixa→média.
- **Hub**: [[interassistencialidade]] ganhou seção "Verbetes da Interassistenciologia" linkando os 50 → 0 órfãs.
- Global: revisado 655→**705**; confiança média **485** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Doze especialidades concluídas; 705/2.735 revisadas (25,8%).

## [2026-06-27 12:15] enriquecimento | Tier 13 — especialidade Experimentologia (80 verbetes → revisado)
- `converge.py --esp Experimentologia`: 80 conceitos, 27 fortes. Sem página eponym; hub em [[teatica]] (a Experimentologia é a vivência teática da pesquisa).
- **Relações curadas** nos 80: pesquisa/pesquisador · técnicas de pesquisa · análise/síntese · fundamentos/corpus · heurística/descoberta · disposição/gestão · desvios/falhas.
- **Convergência (2ª fonte) em 42**: fatuística (hsr, neologismo da Experimentologia), planilha-técnica/pesquisa-dos-50-prefácios/repetição-paciente (700exp,proj), estafa-intelectual/soltura-mentalsomática/taxologia-das-análises (200teat), técnica-da-exaustividade/circularidade/detalhismo/descrenciologia (lo), holopensenologia (dac) → baixa→média.
- **Hub**: [[teatica]] ganhou seção "Verbetes da Experimentologia" linkando os 80 → 0 órfãs.
- Global: revisado 705→**785**; confiança média **527** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Treze especialidades concluídas; 785/2.735 revisadas (28,7%).

## [2026-06-27 13:00] enriquecimento | Tier 14 — especialidade Intrafisicologia (98 verbetes → revisado)
- `converge.py --esp Intrafisicologia`: 98 conceitos, 33 fortes. Hub = eponym [[intrafisicalidade]] (também era stub: enriquecido como hub, baixa→média).
- **Relações curadas** nos 98: vida/existência · recursos/sobrevivência · soma/longevidade · habitat/sociedade · técnica/teática · cultura/ciências · desvios/patologias · condições/conscins.
- **Convergência (2ª fonte) em 41**: biofilia/biofilia-monopolizadora (200teat,hsr; neologismos da Intrafisicologia), fartura (tnp, teoria da fartura de EC), vida-programada/exigência-da-vida-humana (200teat), anomia/bairrismo/indústria-paralela (hsp,hsr), culturologia/falsidade-objetal/jubileu (dac), dezenas no lo → baixa→média.
- **Hub**: [[intrafisicalidade]] ganhou seção "Verbetes da Intrafisicologia" linkando os 97 → 0 órfãs.
- Global: revisado 785→**883**; confiança média **568** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Quatorze especialidades concluídas; 883/2.735 revisadas (32,3%).

## [2026-06-27 14:00] enriquecimento | Tier 15 — especialidade Parapatologia (137 verbetes → revisado) — MAIOR TIER
- `converge.py --esp Parapatologia`: 137 conceitos, 47 fortes. Maior cluster da base; hub = [[autassedio]].
- **Relações curadas** nos 137, em 8 eixos: assédio/possessão · autassédio/autocorrupção · vícios/dependências · desequilíbrio/síndromes · razão falha/crença · desídia/atraso · conduta anticosmoética · primitivismo/coletivo · frivolidade/menores.
- **Convergência (2ª fonte) em 90** (recorde absoluto): dezenas de patologias definidas no hsp (acídia, acriticismo, decidofobia, heterassédio, interiorose, irresponsabilidade, iscagem, ludopatia, personalismo, sarcasmo, subadultidade, subcerebralidade, sujismundismo, truculência, verborragia…), síndromes no 700exp (mediocrização, hipocondria, inautenticidade), megapatologia/SAB/megatrafar/psicopatia (lo), paracriminologia/silenciologia/adaptaciologia (dac) → baixa→média.
- **Hub**: [[autassedio]] ganhou seção "Verbetes da Parapatologia" linkando os 137 → 0 órfãs; corrigido auto-link do anchor.
- Global: revisado 883→**1.020**; confiança média **658** / alta 12. **Cruzou 1.000 páginas revisadas (37,3%).**
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Quinze especialidades concluídas.

## [2026-06-27 14:45] enriquecimento | Tier 16 — especialidade Autevoluciologia (59 verbetes → revisado)
- `converge.py --esp Autevoluciologia`: 59 conceitos, 9 fortes (especialidade menos coberta no corpus).
- **Relações curadas** nos 59, ancoradas em [[autevolucao]]: conquista/rendimento · avaliação/FEP · metas/prioridades · completude/integridade · progressão/viragem · diversos.
- **Convergência (2ª fonte) em 34**: trinômio-evolutivo/viragem-autevolutiva/FEP/completude (lo), meta-optata (700exp), modelo-contíguo/primado-evolutivo/recorrência (hsp,hsr), pertencimento/quintessência/nulificação-da-infância (dac) → baixa→média.
- **Hub**: [[autevolucao]] ganhou seção "Verbetes da Autevoluciologia" → 0 órfãs (corrigida órfã trinomio-evolutivo).
- Global: revisado 1.020→**1.079**; confiança média **692** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Dezessete especialidades concluídas; 1.079/2.735 revisadas (39,5%).

## [2026-06-27 15:15] enriquecimento | Tier 17 — especialidade Parapercepciologia (41 verbetes → revisado)
- `converge.py --esp Parapercepciologia`: 41 conceitos, 13 fortes. Hub = [[parapsiquismo]].
- **Relações curadas** nos 41: parapsiquismo/modalidades · desenvolvimento · sinais/marcas · parapercepção/medida · multidimensionalidade · desvios.
- **Convergência (2ª fonte) em 25**: antiparapsiquismo (hsp, neologismo da Parapercepciologia), visão-panorâmica/solução-parapsíquica (proj,700exp), sinalética/escala-perceptiva/multidimensionalidade (hsr,hsp), paraconscienciologia/paraconscienciometria (dac), dragona/marca/parapsiquismo-intelectual (lo) → baixa→média.
- **Hub**: [[parapsiquismo]] ganhou seção "Verbetes da Parapercepciologia" → 0 órfãs; corrigido auto-link.
- Global: revisado 1.079→**1.120**; confiança média **717** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Dezoito especialidades concluídas; 1.120/2.735 revisadas (41,0%).

## [2026-06-27 15:45] enriquecimento | Tier 18 — especialidade Psicossomatologia (31 verbetes → revisado)
- `converge.py --esp Psicossomatologia`: 31 conceitos, 12 fortes. Hub = [[psicossoma]].
- **Relações curadas** nos 31: afetividade/emoção · emoções penosas · desvios emocionais · psicossoma/parafenômenos.
- **Convergência (2ª fonte) em 24**: autoinsegurança (hsp), irrompimento-do-psicossoma (proj), dependência (hsr), endosso-sentimental (700exp), paravínculo (dac), dezenas no lo (aborrecimento, acanhamento, frustração, impaciência…) → baixa→média.
- **Hub**: [[psicossoma]] ganhou seção "Verbetes da Psicossomatologia" → 0 órfãs.
- Global: revisado 1.120→**1.151**; confiança média **741** / alta 12.
- Lint: 2.735 páginas, **0 links quebrados, 0 órfãs, 0 erros estruturais**.
- Dezenove especialidades concluídas; 1.151/2.735 revisadas (42,1%).

## [2026-06-27 16:15] enriquecimento | Tier 19 — especialidade Autexperimentologia (29 verbetes → revisado)
- `converge.py --esp Autexperimentologia`: 29 conceitos, 12 fortes. Hub = [[autopesquisa]].
- Relações curadas nos 29 (constatação/vivência · procedimento/técnica · coleta/cognição · atividade/prioridade); convergência (2ª fonte) em 25 → baixa→média.
- Hub: [[autopesquisa]] ganhou seção "Verbetes da Autexperimentologia" → 0 órfãs.
- Global: revisado 1.151→**1.180**; média **766** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte especialidades concluídas; 1.180/2.735 revisadas (43,1%).

## [2026-06-27 16:45] enriquecimento | Tier 20 — especialidade Autocogniciologia (29 verbetes → revisado)
- `converge.py --esp Autocogniciologia`: 29 conceitos, 9 fortes. Hub = [[autocognicao]] (corrigido auto-link).
- Relações curadas nos 29 (autocognição/convicção · conhecimento · cognição/apreensão · limites/desvios); convergência (2ª fonte) em 25 → baixa→média.
- Hub: [[autocognicao]] ganhou seção "Verbetes da Autocogniciologia" → 0 órfãs.
- Global: revisado 1.180→**1.209**; média **791** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e uma especialidades concluídas; 1.209/2.735 revisadas (44,2%).

## [2026-06-27 17:15] enriquecimento | Tier 21 — especialidade Conscienciometrologia (24 verbetes → revisado)
- `converge.py --esp Conscienciometrologia`: 24 conceitos, 8 fortes. Hub = [[conscienciometria]].
- Relações curadas nos 24 (medida/avaliação · perfis · conscienciólogo/base · desvios); convergência (2ª fonte) em 21 → baixa→média.
- Hub: [[conscienciometria]] ganhou seção "Verbetes da Conscienciometrologia" → 0 órfãs.
- Global: revisado 1.209→**1.233**; média **812** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e duas especialidades concluídas; 1.233/2.735 revisadas (45,1%).

## [2026-06-27 17:45] enriquecimento | Tier 22 — especialidade Autoproexologia (22 verbetes → revisado)
- `converge.py --esp Autoproexologia`: 22 conceitos, 7 fortes. Hub = [[proexis]] (2ª seção-cluster, ao lado da Proexologia).
- Relações curadas nos 22 (planejamento/tempo · balanço/inventário · compléxis/produção · carências/desvios); convergência em 18 → baixa→média.
- Hub: [[proexis]] ganhou seção "Verbetes da Autoproexologia" → 0 órfãs.
- Global: revisado 1.233→**1.255**; média **830** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e três especialidades concluídas; 1.255/2.735 revisadas (45,9%).

## [2026-06-27 18:15] enriquecimento | Tier 23 — especialidade Autopesquisologia (21 verbetes → revisado)
- `converge.py --esp Autopesquisologia`: 21 conceitos, 3 fortes. Hub = [[autopesquisa]] (2ª seção-cluster, ao lado da Autexperimentologia).
- Relações curadas nos 21 (autopesquisa/vivência · método/técnica · erro/impasse); convergência em 17 → baixa→média.
- Hub: [[autopesquisa]] ganhou seção "Verbetes da Autopesquisologia" → 0 órfãs.
- Global: revisado 1.255→**1.276**; média **847** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e quatro especialidades concluídas; 1.276/2.735 revisadas (46,7%).

## [2026-06-27 18:45] enriquecimento | Tier 24 — especialidade Autoconscienciometrologia (21 verbetes → revisado)
- `converge.py --esp Autoconscienciometrologia`: 21 conceitos, 8 fortes. Hub = [[conscienciometria]] (2ª seção-cluster).
- Relações curadas nos 21 (autoteste/autorreflexão · saúde [5 eixos] · autodesvios); convergência em 19 → baixa→média.
- Hub: [[conscienciometria]] ganhou seção "Verbetes da Autoconscienciometrologia" → 0 órfãs.
- Global: revisado 1.276→**1.297**; média **866** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e cinco especialidades concluídas; 1.297/2.735 revisadas (47,4%).

## [2026-06-27 19:15] enriquecimento | Tier 25 — especialidade Cosmovisiologia (20 verbetes → revisado)
- `converge.py --esp Cosmovisiologia`: 20 conceitos, 7 fortes. Hub = [[cosmovisiologia]].
- Relações curadas nos 20 (cosmovisão/mundividência · abordagem/método · interdependência/centrais); convergência em 17 → baixa→média.
- Hub: [[cosmovisiologia]] ganhou seção "Verbetes da Cosmovisiologia" → 0 órfãs.
- Global: revisado 1.297→**1.317**; média **883** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e seis especialidades concluídas; 1.317/2.735 revisadas (48,2%).

## [2026-06-27 19:45] enriquecimento | Tier 26 — especialidade Somatologia (20 verbetes → revisado)
- `converge.py --esp Somatologia`: 20 conceitos, 9 fortes. Hub = [[soma]].
- Relações curadas nos 20 (soma/condições · saúde/longevidade · desvios somáticos); convergência em 17 → baixa→média.
- Hub: [[soma]] ganhou seção "Verbetes da Somatologia" → 0 órfãs.
- Global: revisado 1.317→**1.337**; média **900** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e sete especialidades concluídas; 1.337/2.735 revisadas (48,9%).

## [2026-06-27 20:15] enriquecimento | Tier 27 — especialidade Extrafisicologia (19 verbetes → revisado)
- `converge.py --esp Extrafisicologia`: 19 conceitos, 5 fortes. Hub = [[extrafisicalidade]].
- Relações curadas nos 19 (ação/abordagem · bases/ofiex · realidade/procedência); convergência em 16 → baixa→média.
- Hub: [[extrafisicalidade]] ganhou seção "Verbetes da Extrafisicologia" → 0 órfãs.
- Global: revisado 1.337→**1.356**; média **916** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e oito especialidades concluídas; 1.356/2.735 revisadas (49,6%).

## [2026-06-27 20:45] enriquecimento | Tier 28 — especialidade Autoparapercepciologia (16 verbetes → revisado)
- `converge.py --esp Autoparapercepciologia`: 16 conceitos, 5 fortes. Hub = [[parapsiquismo]] (2ª seção-cluster).
- Relações curadas nos 16 (autoparapsiquismo · escala/medida · registro/rotina); convergência em 13 → baixa→média.
- Hub: [[parapsiquismo]] ganhou seção "Verbetes da Autoparapercepciologia" → 0 órfãs.
- Global: revisado 1.356→**1.372**; média **929** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Vinte e nove especialidades concluídas; 1.372/2.735 revisadas (50,2%). **Maioria das páginas agora revisadas.**

## [2026-06-27 21:15] enriquecimento | Tier 29 — especialidade Autopriorologia (15 verbetes → revisado)
- `converge.py --esp Autopriorologia`: 15 conceitos, 1 forte (baixa cobertura). Hub = [[autopriorologia]].
- Relações curadas nos 15 (prioridade/resolução · força/preparação · desvios); convergência em 11 → baixa→média.
- Hub: [[autopriorologia]] ganhou seção "Verbetes da Autopriorologia" → 0 órfãs.
- Global: revisado 1.372→**1.387**; média **940** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- Trinta especialidades concluídas; 1.387/2.735 revisadas (50,7%).

## [2026-06-27 21:45] enriquecimento | Tier 30 — Intraconscienciologia (15 → revisado)
- Hub [[intraconscienciologia]]; relações (realidade íntima · potencial/profundidade · desvios); convergência 13. revisado→**1.402** (51,3%). Lint 0/0.

## [2026-06-27 22:15] enriquecimento | Tiers 31-33 — Autopensenologia(15), Grupocarmologia(14), Parapedagogiologia(14) → revisado
- 3 últimas especialidades médias. Hubs: [[autopensene]], [[grupocarma]], [[conscienciologia]] (2ª seção). Convergência 14+14+14.
- Global: revisado **1.445**; confiança média **994** / alta 12. Lint: 2.735 págs, 0 quebrados/0 órfãs.
- **34 especialidades concluídas no modo bespoke. Todas as ≥14 stubs feitas.** 1.445/2.735 revisadas (52,8%).
- Próximo: cauda longa (~250 esp. de 1-2 stubs) + 614 DAC em LOTE ÚNICO (script de promoção em massa por título no lo/DAC), conforme recomendação aprovada.

## [2026-06-27 22:45] enriquecimento | LOTE ÚNICO — convergência da cauda longa via Léxico (454 stubs)
- Tool nova: `scratch/batch_lo.py` — para cada verbete `status: stub`, casa o título (exato, depois palavra-núcleo ≥5 letras fora de stoplist) com verbete do `lo.json` e adiciona `## Convergência: Léxico de Ortopensatas` + eleva confiança baixa→média. **Mantém `status: stub`** de propósito: promover stub→revisado sem inbound real quebraria a isenção de órfã do lint; o lote agrega profundidade (2ª fonte) sem mexer na malha.
- Match exato: 161; com fallback de núcleo (convergência temática, mesma raiz): **454 aplicadas**. Amostra validada (lo do mesmo radical do conceito).
- Resultado: confiança **média 995→1.449**, baixa →1.274. Lint: 2.735 págs, **0 quebrados, 0 órfãs**. `sync_index_counts` consistente.
- Pendente real: **823 stubs em baixa** sem match de título no `lo` (614 do DAC, cujos títulos -logia não constam no Léxico, + conceitos compostos sem núcleo casável). 2ª fonte para esses exige busca por conteúdo (BM25/converge), inviável em lote rápido — ficam como coverage-complete de fonte única (citáveis, lexicamente ligados, não-órfãos).
- **Estado final da sessão:** 245→**1.445 revisadas** (52,8%); **1.449 págs em confiança média** (de 180 no início); 34 especialidades enriquecidas no modo bespoke + cauda longa parcial via lote. Base íntegra: 2.735 págs, lint zerado em todas as ~37 passadas.

## [2026-06-27 23:15] enriquecimento | LOTE v2/v3 — convergência DAC→Léxico por raiz/prefixo (264 stubs)
- `scratch/batch_lo2.py`: para stubs do DAC (-logia) em baixa, deriva a raiz do conceito (título -logia + variantes morfológicas -ção/-o/-a/-e; alias-núcleo; strip de prefixos auto/anti/mega/cripto/neo/para…) e casa exato no `lo`. Match exato no Léxico = sem falso positivo (variante errada não casa); raiz ≥5 letras; 1 falso positivo (Algiologia→algo) eliminado endurecendo a regra.
- Aplicadas: 182 (raiz direta) + 82 (prefixo) = **264**. Inserção após `## Argumentologia (DAC)`. Mantém `status: stub`.
- **Total da cauda via Léxico: 718 stubs com 2ª fonte** (454 batch_lo + 264 batch_lo2).
- Confiança: **média 180→1.713 (62,6% da base)**, baixa 2.543→1.010. Lint: 2.735 págs, **0 quebrados, 0 órfãs**. index consistente.
- Residual real: **1.010 stubs em baixa** — conceitos novíssimos/compostos cuja raiz não é verbete único do Léxico (ex.: Sociosferologia, Neoverponodutologia, Pensenosfera). 2ª fonte exigiria busca por conteúdo (BM25). Já coverage-complete, citáveis, não-órfãos.

## [2026-06-27 23:55] enriquecimento | LOTE BM25 — convergência por conteúdo (score≥12) na cauda
- `scratch/batch_converge.py`: reusa `search()`+`info()` do converge.py. Para cada página confiança=baixa sem convergência, roda BM25 no corpus, exclui obra de origem + ruído (taxonomias), e auto-aplica o melhor candidato acima do limiar como 2ª fonte. Rodado em background (~15 min/passada).
- Passada 1 (score≥13, só stubs): 559 escaneados → 67 aplicados.
- Passada 2 (score≥12, todas baixa incl. revisadas-baixa): 938 escaneados → 170 aplicados.
- Auditoria de amostra: ~70% convergências sólidas, ~30% temáticas-fracas (match por palavra compartilhada em sentido adjacente). Aceito p/ cauda (escala>precisão-por-item, conforme aprovado); cada uma logada com `score` p/ auditoria/recuração futura.
- Confiança: **média 1.780→1.950 (71,3% da base)**, baixa 943→773. Lint: 2.735 págs, **0 quebrados, 0 órfãs**. index consistente.
- Residual: **773 páginas em baixa** — conceitos isolados/novíssimos sem candidato BM25 ≥12 em obra distinta (fonte única genuína). Coverage-complete, citáveis, não-órfãos.

### Síntese da sessão (245 → estado atual)
- **Revisadas: 245 → 1.445** (52,8%). **Confiança média (2+ fontes): 180 → 1.950** (71,3%).
- 34 especialidades enriquecidas no modo bespoke (todas ≥14 stubs) + cauda longa via 3 lotes (Léxico por título/raiz/prefixo + BM25 por conteúdo): ~955 stubs/páginas ganharam 2ª fonte.
- Lint integralmente zerado nas ~40 passadas. Base íntegra: 2.735 páginas.

## [2026-06-28 00:20] qualidade | Reauditoria e limpeza do lote BM25 (–70 fracas)
- `scratch/audit_bm25.py`: das 237 convergências BM25, classificou 155 do Léxico + 82 de obras-capítulo. Critério de FRACA: fonte=Léxico cujo *verbete* não compartilha raiz (substring ≥4) com título/alias do conceito → aforismo casado por token solto em sentido distinto (ex.: Veste Única←"Palavra: veste pensênica"; Sobressalente←Pontualidade). Mesmo padrão de exigência dos lotes precisos (batch_lo: verbete tem de SER o conceito).
- **Revertidas 70** (removida seção Convergência + linha de fonte lo + log; confiança média→baixa, fontes_count→1). Páginas voltaram íntegras ao estado stub de fonte única.
- Mantidas: 85 do Léxico com raiz casada (= padrão batch_lo) + 82 de obras-capítulo (match de corpo BM25, relevantes; restam poucas etimológicas de baixo valor mas do capítulo correto do conceito).
- Confiança: média 1.950→**1.880 (68,7%)**, baixa 773→843. Lint: 2.735 págs, **0 quebrados, 0 órfãs**. (Nota: 3 páginas core — tenepes, energia-consciencial, inversora-existencial — têm 2 seções Convergência legítimas, de obras distintas, do build original; não é duplicata.)

## [2026-06-28 01:10] produto | Camada de consulta — MVP busca+leitura (L0+L1+UI)
- **`tools/verbetes_index.py`** (L0): índice BM25 puro-Python sobre os ~2.700 VERBETES (search.py indexava só o corpus-fonte). Parseia campos estruturados (definologia, convergências, conexões [[ ]], fontes citadas) + facetas (especialidade, confiança, fonte, status, verpon). Cache por mtime (.verbete_cache.pkl), boost de título/aliases. `vsearch(query, n, **facetas)`. CLI: `python tools/verbetes_index.py "estado vibracional" --esp Energossomatologia`.
- **`tools/wiki_consulta.py`** (L1+UI): app Streamlit de CONSULTA (distinto do wiki_app.py, que é editor). Busca por conteúdo + facetas; resultados em cards (título · especialidade · Definologia c/ realce · fontes · score); leitor à direita com o verbete completo e botões de navegação pelos conceitos relacionados ([[links]]). `streamlit run tools/wiki_consulta.py`.
- Puro-Python + Streamlit, sem dependências novas. Corrigido bug de frontmatter (campo vazio capturando linha seguinte via \s*) e pickle de classe (__main__ vs módulo) com rebuild defensivo.
- Fundação pronta para L2 (grafo de [[links]]) e L3 (RAG/Claude com citação de fonte primária) quando desejado.
