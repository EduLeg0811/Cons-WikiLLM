# -*- coding: utf-8 -*-
"""Tier Autodiscernimentologia: aplica julgamento (relações + convergência) determinístico."""
import re, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERB = ROOT / "wiki" / "verbetes"
TODAY = "2026-06-27"

# Relações semânticas curadas por slug (o que o match léxico não pega).
REL = {
 "abordagem-maxima": ["[[autodiscernimento]] — a 3ª abordagem como escolha discernidora", "[[postura-conscienciologica]] · [[medida-justa]]"],
 "adorno-consciencial": ["[[autodiscernimento]] — discernir o essencial do penduricalho", "[[antiutilitario]] — adorno sem função evolutiva", "[[miudeza]]"],
 "ajuizamento-pessoal": ["[[autodiscernimento]] — ajuizar com critério da dimensão extrafísica", "[[criteriologia]] · [[analise]]"],
 "amor-doador": ["[[autodiscernimento]] — discernir o amor puro do calculismo", "[[cosmoetica]] · [[interesse]]"],
 "analise": ["[[autodiscernimento]] — análise como instrumento do discernir", "[[criteriologia]] · [[rigor-racionalistico]]", "[[olho-clinico]]"],
 "antagonismo": ["[[autodiscernimento]] — discernir os polos da dualidade", "[[antagonismologia]] — a ciência que o estuda", "[[antagonismo-extremo]] · [[antagonismo-conscienciologico]]"],
 "antagonismo-conscienciologico": ["[[antagonismo]] — caso aplicado à Conscienciologia", "[[antagonismologia]] · [[verpon]]"],
 "antagonismo-extremo": ["[[antagonismo]] — grau máximo da oposição", "[[antagonismologia-patologica]]"],
 "antagonismo-midiatico": ["[[antagonismo]] — antagonismo no campo da mídia", "[[antagonismologia]]"],
 "antagonismologia": ["[[autodiscernimento]] — discernir antagonismos sadios e patológicos", "[[antagonismo]] — objeto de estudo", "[[antagonismologia-sadia]] · [[antagonismologia-patologica]] · [[antagonismologia-ambigua]]"],
 "antagonismologia-ambigua": ["[[antagonismologia]] — variante de antagonismo ambíguo", "[[autodiscernimento]]"],
 "antagonismologia-patologica": ["[[antagonismologia]] — antagonismos doentios", "[[subcerebro-abdominal]] — polo oposto ao paracérebro", "[[antagonismologia-sadia]] — contraponto"],
 "antagonismologia-sadia": ["[[antagonismologia]] — antagonismo homeostático", "[[antagonismologia-patologica]] — contraponto"],
 "antiutilitario": ["[[autodiscernimento]] — discernir o útil do inútil evolutivo", "[[adorno-consciencial]] · [[miudeza]]", "[[priorizacao-da-proexis]]"],
 "atitude-irretocavel": ["[[autodiscernimento]] — postura mais condizente e acabada", "[[detalhe-irretocavel]] — o todo a partir do detalhe", "[[cosmoetica]] · [[postura-conscienciologica]]"],
 "autesforco-convergente": ["[[autodiscernimento]] — convergir esforços com discernimento", "[[priorizacao-da-proexis]] · [[objetivo-prioritario]]"],
 "autoconsciencialidade-ascendente": ["[[autodiscernimento]] — predomínio do discernimento na intraconsciência", "[[autocognicao]] · [[holomaturidade]]"],
 "autodespriorizacao": ["[[autodiscernimento]] — falha do discernir na priorização", "[[autopriorologia]] — contraponto sadio", "[[priorizacao-da-proexis]]"],
 "autodiscernimento-dinamico": ["[[autodiscernimento]] — modalidade dinâmica do atributo", "[[holomaturidade]] · [[evoluciologia]]"],
 "autopriorologia": ["[[autodiscernimento]] — ciência da autopriorização lúcida", "[[autodespriorizacao]] — desvio oposto", "[[objetivo-prioritario]] · [[priorizacao-da-proexis]]"],
 "autorresolucao": ["[[autodiscernimento]] — deliberar com discernimento", "[[medida-justa]] · [[ajuizamento-pessoal]]"],
 "avanco-da-razao": ["[[autodiscernimento]] — racionalização crescente da consciência", "[[racionalidade-completa]] — patamar superior", "[[racionalidade-rudimentar]] — ponto de partida"],
 "consciencia-conscienciologica": ["[[autodiscernimento]] — consciência de autopensenização evoluída", "[[holomaturidade]] · [[paradigma-consciencial]]"],
 "consciencia-desprogramada": ["[[autodiscernimento]] — liberta da programação instintiva", "[[holomaturidade]] · [[evoluciologia]]"],
 "crescendo-helenismo-conscienciologia": ["[[autodiscernimento]] — cotejo evolutivo de paradigmas", "[[estudiosidade]] · [[principiologia]]"],
 "criteriologia": ["[[autodiscernimento]] — determinação de critérios", "[[analise]] · [[ajuizamento-pessoal]]", "[[rigor-racionalistico]]"],
 "critica-benefica": ["[[autodiscernimento]] — julgar sem preconceito", "[[cosmoetica]] · [[analise]]"],
 "detalhe-irretocavel": ["[[autodiscernimento]] — o detalhe que sugere o todo", "[[atitude-irretocavel]] · [[olho-clinico]]"],
 "douta-ignorancia": ["[[autodiscernimento]] — reconhecer os limites do próprio saber", "[[estudiosidade]] · [[inteligencia-evolutiva]]"],
 "dupla-acumulacao": ["[[autodiscernimento]] — acumulação positiva de experiências", "[[holomaturidade]] · [[estudiosidade]]"],
 "escolha-qualimetrica": ["[[autodiscernimento]] — seletividade qualitativa", "[[preferenciologia]] · [[criteriologia]]", "[[medida-justa]]"],
 "estudiosidade": ["[[autodiscernimento]] — dedicação à autopesquisa", "[[autopesquisa]] · [[douta-ignorancia]]"],
 "fatofilia": ["[[autodiscernimento]] — discernir a partir dos fatos", "[[analise]] · [[cosmoetica]]"],
 "instrumento-de-poder": ["[[autodiscernimento]] — discernir o uso cosmoético do recurso", "[[cosmoetica]] · [[megarrecexologia]]"],
 "interesse": ["[[autodiscernimento]] — discernir o interesse prioritário", "[[preferenciologia]] · [[objetivo-prioritario]]"],
 "irrenunciabilidade": ["[[autodiscernimento]] — o inegociável na evolução", "[[cosmoetica]] · [[priorizacao-da-proexis]]"],
 "medida-justa": ["[[autodiscernimento]] — a tomada de posição na proporção certa", "[[autorresolucao]] · [[criteriologia]]"],
 "megaomissao": ["[[autodiscernimento]] — discernir a omissão deficitária", "[[cosmoetica]] · [[priorizacao-da-proexis]]"],
 "megarrecexologia": ["[[autodiscernimento]] — amplitude autopensênica da recéxis máxima", "[[recexis]] · [[amplitude-autopensenica]]"],
 "miudeza": ["[[autodiscernimento]] — discernir o irrelevante", "[[antiutilitario]] · [[adorno-consciencial]]"],
 "neoego": ["[[autodiscernimento]] — o ego renovado pela recéxis", "[[recexis]] · [[holomaturidade]]"],
 "objetivo-prioritario": ["[[autodiscernimento]] — definir a meta máxima", "[[priorizacao-da-proexis]] · [[autopriorologia]]"],
 "olho-clinico": ["[[autodiscernimento]] — atenção lúcida aos detalhes", "[[detalhe-irretocavel]] · [[analise]]"],
 "pertinencia-evolutiva": ["[[autodiscernimento]] — autocognição crítica magna", "[[autocognicao]] · [[holomaturidade]]"],
 "postura-conscienciologica": ["[[autodiscernimento]] — o jeito avançado de ser", "[[atitude-irretocavel]] · [[cosmoetica]]"],
 "preferenciologia": ["[[autodiscernimento]] — gerenciamento cosmoético das preferências", "[[escolha-qualimetrica]] · [[interesse]]", "[[inteligencia-evolutiva]]"],
 "primeira-impressao": ["[[autodiscernimento]] — aferir a impressão imediata", "[[olho-clinico]] · [[autopesquisa]]"],
 "principiologia": ["[[autodiscernimento]] — sistematização dos princípios evolutivos", "[[criteriologia]] · [[cosmoetica]]"],
 "profissao-evitavel": ["[[autodiscernimento]] — discernir a carreira anti-evolutiva", "[[cosmoetica]] · [[priorizacao-da-proexis]]"],
 "pseudobem": ["[[autodiscernimento]] — discernir o falso bem do bem real", "[[cosmoetica]] · [[antagonismo]]"],
 "racionalidade-completa": ["[[autodiscernimento]] — uso teático pleno da razão", "[[racionalidade-rudimentar]] — contraponto", "[[avanco-da-razao]]"],
 "racionalidade-rudimentar": ["[[autodiscernimento]] — racionalidade ainda incipiente", "[[racionalidade-completa]] — patamar a alcançar", "[[avanco-da-razao]]"],
 "realidade-inexcluivel": ["[[autodiscernimento]] — discernir o impositivo na evolução", "[[fatofilia]] · [[realidade-unica]]"],
 "realidade-unica": ["[[autodiscernimento]] — vivência da realidade integral", "[[realidade-inexcluivel]] · [[holodiscernimento]]"],
 "refem-da-autocognicao": ["[[autodiscernimento]] — sujeição lúcida às injunções do saber", "[[autocognicao]] · [[priorizacao-da-proexis]]"],
 "visao": ["[[autodiscernimento]] — a percepção visual a serviço do discernir", "[[olho-clinico]] · [[primeira-impressao]]"],
 "rigor-racionalistico": ["[[autodiscernimento]] — exatidão e profundidade no discernir", "[[racionalidade-completa]] · [[criteriologia]]", "[[analise]]"],
 "whole-pack-conscienciologico": ["[[autodiscernimento]] — aceitar o paradigma na íntegra", "[[principiologia]] · [[cosmoetica]]"],
 "consciencia-conscienciologica2": [],
}

