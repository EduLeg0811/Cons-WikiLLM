# -*- coding: utf-8 -*-
ESP = "Extrafisicologia"
A = "[[extrafisicalidade]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "abordagem-extrafisica": src("200 Teáticas da Conscienciologia","200teat","cap. 1",21,"Pela paratecnologia, a *abordagem extrafísica* é o ato de acessar uma consciex diretamente, em alguma dimensão extrafísica."),
 "acao-extrafisica": src("Projeciologia","proj","cap. 272",551,"Na dimensão extrafísica o pensamento é ação: pensamento e ação manifestam-se conjunta e concomitantemente, sem defasagem no tempo."),
 "agendex-da-ofiex": lo("Ofiex",1386,"Ofiex: o *home office*, em bases pessoais, da Reurbexologia; os trabalhos da ofiex equivalem às autovivências de uma semidessoma."),
 "base-extrafisica": src("700 Experimentos da Conscienciologia","700exp","cap. 134",198,"A base física do projetor veterano, engajado em equipe assistencial, pode ser transformada em antecâmara da ofiex — oficina extrafísica."),
 "central-extrafisica-de-energia": dac("Tenepessologia",1402,"A tenepes assegura à conscin o acesso fácil à *Central Extrafísica de Energia* (CEE), à autofiex, ao compléxis e à autodesperticidade."),
 "consciexialidade-assexuada": lo("Consciexialidade",500,"Ser humano é uma segunda natureza; a primeira natureza é a **consciexialidade.**"),
 "parafatologia": lo("Parafatologia",1458,"Há gente cujo saldo na FEP está escrito com sangue — os **parafatos** exigem muita compreensão na análise das complexidades da Evoluciologia."),
 "paramomento-impactante": lo("Impacto",1015,"A **verdade** mais impactante é a multidimensional."),
 "paraparentela": lo("Paraparentela",1472,"A *energia consciencial* (EC) gera a **paraparentela** com laços muito mais potentes do que os do parentesco nascido do sangue ou da Genética."),
 "paraprocedencia": lo("Paraprocedenciologia",1479,"A paraprocedência pré-ressomática é o **megamagistério**; quem vive na ostentação confessa a paraprocedência baratrosférica."),
 "pararrealidade": lo("Para-História",1464,"A *História* retrata 50% da realidade; a **Para-História** é fiel à verdadeira realidade e à *pararrealidade.*"),
 "paratecnica": src("Homo sapiens reurbanisatus","hsr","cap. 37",119,"O termo *paratécnica* é neologismo técnico da Paratecnologia; só quem tem parapsiquismo teático avançado a entende bem."),
 "paravivencia": lo("Automegadiscernimento",246,"A **Comunex Evoluída** é o ambiente da paravivência com o automegadiscernimento."),
 "parestacao-de-trabalho": dac("Parestacionologia",1227,"A conscin entende melhor a intermissão a partir da ofiex — *a parestação de trabalho, a central desassediadora, o sustentáculo interdimensional, o laborex vivo* — ainda na vida humana."),
 "parextrapolacionismo": lo("Parextrapolação",1502,"O **parextrapolacionismo** é melhor, e de melhores resultados, quando promovido pela consciex amparadora, na dimensão intermissiva."),
 "transmigraciologia-extrafisica": lo("Transmigraciologia",1957,"A **Transmigraciologia Extrafísica** evidencia que ninguém é indispensável, chegando a provocar a *separabilidade grupocármica.*"),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "abordagem-extrafisica": R("acessar uma consciex na dimenex","[[acao-extrafisica]] · [[paraprocedencia]]"),
 "acao-extrafisica": R("atuar nas dimensões extrafísicas","[[abordagem-extrafisica]] · [[paravivencia]]"),
 "agendex-da-ofiex": R("agenda de tarefas da ofiex","[[base-extrafisica]] · [[parestacao-de-trabalho]] · [[central-extrafisica-de-energia]]"),
 "base-extrafisica": R("condição sólida e permanente da consciência","[[paraprocedencia]] · [[agendex-da-ofiex]]"),
 "central-extrafisica-de-energia": R("parainstituição de estoque de ECs","[[parestacao-de-trabalho]] · [[agendex-da-ofiex]]"),
 "consciexialidade-assexuada": R("consciex liberta das injunções sexuais","[[paravivencia]] · [[paraparentela]]"),
 "parafatologia": R("ciência dos parafatos","[[pararrealidade]] · [[paramomento-impactante]]"),
 "paragafe": R("inabilidade extrafísica desastrada","[[abordagem-extrafisica]] · [[paratecnica]]"),
 "paramomento-impactante": R("instante extrafísico de pináculo evolutivo","[[parextrapolacionismo]] · [[paravivencia]]"),
 "paraparentela": R("consciexes afinizadas (laços de EC)","[[parestamento]] · [[consciexialidade-assexuada]] · [[paraprocedencia]]"),
 "paraprocedencia": R("base extrafísica original da conscin","[[base-extrafisica]] · [[paraparentela]] · [[pararrealidade]]"),
 "pararrealidade": R("a realidade extrafísica do Cosmos","[[parafatologia]] · [[paramomento-impactante]]"),
 "paratecnica": R("processamento da Paratecnologia","[[paragafe]] · [[abordagem-extrafisica]]"),
 "paravivencia": R("autovivência extrafísica da consciex","[[acao-extrafisica]] · [[consciexialidade-assexuada]] · [[paramomento-impactante]]"),
 "parestacao-de-trabalho": R("ambiente extrafísico de trabalho grupal","[[parestamento]] · [[central-extrafisica-de-energia]] · [[agendex-da-ofiex]]"),
 "parestamento": R("grupo de consciexes de mesma função","[[parestacao-de-trabalho]] · [[paraparentela]]"),
 "parextrapolacionismo": R("antecipação parafenomenológica do nível","[[paramomento-impactante]] · [[realce-extrafisico]]"),
 "realce-extrafisico": R("relevância meritória da conscin na dimenex","[[parextrapolacionismo]] · [[abordagem-extrafisica]]"),
 "transmigraciologia-extrafisica": R("ciência das transmigrações extrafísicas","[[paraprocedencia]] · [[pararrealidade]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
