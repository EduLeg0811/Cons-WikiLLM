# -*- coding: utf-8 -*-
ESP = "Somatologia"
A = "[[soma]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "amimia": src("Homo sapiens pacificus","hsp","cap. 373",960,"A paz íntima do *Homo sapiens serenissimus* pode se apresentar como amimia (ausência de mímica), em estado natural, sadio, não-patológico."),
 "antissomatica": lo("Antissomática",122,"*Antissomática: semissuicídio inconsciente* — ex.: o uso mórbido de anabolizantes para inflar os músculos."),
 "antropolatria": src("700 Experimentos da Conscienciologia","700exp","cap. 72",136,"A *antropolatria* — o culto do Homem — está entre as reflexões sobre lucidez versus religiosidade na Holossomatologia."),
 "arbitrariedade-somatica": lo("Somática",1856,"Com a **idade somática**, tudo piora, exceção apenas para a maturidade consciencial."),
 "autografia-cutanea": lo("Tatuagem",1897,"**Tatuagem:** autografia cutânea primitiva e desnecessária; a melhor autografia é a própria existência da conscin."),
 "comando-exterior": lo("Comando",437,"A conscin assistente lúcida, como minipeça do Maximecanismo, é comandada absolutamente pelos amparadores extrafísicos de função (Teleguiamentologia)."),
 "envelhecimento": lo("Envelhecimento",729,"*O envelhecimento compensa.* Ao pessimista é *perecimento*; ao otimista, **enriquecimento.**"),
 "falencia-parcial-dos-orgaos": lo("Falências",846,"A conscin que deixa de crescer evolutivamente sofre a falência geral dos **paraórgãos** antes da falência dos órgãos do corpo humano."),
 "inteligencia-longeva": lo("Longevidade",1188,"Quanto mais longeva a conscin intermissivista, mais preza as **consciexes evoluídas.**"),
 "macrossomatologia": lo("Macrossomatologia",1205,"O macrossoma atua contra as **ficções intrafísicas**; em tese, o macrossoma ginossomático é superior, nos potenciais, ao androssomático."),
 "perda-de-peso-corporal": src("Projeciologia","proj","cap. 217",459,"Quem jejua, em sua maioria, perde entre ½ e 1½ quilo de peso corporal nas primeiras 24 horas."),
 "superdotacao-somatica": lo("Superdotação",1874,"A condição da **superdotação** mais séria e útil é a parapsíquica; a afeição da maternagem ajuda a promover a eclosão da superdotação na criança."),
 "recepcao-somatica": lo("Recepção",1700,"Se a *Comunex Evoluída* recebe poucas consciexes, em compensação nunca expulsa ninguém."),
 "instrumento-pro-saude": lo("Instrumento",1067,"A **ortopensenidade** pessoal é o maior instrumento condutor da consciência."),
 "incompatibilidade-intersomatica": lo("Alergia",78,"*Alergia: incompatibilidade bioquímica* — análoga à incompatibilidade intersomática."),
 "pescoco": src("Temas da Conscienciologia","temas","cap. 24",59,"O pescoço abriga o laringochacra; há 10 ações interpessoais primitivas que se relacionam diretamente com ele."),
 "folclore-somatico": src("Projeciologia","proj","cap. 19",90,"Há folclores: a Alquimia ficou como folclore da Química; a Astrologia, da Astronomia — análogos ao folclore somático sobre o próprio corpo."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "amimia": R("ausência de mímica/gestos (sadia ou patológica)","[[arbitrariedade-somatica]] · [[antissomatica]]"),
 "antissomatica": R("hábito doentio contra o soma (semissuicídio)","[[arbitrariedade-somatica]] · [[folclore-somatico]]"),
 "antropolatria": R("culto a um ser humano (superstar/guru)","[[folclore-somatico]] · [[recepcao-somatica]]"),
 "arbitrariedade-somatica": R("predomínio do soma sobre a consciência","[[antissomatica]] · [[comando-exterior]] · [[envelhecimento]]"),
 "autografia-cutanea": R("manuscrever no próprio corpo","[[folclore-somatico]] · [[antissomatica]]"),
 "autopesagem": R("pesar o próprio corpo humano","[[perda-de-peso-corporal]] · [[arbitrariedade-somatica]]"),
 "comando-exterior": R("comandar as automanifestações pelo soma","[[arbitrariedade-somatica]] · [[recepcao-somatica]]"),
 "conscin-polissemica": R("conscin de múltiplos sentidos somáticos","[[recepcao-somatica]] · [[superdotacao-somatica]]"),
 "envelhecimento": R("avançar na idade física","[[inteligencia-longeva]] · [[falencia-parcial-dos-orgaos]]"),
 "falencia-parcial-dos-orgaos": R("desgaste paulatino dos órgãos","[[envelhecimento]] · [[incompatibilidade-intersomatica]]"),
 "folclore-somatico": R("fantasias sobre o próprio corpo","[[antropolatria]] · [[autografia-cutanea]]"),
 "incompatibilidade-intersomatica": R("discordância entre somas","[[falencia-parcial-dos-orgaos]] · [[recepcao-somatica]]"),
 "instrumento-pro-saude": R("dispositivo a favor da saúde","[[macrossomatologia]] · [[tecnica-da-sesta]]"),
 "inteligencia-longeva": R("hiperacuidade mantida na longevidade","[[envelhecimento]] · [[macrossomatologia]]"),
 "macrossomatologia": R("ciência do macrossoma (soma fora-de-série)","[[superdotacao-somatica]] · [[instrumento-pro-saude]]"),
 "perda-de-peso-corporal": R("diminuir o volume do soma","[[autopesagem]] · [[tecnica-da-sesta]]"),
 "pescoco": R("região do tronco à cabeça (laringochacra)","[[recepcao-somatica]] · [[comando-exterior]]"),
 "recepcao-somatica": R("o soma receber/acolher estímulos","[[comando-exterior]] · [[conscin-polissemica]]"),
 "superdotacao-somatica": R("corpo de potenciais superiores","[[macrossomatologia]] · [[inteligencia-longeva]]"),
 "tecnica-da-sesta": R("soneca pós-prandial restauradora","[[instrumento-pro-saude]] · [[perda-de-peso-corporal]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
