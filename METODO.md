# MÉTODO — Construção de wiki/base de conhecimento a partir de um corpus

Guia transferível, destilado da construção desta wiki. Descreve **como** ingerir
um corpus grande numa base estruturada em Markdown sem cair na armadilha de baixo
recall. Projetado para ser copiado e adaptado a outro projeto (técnico ou não).

> Princípio-mãe: **separe COBERTURA (barata, determinística, código) de
> PROFUNDIDADE (cara, de julgamento, LLM).** Quase tudo decorre disto.

---

## 0. Antes de tudo: meça o gap com um número

"Poucos conceitos foram capturados" é vago e leva a otimizar a coisa errada.
Construa primeiro um **inventário**: cruze *o universo de conceitos na fonte* ×
*o que já existe na base*. O resultado (ex.: `31/2019 = 1,5%`) revela se o
problema é de **método** (baixo recall) ou de **esforço**.

> Regra: nenhuma decisão de estratégia de ingest sem a métrica de cobertura na mão.

---

## 1. Classifique cada fonte em um de dois regimes

Nem toda fonte se ingere igual. Antes de processar, rotule:

| Regime | O que é | Exemplos | Como ingerir |
|---|---|---|---|
| **A. Enumerável** | 1 registro = 1 conceito já segmentado, com um campo citável | dicionário, glossário, enciclopédia, spec, catálogo de APIs, schema | **enumerar-primeiro** (§2) |
| **B. Discursiva** | conceitos diluídos na prosa, sem segmentação natural | livro, artigo, transcrição, documentação narrativa | **dirigido por busca** (§3) |

Erro clássico: aplicar busca-e-curadoria (regime B) a uma fonte enumerável
(regime A). A busca só acha o que você pensa em procurar → recall baixíssimo.

---

## 2. Regime A — Fontes enumeráveis (enumerar-primeiro)

Pipeline de 4 passos. Os passos 1–2 são **código puro** (sem LLM):

1. **ENUMERAR.** Liste todos os títulos/chaves da fonte e cruze com os IDs já
   existentes → backlog de lacunas medível.
2. **COBRIR (mecânico).** Gere um **stub** por lacuna: frontmatter mínimo +
   o campo citável da fonte (definição/assinatura/resumo) *ipsis litteris* + a
   citação. Marque `status: stub`. Gere um **catálogo navegável** que linke todos
   os stubs (resolve inbound de uma vez). Cobertura vai a ~100% a custo zero de LLM.
3. **APROFUNDAR (LLM, por lote temático).** Não enriqueça tudo de uma vez;
   processe por agrupamento (especialidade/módulo/seção):
   - (i) uma ferramenta levanta **candidatos** (2ª fonte, relações) por conceito;
   - (ii) o LLM **escolhe e redige** (a parte de julgamento);
   - (iii) ao promover `stub → revisado`, crie/atualize um **hub** que linka o
     cluster — senão as páginas promovidas viram órfãs.
4. **MEDIR.** Registre `cobertura X/total` no log a cada lote.

> Um **stub** é um esqueleto citável válido, não uma página pronta. A curadoria
> decide *com que profundidade* enriquecer cada item — **nunca se ele existe**.
> Cobertura deixa de competir com qualidade.

---

## 3. Regime B — Fontes discursivas (dirigido por busca)

Para conceitos diluídos na prosa, sem enumeração natural:

1. **Escopo**: uma obra inteira ou um conceito transversal.
2. **Recuperar** trechos relevantes via busca (BM25/semântica).
3. **Extrair** estrutura: definição (preferir a direta, ipsis litteris), relações,
   conceitos conjugados.
4. **Calibrar com o usuário**: "achei N — X novos, Y atualizam, Z marginais?"
5. **Aplicar** citando a fonte canônica (obra + página), nunca o arquivo bruto.
6. **Cross-references**: adicionar backlinks nas páginas que mencionam o novo conceito.
7. **Contradições**: se a fonte contradiz a base, criar seção própria citando ambas.

---

## 4. Divisão de trabalho: código vs. LLM

| Faça em **código** (determinístico) | Faça com **LLM** (julgamento) |
|---|---|
| enumerar conceitos, medir cobertura | escolher qual 2ª fonte converge |
| gerar stubs em massa | redigir relação semântica e sua glosa |
| aplicar edições em lote (frontmatter, seções, log) | detectar contradição entre fontes |
| lint estrutural (links, órfãs, frontmatter) | calibrar escopo com o usuário |
| sincronizar índices/contagens | priorizar a ordem dos lotes |

> Não gaste LLM no que um script resolve, nem tente no LLM o que não cabe no contexto.

### O padrão de aplicação que dá velocidade E consistência
Embuta **o julgamento do LLM como dados** dentro de um script de aplicação
**determinística**. Ex.: o LLM decide `{conceito → (citação, relações)}`; um loop
idempotente insere isso no frontmatter, nas seções e no log. Assim nenhuma página
sai com formato divergente, e o lote inteiro é reprodutível.

---

## 5. Salvaguardas obrigatórias da automação

Para o julgamento automático não virar lixo em escala:

1. **Strip de boilerplate antes de extrair.** Ao minerar relações no texto, remova
   primeiro a linha de citação/atribuição — senão todo item "se relaciona" com a
   própria fonte. *Limpe ruído estrutural antes de qualquer extração.*
2. **Filtro de frequência.** Um alvo que casa com >N% dos itens é genérico demais
   (ruído) — descarte automaticamente. *O que casa com tudo não informa nada.*
3. **Validação antes de gravar.** Scripts de edição em lote devem **abortar** se
   alguma referência aponta para alvo inexistente. *Falhe alto, não em silêncio.*
4. **Idempotência.** Reexecutar uma etapa não deve duplicar conteúdo (cheque marcador
   de "já processado", ex.: placeholder ainda presente).
5. **Não sobrescrever trabalho curado.** Geradores em massa pulam o que já existe.

---

## 6. Saúde estrutural (lint) — rode após cada lote

Verificações mecânicas que mantêm a base íntegra em escala:
links internos quebrados · páginas órfãs (sem inbound) · frontmatter obrigatório
ausente · ID ≠ nome do arquivo · IDs duplicados · distribuição de status/confiança.

Dois cuidados aprendidos na prática:
- **Stubs não são órfãos** — isente `status: stub` da checagem de órfãs (e/ou
  garanta inbound pelo catálogo). Mas **ao promover stub→página revisada, ela perde
  essa isenção**: garanta inbound real (o hub do cluster) na mesma operação.
- **Exclua catálogos/índices** do scan de páginas, mas lembre que então os links
  deles **não contam como inbound** — por isso o hub real é necessário.

---

## 7. Ciclo de vida e métricas

- **Confiança** por nº de fontes convergentes: 1 → baixa; 2–4 → média; 5+ → alta.
  Reflita no frontmatter; é diferente de **status** editorial (stub→rascunho→revisado).
- Registre cada lote no **log** com cabeçalho grep-ável e a métrica de cobertura.
- Mantenha a **tabela de ferramentas** atualizada: toda automação nova entra como
  linha com *o que faz* + *comando de uso*. Senão a próxima sessão reinventa a roda.
- **Registre as armadilhas** (como a regra anti-órfã) junto ao passo onde ocorrem.
  Um documento de método vivo acumula as cicatrizes do projeto.

---

## 8. Resumo em uma frase

> Enumere o que existe, cubra tudo barato com stubs citáveis, e gaste o LLM só na
> profundidade — por lotes, com candidatos levantados por código, validando antes
> de gravar e medindo a cobertura a cada passo.
