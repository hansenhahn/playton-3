#!/usr/bin/env python3
"""Harness de QA para os enigmas (nazo) do layton-qa.

Uso:
    python3 .opencode/scripts/qa_nazo.py --df 0 [--root .] [--report qa_nazo_df0.json] [--md qa_nazo_df0.md]
    python3 .opencode/scripts/qa_nazo.py --df 0 --exhaustive   # dump EN<->PT de TODOS os blocos + qa_nazo_df0.audit.md
    python3 .opencode/scripts/qa_nazo.py --all
    python3 .opencode/scripts/qa_nazo.py --verify-font   # audita CWDH/CMAP

Compara `Textos Originais/rc/nazo/uk/naz_dfN` (EN, verdade) com
`Textos Traduzidos/rc/nazo/uk/naz_dfN` (PT-BR). Nao traduz nem edita: apenas
detecta. A skill layton-qa manda no rewrite cirurgico; este script mecaniza os
cheques deterministicos e gera sidecar de flagrados para o julgamento
semantico (LLM/manual).

Estrutura de um enigma (224/224 arquivos):
    [ea0b...]  metadado (numero, tipo de resposta, recompensa) + marcadores
    [eb0b...]  pergunta        (question)
    [ec0b...]  feedback certo   (correct)
    [ed0b...]  feedback errado  (wrong)
    [ee0b...]  dica 1           (hint1)
    [ef0b...]  dica 2           (hint2)
    [f00b...]  dica 3           (hint3)
    [f10b...]  super dica       (super)
As linhas `[...]` (header/ponteiro) sao identicas EN<->PT e nao devem mudar.

Fonte: `fontq.nftr` (Screen03 Enigmas / Screen08 Dicas, `ScreenXPos 13/20`).

Largura: `decode_font` le CWDH/CMAP do proprio `.nftr` e soma o **3o byte do
CWDH** (`adv`/coluna `Total`), com CMAP em `+16`. Isso foi conferido contra a
tabela de `Spec/Fontes_NFTR.md` (`--verify-font`: 147/147 glifos em fontq e
fontevent). `L+W+R` NAO e o avanco.
"""
import argparse
import collections
import json
import os
import re
import struct
import sys

# fontq: area util ~230px (256 - XPos 13 - margem). EN nao passa de 222px.
HARD_PX = 230
SAFE_PX = 210

# Capacidade real da caixa, derivada da geometria dos fundos + Configs:
#   Screen03 Puzzle.png: painel y~20..189, texto em YPos=22, NewLine=12
#     -> (189-22+1)/12 ~= 14 linhas (pergunta/acerto/erro).
#   Screen08 Hints.png: painel y~30..188, texto em YPos=42, NewLine=12
#     -> (188-42+1)/12 ~= 12 linhas (dicas/super dica).
# Os Originais respeitam exatamente esse teto (EN: max 14 e 12). PT acima do
# teto = WARN; PT > EN mas <= teto = INFO.
HARD_LINES = {
    "meta": 0, "question": 14, "correct": 14, "wrong": 14,
    "hint1": 12, "hint2": 12, "hint3": 12, "super": 12,
}

WARN_POLICY = (
    "FAIL = erro bloqueante (estrutura/token funcional/tag/glossario/encoding/"
    "largura hard/dia-cor). WARN = aviso tecnico/estilistico (largura > safe, "
    "linhas acima do original, numeros) que NAO bloqueia o gate. INFO = "
    "heuristica para revisao manual. Gate/exit code considera apenas FAIL."
)

ROLE = {
    "ea": "meta", "eb": "question", "ec": "correct", "ed": "wrong",
    "ee": "hint1", "ef": "hint2", "f0": "hint3", "f1": "super",
}
ROLE_PT = {
    "meta": "metadado", "question": "pergunta", "correct": "acerto",
    "wrong": "erro", "hint1": "dica1", "hint2": "dica2", "hint3": "dica3",
    "super": "super dica",
}

TAG_RE = re.compile(r"<[^>]+>")
BRACKET_RE = re.compile(r"^\[([0-9a-fA-F]{2})0b")
MARKER_RE = re.compile(r"^n\d+[a-z]?$")
TOKEN_RE = re.compile(r"\{[^}]*\}")
HYPHEN_RE = re.compile(r"[A-Za-zÀ-ÿ]-\s*\n\s*[A-Za-zÀ-ÿ]")

