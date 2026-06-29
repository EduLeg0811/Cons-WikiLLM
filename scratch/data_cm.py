# -*- coding: utf-8 -*-
ESP = "Conscienciometrologia"
A = "[[conscienciometria]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "autocentramento-consciencial": dac("Autoradologia",419,"A conscin anticonflituosa, intimamente harmonizada, evidencia na Estilística Gráfica alto critério de regularidade e uniformidade — reflexo do autocentramento."),
 "base-da-conscienciologia": lo("Conscienciologia",493,"A Conscienciologia atua sobre os **paracérebros** e está apenas engatinhando; talvez daqui a 3 vidas humanas desta geração de intermissivistas pesquisadores."),
 "carrancismo": src("Homo sapiens pacificus","hsp","cap. 26",595,"O *carrancismo* é a condição da pessoa vivendo presa ao passado, apegada aos tradicionalismos de modo pessimista."),
 "categoria-de-consciencia": lo("Contínuo",514,"A **consciência** é a melhor categoria de contínuo existente."),
 "consciencia-atratora": lo("Aglutinação",71,"A aglutinação pessoal depende da **qualificação da consciência** atratora: as abelhas voam atrás do mel."),
 "consciencia-literal": lo("Confor",474,"É literal a afirmação coloquial de que, com a evolução, a **forma** vai para o espaço."),
 "consciencia-poliedrica": dac("Maximologia",902,"A consciência é realidade poliédrica/complexa quanto à evolução, construída pouco a pouco através dos milênios, exigindo abordagens múltiplas."),
 "conscienciofilia": src("Homo sapiens reurbanisatus","hsr","cap. 23",126,"O termo *conscienciofilia* é neologismo técnico da Conscienciometria — a preocupação simultânea com os percentuais dimensionais."),
 "conscienciologo": lo("Conscienciólogo",496,"Até mesmo o conscienciólogo, pesquisador da consciência, vai sempre dessomar com **teorias** ainda não vivenciadas; ele pensa o mundo pelo paracérebro."),
 "consciencula": dac("Voliciolinologia",1452,"Quem possui inteligência e vontade é sempre o princípio consciencial, desde a consciênçula até o Serenão. *Vontade: motor existencial.*"),
 "conscin-benevola": src("700 Experimentos da Conscienciologia","700exp","cap. 602",666,"Em certo nível de maturidade, ninguém e nenhuma causa conseguem mudar a índole benévola ante todos os seres (Serenões)."),
 "cotejo-conscin-conscienciologo": src("Homo sapiens pacificus","hsp","cap. 358",935,"Do conscienciólogo é exigida superior competência, largueza de vistas, visão panorâmica e *background* cultural, energético e multidimensional."),
 "inteligencia": lo("Pré-Inteligência",1607,"A **pré-inteligência** é superior à inteligência e à pós-inteligência: a cautela vem antes da adversidade."),
 "medida-conscienciologica": src("Homo sapiens reurbanisatus","hsr","cap. 194",466,"A *unidade de medida da especialidade conscienciológica* é o estado de grandeza estipulado como critério de valor e termo de comparação para mensuração."),
 "perfilologia": lo("Perfilologia",1538,"O **perfil intraconsciencial** é muito diferente do *perfil somático* do Ser Humano."),
 "personalidade-antipoda": src("Homo sapiens pacificus","hsp","cap. 362",942,"Pela Conscienciometria, a consciência antípoda evolutiva do Serenão é a consréu transmigrável; o amparador é antípodo ao assediador."),
 "personalidade-complexa": lo("Complexidade",448,"Toda **conscin** é complexa: a pessoa mais existencialmente miserável pode ser a mais orgulhosa do seu contexto social."),
 "qualificacao-dos-trafores": lo("Trafores",1945,"*Os trafores fortalecem. Os crimes enfraquecem. Os vícios matam* — os trafores são limitados por medidas cosmoéticas."),
 "trafor-enganador": lo("Trafor",1945,"*Trafor: talento cosmoético* — mas o trafor enganador é o minitraço bom que mascara um perfil geral negativo."),
 "verbaciologia": lo("Verbaciologia",1996,"A Verbaciologia determina o princípio: todo bom *conselho* precisa ser precedido do melhor *exemplo*; a ação vem primeiro."),
 "vicio-da-formacao-cultural": src("Homo sapiens reurbanisatus","hsr","cap. 250",651,"A autorganização diminui o percentual de erros de qualquer pessoa motivada, independentemente do sexo ou da formação cultural."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
T="[[trafor-trafar]]"
REL = {
 "autocentramento-consciencial": R("conscin assentada no cumprimento da proéxis","[[megaqualificacao-consciencial]] · [[conscin-benevola]]"),
 "autoortodoxia": R("conformação absoluta a um critério","[[carrancismo]] · [[consciencia-literal]]"),
 "base-da-conscienciologia": R("princípios do paradigma consciencial","[[conscienciologo]] · [[medida-conscienciologica]]"),
 "carrancismo": R("apego pessimista ao passado","[[autoortodoxia]] · [[vicio-da-formacao-cultural]]"),
 "categoria-de-consciencia": R("nível de excelência evolutiva","[[consciencia-poliedrica]] · [[megaqualificacao-consciencial]] · [[consciencula]]"),
 "consciencia-atratora": R("atrair pela força presencial/holosfera","[[consciencia-poliedrica]] · [[conscin-benevola]]"),
 "consciencia-literal": R("reproduzir ao pé da letra","[[autoortodoxia]] · [[consciencia-poliedrica]]"),
 "consciencia-poliedrica": R("consciência complexa, multifacetada","[[personalidade-complexa]] · [[categoria-de-consciencia]]"),
 "conscienciofilia": R("percentuais dimensionais (cuidar da consciência)","[[conscienciologo]] · [[autocentramento-consciencial]]"),
 "conscienciologo": R("pesquisador da consciência pelo paracérebro","[[cotejo-conscin-conscienciologo]] · [[base-da-conscienciologia]]"),
 "consciencula": R("consciência humana imatura inicial","[[categoria-de-consciencia]] · [[inteligencia]]"),
 "conscin-benevola": R("índole boa (holomaturidade)","[[qualificacao-dos-trafores]] · "+T),
 "cotejo-conscin-conscienciologo": R("comparar conscin comum × conscienciólogo","[[conscienciologo]] · [[personalidade-complexa]]"),
 "instancia-de-avaliacao": R("local/realidade que avalia a conscin","[[medida-conscienciologica]] · [[perfilologia]]"),
 "inteligencia": R("aptidão/discernimento/intelecção","[[consciencula]] · [[categoria-de-consciencia]]"),
 "medida-conscienciologica": R("unidade de medida da especialidade","[[instancia-de-avaliacao]] · [[base-da-conscienciologia]]"),
 "megaqualificacao-consciencial": R("condição evolutiva pinacular","[[qualificacao-dos-trafores]] · [[autocentramento-consciencial]]"),
 "perfilologia": R("ciência do perfil intraconsciencial","[[personalidade-antipoda]] · [[personalidade-complexa]] · [[instancia-de-avaliacao]]"),
 "personalidade-antipoda": R("traços antípodas (amparador × assediador)","[[perfilologia]] · "+T),
 "personalidade-complexa": R("conscin de traços teaticamente complexos","[[consciencia-poliedrica]] · [[perfilologia]]"),
 "qualificacao-dos-trafores": R("qualificar os traços-força","[[trafor-enganador]] · "+T+" · [[megaqualificacao-consciencial]]"),
 "trafor-enganador": R("minitraço bom que mascara perfil negativo","[[qualificacao-dos-trafores]] · "+T),
 "verbaciologia": R("verbo+ação integrados (verbação)","[[conscin-benevola]] · [[autocentramento-consciencial]]"),
 "vicio-da-formacao-cultural": R("defeito grave da formação cultural","[[carrancismo]] · [[autoortodoxia]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
