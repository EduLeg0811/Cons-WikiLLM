# AGENTS.md — Wiki de Conscienciologia (LLM Wiki)

Schema operacional do agente. Gerado a partir do *idea file* (adaptação do padrão LLM Wiki de Karpathy para Conscienciologia). Este arquivo define **como** manter o wiki; o *idea file* define **por quê**.

---

## 0. Missão

Construir e manter incrementalmente um **wiki persistente em Markdown** sobre Conscienciologia, situado entre o usuário e as fontes brutas em `/raw`. O wiki acumula síntese, cross-references e contradições já resolvidas — nunca redescobre do zero a cada query.

Idioma: **português brasileiro**. Neologismos técnicos (tenepes, conscin, consciex, holopensene, ofiex…) **nunca** são traduzidos nem simplificados.

---

## 1. Arquitetura de três camadas

| Camada | Caminho | Regra |
|---|---|---|
| **Corpus** (fonte canônica) | `/corpus` | JSON limpo, segmentado e com citação por registro (`text` + `title`/`pagina`/`number`; a Enciclopédia traz ainda `area`/`theme`/`author`). **Imutável.** É a base primária de ingest. |
| Fontes brutas | `/raw` | Novas fontes ainda **não processadas** (PDF/docx/xlsx/txt). Viram JSON no corpus antes do ingest. **Imutável** — só leitura. |
| Wiki | `/wiki` | Gerado e mantido pelo agente. |
| Ferramentas | `/tools` | Camada algorítmica (Python). Ver Seção 8. |
| Schema | `/AGENTS.md` | Este arquivo. Convenções operacionais. |

> **Citação:** páginas devem citar o **corpus** (obra + `pagina`/`number`), não os PDFs de `/raw`. O corpus é o que dá a localização exata exigida pelo Princípio da descrença (§2.1).

### Estrutura de `/wiki`
```
/wiki
├── index.md            # catálogo de todas as páginas (orientado a conteúdo)
├── log.md              # linha do tempo de ingest/query/lint (orientado a tempo)
├── overview.md         # visão integradora atual
├── sintese.md          # síntese conceitual em evolução
├── verbetes/           # páginas conceituais (formato verbetográfico)
├── especialidades/     # especialidades (logias) da Conscienciologia
├── tecnicas/           # técnicas conscienciológicas
├── pesquisadores/      # autores, verbetógrafos, conscienciólogos
├── obras/              # livros, verbetes oficiais, artigos
├── fenomenos/          # fenômenos parapsíquicos e conscienciais
├── sinteses/           # páginas comparativas/derivadas de queries
└── lint-reports/       # saídas de health-check (YYYY-MM-DD.md)
```
> A camada `autopesquisa/` (vivência pessoal) **não** foi criada nesta instância. Quando solicitada, deve ser rigorosamente isolada do corpus consensual; o agente nunca promove reflexão de autopesquisa a verbete sem confirmação explícita.

---

## 2. Princípios pesquisísticos (obrigatórios)

1. **Princípio da descrença** — nada como dogma. Toda afirmação registra **quem disse, onde, em que contexto**. Sem citação atribuída, não entra.
2. **Fato vs. parafato** — separar observação intrafísica de vivência multidimensional/parapsíquica em seções distintas.
3. **Verpon (verdade relativa de ponta)** — marcar `verpon: true` no frontmatter quando a página contém uma verpon, citando obra/verbete de origem.
4. **Conceitos conjugados** — termos que operam aos pares (holopensene↔pensene, intermissão↔vida intrafísica, tenepes↔ofiex) devem ser cruzados automaticamente.
5. **Neologismos técnicos** — usar o termo técnico, linkar para sua página, nunca traduzir.
6. **Controvérsias** — registrar críticas acadêmicas (ex.: Stoll, Chiesa) e contraposições, sempre identificando a fonte. Conscienciologia não é tratada como dogma.
7. **Referência primária** — quando um conceito apresentar definição explícita e direta no texto, copiar essa definição ispsis litteris, e indicar a fonte ("Extraído de...").

---

## 3. Convenções de arquivo