# Convergência: slug -> (titulo_fonte, texto, citacao_inline, linha_fontes)
CONV = {
 "adorno-consciencial": ("Léxico de Ortopensatas", "*Adorno: penduricalho extra.* Nem todo **adorno** embeleza.", "Léxico de Ortopensatas, p. 62.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Adorno*, p. 62."),
 "ajuizamento-pessoal": ("Léxico de Ortopensatas", "A melhor tendência evolutiva é ajuizar esta dimensão humana com o critério da dimensão extrafísica avançada.", "Léxico de Ortopensatas, p. 75.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Ajuizamento*, p. 75."),
 "amor-doador": ("700 Experimentos da Conscienciologia", "A intervenção do doador, no máximo do prazer físico, com a intenção fixa de cooperar na melhoria ou na autocura da pessoa amada, está entre as maiores provas de amor puro possível a alguém.", "700 Experimentos da Conscienciologia, cap. 274, p. 338.", "`corpus/700exp.json` — 700 Experimentos da Conscienciologia, cap. 274, p. 338."),
 "antagonismo": ("Homo sapiens pacificus", "Há 23 antagonismos — variáveis da Conscienciologia — incluídos entre os 100 grupos nosográficos (ação-inação, amor-ódio etc.).", "Homo sapiens pacificus, cap. 226, p. 642.", "`corpus/hsp.json` — Homo sapiens pacificus, cap. 226, p. 642."),
 "antagonismo-midiatico": ("Homo sapiens pacificus", "O antagonismo midiático bélico ficou evidente, durante a guerra do Afeganistão, entre a CNN estadunidense e a Al-Jazeera do Catar.", "Homo sapiens pacificus, cap. 199, p. 535.", "`corpus/hsp.json` — Homo sapiens pacificus, cap. 199, p. 535."),
 "antagonismologia-patologica": ("Dicionário de Argumentos da Conscienciologia", "As condições frontalmente antagônicas às manifestações do paracérebro são as adstritas ao subcérebro abdominal, predisponentes das lavagens subcerebrais da robéxis na Socin Patológica.", "Dicionário de Argumentos da Conscienciologia, verbete *Autoparacerebrologia*, p. 374.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Autoparacerebrologia*, p. 374."),
 "autesforco-convergente": ("Léxico de Ortopensatas", "O **autesforço** é tudo. *Com nada, ninguém faz nada.* A conscin inteligente troca a *sorte* pelo **autesforço evolutivo.**", "Léxico de Ortopensatas, p. 185.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Autesforço*, p. 185."),
 "autodespriorizacao": ("Léxico de Ortopensatas", "A partir dos fatos, conclui-se racionalmente que todo **suicídio** é devido à autodespriorização evolutiva.", "Léxico de Ortopensatas, p. 222.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Autodespriorização*, p. 222."),
 "autodiscernimento-dinamico": ("Homo sapiens reurbanisatus", "Há recesso ressomático evolutivo, dinâmico, próprio da consciex (p. ex. dos cursos intermissivos das maxiduplas), quanto à condição do autodiscernimento evolutivo ou cosmoético.", "Homo sapiens reurbanisatus, cap. 64, p. 197.", "`corpus/hsr.json` — Homo sapiens reurbanisatus, cap. 64, p. 197."),
 "autorresolucao": ("Léxico de Ortopensatas", "Ser inteligente é saber mudar de imediato a **autorresolução** menos digna.", "Léxico de Ortopensatas, p. 291.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Autorresolução*, p. 291."),
 "criteriologia": ("Dicionário de Argumentos da Conscienciologia", "Há 11 critérios aplicáveis na escolha dos temas das redações da megagescon escrita do intermissivista.", "Dicionário de Argumentos da Conscienciologia, verbete *Criteriologia*, p. 550.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Criteriologia*, p. 550."),
 "detalhe-irretocavel": ("Léxico de Ortopensatas", "*O detalhe sugere. O todo denuncia.* Nem todo **detalhe** é fragmento.", "Léxico de Ortopensatas, p. 630.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Detalhe*, p. 630."),
 "douta-ignorancia": ("Léxico de Ortopensatas", "A **douta ignorância** é própria do *scholar* que desconhece a *Inteligência Evolutiva* (IE).", "Léxico de Ortopensatas, p. 1003.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Ignorância*, p. 1003."),
 "fatofilia": ("Dicionário de Argumentos da Conscienciologia", "A *fatofilia* é a base do *Conscienciograma*, do *Código Grupal de Cosmoética* (CGC); sem análise dos fatos a assertiva não aparece e erra-se mais.", "Dicionário de Argumentos da Conscienciologia, verbete *Abstraciologia*, p. 69.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Abstraciologia*, p. 69."),
 "megarrecexologia": ("Dicionário de Argumentos da Conscienciologia", "Com o desenvolvimento das autopotencialidades, a conscin deixa o *mundinho pessoal* para vivenciar a *amplitude autopensênica*, ainda conduta-exceção.", "Dicionário de Argumentos da Conscienciologia, verbete *Autopotencializaciologia*, p. 404.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Autopotencializaciologia*, p. 404."),
 "objetivo-prioritario": ("Manual da Dupla Evolutiva", "A otimização da projetabilidade lúcida pode ser objetivo prioritário da dupla evolutiva, para cada parceiro acessar conhecimentos transcendentes libertários.", "Manual da Dupla Evolutiva, cap. 34, p. 128.", "`corpus/dupla.json` — Manual da Dupla Evolutiva, cap. 34, p. 128."),
 "olho-clinico": ("Dicionário de Argumentos da Conscienciologia", "O diagnóstico visual da subinteligência humana pode ser realizado por pessoa observadora desde o primeiro encontro, de modo objetivo e concreto.", "Dicionário de Argumentos da Conscienciologia, verbete *Subinteligenciologia*, p. 1367.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Subinteligenciologia*, p. 1367."),
 "pertinencia-evolutiva": ("Léxico de Ortopensatas", "A densidade e a intensidade evolutivas da consciência dependem da pertinência, ou seja, da **autocognição crítica magna.**", "Léxico de Ortopensatas, p. 1548.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Pertinência*, p. 1548."),
 "preferenciologia": ("Dicionário de Argumentos da Conscienciologia", "A *Inteligência Evolutiva* (IE) destaca o ato de viver com o gerenciamento cosmoético das autopreferências, predileções e escolhas na holomaturidade.", "Dicionário de Argumentos da Conscienciologia, verbete *Acepciologia*, p. 77.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Acepciologia*, p. 77."),
 "primeira-impressao": ("Léxico de Ortopensatas", "A **primeira impressão**, em muitas ocasiões, pode ser a mais correta; contudo, importa ater-se aos detalhes das ocorrências e paraocorrências para confirmar.", "Léxico de Ortopensatas, p. 266.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Autopesquisa*, p. 266."),
 "principiologia": ("Dicionário de Argumentos da Conscienciologia", "35. Principiologia: 7 categorias de *princípios conscienciais fundamentais.*", "Dicionário de Argumentos da Conscienciologia, verbete *Heptetologia*, p. 730.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Heptetologia*, p. 730."),
 "pseudobem": ("Léxico de Ortopensatas", "O **falso bem** é um mal verdadeiro.", "Léxico de Ortopensatas, p. 1663.", "`corpus/lo.json` — [[lexico-de-ortopensatas|Léxico de Ortopensatas]], verbete *Pseudobem*, p. 1663."),
 "refem-da-autocognicao": ("Dicionário de Argumentos da Conscienciologia", "Na preservação intelectiva, o assistente interconsciencial torna-se, ao menos temporariamente, refém da autocognição, porém lúcido quanto à priorização evolutiva e ao *timing* exato.", "Dicionário de Argumentos da Conscienciologia, verbete *Preservaciologia*, p. 1268.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Preservaciologia*, p. 1268."),
 "rigor-racionalistico": ("Dicionário de Argumentos da Conscienciologia", "A conscin autora anticonflituosa evidencia, na Estilística Gráfica, alto critério de regularidade e uniformidade sistemática, com rigor racionalístico.", "Dicionário de Argumentos da Conscienciologia, verbete *Autoradologia*, p. 419.", "`corpus/dac.json` — [[dicionario-de-argumentos-da-conscienciologia|DAC]], verbete *Autoradologia*, p. 419."),
 "visao": ("Projeciologia", "A visão extrafísica apresenta ao menos 23 características e tipos (monocular, estereoscópica, uniforme, instável etc.).", "Projeciologia, cap. 278, p. 565.", "`corpus/proj.json` — Projeciologia, cap. 278, p. 565."),
}

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    return m.group(1), m.group(2)

