# -*- coding: utf-8 -*-
ESP = "Autopesquisologia"
A = "[[autopesquisa]]"
def lo(v,p,t): return ("Léxico de Ortopensatas", t, f"Léxico de Ortopensatas, p. {p}.", f"`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *{v}*, p. {p}.")
def dac(v,p,t): return ("Dicionário de Argumentos da Conscienciologia", t, f"Dicionário de Argumentos da Conscienciologia, verbete *{v}*, p. {p}.", f"`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *{v}*, p. {p}.")
def src(book,file,cap,p,t): return (book, t, f"{book}, {cap}, p. {p}.", f"`corpus/{file}.json` — {book}, {cap}, p. {p}.")

CONV = {
 "autautoridade-vivencial": lo("Memória",1275,"*Memória: autopatrimônio vivencial* — base da autautoridade vivencial."),
 "autoparapercepciologia-ideal": lo("Autoparapercepciologia",252,"A expressão máxima do Ser Humano não é a Ciência Convencional nem a Arte, mas a Autoparapercepciologia, que o coloca vivenciando a Multidimensiologia."),
 "autopesquisa-inarredavel": lo("Autopesquisa",265,"A melhor **autexperiência** é gerada pela autopesquisa; a maior inutilidade da consciência é a falta da autopesquisa."),
 "barreira-teorica": lo("Autorreflexão",286,"*Autorreflexão: autexperimentação teórica* — o 1% da teoria, quando monopolizador, vira barreira teórica."),
 "conceito-tecnico": src("Homo sapiens reurbanisatus","hsr","cap. 142",358,"A expressão *conceito conjugado* é neologismo técnico da Comunicologia; nenhum conceito é 100% virgem."),
 "consciencia-crescente": src("Temas da Conscienciologia","temas","cap. 87",185,"A evolução da consciência se faz pela simplificação *sofisticada*, crescente, das estruturas dos veículos do holossoma."),
 "curiosologia": lo("Curiosologia",567,"Não podemos perder a curiosidade, mas sim qualificá-la por meio das pesquisas técnicas — desde gatos já tínhamos curiosidade."),
 "desafio-da-conscienciologia": src("700 Experimentos da Conscienciologia","700exp","cap. 205",269,"A Conscienciologia desafia as personalidades à lógica, à racionalidade, ao discernimento e ao autoconhecimento direto."),
 "impasse-na-pesquisa": lo("Pesquisa",1551,"Na **pesquisa evolutiva** é permitido, cosmoeticamente, até ciscar, contudo sem bisbilhotar."),
 "interacao-evolutiva": src("700 Experimentos da Conscienciologia","700exp","cap. 666",730,"Quanto maior a interação, em mão dupla, na mutualidade das variáveis, mais o amor perdura na dupla evolutiva (*primener a 2*)."),
 "megateste-conscienciologico": lo("Megateste",1269,"O **megateste** mais difícil da vida humana é manter a personalidade equilibrada continuamente."),
 "personalizacao-da-enciclopedia": src("Homo sapiens reurbanisatus","hsr","cap. 236",609,"Sem o esforço do experimento pessoal — a autopesquisa — a evolução da consciência não acontece; a Enciclopédia é a melhor autoconfrontação."),
 "pesquisa-do-erro": lo("Pretexto",1621,"Quem pesquisa algum **pretexto** para o erro ainda não realiza investigação inteligente."),
 "ponto-cego": src("200 Teáticas da Conscienciologia","200teat","cap. 91",111,"Pela conscienciometria, o guia cego pode ser consciex guia extrafísico cego ou conscin guia intrafísico cego — o ponto cego é o local de menor consistência autevolutiva."),
 "procedimento-extrapauta": dac("Preservaciologia",1267,"Extrapauta interassistencial: o *feedback* de amigo para amigo sobre informação crítica ou privilegiada."),
 "reparo-tecnico": lo("Autorrevisão",297,"Devido à Seriexologia, o reparo que você faz às parêmias do antigo pensador pode ser mera **autorrevisão**."),
 "tecnica-conscienciologica-curiosa": src("200 Teáticas da Conscienciologia","200teat","cap. 69",89,"A empresa intrafísica conscienciológica é a execução técnica da *filosofia cosmoética dos negócios* nas gestações conscienciais."),
}
CONV = {k:v for k,v in CONV.items() if v}