- **Filename = slug**: kebab-case, **sem acentos** (`projecao-consciencial-lucida.md`). É o **ID imutável** — referenciado por `[[slug]]`. Nunca renomear à mão (quebra links); se precisar, é o único campo que justifica reprocessamento de referências.
- **Título interno** (`titulo:` + `# H1`): nome de exibição, **editável**, preserva acentos (`# Projeção Consciencial Lúcida`). Para alterá-lo num só ponto, use `tools/rename.py` (Seção 8).
- **`aliases:`** (opcional): lista de nomes alternativos/antigos do conceito (`aliases: [Inversora Existencial, Invexista]`). Fonte única de sinônimos de exibição; alimentada por `rename.py --add-alias`.
- **Frontmatter YAML obrigatório** em toda página de conteúdo (ver templates).
- **Links internos**: estilo Obsidian `[[slug]]` (usa o `slug`, não o título).
- **Links externos** (referência, não-canônicos): Conscienciopédia, Verbetoteca, Reposicons, ICGE — opcionais, marcados como uso interno.
- **Datas**: ISO `YYYY-MM-DD`. Converter datas relativas para absolutas.

### Áreas de classificação (tag `area:`)
Autoconscienciologia · Conscienciologia · Intraconscienciologia · Extraconscienciologia · Paraconscienciologia · Interconscienciologia · Policonscienciologia

---

## 4. Templates

### 4.1 Verbete (`/wiki/verbetes/<slug>.md`)
```markdown
---
tipo: verbete
slug: holopensene
titulo: Holopensene
especialidade: Holopensenologia
area: Intraconscienciologia
status: rascunho           # rascunho | revisado | consolidado
confianca: baixa           # baixa (1 fonte) | media | alta (5+ convergentes)
fontes_count: 0
ultima_atualizacao: 2026-06-08
tags: [pensene, ambiente-energetico]
verpon: false
---

# Holopensene

## Definologia
[Definição sintética. Quando houver definição própria e direta  na fonte, copiar ipsis litteris entre aspas, e indicar a fonte ("Extraído de...")]

## Etimologia
[Origem do termo, datas, cunhador quando aplicável.]

## Sinonimologia
1. ...

## Fatologia / Parafatologia
[Separar explicitamente fatos intrafísicos de parafatos multidimensionais.]

## Verponímia
[Verpons associadas — fonte explícita.]

## Controvérsias
[Apenas se houver contradição entre fontes. Citar ambas.]

## Conexões internas
- [[pensene]] — conceito conjugado
- [[ofiex]] — relação técnica

## Fontes ingeridas
- `raw/<arquivo>.pdf` — cap./p. X

## Referência externa (uso interno)
- Conscienciopédia: https://pt.conscienciopedia.org/index.php/Holopensene

## Log de revisões
- 2026-06-08: criação a partir de `raw/<arquivo>.pdf`
```

Páginas de **especialidades/técnicas/pesquisadores/obras/fenômenos** seguem o mesmo frontmatter (ajustando `tipo:`) e usam as seções pertinentes (uma técnica troca *Definologia/Etimologia* por *Objetivo/Procedimento/Pré-requisitos/Resultados*, etc.).

---

## 5. Operações

### 5.1 Ingest (a partir do corpus em `/corpus`)

Há **dois regimes de ingest**, conforme a natureza da fonte:

**A. Fontes-dicionário (Enciclopédia, DAC) — *enumerar-primeiro*.** São dicionários de conceitos já pré-segmentados (1 registro = 1 verbete com `title` + Definologia + `area`). Aqui a busca-e-curadoria tem **baixo recall por design** (descarta a maioria → cobertura ~1%). A doutrina correta:
1. **Enumerar** todo o universo de conceitos: `python tools/inventory.py [--gaps ec]` (cruza títulos da fonte com os slugs existentes → backlog de lacunas).
2. **Cobertura mecânica**: `python tools/build_stubs.py` gera páginas-stub (`status: stub`, Definologia ipsis litteris + fonte) para toda lacuna, e o catálogo `catalogo-ec.md`. Cobertura sobe a ~100% sem gastar LLM.
3. **Profundidade por tier (LLM)**: a curadoria decide *com que profundidade* enriquecer cada stub (relações, convergência, controvérsias), **não se o conceito existe**. Stub → rascunho → revisado. Fluxo do tier por especialidade: (i) `converge.py --esp <X>` levanta candidatos a 2ª fonte por conceito; (ii) o LLM escolhe a convergência e redige as relações semânticas com glosa; (iii) **ao promover stub→revisado, criar/atualizar a seção-hub no verbete-eponímo da especialidade** linkando o cluster — senão as páginas promovidas viram órfãs (perdem a isenção de stub; o catálogo não conta como inbound).
4. **Métrica**: registrar cobertura (`X/total`) no log; `inventory.py` mede a qualquer momento.