EN_RESIDUAL = re.compile(
    r"\bpuzzle\b|\bhint coin\b|\bInspector\b|\bConstable\b|\bGranny\b", re.I
)
PT_WRONG = re.compile(
    r"quebra-cabeça|quebra-cabeca|moeda de pista|Índice de Enigmas|Indice de Enigmas"
    r"|Inspector|Constable|Granny",
    re.I,
)
NUM_RE = re.compile(r"\d+")
WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+")
# Numeros escritos por extenso (EN e PT) -> valor, para nao acusar `70` vs
# `setenta`. Multidigitos continuam por digito literal.
NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
    "dois": 2, "duas": 2, "três": 3, "tres": 3, "quatro": 4,
    "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
    "onze": 11, "doze": 12, "treze": 13, "catorze": 14, "quatorze": 14,
    "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18,
    "dezenove": 19, "vinte": 20, "trinta": 30, "quarenta": 40,
    "cinquenta": 50, "sessenta": 60, "setenta": 70, "oitenta": 80,
    "noventa": 90, "cem": 100, "cento": 100, "mil": 1000,
    "milésimo": 1000, "milésimos": 1000, "centésimo": 100, "centésimos": 100,
    "décimo": 10, "décimos": 10,
}


def number_mentions(text):
    c = collections.Counter()
    for d in NUM_RE.findall(text):
        c[int(d)] += 1
    for w in WORD_RE.findall(text.lower()):
        if w in NUMBER_WORDS:
            c[NUMBER_WORDS[w]] += 1
    return c

# Tokens de controle `{...}`. `{''}` (aspas) e `{\d}` (glifo/apostrofo, ex.
# `{9}` = ' ) sao estilisticos -> INFO. O resto (`{#A}`, `{po}` = libra, `{.}`
# = marcador de lista) e funcional -> FAIL se sumir/mudar.
GLYPH_TOKENS = re.compile(r"^\{''\}$|^\{\d\}$")

# Vocabulario critico de enigma: se aparece no EN, o equivalente PT precisa
# aparecer no bloco. Dia da semana e cor sao WARN (erram a resposta); o resto
# e INFO (revisao manual).
WEEKDAYS = {
    "monday": r"segunda", "tuesday": r"ter[çc]a", "wednesday": r"quarta",
    "thursday": r"quinta", "friday": r"sexta", "saturday": r"s[áa]bado",
    "sunday": r"domingo",
}
COLORS = {
    "red": r"vermelh|rubr|encarnad", "blue": r"azu[il]", "green": r"verde",
    "yellow": r"amarel", "white": r"branc", "black": r"pret|negro",
    "purple": r"rox|p[úu]rpura|violeta", "orange": r"laranja",
    "pink": r"rosa|cor-de-rosa", "brown": r"marrom|castanho",
    "grey": r"cinza|cinzent", "gray": r"cinza|cinzent",
}
CRITICAL = [
    (re.compile(r"\bclockwise\b", re.I), r"hor[áa]rio", "sentido horario"),
    (re.compile(r"anti-?clockwise|counterclockwise", re.I),
     r"anti-?hor[áa]rio", "sentido anti-horario"),
    (re.compile(r"\b(?:to|on|at) the left\b|\bleft side\b|\bturn left\b", re.I),
     r"esquerd", "esquerda"),
    (re.compile(r"\b(?:to|on|at) the right\b|\bright side\b|\bturn right\b", re.I),
     r"direit", "direita"),
    (re.compile(r"\babove\b", re.I), r"acima|sobre", "acima"),
    (re.compile(r"\bbelow\b|\bunder(?:neath)?\b", re.I), r"abaixo|sob|debaixo", "abaixo"),
    (re.compile(r"\bodd numbers?\b", re.I), r"[íi]mpares?", "impar"),
    (re.compile(r"\beven numbers?\b", re.I), r"\bpares?\b", "par"),
    (re.compile(r"\bdouble\b", re.I), r"dobr|duas vezes|2 vezes", "dobro"),
    (re.compile(r"\bhalf\b", re.I), r"metade|meio", "metade"),
    (re.compile(r"\bbefore\b", re.I), r"antes", "antes"),
    (re.compile(r"\bafter\b", re.I), r"depois|ap[óo]s", "depois"),
    (re.compile(r"\bgreater\b|\bmore than\b", re.I), r"maior|mais de", "maior"),
    (re.compile(r"\bsmaller\b|\bless than\b|\bfewer\b", re.I),
     r"menor|menos de", "menor"),
    (re.compile(r"\bsame\b", re.I), r"mesm|igual", "mesmo"),
    (re.compile(r"\bdifferent\b", re.I), r"diferent", "diferente"),
    (re.compile(r"\bin a row\b|\brow\b", re.I), r"fileira|linha|fila", "fileira"),
    (re.compile(r"\bcolumn\b", re.I), r"coluna", "coluna"),
    (re.compile(r"\bdiagonal(?:ly)?\b", re.I), r"diagonal", "diagonal"),
    (re.compile(r"\badjacent\b", re.I), r"adjacent|vizinha|ao lado", "adjacente"),
    (re.compile(r"\bmultiplied?\b|\btimes\b|\bmultiply\b", re.I),
     r"multiplic|\bvezes\b", "multiplicar"),
    (re.compile(r"\bdivided?\b", re.I), r"divid", "dividir"),
    (re.compile(r"\bsum\b|\btotal\b", re.I), r"soma|total", "soma"),
]
# Frases fixas do glossario (REGRAS_TRADUCAO.md:32-33). WARN: a traducao
# autonoma pode usar sinonimo aceitavel, mas o harness aponta o desvio.
GLOSSARY_PHRASES = [
    (re.compile(r"\bGood thinking!"), r"bem pensado",
     "Good thinking! -> Bem pensado! (REGRAS_TRADUCAO.md:32)"),
    (re.compile(r"\bExcellent work!"), r"bom trabalho",
     "Excellent work! -> Bom trabalho! (REGRAS_TRADUCAO.md:33)"),
    (re.compile(r"\bBrilliant!"), r"excelente",
     "Brilliant! -> Excelente! (REGRAS_TRADUCAO.md:33)"),
]

