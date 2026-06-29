# -*- coding: utf-8 -*-
ESP = "Autopriorologia"
A = "[[autopriorologia]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "abordagem-relevante": lo("Abordagem",43,"*Abordagem: primeiro passo* — a abordagem relevante parte dos conceitos da Conscienciologia com realismo máximo."),
 "autoposicionamento-de-ponta": lo("Autoposicionamento",269,"Se todas as pessoas estão contra você, ou você é a *mais errada* ou a **mais certa** em seu holopensene existencial."),
 "autovivencia-das-prioridades": src("700 Experimentos da Conscienciologia","700exp","cap. 501",565,"As prioridades evolutivas são descobertas e empregadas através da vivência do discernimento consciencial magno (Mentalsomatologia)."),
 "bem-escasso": dac("Aquisiciologia",207,"As tenepes, ofiexes e autodesperticidades multiexistenciais eram acessíveis, antes, apenas a escasso número de evoluciólogos e raros Serenões."),
 "defesa-da-verpon": lo("Verpon",2003,"A verpon é o rolo compressor da **hiperacuidade**; *Verpon: realidade uniparacerebral.*"),
 "forca-integral": lo("Força",881,"A **inteligência** é a única força de fato funcional."),
 "megaenfoque-sadio": lo("Conjuntura",478,"O **sobrepairamento** sadio exige tempo — base do megaenfoque sadio da própria realidade."),
 "prerrogativa": src("700 Experimentos da Conscienciologia","700exp","cap. 520",584,"A conscin desperta define como perdas de esforços 10 posturas antiquadas, entre elas a Aristocracia (a prerrogativa de sangue)."),
 "resolucao-prioritaria": lo("Resolução",1737,"A melhor resolução é aquela gerada pelo pararraciocínio ou a Paramatematicologia da **autoponderação.**"),
 "teatica-prioritaria": lo("Poder",1573,"O maior poder da consciência emana da ***Inteligência Evolutiva*** (IE) teática, cosmoética, prioritária."),
 "megatares": dac("Paramateriologia",1173,"Nas condições de projetores autoconscientes ou consciexes recém-dessomadas, enfrenta-se a pararrealidade materiológica das consciexes assistidas — campo da megatares."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
P="[[priorizacao-da-proexis]]"
REL = {
 "abandonador": R("conscin que abandona deveres/pessoas","[[microinteresse]] · [[abordagem-relevante]]"),
 "abordagem-relevante": R("abordar a realidade com realismo máximo","[[megaenfoque-sadio]] · [[teatica-prioritaria]]"),
 "autoposicionamento-de-ponta": R("posição definida e exposta sem rodeios","[[defesa-da-verpon]] · [[autovivencia-das-prioridades]]"),
 "autovivencia-das-prioridades": R("identificar e atender a prioridade","[[resolucao-prioritaria]] · [[teatica-prioritaria]] · "+P),
 "bem-escasso": R("realidade positiva rara na vida intrafísica","[[prerrogativa]] · [[forca-integral]]"),
 "defesa-da-verpon": R("defender a verpon pelo discernimento","[[autoposicionamento-de-ponta]] · [[teatica-prioritaria]]"),
 "forca-integral": R("aplicar as autopotencialidades por inteiro","[[megapreparacao]] · [[megatares]]"),
 "inconcretude": R("qualidade do imaterial/abstrato","[[microinteresse]] · [[megaenfoque-sadio]]"),
 "megaenfoque-sadio": R("racionalidade analítica da própria realidade","[[abordagem-relevante]] · [[autovivencia-das-prioridades]]"),
 "megapreparacao": R("fundamentar o empreendimento evolutivo","[[forca-integral]] · [[megatares]]"),
 "megatares": R("trabalho de heterodespertamento autodeterminado","[[megapreparacao]] · [[forca-integral]]"),
 "microinteresse": R("o desimportante/desvantajoso","[[inconcretude]] · [[abandonador]]"),
 "prerrogativa": R("privilégio/direito especial","[[bem-escasso]] · [[autoposicionamento-de-ponta]]"),
 "resolucao-prioritaria": R("selecionar a resolução prioritária","[[autovivencia-das-prioridades]] · [[teatica-prioritaria]]"),
 "teatica-prioritaria": R("teoria+prática mais pertinente (IE)","[[autovivencia-das-prioridades]] · [[resolucao-prioritaria]] · "+P),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