def R(*xs): return [A+" — "+xs[0]] + list(xs[1:])
REL = {
 "atelia": R("ausência de finalidade do ato pensênico","[[impasse-na-pesquisa]] · [[barreira-teorica]]"),
 "autautoridade-vivencial": R("autoridade pela própria vivência","[[autopesquisa-inarredavel]] · [[megateste-conscienciologico]]"),
 "autoparapercepciologia-ideal": R("vivência ideal dos potenciais parapsíquicos","[[autopesquisa-inarredavel]] · [[interacao-evolutiva]]"),
 "autopesquisa-inarredavel": R("autopesquisa com todos os instrumentos","[[autautoridade-vivencial]] · [[personalizacao-da-enciclopedia]] · [[curiosologia]]"),
 "barreira-teorica": R("teoria monopolizadora (1% que trava)","[[atelia]] · [[impasse-na-pesquisa]]"),
 "conceito-tecnico": R("produto da faculdade de investigar","[[reparo-tecnico]] · [[exotismo-conscienciologico]]"),
 "consciencia-crescente": R("evolução natural crescente da conscin","[[interacao-evolutiva]] · [[autopesquisa-inarredavel]]"),
 "corte-da-realidade": R("abordagem de pormenor do Cosmos","[[conceito-tecnico]] · [[zetetica]]"),
 "curiosologia": R("ciência da curiosidade qualificada","[[autopesquisa-inarredavel]] · [[tecnica-conscienciologica-curiosa]]"),
 "desafio-da-conscienciologia": R("condição autossuperadora exigida","[[megateste-conscienciologico]] · [[ponto-cego]]"),
 "exotismo-conscienciologico": R("qualidade exótica da terminologia","[[conceito-tecnico]] · [[corte-da-realidade]]"),
 "impasse-na-pesquisa": R("investigação paralisada (resolução)","[[barreira-teorica]] · [[pesquisa-do-erro]]"),
 "interacao-evolutiva": R("aproximação quase simbiótica evolutiva","[[consciencia-crescente]] · [[autoparapercepciologia-ideal]]"),
 "megateste-conscienciologico": R("aferição da extrafisicalidade palpável","[[desafio-da-conscienciologia]] · [[autautoridade-vivencial]]"),
 "personalizacao-da-enciclopedia": R("tornar pessoal o exemplo da Enciclopédia","[[autopesquisa-inarredavel]] · [[tecnica-conscienciologica-curiosa]]"),
 "pesquisa-do-erro": R("investigar a causa do erro","[[reparo-tecnico]] · [[ponto-cego]]"),
 "ponto-cego": R("local de menor consistência autevolutiva","[[pesquisa-do-erro]] · [[desafio-da-conscienciologia]]"),
 "procedimento-extrapauta": R("agir fora da pauta (feedback crítico)","[[reparo-tecnico]] · [[impasse-na-pesquisa]]"),
 "reparo-tecnico": R("observar/analisar com atenção redobrada","[[pesquisa-do-erro]] · [[procedimento-extrapauta]]"),
 "tecnica-conscienciologica-curiosa": R("processo metódico de amplificação","[[curiosologia]] · [[personalizacao-da-enciclopedia]]"),
 "zetetica": R("metodologia investigativa/indagatória","[[corte-da-realidade]] · [[autopesquisa-inarredavel]]"),
}
for k,v in list(REL.items()):
    REL[k] = [x for x in v if x]