> Separar **cobertura** (barata, Python) de **profundidade** (cara, LLM) é o princípio central. Um stub é um esqueleto citável válido, não uma página pronta.

**B. Fontes discursivas (Projeciologia, hsr, hsp, manuais) — *dirigido por busca*.** Conceitos diluídos na prosa; não há enumeração natural. O agente recupera trechos via `tools/search.py` e trabalha sobre eles:

1. **Definir escopo**: uma obra (`--book ec`) ou um conceito transversal (busca sem filtro).
2. **Recuperar** os trechos pertinentes: `python tools/search.py "<conceito>" [--book <ids>] -n <N> --full`.
3. **Extração estruturada** sobre os trechos recuperados: definição (preferir a *Definologia* direta, ipsis litteris), especialidade, área, verpons, neologismos, conceitos conjugados.
4. **Conversa de calibração** com o usuário: "Achei N conceitos — X novos (criar página?), Y atualizam páginas existentes, Z menções marginais (só log)?"
5. **Aplicação** das mudanças confirmadas. **Citar o corpus** (obra + `pagina`/`number`), nunca o PDF.
6. **Atualizar** `index.md` e `log.md`.
7. **Cross-references** — adicionar `[[backlinks]]` em todas as páginas que mencionam conceito recém-criado.
8. **Detecção de contradições** — se a fonte contradiz o wiki, criar seção `## Controvérsias` citando ambas.

> **Novas fontes em `/raw`**: converter para o formato do corpus (`{text, title, pagina, …}`, ver `corpus/index.json`) e registrar a obra em `corpus/index.json` **antes** de ingerir. A conversão de formato é tarefa de Python, não de LLM.

### 5.2 Query — named templates
| Comando | Ação |
|---|---|
| `/define <termo>` | Verbete curto sintético, com citações. |
| `/compare <A> <B>` | Tabela comparativa → `/wiki/sinteses/<a>-vs-<b>.md`. |
| `/cinco-w-um-h <verbete>` | Quadro What/Why/How/Who/When/Where. |
| `/timeline <tema>` | Linha do tempo do conceito no corpus. |
| `/contradicoes` | Contradições atuais, por gravidade. |
| `/verpons` | Páginas `verpon: true`. |
| `/orfas` | Páginas sem inbound links. |
| `/lacunas` | Conceitos mencionados sem página própria. |
| `/relacionar <termo>` | Conexões não-óbvias. |
| `/autopesquisa <tema>` | Cruza páginas com reflexão pessoal (requer camada autopesquisa). |

> Respostas valiosas de query são **arquivadas** em `/wiki/sinteses/` — exploração não vira chat history descartável.

### 5.3 Lint (health-check → `/wiki/lint-reports/YYYY-MM-DD.md`)
- Páginas órfãs (sem inbound links)
- Links `[[...]]` quebrados
- Conceitos mencionados sem página (lacunas)
- Contradições não-anotadas
- `status: rascunho` estagnado há > N dias

### 5.4 Lifecycle
- **Confiança**: 1 fonte → `baixa`; 5+ fontes convergentes → `alta`. Refletir no frontmatter `confianca:`.

---

## 6. Formato do log (`log.md`)

Cabeçalho grep-ável: `## [YYYY-MM-DD HH:MM] <tipo> | <descrição>`. Tipos: `ingest`, `query`, `lint`.
`grep "^## \[" log.md | tail -10` → últimos 10 eventos.

---

## 8. Camada algorítmica (`/tools`) — Python vs. LLM

Trabalho **fixo/determinístico** é Python; trabalho **semântico/de julgamento** é LLM. Não gastar LLM no que um script resolve, nem tentar no LLM o que não cabe no contexto.

