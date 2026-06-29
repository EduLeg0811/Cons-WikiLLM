# -*- coding: utf-8 -*-
ESP = "Autocogniciologia"
A = "[[autocognicao]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "afinidade-cognitiva": lo("Afinidade",66,"A **telepatia** é facilitada pela afinidade e pelo convívio mais íntimo."),
 "apreensibilidade": dac("Cadenciologia",478,"O impacto pode ser intenso ou moderado em função da apreensibilidade gradual do conteúdo da exposição (Comunicologia)."),
 "assunto-mateologico": lo("Assunto",167,"Dependendo do **assunto**, até o Ser Serenão pode ser ignorante."),
 "autocognicao": lo("Autocognição",196,"*Autocognição: autodigestão mentalsomática. Autocognição constitui autossegurança.*"),
 "autocognicao-exaustiva": lo("Autocognição",196,"*Autocognição: autodigestão mentalsomática* — levada incansavelmente à exaustividade."),
 "autocognicao-gratificante": lo("Autocognição",196,"*Autocognição constitui autossegurança* — a autocognição gratificante advém do ato de ensinar e aprender."),
 "autoconviccao": lo("Autoconvicção",208,"A **autoconvicção** é fruto da autocognição máxima e o que mais se aproxima da verdade da consciência; é a confissão do próprio pensamento."),
 "autoconviccao-vivenciada": lo("Autoconvicção",208,"A **autoconvicção** é fruto da autocognição máxima — quando vivenciada, aproxima-se mais da realidade da consciência."),
 "autoidentificacao": src("700 Experimentos da Conscienciologia","700exp","cap. 399",463,"Fazer a autoidentificação (ante a condição assédio/desassédio) também se impõe."),
 "complemento-da-descrenciologia": lo("Descrenciologia",604,"O ***princípio da descrença*** (PD) constitui a autexperimentação pura."),
 "conhecimento": lo("Conhecimento",477,"Somente o **conhecimento** de si mesmo abre a porta para a autoimperturbabilidade; o seu conhecimento amplia o conhecimento alheio."),
 "conhecimento-previo": src("Homo sapiens reurbanisatus","hsr","cap. 70",210,"Pela Ressomática, toda consciência renasce com enorme *bagagem de conhecimento* em função da Paragenética — conhecimento prévio sadio ou patológico."),
 "conjuncao-autocognitiva": lo("Retrocognição",1749,"*Retrocognição: iluminação autocognitiva* (e *Ignorância: invisibilidade autocognitiva*)."),
 "dominio-cognitivo": lo("Nível",1361,"— O seu nível de domínio do contexto da vida intrafísica corresponde ao nível cognitivo da sua contemporaneidade, ou o ultrapassa?"),
 "entendimento-distorcido": lo("Entendimento",724,"O **entendimento maior** exige tempo de autorreflexão; quem aprofunda o entendimento aumenta a holomemória."),
 "equacao-cognitiva": lo("Equação",735,"A equação da **vida autevolutiva** é constituída por 2 termos: 99% de autesforços conquistadores e 1% de dádivas naturais."),
 "fonte-cognitiva": lo("Dicionário",638,"O **dicionário** é a fonte mais fecunda de inspiração cognitiva, intelectual, verponológica ou heurística."),
 "formacao-conscienciologica": src("200 Teáticas da Conscienciologia","200teat","cap. 180",200,"Pela evoluciologia, o grupelho, o grupúsculo e o grupo humano inicial desencadeiam a formação gradativa da Socin (Conscienciológica)."),
 "ilusao-da-regularidade": lo("Ilusão",1009,"A realidade ocupa o lugar da ilusão a partir das **autexperiências**; a imaginação e a hipótese vivem no mundo da ilusão."),
 "impossibilidade-cognitiva": lo("Impossibilidade",1022,"*Impossibilidade é inexperiência.* A aparente impossibilidade deixa de existir ao buscarmos vivenciá-la."),
 "liberdade-interior": lo("Endorreflexologia",719,"A pessoa não vivencia a liberdade interior porque não reconhece esse tesouro: a câmara de autorreflexão para escolher os próprios pensenes."),
 "megaconhecimento-organizado": lo("Megaconhecimento",1241,"A *Enciclopédia da Conscienciologia* é a sistematização do **megaconhecimento**, por especialidades, variáveis e minivariáveis, levadas à exaustividade detalhista."),
 "pista-de-reflexao": lo("Pista",1563,"A **pista mnemônica** desencadeia as autorretrocognições e expõe os detalhes do *passadão* da conscin intermissivista."),
 "reserva-de-leitura": src("Manual da Proéxis","proexis","cap. 22",92,"O ideal é a conscin manter uma reserva de potencialidades do microuniverso consciencial para manter a homeostase holossomática."),
 "saber-transversal": lo("Lateropensene",1149,"A segunda lateralidade é a **ideia transversal** simultânea ao lateropensene inspiracional, captada pela conscin escritora parapsíquica."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "afinidade-cognitiva": R("empatia/autocompreensão imediata de um constructo","[[fonte-cognitiva]] · [[apreensibilidade]]"),
 "apreensibilidade": R("capacidade mentalsomática de apreender","[[afinidade-cognitiva]] · [[dominio-cognitivo]]"),
 "assunto-mateologico": R("tema fora do escopo comum (Mateologia)","[[impossibilidade-cognitiva]] · [[conhecimento]]"),
 "autocognicao": R("autoconhecimento teático (autodigestão mentalsomática)","[[autocognicao-exaustiva]] · [[autoconviccao]] · [[conhecimento]]"),
 "autocognicao-exaustiva": R("autocognição levada à exaustividade","[[autocognicao]] · [[megaconhecimento-organizado]]"),
 "autocognicao-gratificante": R("autocognição compensadora de bem-estar","[[autocognicao]] · [[autoconviccao-vivenciada]]"),
 "autoconviccao": R("certeza firme fruto da autocognição máxima","[[autoconviccao-vivenciada]] · [[autocognicao]]"),
 "autoconviccao-vivenciada": R("autoconvicção comprovada na vivência","[[autoconviccao]] · [[autoidentificacao]]"),
 "autoidentificacao": R("identificar e admitir a si mesma","[[autoconviccao-vivenciada]] · [[liberdade-interior]]"),
 "complemento-da-descrenciologia": R("autopensenização que amplia a autexperiência","[[ilusao-da-regularidade]] · [[autoconviccao]]"),
 "conhecimento": R("apreender/compreender objeto e sujeito","[[conhecimento-previo]] · [[conhecimento-conscienciologico]] · [[megaconhecimento-organizado]]"),
 "conhecimento-conscienciologico": R("princípios/técnicas teáticas da Conscienciologia","[[conhecimento]] · [[formacao-conscienciologica]]"),
 "conhecimento-previo": R("bagagem cognitiva da Paragenética","[[conhecimento]] · [[reserva-de-leitura]]"),
 "conjuncao-autocognitiva": R("associar assuntos diferentes na cognição","[[saber-transversal]] · [[megaconhecimento-organizado]]"),
 "dominio-cognitivo": R("posse plena do conteúdo","[[apreensibilidade]] · [[megaconhecimento-organizado]]"),
 "entendimento-distorcido": R("apreensão deformada do conteúdo","[[ilusao-da-regularidade]] · [[impossibilidade-cognitiva]]"),
 "equacao-cognitiva": R("igualdade entre 2 autotrafores/atributos","[[conjuncao-autocognitiva]] · [[autoconviccao]]"),
 "filial-cognitiva": R("interdependência cognitiva entre condições","[[afinidade-cognitiva]] · [[conhecimento]]"),
 "fonte-cognitiva": R("objeto/texto que gera cognição","[[reserva-de-leitura]] · [[afinidade-cognitiva]]"),
 "formacao-conscienciologica": R("alcançar a condição conscienciológica","[[conhecimento-conscienciologico]] · [[megaconhecimento-organizado]]"),
 "ilusao-da-regularidade": R("regularidade aparente, enganosa","[[entendimento-distorcido]] · [[complemento-da-descrenciologia]]"),
 "impossibilidade-cognitiva": R("incapacidade relativa de conhecer","[[assunto-mateologico]] · [[entendimento-distorcido]]"),
 "liberdade-interior": R("câmara de autorreflexão livre","[[autoidentificacao]] · [[poder-ideologico]]"),
 "megaconhecimento-organizado": R("conhecer e reter sistematizadamente","[[autocognicao-exaustiva]] · [[dominio-cognitivo]] · [[conhecimento]]"),
 "pista-de-reflexao": R("rastro orientador da autopensenização","[[liberdade-interior]] · [[saber-transversal]]"),
 "poder-ideologico": R("poder pela posse de conhecimentos","[[megaconhecimento-organizado]] · [[liberdade-interior]]"),
 "primoponente": R("consciência que propõe primeiro","[[autoconviccao]] · [[conhecimento-conscienciologico]]"),
 "reserva-de-leitura": R("manter fontes técnicas disponíveis","[[fonte-cognitiva]] · [[conhecimento-previo]]"),
 "saber-transversal": R("autocognição lateral suplementar","[[conjuncao-autocognitiva]] · [[pista-de-reflexao]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
