# -*- coding: utf-8 -*-
ESP = "Parapedagogiologia"
A = "[[conscienciologia]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "apedeutismo": lo("Apedeutismo",126,"*Apedeutismo: megapatologia mentalsomática.* A maior patologia da Humanidade é a ignorância evolutiva."),
 "aula-de-conscienciologia": lo("Aula",179,"A **aula magna** da Escola da Autexperiência é a vivência da *técnica das autorreflexões de 5 horas*; quem dá a aula é a primeira pessoa a recebê-la."),
 "autodidatismo": lo("Autodidatismo",226,"*Autodidatismo é autocriatividade.* A melhor educação pessoal é a mantida ininterruptamente pelo autodidatismo."),
 "exemplologia": lo("Exemplologia",824,"*Conscienciologia: Exemplologia Cosmoética* — o vocábulo Exemplologia é sinônimo de História, nem sempre com qualificação edificante."),
 "facilitador-da-conscienciologia": lo("Você",2032,"O maior *travão* da sua vida é você mesmo; em compensação, o maior **facilitador** da sua vida é também você mesmo."),
 "informacao-esclarecedora": lo("Informação",1053,"Quem pede **informação** evita erros — base das tarefas diárias do esclarecimento."),
 "paratecnica-didatica": lo("Visitação",2022,"A promoção da visita da consciex intermissivista à *Comunex Evoluída* é uma **paratécnica didática** de alta expressão."),
 "tempo-dos-cursos-intermissivos": src("Projeciologia","proj","cap. 426",820,"Os cursos intermissivos têm utilidades claras para a evolução: é questão de lógica e de simples despertamento da inteligência."),
 "tertulia-conscienciologica": lo("Tertúlia",1926,"O objetivo da **tertúlia conscienciológica** não é alguém ser entronizado no pódio, mas todos alcançarem esclarecimentos evolutivos."),
 "transmissao-gratificante": lo("Verpons",2005,"Descobrir as **verpons** é a conduta mais difícil, mas a mais gratificante e rentável evolutivamente — base da transmissão gratificante."),
 "antidoutrinacao": src("700 Experimentos da Conscienciologia","700exp","cap. 631",695,"A invéxis é antidoutrinação com autocrítica máxima, não um novo salvacionismo catequista."),
 "prova-geral-de-conscienciologia": lo("Íntimo",1106,"O **óbvio de hoje** é a prova remanescente da ignorância geral de ontem."),
 "tecnica-do-bloco-tridisciplinar": src("Projeciologia","proj","cap. 155",342,"Os fenômenos conscienciais inserem-se em blocos fenomenológicos (1 a 10) — base da técnica do bloco tridisciplinar (reunião de 3 disciplinas)."),
 "auteducabilidade": dac("Antidepressiologia",140,"Toda vez que pensar em algo negativo, pense que pode ser autassédio e busque mudar o foco da autopensenização — a auteducabilidade exercita esse redirecionamento."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "antidoutrinacao": R("evitar a imposição de doutrinas","[[informacao-esclarecedora]] · [[exemplologia]]"),
 "apedeutismo": R("falta de instrução (megapatologia mentalsomática)","[[auteducabilidade]] · [[autodidatismo]]"),
 "aula-de-conscienciologia": R("lição de tema conscienciológico","[[tertulia-conscienciologica]] · [[paratecnica-didatica]] · [[prova-geral-de-conscienciologia]]"),
 "auteducabilidade": R("ser educável/autoeducar-se","[[autodidatismo]] · [[apedeutismo]]"),
 "autodidatismo": R("recin/recéxis com autoatualização","[[auteducabilidade]] · [[transmissao-gratificante]]"),
 "exemplologia": R("ciência dos exemplos (Exemplologia Cosmoética)","[[facilitador-da-conscienciologia]] · [[transmissao-gratificante]]"),
 "facilitador-da-conscienciologia": R("quem expõe com o exemplo cosmoético","[[aula-de-conscienciologia]] · [[exemplologia]]"),
 "informacao-esclarecedora": R("base das tarefas do esclarecimento","[[antidoutrinacao]] · [[transmissao-gratificante]]"),
 "paratecnica-didatica": R("paratécnica de ensino multidimensional","[[aula-de-conscienciologia]] · [[tecnica-do-bloco-tridisciplinar]]"),
 "prova-geral-de-conscienciologia": R("aferição pedagógica periódica","[[aula-de-conscienciologia]] · [[autodidatismo]]"),
 "tecnica-do-bloco-tridisciplinar": R("reunir 3 disciplinas afins","[[paratecnica-didatica]] · [[aula-de-conscienciologia]]"),
 "tempo-dos-cursos-intermissivos": R("período/sentido dos CIs","[[paratecnica-didatica]] · [[informacao-esclarecedora]]"),
 "tertulia-conscienciologica": R("círculo de debates evolutivos","[[aula-de-conscienciologia]] · [[transmissao-gratificante]]"),
 "transmissao-gratificante": R("comunicar o autoconhecimento a outrem","[[informacao-esclarecedora]] · [[exemplologia]] · [[tertulia-conscienciologica]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