# Continuidade de falas: o mesmo trecho EN entre {''} que reaparece em blocos
# diferentes (pergunta <-> dica) deve ter PT identico (REGRAS_TRADUCAO.md,
# "Continuidade de falas repetidas"). Divergencia = WARN.
QUOTE_RE = re.compile(r"\{''\}(.*?)\{''\}", re.S)

# Watchlist gramatical de alta precisao (INFO): padroes que quase sempre
# indicam desvio de PT-BR. Nao bloqueiam o gate; alimentam o passe gramatical
# obrigatorio (REGRAS_TRADUCAO.md, "Gramatica PT-BR").
GRAMMAR_WATCH = [
    (re.compile(r"\bem baixo\b", re.I), "ortografia: use 'embaixo'"),
    (re.compile(r"[Ss]upondo que[^\n]*\bn[ãa]o pode\b"),
     "subjuntivo: 'supondo que ... nao possa'"),
    (re.compile(r"\bp[áa]reo contra\b", re.I),
     "regência: 'páreo para', não 'páreo contra'"),
    (re.compile(r"\bolh\w+[^\n]*\bde perto nas\b", re.I),
     "regência: 'olhar as' (sem 'nas')"),
    (re.compile(r"\bEm que cor\b", re.I), "regência: 'De que cor'"),
    (re.compile(r"\bchegar (?:na|no|nele|nela|neles|nelas)\b", re.I),
     "regência/crase: 'chegar a/ao/à/a ele'"),
    (re.compile(r"\bdesliz\w+ (?:a|à|ao) parede\b", re.I),
     "regência: 'deslizar até a parede'"),
    (re.compile(r"\bfalar sobre [A-D]\b"), "fidelidade: 'aplicar-se a'"),
    (re.compile(r"\bformam juntos\b", re.I), "ordem: 'que juntos formam'"),
]


def norm_quote(s):
    """Normaliza aspas de fala para comparar continuidade EN<->PT."""
    return re.sub(r"\s+", " ", TAG_RE.sub("", s)).strip()



def decode_font(nftr_path):
    """Decodifica CWDH+CMAP de um `.nftr`.

    Verificado contra `Spec/Fontes_NFTR.md` (ver `verify_font`): o avanco e o
    3o byte do CWDH (`cw[idx][2]`, == coluna `Total` documentada, 147/147
    glifos em fontq e fontevent) e o CMAP comeca em `+16`, nao `+20`.
    Retorna dict `{cw, cmap, mmin, mmax}` ou None.
    """
    try:
        with open(nftr_path, "rb") as f:
            data = f.read()
        co = data.find(b"HDWC")
        mo = data.find(b"PAMC")
        if co < 0 or mo < 0:
            return None
        cmin = struct.unpack_from("<H", data, co + 8)[0]
        cmax = struct.unpack_from("<H", data, co + 10)[0]
        mmin = struct.unpack_from("<H", data, mo + 8)[0]
        mmax = struct.unpack_from("<H", data, mo + 10)[0]
        cw = [
            (data[co + 16 + i * 3], data[co + 16 + i * 3 + 1], data[co + 16 + i * 3 + 2])
            for i in range(cmax - cmin + 1)
        ]
        cmap = [
            struct.unpack_from("<H", data, mo + 16 + i * 2)[0]
            for i in range(mmax - mmin + 1)
        ]
        return {"cw": cw, "cmap": cmap, "mmin": mmin, "mmax": mmax}
    except (OSError, struct.error):
        return None


