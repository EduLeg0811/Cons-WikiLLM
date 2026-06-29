# -*- coding: utf-8 -*-
ESP = "Cosmovisiologia"
A = "[[cosmovisiologia]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "autopensenizacao-cosmovisiologica": lo("Autopensenização",264,"A autopensenização é o ato que alcança o maior nível da **liberdade** consciencial."),
 "autovisao-coletiva": lo("Autovisão",311,"A pessoa pessimista vê as sombras do próximo; a **pessoa otimista** vê as luzes do próximo — a cosmovisão amplia a autovisão detalhista."),
 "central-extrafisica-da-fraternidade": dac("Interaciologia",811,"Há interações essenciais à evolução consciencial merecedoras de atenção em função das sincronicidades — campo da Central Extrafísica da Fraternidade."),
 "central-extrafisica-da-verdade": lo("Parapsicotecas",1481,"A *Central Extrafísica da Verdade* (CEV) é uma miniparapsicoteca, ou paraconcha cognitiva, voltada para o *passado, já presente*, das consciências."),
 "conciliacao-das-interdependencias": lo("Conciliação",467,"A **conciliação** é sempre mais inteligente do que o *litígio.*"),
 "conexao-acumulada": lo("Conexão",470,"A **conexão interconsciencial** mais profunda e duradoura é de paracérebro a paracérebro."),
 "cosmovisao-humana": lo("Cosmovisão",539,"*Cosmovisão constitui autossobrepairamento.* Ter cosmovisão depende do eustresse."),
 "curiosidade-pesquisistica": lo("Curiosidade",567,"Quanto mais evoluída a consciência, mais se dedica à **curiosidade pesquisística.**"),
 "dinamica-das-complexidades": src("Homo sapiens reurbanisatus","hsr","cap. 200",489,"Ensinar é descomplicar as complexidades *primárias* para as consciências suportarem as complexidades *evoluídas*."),
 "enciclopediologia": lo("Enciclopediologia",716,"A *Enciclopédia da Conscienciologia* é **megarrevezamento grupal**, repositório amplo de conceitos sobre a evolução da consciência nesta dimenin."),
 "generalizacao": lo("Ociosidade",1380,"Ninguém nasceu para permanecer de braços cruzados — esta é uma generalização inevitável."),
 "leitura-correta": lo("Leitura",1155,"*Leitura: maratona mentalsomática. Leitura é evocação.*"),
 "magnificacao-mentalsomatica": lo("Mentalsomática",1285,"A **riqueza maior** é a de natureza mentalsomática ou do autodiscernimento."),
 "mundividencia": lo("Mundividência",1333,"Não há como chegar à **mundividência máxima** sem a natureza galáctica do paracérebro da *Consciex Livre* (CL)."),
 "mundividencia-traforista": src("700 Experimentos da Conscienciologia","700exp","cap. 384",448,"No Teste da Consciência Traforista, verifica-se se os traços e tendências predominam na coluna dos trafores ou dos trafares."),
 "pre-cosmovisao": lo("Cosmovisão",540,"Os amparadores de função têm, simultaneamente, a retrocognição, a simulcognição e a precognição a nosso respeito."),
 "abordagem-macro-micro": src("Homo sapiens reurbanisatus","hsr","cap. 74",221,"O parapsiquismo torna a multidimensionalidade vivida acessível ao sensitivo, da microminoria lúcida ao macro — base da abordagem macro-micro."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
M="[[mundividencia]]"; C="[[cosmovisao-humana]]"
REL = {
 "abordagem-macro-micro": R("enfoque do conhecimento do macro ao micro","[[dinamica-das-complexidades]] · "+C),
 "autopensenizacao-cosmovisiologica": R("pensenizar fixado em objetivos grandiosos","[[autovisao-coletiva]] · [[magnificacao-mentalsomatica]]"),
 "autovisao-coletiva": R("autovisão ampliada ao coletivo","[[cosmovisao-humana]] · [[autopensenizacao-cosmovisiologica]]"),
 "central-extrafisica-da-fraternidade": R("comunex da fraternidade","[[central-extrafisica-da-verdade]] · [[conciliacao-das-interdependencias]]"),
 "central-extrafisica-da-verdade": R("paraconcha cognitiva da verdade","[[central-extrafisica-da-fraternidade]] · [[enciclopediologia]]"),
 "conciliacao-das-interdependencias": R("acordos das interdependências","[[conexao-acumulada]] · [[central-extrafisica-da-fraternidade]]"),
 "conexao-acumulada": R("vínculo de paracérebro a paracérebro acumulado","[[conciliacao-das-interdependencias]] · "+M),
 "cosmovisao-humana": R("enxergar além do banal (autossobrepairamento)","[[pre-cosmovisao]] · [[mundividencia]] · [[cosmovisiologo]]"),
 "cosmovisiologo": R("conscin de mundividência cosmovisiológica","[[mundividencia]] · [[mundividencia-traforista]] · [[cosmovisao-humana]]"),
 "curiosidade-pesquisistica": R("investigação técnica da consciência evoluída","[[pluriprospectividade]] · [[leitura-correta]]"),
 "dinamica-das-complexidades": R("análises extensivas + sínteses intensivas","[[abordagem-macro-micro]] · [[magnificacao-mentalsomatica]]"),
 "enciclopediologia": R("ciência da construção de enciclopédia","[[central-extrafisica-da-verdade]] · [[leitura-correta]]"),
 "generalizacao": R("difundir/vulgarizar uma ideia","[[abordagem-macro-micro]] · [[leitura-correta]]"),
 "holofisiologia": R("ciência da fisiologia integral do holossoma","[[magnificacao-mentalsomatica]] · "+C),
 "leitura-correta": R("apreensão exata da realidade (evocação)","[[enciclopediologia]] · [[curiosidade-pesquisistica]]"),
 "magnificacao-mentalsomatica": R("levar às últimas consequências (Holofilosofia)","[[dinamica-das-complexidades]] · [[mundividencia]]"),
 "mundividencia": R("megaconcepção do mundo/Universo","[[mundividencia-traforista]] · [[cosmovisao-humana]] · [[pre-cosmovisao]]"),
 "mundividencia-traforista": R("mundividência centrada nos trafores","[[mundividencia]] · [[cosmovisiologo]]"),
 "pluriprospectividade": R("autopesquisas diferenciadas e prospectivas","[[curiosidade-pesquisistica]] · [[pre-cosmovisao]]"),
 "pre-cosmovisao": R("avaliar com acurácia antes da cosmovisão","[[cosmovisao-humana]] · [[pluriprospectividade]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
