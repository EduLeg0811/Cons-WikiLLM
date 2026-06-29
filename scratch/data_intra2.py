# -*- coding: utf-8 -*-
ESP = "Intraconscienciologia"
A = "[[intraconscienciologia]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "apetite-insaciavel": src("Homo sapiens pacificus","hsp","cap. 23",593,"O termo *bulimia* ('apetite insaciável') surgiu em 1803, do grego *boulimia* ('fome devoradora', 'fome de boi') — base intraconsciencial da insaciabilidade evolutiva."),
 "autorrealidade-intraconsciencial": lo("Temperamento",1908,"O **temperamento** é a autorrealidade nua e crua da consciência, *temperado* pelos autesforços despendidos nos milênios da evolução."),
 "conscienciologia-profunda": dac("Questiunculologia",1297,"*Tudologia: Conscienciologia Profunda.* — a Neociência em nível de máxima profundidade e abrangência."),
 "conteudo-da-consciencia": lo("Conteúdo",512,"A **holosfera energética** pessoal é o *conteúdo* da consciência; o rosto é o *embrulho.*"),
 "descompressao-consciencial": dac("Baratrosferologia",461,"A Baratrosfera é a *câmara extrafísica de compressão*; a descompressão consciencial é a saída dessa autoconsciencialidade reprimida."),
 "microuniverso-intransitavel": lo("Microuniverso",1294,"O **microuniverso pessoal** é o maior campo de ação da consciência — quando fechado em si mesma, torna-se intransitável."),
 "potencial-consciencial": lo("Potencial",1595,"**Potencial evolutivo** todas as consciências têm; o que falta, em muitos casos, é a aplicação cosmoética das próprias aquisições."),
 "principio-megafocal": lo("Perseverança",1543,"*Perseverança: constância megafocal.*"),
 "realidade-intraconsciencial": src("Manual da Proéxis","proexis","cap. 16",59,"Não adianta forçar a verpon: a autocorrupção não resolve a nossa melhoria intraconsciencial."),
 "truncagem-intraconsciencial": src("200 Teáticas da Conscienciologia","200teat","cap. 194",214,"A monodotação intraconsciencial (uma só inteligência) é a condição oposta, negativa, à tridotação intraconsciencial."),
 "autopotencial-integrado": lo("Parapsiquismo",1481,"O **parapsiquismo mais sério** é o proexológico, integrado à autoproéxis — base do autopotencial integrado."),
 "ancoragem-consciencial-intima": lo("Transcendentalidade",1954,"É necessária tranquilidade íntima para acessar os **conceitos avançados** da evolução consciencial."),
 "autodepuracao-refinada": lo("Vaidade",1986,"A **vaidade** é refinada nos intermissivistas, mas mesmo assim não deixa de ser negativa — a autodepuração refinada a alija."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "ancoragem-consciencial-intima": R("fixação da consciência pelo mentalsoma","[[autorrealidade-intraconsciencial]] · [[realidade-intraconsciencial]]"),
 "apetite-insaciavel": R("insaciabilidade da evolução infinita","[[potencial-consciencial]] · [[autopotencial-integrado]]"),
 "autodepuracao-refinada": R("purificação teática permanente da autopensenidade","[[endoconsistencia]] · [[autorrealidade-intraconsciencial]]"),
 "autopotencial-integrado": R("reunião integrada dos potenciais","[[potencial-consciencial]] · [[autodepuracao-refinada]]"),
 "autorrealidade-intraconsciencial": R("a verdade mais íntima do microuniverso","[[realidade-intraconsciencial]] · [[conteudo-da-consciencia]] · [[endoconsistencia]]"),
 "conscienciologia-profunda": R("a Neociência em máxima profundidade","[[principio-megafocal]] · [[realidade-intraconsciencial]]"),
 "conteudo-da-consciencia": R("essência/intencionalidade do ego","[[autorrealidade-intraconsciencial]] · [[mentales]]"),
 "descompressao-consciencial": R("saída da autoconsciencialidade reprimida","[[microuniverso-intransitavel]] · [[truncagem-intraconsciencial]]"),
 "endoconsistencia": R("consistência interna do princípio consciencial","[[autodepuracao-refinada]] · [[autorrealidade-intraconsciencial]]"),
 "mentales": R("língua íntima do microuniverso","[[conteudo-da-consciencia]] · [[autorrealidade-intraconsciencial]]"),
 "microuniverso-intransitavel": R("consciência fechada em si mesma","[[descompressao-consciencial]] · [[truncagem-intraconsciencial]]"),
 "potencial-consciencial": R("potência latente da consciência","[[autopotencial-integrado]] · [[apetite-insaciavel]]"),
 "principio-megafocal": R("fundamento do megafoco evolutivo","[[conscienciologia-profunda]] · [[autorrealidade-intraconsciencial]]"),
 "realidade-intraconsciencial": R("estrutura mais íntima do microuniverso","[[autorrealidade-intraconsciencial]] · [[ancoragem-consciencial-intima]]"),
 "truncagem-intraconsciencial": R("mutilação involuntária do conteúdo íntimo","[[microuniverso-intransitavel]] · [[descompressao-consciencial]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