def load_widths(nftr_path):
    """Retorna funcao largura(texto)->px somando adv (Spec/Fontes_NFTR.md:4)."""
    font = decode_font(nftr_path)
    if font is None:
        return None
    cw, cmap, mmin, mmax = font["cw"], font["cmap"], font["mmin"], font["mmax"]

    def w(t):
        s = 0
        for ch in t:
            cp = ord(ch)
            if mmin <= cp <= mmax:
                idx = cmap[cp - mmin]
                s += cw[idx][2] if idx != 0xFFFF else 4
            else:
                s += 4
        return s

    return w


def verify_font(root):
    """Confere a decodificacao do .nftr contra a tabela documentada na Spec."""
    spec_path = os.path.join(root, "Spec", "Fontes_NFTR.md")
    try:
        spec = open(spec_path, encoding="utf-8").read()
    except OSError:
        print("Spec/Fontes_NFTR.md nao encontrada", file=sys.stderr)
        return 2
    targets = [
        ("fontq.nftr", "### 3.2", "fontq (Enigmas/Dicas)"),
        ("fontevent.nftr", "### 3.1", "fontevent (Textos)"),
    ]
    rc = 0
    for fname, marker, label in targets:
        parts = spec.split(marker, 1)
        if len(parts) < 2:
            print(f"{label}: secao {marker} nao encontrada", file=sys.stderr)
            rc = 2
            continue
        seg = parts[1].split("## ", 1)[0]
        rows = []
        for line in seg.splitlines():
            m = re.match(
                r"\|\s*(\d+)\s*\|\s*U\+[0-9A-Fa-f]+\s*\|\s*`.*?`\s*\|"
                r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*"
                r"\|\s*\*\*(\d+)\*\*\s*\|",
                line,
            )
            if m:
                rows.append((int(m.group(1)), int(m.group(6))))
        font = decode_font(os.path.join(root, "Previewer", "Fontes", fname))
        if font is None or not rows:
            print(f"{label}: falha ao decodificar ({fname})", file=sys.stderr)
            rc = 2
            continue
        cw, cmap, mmin = font["cw"], font["cmap"], font["mmin"]
        bad = []
        for cp, total in rows:
            idx = cmap[cp - mmin]
            if idx != 0xFFFF and cw[idx][2] != total:
                bad.append((chr(cp), cw[idx], total))
        status = "OK" if not bad else "FALHA"
        print(f"{label}: {len(rows) - len(bad)}/{len(rows)} larguras conferem [{status}]")
        for ch, raw, total in bad[:10]:
            print(f"  {ch!r} raw={raw} esperado Total={total}")
        if bad:
            rc = 1
    return rc


def role_of(header):
    m = BRACKET_RE.match(header)
    return ROLE.get(m.group(1), "?") if m else "?"


def parse_sections(text):
    """Divide o arquivo nos blocos delimitados pelas linhas `[...]`."""
    sections = []
    cur = None
    for i, line in enumerate(text.split("\n")):
        if line.startswith("[") and line.endswith("]"):
            if cur:
                sections.append(cur)
            cur = {
                "header": line,
                "role": role_of(line),
                "start_line": i + 1,
                "lines": [line],
            }
        elif cur is not None:
            cur["lines"].append(line)
    if cur:
        sections.append(cur)
    return sections


def content_lines(section):
    out = []
    for line in section["lines"][1:]:
        s = line.strip()
        if not s:
            continue
        if set(s) <= set("*!-"):
            continue
        if MARKER_RE.match(s):
            continue
        out.append(s)
    return out


def block_text(section):
    return "\n".join(content_lines(section))


def norm_for_width(s):
    return re.sub(r"\{[^}]*\}", '"', TAG_RE.sub("", s))


def tokens(text):
    return TOKEN_RE.findall(text)


def find_weekdays(text):
    low = text.lower()
    return {d for d in WEEKDAYS if re.search(r"\b" + d + r"\b", low)}


def find_colors(text):
    low = text.lower()
    return {c for c in COLORS if re.search(r"\b" + c + r"\b", low)}


