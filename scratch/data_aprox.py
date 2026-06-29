# -*- coding: utf-8 -*-
ESP = "Autoproexologia"
A = "[[proexis]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "aproveitamento-do-tempo": lo("Conhecimento",477,"O melhor **aproveitamento do tempo** é a busca diuturna do conhecimento (*Carpe diem*)."),
 "autorresolucao-derradeira": lo("Autorresolução",291,"Ser inteligente é saber mudar de imediato a **autorresolução** menos digna."),
 "balanco-pre-evoluciologo": lo("Evoluciólogo",807,"O *evoluciólogo* não erra igual a nós, pré-serenões; a liderança interassistencial é caminho aberto para alcançá-lo."),
 "cinco-ciclos": src("700 Experimentos da Conscienciologia","700exp","cap. 536",600,"Quanto aos ciclos multiexistenciais, cada consciência precisa ser analisada de per si; os calendários humanos pouco influem nos critérios."),
 "cultura-conscienciocentrica": src("Homo sapiens reurbanisatus","hsr","cap. 130",335,"Há 29 tipos de *culturas paralelas* à cultura consciencial, cosmoética e evolutiva — a evitar."),
 "extraproexis": lo("Cirurgia",415,"A cirurgia de destino mais comum promove a **extraproéxis**, ocorrendo por mérito próprio."),
 "fase-existencial": lo("Fases",857,"A infância é a fase existencial dos pulos; a meia-idade, das caminhadas; a velhice, das siestas."),
 "inventario-proexologico": lo("Paracérebro",1442,"*Paracérebro: inventário autocognitivo* — base do inventário proexológico (CPC: minibreviário proexológico)."),
 "megacomplexis": dac("Inacabamentologia",787,"Completar (megacompléxis) a megagestação consciencial exige aplicar o acervo intelectual acumulado em décadas de autesforços pesquisísticos."),
 "meio": lo("Meio",1272,"Entre o princípio e o fim, há sempre o **meio** onde se decide o empreendimento."),
 "planejamento-milimetrico": lo("Planejamento",1566,"O bom planejamento precede o empreendimento; antes de remar, fixe os remos firmemente no barco."),
 "pos-complexis": dac("Automegaprospectivologia",345,"Na terceira e quarta idades físicas importa fixar a meta única segundo a automegaprospectiva, visando à acabativa da autoproéxis."),
 "profissao-herdada": lo("Profissão",1643,"*Profissão é sobrevivência. Do instrumento vem o sustento.*"),
 "sementeira-intrafisica": lo("Sementeira",1801,"*Cada qual semeia o campo da sua mente.* Estudemos sem parar."),
 "taxologia-das-megagestacoes": src("Homo sapiens reurbanisatus","hsr","cap. 79",231,"As megagestações humanas são efeitos das reurbexes antes de serem efeitos da Biotecnologia, gerando a invasão das consréus na vida intrafísica."),
 "vocacao-frustrada": lo("Vocação",2031,"Você é a sua **vocação** — a vocação frustrada é a disposição natural não exercida."),
 "carencia-insatisfeita": lo("Carência",380,"Evolutivamente, todos carecemos uns dos outros; assistentes e assistidos carecem de mais talentos evolutivos."),
 "autofracasso-deslocado": lo("Autoritarismo",283,"O autoritarismo na IC é tão deslocado como *a canção de noivado no cemitério* — análogo ao autofracasso deslocado do assistente."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "aproveitamento-do-tempo": R("aplicar sabiamente as horas da vida","[[planejamento-milimetrico]] · [[fase-existencial]]"),
 "autofracasso-deslocado": R("assistente influenciado pelo fracasso alheio","[[carencia-insatisfeita]] · [[vocacao-frustrada]]"),
 "autorresolucao-derradeira": R("postura da fase final da vida","[[inventario-proexologico]] · [[retrospectiva-decenal]]"),
 "balanco-pre-evoluciologo": R("autocrítica do estado pré-evoluciólogo","[[inventario-proexologico]] · [[retrospectiva-decenal]]"),
 "bidoacao-pessoal": R("1ª doação (aportes) + 2ª doação (gescons)","[[sementeira-intrafisica]] · [[megacomplexis]]"),
 "carencia-insatisfeita": R("irrealização íntima de uma carência","[[vocacao-frustrada]] · [[autofracasso-deslocado]]"),
 "cinco-ciclos": R("periodicidade pentacíclica (CI→dessoma)","[[fase-existencial]] · [[retrospectiva-decenal]]"),
 "cultura-conscienciocentrica": R("erudição centrada na consciência","[[sementeira-intrafisica]] · [[aproveitamento-do-tempo]]"),
 "extraproexis": R("tarefa superveniente extraordinária","[[megacomplexis]] · [[pos-complexis]]"),
 "fase-existencial": R("período específico da vida intrafísica","[[cinco-ciclos]] · [[autorresolucao-derradeira]] · [[aproveitamento-do-tempo]]"),
 "inventario-proexologico": R("balanço geral da vida humana","[[balanco-pre-evoluciologo]] · [[retrospectiva-decenal]] · [[autorresolucao-derradeira]]"),
 "linha-de-abertura": R("realização vivencial mais acessível","[[planejamento-milimetrico]] · [[meio]]"),
 "megacomplexis": R("3 conquistas: ofiex, despertologia, megagescon","[[pos-complexis]] · [[extraproexis]] · [[taxologia-das-megagestacoes]]"),
 "meio": R("recurso intermediário para o fim","[[linha-de-abertura]] · [[planejamento-milimetrico]]"),
 "planejamento-milimetrico": R("planejar a proéxis em detalhe","[[aproveitamento-do-tempo]] · [[meio]] · [[linha-de-abertura]]"),
 "pos-complexis": R("período gratificante após o compléxis","[[megacomplexis]] · [[extraproexis]]"),
 "profissao-herdada": R("atividade preparada (sustento)","[[vocacao-frustrada]] · [[meio]]"),
 "retrospectiva-decenal": R("avaliação pormenorizada por décadas","[[inventario-proexologico]] · [[balanco-pre-evoluciologo]]"),
 "sementeira-intrafisica": R("semear o esclarecimento consciencial","[[bidoacao-pessoal]] · [[cultura-conscienciocentrica]]"),
 "taxologia-das-megagestacoes": R("classificação das obras de megagestação","[[megacomplexis]] · [[bidoacao-pessoal]]"),
 "tesaurizacao": R("entesourar bens para a proéxis","[[bidoacao-pessoal]] · [[aproveitamento-do-tempo]]"),
 "vocacao-frustrada": R("disposição natural não exercida","[[profissao-herdada]] · [[carencia-insatisfeita]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
