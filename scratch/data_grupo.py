# -*- coding: utf-8 -*-
ESP = "Grupocarmologia"
A = "[[grupocarma]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "acerto-grupocarmico": src("Homo sapiens reurbanisatus","hsr","cap. 161",406,"O acerto grupocármico é a pararregeneração das opiniões prioritárias, sem radicalismos, no caminho da megafraternidade."),
 "amortizacao-evolutiva": src("700 Experimentos da Conscienciologia","700exp","cap. 564",628,"Você tem conta de *amortização* aberta com as consciências da família nuclear, sujeita a desaparecer depois de 2 ou mais renascimentos?"),
 "consciencia-de-equipe": lo("Equipe",736,"Os **grandes feitos** nunca são realizados por uma única consciência."),
 "consciencia-grupocarmica": src("700 Experimentos da Conscienciologia","700exp","cap. 562",626,"Com autocrítica máxima, você pode plotar a avaliação da sua realidade grupocármica — em qual *estágio policármico* se localiza hoje?"),
 "conscin-trafar": src("Manual da Proéxis","proexis","cap. 39",137,"Um minitraço consciencial nem sempre representa um trafar: pode ser um *pré-trafor.*"),
 "elencologia": lo("Elencologia",699,"No universo da Elencologia, a ***técnica do dever*** é axioma fundamental empregado pelos evoluciólogos."),
 "inseparabilidade-grupocarmica": src("700 Experimentos da Conscienciologia","700exp","cap. 604",668,"A inseparabilidade evolutiva — ou grupocármica — entre consciências é uma das leis básicas e inarredáveis da evolução."),
 "interassedialidade": lo("Preceptoria",1601,"Ser preceptor de preceptorando anticosmoético recalcitrante é compactuar com a interassedialidade."),
 "interdependenciologia": dac("Modismologia",1014,"A conscin lúcida tem de ser independente até certo ponto para ser, de fato, interdependente: *ninguém evolui sozinho.*"),
 "interprisiologia": lo("Interprisiologia",1103,"Os **cegos intencionais**, por interesse, geram interprisões grupocármicas."),
 "libertacao-do-cla": lo("Libertação",1168,"Somos escravizados à ignorância dos compassageiros evolutivos; na autovivência da tares vem a nossa libertação."),
 "pangrafia-grupocarmica": lo("Pangrafia",1436,"*Pangrafia: cosmovisão parapsíquica* — a pangrafia pode reunir múltiplos fenômenos holobiográficos."),
 "recin-grupal": src("Homo sapiens pacificus","hsp","cap. 152",431,"A única solução cosmoética para diminuir as contradições das armas é conscientizar os mercadores da morte quanto à *recin grupal.*"),
 "coletivo-conscienciologico": lo("Parapoliticologia",1478,"A democracia pura é o **amor coletivo** em ação."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "acerto-grupocarmico": R("ajuste cármico simultâneo no grupo","[[amortizacao-evolutiva]] · [[consciencia-grupocarmica]]"),
 "amortizacao-evolutiva": R("repagamento gradual das dívidas cármicas","[[acerto-grupocarmico]] · [[libertacao-do-cla]]"),
 "coletivo-conscienciologico": R("conjunto de realidades da CCCI","[[consciencia-de-equipe]] · [[elencologia]]"),
 "consciencia-de-equipe": R("autolucidez da função no conjunto","[[coletivo-conscienciologico]] · [[elencologia]]"),
 "consciencia-grupocarmica": R("autolucidez da coexistência grupocármica","[[inseparabilidade-grupocarmica]] · [[acerto-grupocarmico]]"),
 "conscin-trafar": R("conscin traço-fardo dependente","[[interassedialidade]] · [[interprisiologia]]"),
 "elencologia": R("ciência do elenco de consciências","[[coletivo-conscienciologico]] · [[consciencia-de-equipe]]"),
 "inseparabilidade-grupocarmica": R("união existencial inarredável do grupo","[[interdependenciologia]] · [[consciencia-grupocarmica]] · [[interprisiologia]]"),
 "interassedialidade": R("assédio mútuo dentro do grupo","[[conscin-trafar]] · [[interprisiologia]]"),
 "interdependenciologia": R("ciência das interdependências evolutivas","[[inseparabilidade-grupocarmica]] · [[consciencia-de-equipe]]"),
 "interprisiologia": R("ciência das interprisões grupocármicas","[[interassedialidade]] · [[libertacao-do-cla]] · [[inseparabilidade-grupocarmica]]"),
 "libertacao-do-cla": R("autesforço de libertar o clã (tares)","[[amortizacao-evolutiva]] · [[recin-grupal]]"),
 "pangrafia-grupocarmica": R("megaabordagem holobiográfica do grupo","[[consciencia-grupocarmica]] · [[recin-grupal]]"),
 "recin-grupal": R("recin que afeta todo o grupo evolutivo","[[libertacao-do-cla]] · [[pangrafia-grupocarmica]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