def check_pair(en_sec, pt_sec, f, puzzle, wfunc, block_idx=0):
    findings = []
    role = en_sec["role"]

    def add(sev, cat, target, _block, line, msg, rule=None):
        findings.append({
            "sev": sev, "cat": cat, "target": target, "file": f, "puzzle": puzzle,
            "role": role, "block": block_idx, "line": line, "msg": msg, "rule": rule,
        })

    # header/ponteiro identico
    if en_sec["header"] != pt_sec["header"]:
        add("FAIL", "estrutura", "PT", en_sec["start_line"] - 1,
            pt_sec["start_line"], f"header difere EN={en_sec['header']} PT={pt_sec['header']}",
            "estrutura lbin")

    en_text = block_text(en_sec)
    pt_text = block_text(pt_sec)
    en_plain = TAG_RE.sub("", en_text)
    pt_plain = TAG_RE.sub("", pt_text)
    # prosa = sem tags e sem tokens `{...}` (evita ler `{9}`/`{#2}` como numero).
    # `1/1000` = fracao: mantem so o denominador para casar com `milésimo`.
    en_prose = re.sub(r"\b1/(\d+)", r"\1", TOKEN_RE.sub("", en_plain))
    pt_prose = re.sub(r"\b1/(\d+)", r"\1", TOKEN_RE.sub("", pt_plain))

    # tags
    en_tags = sorted(TAG_RE.findall(en_text))
    pt_tags = sorted(TAG_RE.findall(pt_text))
    if en_tags != pt_tags:
        add("FAIL", "tecnico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"tags EN={en_tags} PT={pt_tags}", "REGRAS_TRADUCAO.md:68")

    # tokens de controle {..}
    en_toks = tokens(en_text)
    pt_toks = tokens(pt_text)
    if sorted(en_toks) != sorted(pt_toks):
        en_non = sorted(t for t in en_toks if not GLYPH_TOKENS.match(t))
        pt_non = sorted(t for t in pt_toks if not GLYPH_TOKENS.match(t))
        if en_non != pt_non:
            add("FAIL", "referencia", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"token funcional EN={en_non} PT={pt_non}", "controle {#X}/{po}/{.}")
        glyph_diff = collections.Counter(en_toks) - collections.Counter(pt_toks)
        glyph_diff.update(-(collections.Counter(pt_toks) - collections.Counter(en_toks)))
        glyph_diff = {k: v for k, v in glyph_diff.items() if v and GLYPH_TOKENS.match(k)}
        if glyph_diff:
            add("INFO", "referencia", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"glifo/aspas difere EN<->PT: {glyph_diff}", "token estilistico")

    # largura por linha (fontq)
    if wfunc:
        for ln, line in enumerate(content_lines(pt_sec)):
            s = norm_for_width(line)
            px = wfunc(s)
            fline = pt_sec["start_line"] + 1 + ln
            if px > HARD_PX:
                add("FAIL", "tecnico", "PT", en_sec["start_line"] - 1, fline,
                    f"largura {px}px > hard {HARD_PX}: {line[:80]}",
                    "Fontes_NFTR.md:4/Screen03")
            elif px > SAFE_PX:
                add("WARN", "tecnico", "PT", en_sec["start_line"] - 1, fline,
                    f"largura {px}px > safe {SAFE_PX}: {line[:80]}",
                    "REGRAS_TRADUCAO.md:73")

    # hifenizacao
    if HYPHEN_RE.search(pt_text):
        add("FAIL", "tecnico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            "possivel hifenizacao (palavra quebrada com '-')", "REGRAS_TRADUCAO.md:71")

    # contagem de linhas
    nl_en = len(content_lines(en_sec))
    nl_pt = len(content_lines(pt_sec))
    if role in HARD_LINES and nl_pt > HARD_LINES[role]:
        add("WARN", "tecnico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"{nl_pt} linhas > teto {HARD_LINES[role]} ({ROLE_PT.get(role, role)})",
            "REGRAS_TRADUCAO.md:69")
    elif nl_pt > nl_en:
        add("INFO", "tecnico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"{nl_pt} linhas PT vs {nl_en} EN ({ROLE_PT.get(role, role)})",
            "possivel overflow de caixa")

    # glossario
    m = EN_RESIDUAL.search(pt_plain)
    if m:
        add("FAIL", "glossario", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"ingles residual: {m.group(0)}", "REGRAS_TRADUCAO.md:2")
    m = PT_WRONG.search(pt_plain)
    if m:
        add("FAIL", "glossario", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"termo PT proibido: {m.group(0)}", "REGRAS_TRADUCAO.md:2")

    # numeros (resposta): so digitos explicitos do EN contam (evita falso
    # positivo do pronome "one"); PT aceita digito OU numero escrito por
    # extenso. EN sem equivalente PT = possivel omissao (WARN); PT extra =
    # possivel invencao (INFO).
    en_nums = {int(d) for d in NUM_RE.findall(en_prose)}
    pt_nums = set(number_mentions(pt_prose))
    if re.search(r"\bum\b|\buma\b", pt_prose, re.I):
        pt_nums.add(1)  # "um/uma" casa com o digito 1
    missing = sorted(en_nums - pt_nums)
    if missing:
        add("WARN", "semantico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
            f"numeros EN ausentes no PT: {missing}", "contexto do enigma")

    # dias da semana / cores (resposta)
    for d in sorted(find_weekdays(en_prose)):
        if not re.search(WEEKDAYS[d], pt_prose, re.I):
            add("FAIL", "semantico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"dia EN '{d}' sem equivalente PT ('{WEEKDAYS[d]}')", "resposta do enigma")
    for c in sorted(find_colors(en_prose)):
        if not re.search(COLORS[c], pt_prose, re.I):
            add("WARN", "semantico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"cor EN '{c}' sem equivalente PT ('{COLORS[c]}')", "resposta do enigma")

    # vocabulario critico (direcao/ordem/matematica)
    for rx, ptx, label in CRITICAL:
        m = rx.search(en_prose)
        if m and not re.search(ptx, pt_prose, re.I):
            add("INFO", "semantico", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"termo critico EN '{m.group(0)}' ({label}) sem equivalente PT esperado ('{ptx}')",
                "back-translation")

    # frases fixas do glossario
    for erx, prx, rule in GLOSSARY_PHRASES:
        m = erx.search(en_prose)
        if m and not re.search(prx, pt_prose, re.I):
            add("WARN", "glossario", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"EN '{m.group(0)}' sem '{prx}' no PT", rule)

    # watchlist gramatical (INFO) — alimenta o passe gramatical obrigatorio
    for grx, note in GRAMMAR_WATCH:
        m = grx.search(pt_plain)
        if m:
            add("INFO", "gramatica", "PT", en_sec["start_line"] - 1, pt_sec["start_line"],
                f"{note}: '{m.group(0).strip()}'", "REGRAS_TRADUCAO.md/gramatica")

    return findings


def check_file(en_path, pt_path, wfunc):
    findings = []
    en_txt = open(en_path, encoding="utf-8", errors="replace").read()
    puzzle = os.path.basename(en_path).split(".")[0]

    if "�" in en_txt:
        findings.append({"sev": "FAIL", "cat": "tecnico", "target": "EN", "file": os.path.basename(en_path),
                         "puzzle": puzzle, "line": 1, "msg": "replacement char U+FFFD no EN",
                         "rule": "encoding"})
    if not pt_path or not os.path.exists(pt_path):
        findings.append({"sev": "FAIL", "cat": "cobertura", "target": "PT", "file": os.path.basename(en_path),
                         "puzzle": puzzle, "line": 1, "msg": "sem par PT (arquivo faltando)",
                         "rule": "cobertura"})
        return findings

    pt_txt = open(pt_path, encoding="utf-8", errors="replace").read()
    if "�" in pt_txt:
        findings.append({"sev": "FAIL", "cat": "tecnico", "target": "PT", "file": os.path.basename(en_path),
                         "puzzle": puzzle, "line": 1, "msg": "replacement char U+FFFD no PT",
                         "rule": "REGRAS_TRADUCAO.md:5/windows-1252"})

    en_secs = parse_sections(en_txt)
    pt_secs = parse_sections(pt_txt)
    if len(en_secs) != len(pt_secs):
        findings.append({"sev": "FAIL", "cat": "estrutura", "target": "PT",
                         "file": os.path.basename(en_path), "puzzle": puzzle, "line": 1,
                         "msg": f"blocos EN={len(en_secs)} PT={len(pt_secs)} (truncamento?)",
                         "rule": "estrutura lbin"})
    en_markers = [l.strip() for l in en_txt.split("\n") if MARKER_RE.match(l.strip())]
    pt_markers = [l.strip() for l in pt_txt.split("\n") if MARKER_RE.match(l.strip())]
    if en_markers != pt_markers:
        findings.append({"sev": "FAIL", "cat": "estrutura", "target": "PT",
                         "file": os.path.basename(en_path), "puzzle": puzzle, "line": 1,
                         "msg": f"marcadores EN={en_markers} PT={pt_markers}",
                         "rule": "estrutura lbin"})

    for i, (es, ps) in enumerate(zip(en_secs, pt_secs)):
        findings.extend(check_pair(es, ps, os.path.basename(en_path), puzzle, wfunc, i))

    # continuidade de falas repetidas: mesmo trecho EN {''}-> PT identico
    en_quotes = [norm_quote(q) for q in QUOTE_RE.findall(en_txt)]
    pt_quotes = [norm_quote(q) for q in QUOTE_RE.findall(pt_txt)]
    if len(en_quotes) == len(pt_quotes) and len(en_quotes) > 1:
        by_en = collections.defaultdict(list)
        for i, q in enumerate(en_quotes):
            by_en[q].append(i)
        for q, idxs in by_en.items():
            if len(idxs) > 1 and len({pt_quotes[i] for i in idxs}) > 1:
                findings.append({
                    "sev": "WARN", "cat": "continuidade", "target": "PT",
                    "file": os.path.basename(en_path), "puzzle": puzzle,
                    "block": idxs[0], "line": 1,
                    "msg": (f"fala repetida EN '{q[:60]}' com PT divergente: "
                            + " | ".join(f"'{pt_quotes[i][:40]}'" for i in idxs)),
                    "rule": "REGRAS_TRADUCAO.md/continuidade",
                })
    return findings


def run(root, group, wfunc):
    en_dir = os.path.join(root, "Textos Originais", "rc", "nazo", "uk", group)
    pt_dir = os.path.join(root, "Textos Traduzidos", "rc", "nazo", "uk", group)
    if not os.path.isdir(en_dir):
        print(f"grupo nao encontrado: {en_dir}", file=sys.stderr)
        return None
    files = sorted(f for f in os.listdir(en_dir) if f.endswith(".lbin.txt"))
    findings = []
    total_blocks = 0
    for f in files:
        ff = check_file(os.path.join(en_dir, f),
                        os.path.join(pt_dir, f) if os.path.isdir(pt_dir) else None,
                        wfunc)
        findings.extend(ff)
        total_blocks += len(parse_sections(
            open(os.path.join(en_dir, f), encoding="utf-8", errors="replace").read()))
    for x in findings:
        x["blocking"] = x["sev"] == "FAIL"
    return {"group": group, "files": len(files), "blocks": total_blocks,
            "findings": findings}


def write_reports(root, report, out_json, out_md):
    findings = report["findings"]
    fails = [x for x in findings if x["sev"] == "FAIL"]
    warns = [x for x in findings if x["sev"] == "WARN"]
    infos = [x for x in findings if x["sev"] == "INFO"]
    gate = "BLOCKED" if fails else "PASS"
    cat = collections.Counter((x["sev"], x["cat"]) for x in findings)
    data = {
        "group": report["group"], "files": report["files"], "blocks": report["blocks"],
        "gate": gate, "fails": len(fails), "warns": len(warns), "infos": len(infos),
        "warn_policy": WARN_POLICY,
        "findings": sorted(findings, key=lambda x: (
            x.get("file", ""), x.get("line", 0), x.get("sev", ""))),
    }
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)

    def fmt(x):
        role = ROLE_PT.get(x.get("role", ""), x.get("role", ""))
        where = f"{x.get('file','')}:{x.get('line','?')}"
        return (f"- [{x['sev']}/{x['cat']}] {where} ({x.get('target','')}) "
                f"{x.get('puzzle','')}/{role}: {x['msg']}"
                + (f" [{x['rule']}]" if x.get("rule") else "") + "\n")

    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write(f"# QA enigmas {report['group']} — {report['files']} enigmas, "
                 f"{report['blocks']} blocos EN\n\n")
        fh.write(f"**gate={gate}** · FAIL={len(fails)} (erros) · "
                 f"WARN={len(warns)} (avisos) · INFO={len(infos)} (revisao manual)\n\n")
        fh.write(f"> {WARN_POLICY}\n\n")
        fh.write("## Por categoria\n\n")
        for (sev, c), n in sorted(cat.items()):
            fh.write(f"- {sev}/{c}: {n}\n")
        for title, sev, note in (
            ("Bloqueantes (FAIL — erros)", "FAIL", "Corrigir: impedem o veredito."),
            ("Avisos (WARN — não bloqueiam)", "WARN", "Revisão opcional/contextual."),
            ("Informativos (INFO — revisão manual)", "INFO", "Heurísticas/watchlist."),
        ):
            subset = [x for x in findings if x["sev"] == sev]
            fh.write(f"\n## {title}\n\n> {note}\n\n")
            if subset:
                for x in sorted(subset, key=lambda v: (v.get("file", ""), v.get("line", 0))):
                    fh.write(fmt(x))
            else:
                fh.write("- nenhum\n")
    print(f"{report['group']}: {report['files']} enigmas, {report['blocks']} blocos EN, "
          f"gate={gate} FAIL={len(fails)} WARN={len(warns)} INFO={len(infos)} "
          f"-> {out_json}, {out_md}")
    return 1 if fails else 0


def write_audit(root, report, group, out_path):
    """Dump EN<->PT de TODOS os blocos para forcar leitura exaustiva.

    `gate=PASS` nao significa "sem achados": este artefato existe para que a
    varredura bloco-a-bloco seja auditavel e para que a proxima run COMPARE com
    a anterior em vez de re-resumir. Nao julga: so mostra o par EN<->PT e marca
    os blocos que o harness flagrou.
    """
    en_dir = os.path.join(root, "Textos Originais", "rc", "nazo", "uk", group)
    pt_dir = os.path.join(root, "Textos Traduzidos", "rc", "nazo", "uk", group)
    files = sorted(f for f in os.listdir(en_dir) if f.endswith(".lbin.txt"))
    by_block = collections.defaultdict(list)
    for x in report["findings"]:
        by_block[(x.get("file"), x.get("role"), x.get("block"))].append(x)

    rows = []
    for f in files:
        en_txt = open(os.path.join(en_dir, f), encoding="utf-8", errors="replace").read()
        pt_path = os.path.join(pt_dir, f)
        pt_txt = (open(pt_path, encoding="utf-8", errors="replace").read()
                  if os.path.exists(pt_path) else "")
        en_secs = parse_sections(en_txt)
        pt_secs = parse_sections(pt_txt)
        for i, es in enumerate(en_secs):
            ps = pt_secs[i] if i < len(pt_secs) else None
            rows.append({
                "file": f, "puzzle": f.split(".")[0], "block": i,
                "role": es["role"], "line": es["start_line"],
                "en": block_text(es),
                "pt": block_text(ps) if ps is not None else "(sem par PT)",
                "findings": by_block.get((f, es["role"], i), []),
            })

    total = len(rows)
    empty = sum(1 for r in rows if not r["en"].strip())
    flagged = sum(1 for r in rows if r["findings"])
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"# Auditoria exaustiva {group} — todos os blocos EN<->PT\n\n")
        fh.write(f"Blocos: **{total}** ({empty} vazios/placeholder) · "
                 f"com achado do harness: **{flagged}**\n\n")
        fh.write("> `gate=PASS` NAO significa \"sem achados\". Leia cada bloco e "
                 "atribua veredito nas 7 dimensoes: resposta/condicao, fidelidade "
                 "(adicao/omissao), gramatica/ortografia, voz/registro, glossario, "
                 "tokens/tags, caixa (fontq 230/210 + teto 14/12). Nada pode ser "
                 "omitido por gravidade; priorizar so ordena, nao filtra.\n\n")
        last = None
        for r in rows:
            if r["file"] != last:
                fh.write(f"\n# {r['file']}\n")
                last = r["file"]
            sev = ""
            if r["findings"]:
                sev = " ⚠ " + ", ".join(sorted({x["sev"] for x in r["findings"]}))
            fh.write(f"\n## {r['puzzle']}/{ROLE_PT.get(r['role'], r['role'])} "
                     f"(linha {r['line']}){sev}\n\n")
            fh.write("**EN:**\n```\n" + (r["en"] or "(vazio)") + "\n```\n\n")
            fh.write("**PT:**\n```\n" + (r["pt"] or "(vazio)") + "\n```\n")
            for x in r["findings"]:
                fh.write(f"- `{x['sev']}/{x['cat']}` {x['msg']}"
                         + (f" [{x['rule']}]" if x.get("rule") else "") + "\n")
    print(f"auditoria: {out_path} ({total} blocos, {empty} vazios, {flagged} com achado)")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Harness QA layton-qa — enigmas (nazo)")
    ap.add_argument("--df", default=None, help="grupo 0..9 (naz_dfN)")
    ap.add_argument("--all", action="store_true", help="todos os grupos naz_df0..9")
    ap.add_argument("--root", default=".", help="raiz do repo")
    ap.add_argument("--report", default=None, help="json de saida")
    ap.add_argument("--md", default=None, help="resumo markdown")
    ap.add_argument("--exhaustive", action="store_true",
                    help="dump EN<->PT de todos os blocos + qa_nazo_dfN.audit.md")
    ap.add_argument("--verify-font", action="store_true",
                    help="confere CWDH/CMAP do .nftr contra Spec/Fontes_NFTR.md e sai")
    args = ap.parse_args()

    if args.verify_font:
        return verify_font(args.root)
    if not args.all and args.df is None:
        ap.error("informe --df N ou --all")
    groups = (["naz_df%d" % i for i in range(10)] if args.all
              else [f"naz_df{args.df}"])

    wfunc = load_widths(os.path.join(args.root, "Previewer", "Fontes", "fontq.nftr"))
    if wfunc is None:
        print("aviso: fontq.nftr nao lido; cheque de largura desativado", file=sys.stderr)

    rc = 0
    for g in groups:
        rep = run(args.root, g, wfunc)
        if rep is None:
            rc = 2
            continue
        suffix = g.replace("naz_", "")
        out_json = args.report or f"qa_nazo_{suffix}.json"
        out_md = args.md or f"qa_nazo_{suffix}.md"
        if write_reports(args.root, rep, out_json, out_md):
            rc = 1
        if args.exhaustive:
            write_audit(args.root, rep, g, f"qa_nazo_{suffix}.audit.md")
    return rc


if __name__ == "__main__":
    sys.exit(main())