| Ferramenta | Faz | Uso |
|---|---|---|
| `tools/corpus.py` | Carrega e **normaliza** o corpus heterogêneo numa interface única (`Record`: book, text, title, page, area…). | `python tools/corpus.py` → estatísticas por obra. Importado pelas demais. |
| `tools/search.py` | **Busca BM25** sobre os ~67k registros (Python puro, cache automático por mtime). Retorna trechos + citação pronta. | `python tools/search.py "<query>" [--book ec,tnp] [-n 8] [--full]` |
| `tools/inventory.py` | **Inventário de cobertura**: enumera os conceitos das fontes-dicionário (EC, DAC) e cruza com os slugs do wiki → backlog de lacunas medível (§5.1-A). | `python tools/inventory.py [--book ec] [--gaps ec]` |
| `tools/converge.py` | **Busca de convergência por conceito** (acelera o enriquecimento por tier): para cada stub de uma especialidade, roda BM25 excluindo a fonte de origem e devolve candidatos a 2ª fonte com citação pronta + marca de força (★), filtrando listas/taxonomias. O LLM só escolhe e redige. | `python tools/converge.py --esp Recexologia [-o cand.txt]` |
| `tools/build_stubs.py` | **Gera stubs em massa** de uma fonte-dicionário (`--book ec\|dac`) + `catalogo-<book>.md` (dá inbound aos stubs). EC: Definologia ipsis litteris. DAC: argumento-líder + detecção do conceito-núcleo embutido como `alias` (n-grama recorrente cuja raiz bate com o título, ex.: *Inacabamentologia*→_Inacabamento a Maior_). Não sobrescreve curadas. | `python tools/build_stubs.py --book dac [--dry-run]` |
| `tools/sync_index_counts.py` | Sincroniza as contagens `(N)` do `index.md` com o `fontes_count` real do frontmatter. Rodar após cada convergência. | `python tools/sync_index_counts.py [--check]` |
| `tools/lint.py` | Health-check estrutural (§5.3): links quebrados, órfãs, frontmatter, slug≠arquivo, duplicados, status/confiança. Gera `wiki/lint-reports/AAAA-MM-DD.md`. | `python tools/lint.py [--no-write]` |
| `tools/rename.py` | Renomeia o **título** de um conceito a partir de 1 ponto (atualiza `titulo:`+`# H1`, opcional `aliases:`), varre menções na prosa para revisão (não toca citações ipsis litteris) e roda o lint. O **slug é imutável** (preserva os links). | `python tools/rename.py <slug> --titulo "Novo Nome" [--add-alias] [--apply-prose]` |
| `tools/api/` (FastAPI) | **API** que serve a SPA: busca BM25, leitura e gravação de verbetes (dispara `rename.py`+`sync` quando o título muda). Reaproveita `verbetes_index`/`rename`/`sync_index_counts`; `verbetes_io.py` é o parse/serialize canônico. Não reimplementa nada. | `cd tools && python -m uvicorn api.main:app --reload` |
| `web/` (React + Vite) | **SPA moderna** (React 19 · Vite 8 · Tailwind v4 OKLCH · Motion · Sonner). Duas telas: **Consulta** (busca/facetas/leitor com navegação por `[[links]]`) e **Editor** (lista filtrável · edição de campos+corpo · gravação em lote). Consome a API. Aposentou os apps Streamlit `wiki_app.py`/`wiki_consulta.py`. | `pwsh dev.ps1` (sobe API+SPA juntas) |

**LLM faz** (não automatizar): extração de conceitos, redação verbetográfica, detecção de contradições, convergência entre fontes, calibração com o usuário, respostas de query.

> Pendentes previstos (mesma filosofia minimalista, 1 script cada quando necessário): `build_index.py` (regenerar `index.md` inteiro a partir do frontmatter — hoje só as contagens são sincronizadas), `ingest_raw.py` (PDF/docx/xlsx → JSON do corpus).

---

## 7. Fontes externas para referência cruzada
- Conscienciopédia: `https://pt.conscienciopedia.org/index.php/<verbete>`
- Verbetoteca: `https://verbetoteca.info/verbete/<verbete>`
- Reposicons (PDFs oficiais): `https://reposicons.org/`
- ICGE (tabela de verbetes de Waldo Vieira): `https://www.icge.org.br/?page_id=4229`
