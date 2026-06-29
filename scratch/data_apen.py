# -*- coding: utf-8 -*-
ESP = "Autopensenologia"
A = "[[autopensene]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "ato-de-pensenizar": lo("Pensenizar",1527,"Você vale o seu poder de **pensenizar**; o ato de pensenizar vem antes e é mais importante que o ato de falar."),
 "autopensene-inato-raro": lo("Paragenética",1462,"*Paragenética: talento inato* — o autopensene inato raro provém da Paragenética."),
 "autopensene-prioritario": lo("Autopensene",260,"O autopensene é a última partícula da fissão do **paracérebro**; qualifica as realidades de qualquer dimensão."),
 "autopensenizacao": lo("Autopensenização",263,"A autopensenização pode ser móvel (a fala do professor) ou fixa (o texto do escritor); é o ato que alcança o maior nível da liberdade consciencial."),
 "autopensenizacao-analogica": lo("Autopensenização",264,"A autopensenização é o ato que alcança o maior nível da **liberdade** consciencial — a analógica conjuga realidades por semelhança."),
 "autopensenizacao-vigorosa": lo("Autopensenização",264,"A autopensenização é o ato que alcança o maior nível da **liberdade** consciencial — a vigorosa, de alta intensidade."),
 "autopredisposicao-extraordinaria": lo("Pensatogenia",1525,"Assim como há a autopredisposição ginasticogênica, há a **autopredisposição pensatogênica** — o momento pensatogênico."),
 "dubiopensenidade": src("Homo sapiens pacificus","hsp","cap. 231",653,"Entre as 57 patopensenidades dos grupos nosográficos figura a ambivalência da dubiopensenidade (vacilações, indecisões)."),
 "genopensene": src("Homo sapiens reurbanisatus","hsr","cap. 195",468,"Entre as 100 unidades conscienciométricas pensênicas, o genopensene corresponde à ideia inata (retroinformação)."),
 "linearidade-da-autopensenizacao": lo("Autorreflexão",286,"A autopensenização mais avançada passa, inevitavelmente, pela autorreflexão; a *linearidade autopensênica* é resultado das autorreflexões."),
 "megafoco-autopensenico": lo("Sincronicidade",1835,"*Sincronicidade: alinhamento autopensênico* — o megafoco mantém a autopensenidade num ponto ideativo."),
 "pensene-empatico": lo("Pensene",1525,"*Pensene: criação paracerebral.* O pensene renovador vale por 100 outros — o empático harmoniza-se com o fluxo construtivo."),
 "pensene-sistematico": lo("Pensene",1525,"*Pensene: criação paracerebral* — o sistemático embasa-se na racionalidade, na lógica e na Cosmoeticologia."),
 "limite-da-autopensenizacao": lo("Autopensenização",264,"A autopensenização é o ato que alcança o maior nível da **liberdade** consciencial — há, porém, o seu limite pontual."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "ato-de-pensenizar": R("a ação básica e mais complexa da consciência","[[autopensenizacao]] · [[autoortopensenizacao]]"),
 "autoortopensenizacao": R("manter a pensenidade reta (ortopensene)","[[linearidade-da-autopensenizacao]] · [[pensene-sistematico]]"),
 "autopensene-inato-raro": R("neoverpon inata da Paragenética","[[genopensene]] · [[autopensene-prioritario]]"),
 "autopensene-prioritario": R("pensamento imposto como prioridade executiva","[[megafoco-autopensenico]] · [[autopensene-inato-raro]]"),
 "autopensenizacao": R("elaboração intraconsciencial do pensenizar","[[ato-de-pensenizar]] · [[autopensenizacao-vigorosa]] · [[autopensenizacao-analogica]]"),
 "autopensenizacao-analogica": R("pensenizar por analogia/semelhança","[[autopensenizacao]] · [[pensene-empatico]]"),
 "autopensenizacao-vigorosa": R("pensenização de alta intensidade","[[autopensenizacao]] · [[megafoco-autopensenico]]"),
 "autopredisposicao-extraordinaria": R("momento pensatogênico espontâneo","[[autopensene-inato-raro]] · [[megafoco-autopensenico]]"),
 "dubiopensenidade": R("autopensenidade ambivalente/vacilante","[[pensene-sistematico]]" if False else "[[limite-da-autopensenizacao]] · [[pensene-sistematico]]"),
 "genopensene": R("pensene da ideia inata (retroinformação)","[[autopensene-inato-raro]] · [[autopensene-prioritario]]"),
 "limite-da-autopensenizacao": R("raia da pensenização possível","[[autopensenizacao]] · [[dubiopensenidade]]"),
 "linearidade-da-autopensenizacao": R("pensenidade refletida e ininterrupta","[[autoortopensenizacao]] · [[pensene-sistematico]]"),
 "megafoco-autopensenico": R("autopensenidade fixa num ponto ideativo","[[autopensene-prioritario]] · [[autopensenizacao-vigorosa]]"),
 "pensene-empatico": R("autopensene harmonizado com o construtivo","[[pensene-sistematico]] · [[autopensenizacao-analogica]]"),
 "pensene-sistematico": R("pensene racional, lógico, cosmoético","[[pensene-empatico]] · [[autoortopensenizacao]] · [[linearidade-da-autopensenizacao]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
