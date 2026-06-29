# -*- coding: utf-8 -*-
ESP = "Autoconscienciometrologia"
A = "[[conscienciometria]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "autorrecuperacao-dos-megacons": lo("Retrocognição",1749,"A **autorrecuperação de megacons** é ato genuinamente retrocognitivo."),
 "autorreflexao-de-5-horas": lo("Autorreflexão",287,"A *técnica das autorreflexões de 5 horas* é **profilaxia** eficaz ante o cometimento habitual de erros, enganos e omissões deficitárias."),
 "autossaturacao-intraconsciencial": dac("Diversificaciologia",595,"Não devemos nos render à autossaturação com facilidade; enquanto submissa ao enjoo fácil, a pessoa demora a evoluir."),
 "autoteste-da-evolucao-cronologica": lo("Autoteste",305,"Se você ainda admite a união dos sexos como o megaprazer da vida humana, nada sabe da autotransafetividade nem esteve em Comunex Evoluída."),
 "autotortura": lo("Autotortura",305,"Todo **estado depressivo** começa por alguma autotortura da consciência."),
 "cacoete-holobiografico": src("Homo sapiens pacificus","hsp","cap. 181",497,"*Há endotrafares multiexistenciais. Trafar: cacoete consciencial.*"),
 "compensacao-intraconsciencial": src("200 Teáticas da Conscienciologia","200teat","cap. 36",56,"Pela experimentologia, existem múltiplos atributos compensatórios dentro da teática da compensação intraconsciencial."),
 "conscin-displicente": src("Homo sapiens pacificus","hsp","cap. 334",889,"A conscin incapaz de criar o boato, mas que ajuda a circular calúnias diariamente (*fofin*), compõe condição da conscin displicente."),
 "dominio-pessoal": lo("Paixões",1430,"O **domínio** das paixões do Ser Humano é iniciativa inteiramente pessoal, sem apelações de quaisquer naturezas."),
 "economia-da-vida-consciencial": src("700 Experimentos da Conscienciologia","700exp","cap. 569",633,"Desponta a *lei de economia de bens* que vigora em múltiplos setores da vida consciencial."),
 "especialismo-holobiografico": lo("Especialismo",766,"O especialista tende a se apaixonar pelo objeto dos seus estudos, levando-o à estagnação pesquisística redutora do ponto de vista panorâmico e prioritário."),
 "prova-do-orgulho": lo("Orgulho",1409,"O **orgulho** é o inchaço do ego; irmão gêmeo do egoísmo, gera a tendência à supremacia."),
 "saude-fisica": lo("Saúde",1795,"Para manter a saúde física e mental é necessário o período de **sono** prolongado e ao menos uma refeição quente por dia."),
 "saude-mental": src("700 Experimentos da Conscienciologia","700exp","cap. 236",300,"Para alguns existe a *Indústria da Saúde*; para a maioria, existe tão só a *Indústria da Doença* — base da reflexão sobre saúde mental."),
 "saude-intelectual": src("700 Experimentos da Conscienciologia","700exp","cap. 654",718,"Nossa consciência faz e mantém a saúde, a disposição física e intelectual, e o aproveitamento da oportunidade e do tempo humano."),
 "saude-emocional": lo("Saúde",1795,"*Saúde: processo evolutivo. Educação é saúde.*"),
 "saude-parapsiquica": lo("Ouvidos",1421,"Os **fones de ouvido** alteram a sensibilidade parapsíquica e podem influir na saúde da mente."),
 "segunda-vocacao": lo("Vocação",2031,"Você é a sua **vocação** — a segunda vocação é a disposição da pessoa versátil para uma atividade adicional."),
 "autodesrespeito": src("Homo sapiens pacificus","hsp","cap. 18",591,"O autodesrespeito associa-se à autoinsegurança, à desproteção na vida e ao estranhamento de si."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
T="[[trafor-trafar]]"
REL = {
 "autodesrespeito": R("desrespeito da consciência a si mesma","[[autotortura]] · [[prova-do-orgulho]]"),
 "autojustificativa": R("álibi para comprovar a própria intenção","[[autodesrespeito]] · [[cacoete-holobiografico]]"),
 "autorrecuperacao-dos-megacons": R("reacessar os megacons (retrocognição)","[[autoteste-da-evolucao-cronologica]] · [[especialismo-holobiografico]]"),
 "autorreflexao-de-5-horas": R("técnica profilática de autorreflexão","[[compensacao-intraconsciencial]] · [[dominio-pessoal]]"),
 "autossaturacao-intraconsciencial": R("esgotamento íntimo por enjoo","[[conscin-displicente]] · [[autotortura]]"),
 "autoteste-da-evolucao-cronologica": R("autoteste do progresso evolutivo no tempo","[[autorrecuperacao-dos-megacons]] · [[economia-da-vida-consciencial]]"),
 "autotortura": R("torturar-se voluntariamente (depressão)","[[autodesrespeito]] · [[autossaturacao-intraconsciencial]]"),
 "cacoete-holobiografico": R("mau hábito multiexistencial (trafar)","[[autojustificativa]] · "+T),
 "compensacao-intraconsciencial": R("compensar com atributo maior","[[dominio-pessoal]] · [[autorreflexao-de-5-horas]]"),
 "conscin-displicente": R("apática, descontente, fofoqueira","[[autossaturacao-intraconsciencial]] · [[autodesrespeito]]"),
 "dominio-pessoal": R("governo das próprias ações/paixões","[[compensacao-intraconsciencial]] · [[autorreflexao-de-5-horas]]"),
 "economia-da-vida-consciencial": R("gerenciar a existência (lei de economia de bens)","[[dominio-pessoal]] · [[autoteste-da-evolucao-cronologica]]"),
 "especialismo-holobiografico": R("especialidade multiexistencial da consciência","[[segunda-vocacao]] · [[autorrecuperacao-dos-megacons]]"),
 "interacao-psicossomatica": R("trafar causal × contexto psicossomático","[[interacao-psicossomatica]]" if False else "[[saude-emocional]] · "+T),
 "prova-do-orgulho": R("exame que demonstra o orgulho","[[autodesrespeito]] · [[cacoete-holobiografico]]"),
 "saude-emocional": R("equilíbrio dinâmico das emoções","[[saude-mental]] · [[interacao-psicossomatica]]"),
 "saude-fisica": R("equilíbrio do organismo biológico","[[saude-mental]] · [[saude-intelectual]]"),
 "saude-intelectual": R("equilíbrio do organismo intelectual","[[saude-mental]] · [[saude-fisica]]"),
 "saude-mental": R("equilíbrio do organismo mental","[[saude-emocional]] · [[saude-fisica]] · [[saude-parapsiquica]]"),
 "saude-parapsiquica": R("equilíbrio do organismo parapsíquico","[[saude-mental]] · [[autorrecuperacao-dos-megacons]]"),
 "segunda-vocacao": R("vocação adicional da pessoa versátil","[[especialismo-holobiografico]] · [[economia-da-vida-consciencial]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
