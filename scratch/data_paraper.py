# -*- coding: utf-8 -*-
ESP = "Parapercepciologia"
A = "[[parapsiquismo]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "agudizacao-do-autoparapsiquismo": lo("Autoparapsiquismo",255,"A vivência do **autoparapsiquismo** aumenta as previsões e diminui os acidentes; mais vale um grão de autoparapsiquismo do que arrobas de artesanalidade."),
 "alucinacao": lo("Alucinação",83,"*Alucinação: imaginação antissensorial.* A alucinação é filha da imaginação."),
 "antiparapsiquismo": src("Homo sapiens pacificus","hsp","cap. 10",584,"Os vocábulos *antiparapsiquismo* e *antiparapsiquista* são neologismos técnicos da Parapercepciologia."),
 "autoproexis-parapsiquica": lo("Autoproéxis",272,"*Autoproéxis: sumário existencial. Autoproéxis: arcabouço existencial.*"),
 "consistencia-paraperceptiva": lo("Consistência",505,"A inconsistência do romantismo *versus* a **consistência do autodiscernimento** oferece a síntese teática mais relevante da Mentalsomatologia."),
 "desrepressao-parapsiquica": src("Manual da Proéxis","proexis","cap. 39",138,"A desrepressão consciencial começa no soma até atingir o mentalsoma, através da autorganização."),
 "distorcao-parapsiquica": src("Homo sapiens pacificus","hsp","cap. 329",880,"O fator de distorção autoconsciencial compõe a condição de autassédio (intra) ou heterassédio (inter) na conscin desestabilizada."),
 "dragona-parapsiquica": lo("Dragona",670,"A dragona parapsíquica favorece as **autorretrocognições** da conscin portadora; certas marcas físicas são manifestações do mentalsoma na fisiologia do soma."),
 "escala-perceptiva-das-consciencias": src("Homo sapiens reurbanisatus","hsr","cap. 65",198,"A Escala Evolutiva das Consciências (Tabela 06) ordena as percepções das conscins na ordem evolutiva."),
 "marca-parapsiquica": lo("Marcas",1220,"O *nevo* é a marca somática de nascimento da Genética; a **dragona parapsíquica** é a marca somática de nascimento da Paragenética da conscin ou consciex ressomada."),
 "multidimensiologia": lo("Multidimensiologia",1330,"Uma só verpon, quanto à Multidimensiologia, vale mais do que 1 milhão de mentiras dos idiotismos culturais desta dimensão respiratória."),
 "multidimensionalidade-consciencial": src("Homo sapiens pacificus","hsp","cap. 334",890,"A condição da multidimensionalidade consciencial somente é bem entendida quando assentada na Holossomática."),
 "paraconscienciologia": dac("Paraconscienciologia",1139,"Nas automaxiconquistas dos paraconscienciólogos importa a interação Intraconscienciologia-Paraconscienciologia, antes, durante e depois dos Cursos Intermissivos."),
 "paraconscienciometria": dac("Autoparageometriologia",375,"A exegese da Cosmanálise — Conscienciometria e Paraconscienciometria — desenvolve a Geometria da Automegacognição."),
 "paraperceptibilidade-da-consciex": lo("Paraperceptibilidade",1475,"— Qual a reação mais sutil que você pode ter perante uma consciex? Você não deve se perturbar com a claridade da luz extrafísica."),
 "parapsiquismo": lo("Parapsiquismo",1482,"A **autolucidez** quanto ao parapsiquismo elimina a solidão egocêntrica; você vale as suas parapercepções."),
 "parapsiquismo-intelectual": lo("Parapsiquismo",1485,"O ápice qualificativo do parapsiquismo é o intelectual, quando aplica a **Mentalsomatologia** teaticamente; misticismos e ritualísticas ainda são primários."),
 "parapsiquismo-paraproxemico": lo("Parapsiquismo",1482,"A autolucidez quanto ao parapsiquismo elimina a solidão egocêntrica — base do parapsiquismo paraproxêmico (Cronêmica/Proxêmica)."),
 "paratecnologia-da-inteleccao": lo("Intelecção",1069,"Com o emprego da **intelecção**, todas as questões ficam mais claras."),
 "pedagio-parapsiquico": lo("Pedágio",1516,"O pedágio mais sério na vida humana é a manutenção permanente da **autolucidez** relativa ao contexto e ao momento evolutivo."),
 "sinaletica-parapsiquica": src("Homo sapiens reurbanisatus","hsr","cap. 138",354,"O *trinômio* das sinaléticas pessoais é constituído pela sinalética bioenergética, a anímica e a parapsíquica."),
 "solucao-parapsiquica": src("700 Experimentos da Conscienciologia","700exp","cap. 426",490,"A solução parapsíquica resolve questões da maturidade parapsíquica e sexual onde a razão comum não alcança."),
 "traducao-parapsiquica": lo("Tradução",1943,"*Tradução: tares fraternal.* (Interpretação/exegese do parafenômeno.)"),
 "visao-panoramica": src("Projeciologia","proj","cap. 55",154,"A visão panorâmica projetiva é a clarividência retrospectiva espontânea, em bloco, de fatos humanos e condições psicológicas, pela superatividade da memória evocativa."),
 "megarrevelacao-racional": lo("Autodiscernimento",227,"*Autodiscernimento: freio racional* — base da captação racional da verpon na megarrevelação."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
PS="[[sinaletica-parapsiquica]]"; AP="[[parapsiquismo-intelectual]]"
REL = {
 "agudizacao-do-autoparapsiquismo": R("incremento agudo das parapercepções","[[recurso-parapsiquico]] · [[despertamento-parapsiquico-precoce]]"),
 "alucinacao": R("percepção aparente sem objeto real","[[distorcao-parapsiquica]] · [[pseudoerro]]"),
 "antiparapsiquismo": R("reação contra o parapsiquismo","[[jejunice-parapsiquica]] · [[atitude-parapsiquica-passiva]]"),
 "atitude-parapsiquica-passiva": R("apassivar-se no transe","[[antiparapsiquismo]] · [[desrepressao-parapsiquica]]"),
 "autoproexis-parapsiquica": R("proéxis embasada no parapsiquismo","[[recurso-parapsiquico]] · [[parapsiquismo-intelectual]]"),
 "coativacao-atributiva": R("ativação simultânea de atributos","[[consistencia-paraperceptiva]] · [[parapsiquismo-intelectual]]"),
 "conotacao-parapsiquica": R("associação/vinculação parapsíquica","[[traducao-parapsiquica]] · [[parapercepto]]"),
 "consistencia-paraperceptiva": R("integridade da parapercepção","[[parapercepto]] · [[paraperceptometria]]"),
 "desintermediacao": R("eliminar o intermediário parapsíquico","[[autoproexis-parapsiquica]] · [[agudizacao-do-autoparapsiquismo]]"),
 "despertamento-parapsiquico-precoce": R("despertar precoce das potencialidades","[[agudizacao-do-autoparapsiquismo]] · [[desrepressao-parapsiquica]]"),
 "desrepressao-parapsiquica": R("desreprimir as sensibilidades parapsíquicas","[[atitude-parapsiquica-passiva]] · [[despertamento-parapsiquico-precoce]]"),
 "distorcao-parapsiquica": R("deformação da parapercepção","[[alucinacao]] · [[pseudoerro]]"),
 "dragona-parapsiquica": R("marca paragenética de nascimento","[[marca-parapsiquica]] · "+PS),
 "escala-perceptiva-das-consciencias": R("sequência das percepções por nível","[[paraperceptibilidade-da-consciex]] · [[multidimensionalidade-consciencial]]"),
 "jejunice-parapsiquica": R("ignorância nosográfica do parapsiquismo","[[antiparapsiquismo]] · [[atitude-parapsiquica-passiva]]"),
 "marca-parapsiquica": R("traço parapsíquico no soma","[[dragona-parapsiquica]] · "+PS),
 "megafenomenologia": R("ciência dos megaparafenômenos","[[multidimensiologia]] · [[paraconscienciologia]]"),
 "megarrevelacao-racional": R("captação racional da verpon","[[solucao-parapsiquica]] · [[parapsiquismo-intelectual]]"),
 "monitoramento-consciencial": R("controle indireto (sadio ou vampirizador)","[[pedagio-parapsiquico]] · [[distorcao-parapsiquica]]"),
 "multidimensiologia": R("ciência da multidimensionalidade","[[multidimensionalidade-consciencial]] · [[paraconscienciologia]]"),
 "multidimensionalidade-consciencial": R("viver em mais de uma dimensão","[[multidimensiologia]] · [[escala-perceptiva-das-consciencias]]"),
 "paraconscienciologia": R("ciência do parapsiquismo","[[paraconscienciometria]] · [[multidimensiologia]]"),
 "paraconscienciometria": R("medir a consciência por parapercepção","[[paraconscienciologia]] · [[paraperceptometria]]"),
 "paracontato": R("sentir convictamente a paratato/paracontato","[[paraperceptibilidade-da-consciex]] · [[paramizade]]"),
 "paramizade": R("amizade na convivialidade multidimensional","[[paracontato]] · [[paraperceptibilidade-da-consciex]]"),
 "paraperceptibilidade-da-consciex": R("percepção transcendente da consciex","[[escala-perceptiva-das-consciencias]] · [[paracontato]]"),
 "parapercepto": R("o conteúdo da parapercepção","[[consistencia-paraperceptiva]] · [[paraperceptometria]]"),
 "paraperceptometria": R("ciência da medida da parapercepção","[[parapercepto]] · [[paraconscienciometria]]"),
 "parapsiquismo": R("vivenciar parapercepções além dos sentidos","[[parapsiquismo-intelectual]] · [[autoproexis-parapsiquica]] · "+PS),
 "parapsiquismo-despercebido": R("parafenômenos vividos sem se notar","[[semiparapercepcao]] · [[parapsiquismo]]"),
 "parapsiquismo-intelectual": R("ápice: parapsiquismo com Mentalsomatologia","[[parapsiquismo]] · [[paratecnologia-da-inteleccao]]"),
 "parapsiquismo-paraproxemico": R("parapercepção de contraponto (espaço/tempo)","[[parapsiquismo]] · [[conotacao-parapsiquica]]"),
 "paratecnologia-da-inteleccao": R("paraciência da intelecção","[[parapsiquismo-intelectual]] · [[megarrevelacao-racional]]"),
 "pedagio-parapsiquico": R("cobrança anticosmoética energética","[[monitoramento-consciencial]] · [[distorcao-parapsiquica]]"),
 "pseudoerro": R("equívoco aparente, na verdade acerto","[[distorcao-parapsiquica]] · [[alucinacao]]"),
 "recurso-parapsiquico": R("técnica maior da conscin parapsíquica","[[solucao-parapsiquica]] · [[agudizacao-do-autoparapsiquismo]]"),
 "semiparapercepcao": R("parapercepção da inspiração do amparador","[[parapsiquismo-despercebido]] · [[conotacao-parapsiquica]]"),
 "sinaletica-parapsiquica": R("sinais parapsíquicos identificados","[[marca-parapsiquica]] · [[recurso-parapsiquico]] · [[parapsiquismo]]"),
 "solucao-parapsiquica": R("resposta parapsíquica à dificuldade","[[recurso-parapsiquico]] · [[megarrevelacao-racional]]"),
 "traducao-parapsiquica": R("hermenêutica do parafenômeno","[[conotacao-parapsiquica]] · [[parapercepto]]"),
 "visao-panoramica": R("clarividência retrospectiva em bloco","[[parapsiquismo]] · [[recurso-parapsiquico]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
