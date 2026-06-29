# -*- coding: utf-8 -*-
ESP = "Autoparapercepciologia"
A = "[[parapsiquismo]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "autocomprovacao-parapsiquica": lo("Encapsulamento",715,"Quem vivencia o encapsulamento energético promovido por amparador jamais deixa de pensar na extrafisicalidade, pela inexorável autocomprovação de sinaléticas."),
 "autoparapsiquismo-aflorado": lo("Autoparapsiquismo",254,"*Pesquisemos o autoparapsiquismo.* Não há sabedoria razoável sem o autoparapsiquismo; o autoparapsiquismo inconsciente é um heterassédio psicopático."),
 "autoparapsiquismo-avancado": lo("Autoparapsiquismo",255,"O autoparapsiquismo racional com a **Ciência** é muito mais avançado que os arremedos do parapsiquismo infantil, místico, das seitas e religiões."),
 "escala-das-parapercepcoes": dac("Parassensoriamentologia",1199,"Pode-se estabelecer uma *escala de parassensoriamentos* entre parafatos, segundo os valores das hiperacuidades das parapercepções."),
 "estatura-parapsiquica": lo("Estaturas",780,"Nem sempre a *estatura corporal* corresponde à **estatura cerebral** — análogo à estatura parapsíquica."),
 "isolamento-dignificador": lo("Isolamento",1120,"*Isolamento: dieta espacial.* O isolamento expande as definições da consciência; um retiro de isolamento atarefado é inevitável à conscin escritora."),
 "parapercepcao-impressiva": src("Homo sapiens pacificus","hsp","cap. 67",205,"A unidade de trabalho ou medida da Parapercepciologia é a *parapercepção.*"),
 "parapercepcao-patologica": src("Projeciologia","proj","cap. 408",776,"Há parapercepção consciencial pura do ambiente extrafísico (Extrafisicologia) e da dimensão mentalsomática — quando desequilibrada na conscin inexperiente, torna-se patológica."),
 "parapolimatia": dac("Imitaciologia",782,"Os extrapolacionismos parapsíquicos (Autoparapercepciologia), promovidos pelos amparadores de função, atuam como bônus evolutivos multidimensionais — base da parapolimatia."),
 "preco-da-autoparaperceptibilidade": lo("Autoparaperceptibilidade",253,"A **autoparaperceptibilidade** é o fator máximo de enriquecimento da vida humana; quanto maior, maior a qualificação evolutiva da assistência prestada."),
 "prioridade-parapsiquica": lo("Prioridade",1627,"Quem identifica mais prioridade no **processo evolutivo** das consciências acerta mais na interassistencialidade."),
 "sub-rotina-parapsiquica": src("200 Teáticas da Conscienciologia","200teat","cap. 59",79,"Pela parapercepciologia, o desperto usa a sinalética energética, intraconsciencial e parapsíquica ao máximo, de rotina, o tempo todo."),
 "teto-parapsiquico": lo("Teto",1930,"No teto mal vedado da cabeça da pessoa irrefletida entram as chuvas das coisas mais absurdas — precisamos de autorreflexões."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
S="[[sinaletica-parapsiquica]]"
REL = {
 "autocomprovacao-parapsiquica": R("testar/verificar o parafenômeno na própria vivência","[[autoparapsiquismo-aflorado]] · "+S),
 "autoparapsiquismo-aflorado": R("surgimento das parapercepções (autodiscernimento)","[[autoparapsiquismo-avancado]] · [[autocomprovacao-parapsiquica]]"),
 "autoparapsiquismo-avancado": R("predomínio racional do autoparapsiquismo","[[autoparapsiquismo-aflorado]] · [[parapolimatia]]"),
 "autoparassomatologia": R("ciência dos parafenômenos do parassoma","[[autoparapsiquismo-avancado]] · [[codex-subtilissimus-pessoal]]"),
 "codex-subtilissimus-pessoal": R("compilação dos parafenômenos pessoais","[[sequenciamento-parafactual]] · "+S),
 "escala-das-parapercepcoes": R("hierarquia inteligente das parapercepções","[[estatura-parapsiquica]] · [[teto-parapsiquico]]"),
 "estatura-parapsiquica": R("qualidade das parapercepções aplicadas","[[teto-parapsiquico]] · [[autoparapsiquismo-avancado]]"),
 "isolamento-dignificador": R("isolar-se para qualificar o parapsiquismo","[[prioridade-parapsiquica]] · [[autoparapsiquismo-aflorado]]"),
 "parapercepcao-impressiva": R("identificar objetivamente a presença da consciex","[[autocomprovacao-parapsiquica]] · [[parapercepcao-patologica]]"),
 "parapercepcao-patologica": R("sensibilidades parapsíquicas desequilibradas","[[parapercepcao-impressiva]] · [[teto-parapsiquico]]"),
 "parapolimatia": R("cultura extensa de autovivências multidimensionais","[[autoparapsiquismo-avancado]] · [[preco-da-autoparaperceptibilidade]]"),
 "preco-da-autoparaperceptibilidade": R("o valor exigido pela autoparaperceptibilidade","[[parapolimatia]] · [[autoparapsiquismo-avancado]]"),
 "prioridade-parapsiquica": R("a realidade parapsíquica mais relevante primeiro","[[isolamento-dignificador]] · [[sub-rotina-parapsiquica]]"),
 "sequenciamento-parafactual": R("registrar a sequência dos parafatos","[[codex-subtilissimus-pessoal]] · "+S),
 "sub-rotina-parapsiquica": R("sequência de manifestações paraperceptivas","[[prioridade-parapsiquica]] · "+S),
 "teto-parapsiquico": R("limite máximo do desenvolvimento parapsíquico","[[estatura-parapsiquica]] · [[escala-das-parapercepcoes]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
