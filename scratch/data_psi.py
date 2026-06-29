# -*- coding: utf-8 -*-
ESP = "Psicossomatologia"
A = "[[psicossoma]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "aborrecimento": lo("Aborrecimento",44,"*Aborrecimento: dor moral.* O aborrecimento, mesmo cordial, entre duas pessoas tem raiz baratrosférica."),
 "acanhamento": lo("Acanhamento",48,"*Acanhamento: primeira covardia.* A raiz do acanhamento, em geral, tem a ver com a repressão dos pais na fase infantil."),
 "aconchego": lo("Atos",174,"O ato de *acolher* é o aconchego; o de *instruir* é o levantamento; o de *encaminhar* é o amparo."),
 "afetividade": lo("Afetividade",65,"Existe **afetividade pura** mesmo sem perfeição e sem entusiasmo."),
 "ansiedade": lo("Ansiedade",108,"*Ansiedade é prematuridade.* A ansiedade é a primeira manifestação de desequilíbrio mental."),
 "antagonismo-bem-estar-malestar": lo("Bioquimicologia",346,"Os **autopensenes** detonam a bioquímica do soma, gerando bem-estar ou malestar: os humores do corpo determinam o humor."),
 "autoinseguranca": src("Homo sapiens pacificus","hsp","cap. 18",590,"A *autoinsegurança* é a condição da pessoa insegura consigo mesma, com falta de confiança nas próprias qualidades e potenciais."),
 "automotivacao": lo("Automotivação",250,"Sem automotivação não há **autocompreensão** razoável; a automotivação, a rigor, não é entusiasmo pessoal."),
 "beatice": lo("Beatice",331,"A história da beatice é a história lastimável da idolatria, da imaturidade, da inexperiência e da ignorância humana."),
 "beleza": lo("Beleza",332,"*Beleza: glória verponológica. Beleza: anticaos natural.*"),
 "comodismo-piegas": lo("Profile",1643,"A condição do *low-profile* pessoal, em muitos casos, é puro comodismo — fio da navalha entre o low-profile e o comodismo."),
 "credulidade": lo("Credulidade",548,"*Credulidade: autorreação infantil.* Quem vive a partir do princípio da descrença lastima a credulidade que chega à bovinolatria."),
 "dependencia": src("Homo sapiens reurbanisatus","hsr","cap. 69",206,"Há *dependências* ou coleiras compulsórias do ego (alimentar, econômico-financeira etc.); o líder é mais dependente do que o liderado."),
 "euforin": lo("Euforin",791,"A *euforin* e a automegaeuforização aparecem com o desenvolvimento de nossos talentos."),
 "frustracao": lo("Frustração",891,"A **autovivência da frustração** é uma bênção evolutiva."),
 "frustracao-cosmoetica": lo("Frustração",891,"A **autovivência da frustração** é uma bênção evolutiva — negar precipitadamente a realidade gera a frustração cosmoética."),
 "impaciencia-disfuncional": lo("Impaciência",1015,"Quando a *impaciência* entra pela porta, a **prudência** sai pela janela; o impaciente habitual caminha à depressão ou distimia."),
 "irrompimento-do-psicossoma": src("Projeciologia","proj","cap. 130",296,"O irrompimento do psicossoma é decorrência natural do desenvolvimento parapsíquico; os portadores de macrossomas são os mais predispostos."),
 "obsolescencia-psicossomatica": lo("Obsolescência",1378,"A obsolescência das ideias predispõe inevitavelmente a eclosão das **neoverpons.**"),
 "reacao-exagerada": lo("Admiração",60,"A **idolatria** é a admiração exagerada e patológica; a admiração deve caminhar para a autocompreensão."),
 "satisfacao-ambigua": lo("Satisfação",1794,"A **satisfação** é a base da vida; vivemos satisfeitos com o que possuímos e insatisfeitos com o que ainda precisamos adquirir."),
 "seducao-da-simplificacao": lo("Simplificação",1831,"Os contextos da Conscienciologia simplificam a complexidade da vida a partir do princípio da descrença — sem ceder à sedução da simplificação açodada."),
 "endosso-sentimental": src("700 Experimentos da Conscienciologia","700exp","cap. 444",508,"O local de libertação das consciências não pode ser consultório sentimental para as paixões egocêntricas do instante: a Terra é a Megaescola."),
 "paravinculo": dac("Autoparamegavincologia",381,"O evoluciólogo ou parapreceptor do CI aponta a ideia fundamental ou paravinco para a consciex, demonstrando a importância de reter a essência da próxima existência."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "aborrecimento": R("desgosto de raiz baratrosférica","[[ansiedade]] · [[impaciencia-disfuncional]]"),
 "acanhamento": R("covardia inicial (repressão infantil)","[[autoinseguranca]] · [[comodismo-piegas]]"),
 "aconchego": R("acolhimento/amparo afetivo","[[afetividade]] · [[automotivacao]]"),
 "afetividade": R("fenômenos psíquicos (emoção/sentimento)","[[aconchego]] · [[satisfacao-ambigua]] · [[satisfacao-benevola]]"),
 "ansiedade": R("apreensão sem causa (desequilíbrio)","[[aborrecimento]] · [[impaciencia-disfuncional]]"),
 "antagonismo-bem-estar-malestar": R("dualidade bem-estar/malestar","[[satisfacao-ambigua]] · [[frustracao]]"),
 "antitipo-extrafisico": R("consciex transfigurada pelo psicossoma","[[irrompimento-do-psicossoma]] · [[paraanaplasia]]"),
 "autofuga": R("fugir do autenfrentamento","[[comodismo-piegas]] · [[seducao-da-simplificacao]]"),
 "autoinseguranca": R("insegurança consigo (ciúme)","[[acanhamento]] · [[ansiedade]]"),
 "automotivacao": R("disposição sadia e otimista","[[euforin]] · [[afetividade]]"),
 "beatice": R("fé sem vivência (crendice)","[[credulidade]] · [[reacao-exagerada]]"),
 "beleza": R("qualidade do belo (anticaos)","[[satisfacao-benevola]] · [[afetividade]]"),
 "comodismo-piegas": R("comodismo da lei do menor esforço","[[autofuga]] · [[acanhamento]]"),
 "credulidade": R("crer facilmente (autorreação infantil)","[[beatice]] · [[reacao-exagerada]]"),
 "dependencia": R("incapacidade de decidir sozinho","[[autoinseguranca]] · [[comodismo-piegas]]"),
 "efusividade": R("manifestar-se com efusão","[[afetividade]] · [[reacao-exagerada]]"),
 "endosso-sentimental": R("aprovar por apego sentimental","[[afetividade]] · [[satisfacao-ambigua]]"),
 "estigma-autobiografico": R("megatrafar ainda indescartável","[[obsolescencia-psicossomatica]] · [[paravinculo]]"),
 "euforin": R("euforia intrafísica pré-dessoma","[[automotivacao]] · [[satisfacao-benevola]]"),
 "frustracao": R("privação do desfrute (bênção evolutiva)","[[frustracao-cosmoetica]] · [[satisfacao-ambigua]]"),
 "frustracao-cosmoetica": R("negar precipitadamente a realidade","[[frustracao]] · [[seducao-da-simplificacao]]"),
 "impaciencia-disfuncional": R("falta de paciência (distimia)","[[ansiedade]] · [[aborrecimento]]"),
 "inducao-inicial": R("indução remota na infância","[[paravinculo]] · [[dependencia]]"),
 "irrompimento-do-psicossoma": R("insinuação do paracorpo dos desejos","[[antitipo-extrafisico]] · [[paraanaplasia]]"),
 "obsolescencia-psicossomatica": R("decrepitude dos recursos emocionais","[[estigma-autobiografico]] · [[frustracao]]"),
 "paraanaplasia": R("consciex restabelece a forma (2ª dessoma)","[[antitipo-extrafisico]] · [[irrompimento-do-psicossoma]]"),
 "paravinculo": R("paravinco insculpido no psicossoma","[[inducao-inicial]] · [[estigma-autobiografico]]"),
 "reacao-exagerada": R("arrebatamento perante um fato","[[impaciencia-disfuncional]] · [[credulidade]]"),
 "satisfacao-ambigua": R("prazer contraditório/dúbio","[[satisfacao-benevola]] · [[frustracao]]"),
 "satisfacao-benevola": R("prazer sincero pelo êxito alheio","[[satisfacao-ambigua]] · [[afetividade]]"),
 "seducao-da-simplificacao": R("simplificar açodadamente por ansiedade","[[autofuga]] · [[frustracao-cosmoetica]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
