# -*- coding: utf-8 -*-
ESP = "Autexperimentologia"
A = "[[autopesquisa]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "abordagem-da-antessala": lo("Antessala",111,"Os **preâmbulos** minimizam os impactos desnecessários na antessala dos acontecimentos; o ambiente de autorreflexão pode anteceder com proveito qualquer atividade."),
 "aptidao-a-conhecer": lo("Aptidão",134,"*As consciexes ressomam. As conscins dessomam* — toda consciex ressoma inteiramente apta."),
 "atividade-homogenea": lo("Atividade",172,"A **boa atividade** aumenta a longevidade da conscin; a atividade física duplica a força."),
 "autochecagem-indispensavel": src("200 Teáticas da Conscienciologia","200teat","cap. 84",104,"O projetor consciente instala, antes de dormir, rápido estado vibracional de *autochecagem energética.*"),
 "autoconstatacao": lo("Autossinaleticologia",300,"O **banho energético** pode confirmar o amparo extrafísico via autossinalética energética timpânica — base da autoconstatação."),
 "autodispersividade": lo("Autodispersividade",232,"O maior problema da vítima dos próprios talentos versáteis é a **autodispersividade**, com o descarte do essencial; pense no mentalsoma."),
 "autopersuasao-primaria": lo("Autopersuasão",265,"A **conversa** da pessoa que fala para se persuadir não é confiável."),
 "autovivencia-experimental": lo("Autovivência",312,"*Autovivência: holoteca experiencial.* A prática é a autovivência."),
 "binomio-problema-solucao": lo("Problema",1631,"*Problema significa dificuldade.* A questão fácil traz, em si, a solução."),
 "convite-ao-intermissivista": lo("Autodeterminação",224,"Quem declina do convite ao *Curso Intermissivo* (CI) carece de autodeterminação e força para as renovações evolutivas."),
 "duplicidade-de-objetos": src("Homo sapiens reurbanisatus","hsr","cap. 428",1032,"Há a duplicidade anticosmoética — o *bifrentismo patológico* de duas linhas de atividade paralelas não-positivas ao mesmo tempo."),
 "estatistica-motivadora": lo("Estatística",779,"A *consréu* possui mais de 50% de negatividade; o *intermissivista* já possui mais de 50% de positividade."),
 "momento-da-circunspeccao": lo("Circunspecção",414,"Circunspecção inteligente não é pensenizar em círculos."),
 "objeto-ritual": lo("Protocolo",1657,"*Protocolo* é o nome técnico do **ritual científico**: o protocolo substitui o ritual, a etiqueta e os costumes ultrapassados."),
 "parada-produtiva": src("Projeciologia","proj","cap. 489",932,"Análoga à parada cardíaca voluntária no plano técnico — interromper conscientemente a atividade para render mais."),
 "primeira-acao": lo("Pensene",1525,"O **pensene** é sempre a primeira ação gerada pela consciência."),
 "primeira-preocupacao": lo("Preocupação",1614,"A primeira abordagem racional ante qualquer preocupação: — Tal preocupação é mal real ou imaginário? *Preocupação significa autodesorganização.*"),
 "ranque-de-prioridade": lo("Prioridade",1627,"Quem identifica mais prioridade no **processo evolutivo** das consciências acerta mais na interassistencialidade."),
 "rendicao-a-verpon": lo("Rendição",1725,"*Vontade vendida, consciência rendida* — mas render-se à verpon é admitir e aplicar teaticamente a verdade de ponta."),
 "sutileza-tecnica": lo("Sutileza",1882,"Não se esqueça da **sutileza**: quem escreve e lê é muito diferente de quem lê e escreve."),
 "trabalho-antelucano": lo("Antelucano",110,"O período antelucano de **trabalho** em geral é o mais produtivo: *o que à noite se faz, pela manhã aparece.*"),
 "coleta-seletiva": lo("Leitura",1156,"A **leitura seletiva** pode induzir a criatividade das suas ortopensatas."),
 "conscin-fonte": lo("Fonte",880,"A *Comunex Evoluída* é como a fonte dos antídotos e panaceias dos conflitos da consciência pré-serenona."),
 "convite-ao-intermissivista2": None,
 "regra-conscienciologica-recursiva": lo("Regra",1718,"Devemos evitar o engano primário: o bem e o mal não se fundem, mas se apartam — regra sem exceção."),
 "teste-dos-vocabulos": lo("Vocábulos",2031,"A acepção dos vocábulos sempre exige atenção: *carne*, na Gastronomia, tem um significado, e na Sexologia, outro."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "abordagem-da-antessala": R("contato preliminar de pesquisa","[[momento-da-circunspeccao]] · [[primeira-acao]]"),
 "aptidao-a-conhecer": R("predisposição a inteirar-se","[[autovivencia-experimental]] · [[coleta-seletiva]]"),
 "atividade-homogenea": R("sequência homogênea de atos","[[atividade-omnidimensional]] · [[parada-produtiva]]"),
 "atividade-omnidimensional": R("ação cosmoética prioritária em todas as dimensões","[[atividade-homogenea]] · [[ranque-de-prioridade]]"),
 "autochecagem-indispensavel": R("autochecar antes de qualquer abordagem","[[autoconstatacao]] · [[momento-da-circunspeccao]]"),
 "autoconstatacao": R("constatação direta autexperimentológica","[[autovivencia-experimental]] · [[autochecagem-indispensavel]]"),
 "autodispersividade": R("dispersão dos talentos versáteis","[[momento-da-circunspeccao]] · [[ranque-de-prioridade]]"),
 "autopersuasao-primaria": R("autopersuadir-se ainda inseguro","[[autoconstatacao]] · [[rendicao-a-verpon]]"),
 "autovivencia-experimental": R("experiência que fornece subsídios","[[autoconstatacao]] · [[estatistica-motivadora]]"),
 "binomio-problema-solucao": R("desafio questão↔resposta","[[interacao-consciencia-fato]] · [[primeira-acao]]"),
 "coleta-seletiva": R("recolher informações seletivamente","[[teste-dos-vocabulos]] · [[conscin-fonte]]"),
 "conscin-fonte": R("detentora do conhecimento teático","[[coleta-seletiva]] · [[teste-dos-vocabulos]]"),
 "convite-ao-intermissivista": R("convocação tácita à evolução","[[rendicao-a-verpon]] · [[primeira-acao]]"),
 "duplicidade-de-objetos": R("técnica de 2 objetos afins","[[objeto-ritual]] · [[tecnica-dos-100-procedimentos]]"),
 "estatistica-motivadora": R("registrar dados que motivam","[[autovivencia-experimental]] · [[megarreverificaciologia]]"),
 "interacao-consciencia-fato": R("identificar a incidência do fenômeno","[[binomio-problema-solucao]] · [[autoconstatacao]]"),
 "megarreverificaciologia": R("ciência da megarreverificação","[[autochecagem-indispensavel]] · [[regra-conscienciologica-recursiva]]"),
 "momento-da-circunspeccao": R("ponderação no instante da decisão","[[abordagem-da-antessala]] · [[autodispersividade]]"),
 "objeto-ritual": R("instrumento do ritual/protocolo","[[duplicidade-de-objetos]] · [[tecnica-dos-100-procedimentos]]"),
 "parada-produtiva": R("interromper a atividade para render","[[atividade-homogenea]] · [[trabalho-antelucano]]"),
 "primeira-acao": R("ato inicial prioritário (pensene)","[[primeira-preocupacao]] · [[convite-ao-intermissivista]]"),
 "primeira-preocupacao": R("atenção inicial dirigida (real/imaginário)","[[primeira-acao]] · [[momento-da-circunspeccao]]"),
 "ranque-de-prioridade": R("melhor posição na classificação evolutiva","[[atividade-omnidimensional]] · [[autodispersividade]]"),
 "regra-conscienciologica-recursiva": R("recursividade dos princípios","[[megarreverificaciologia]] · [[sutileza-tecnica]]"),
 "rendicao-a-verpon": R("admitir e aplicar a verpon","[[autopersuasao-primaria]] · [[convite-ao-intermissivista]]"),
 "sutileza-tecnica": R("caráter sutil dos conceitos aplicados","[[regra-conscienciologica-recursiva]] · [[teste-dos-vocabulos]]"),
 "tecnica-dos-100-procedimentos": R("emprego conjunto dos recursos","[[objeto-ritual]] · [[duplicidade-de-objetos]]"),
 "teste-dos-vocabulos": R("uso técnico de verbetes da Enciclopédia","[[coleta-seletiva]] · [[sutileza-tecnica]]"),
 "trabalho-antelucano": R("trabalho produtivo da madrugada","[[parada-produtiva]] · [[atividade-homogenea]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