def set_fm(fm, key, val):
    return re.sub(rf"(?m)^{key}:.*$", f"{key}: {val}", fm)

def replace_section(body, header, new_content):
    # substitui o conteúdo de '## header' até a próxima '## ' (ou fim)
    pat = re.compile(rf"(?ms)^## {re.escape(header)}\n.*?(?=^## |\Z)")
    repl = f"## {header}\n{new_content}\n\n"
    if pat.search(body):
        return pat.sub(repl, body, count=1)
    return body

def insert_after(body, after_header, block):
    pat = re.compile(rf"(?ms)^(## {re.escape(after_header)}\n.*?)(?=^## |\Z)")
    def f(m):
        return m.group(1).rstrip() + "\n\n" + block + "\n\n"
    return pat.sub(f, body, count=1)

changed = 0
conv_n = 0
for slug, rels in REL.items():
    if slug.endswith("2"):
        continue
    p = VERB / f"{slug}.md"
    if not p.exists():
        print("FALTA", slug); continue
    txt = p.read_text(encoding="utf-8")
    fm, body = split_front(txt)
    if "tier Autodiscernimentologia" in body:
        continue  # idempotente
    # relações
    rel_block = "\n".join(f"- {r}" for r in rels) if rels else "- [[autodiscernimento]]"
    body = replace_section(body, "Conexões internas", rel_block)
    # convergência
    has_conv = slug in CONV
    if has_conv:
        titulo, texto, cit, fonte_line = CONV[slug]
        conv_block = f"## Convergência: {titulo}\n\"{texto}\" — {cit}"
        # insere após Definologia
        body = insert_after(body, "Definologia", conv_block)
        # adiciona linha de fonte
        body = re.sub(r"(?ms)^(## Fontes ingeridas\n)", r"\1- " + fonte_line.replace("\\", "\\\\") + "\n", body, count=1)
        conv_n += 1
    # frontmatter
    fm = set_fm(fm, "status", "revisado")
    fm = set_fm(fm, "ultima_atualizacao", TODAY)
    if has_conv:
        fm = set_fm(fm, "confianca", "media")
        fm = set_fm(fm, "fontes_count", "2")
    # log
    note = "relações semânticas" + ("; convergência 2ª fonte; baixa→média" if has_conv else "")
    logline = f"- {TODAY}: enriquecido (tier Autodiscernimentologia): {note}; stub→revisado."
    body = re.sub(r"(?ms)^(## Log de revisões\n)", r"\1" + logline + "\n", body, count=1)
    p.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")
    changed += 1

print(f"alterados={changed} convergencias={conv_n}")
