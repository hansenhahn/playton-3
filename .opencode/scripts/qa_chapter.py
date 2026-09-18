#!/usr/bin/env python3
"""Harness generico de QA para layton-qa (todos os capitulos).

Uso:
    python3 .opencode/scripts/qa_chapter.py --cap 01 [--root .] [--report qa_01.json] [--md qa_01.md]

Nao traduz nem edita: apenas detecta. A skill layton-qa continua mandando
no rewrite cirurgico; este script mecaniza os bullets deterministicos e
gera sidecar de flagrados para o julgamento semantico (LLM/manual).

Cobertura por bloco: split('<T>') -> termina em </V> ou !---!/!***!
(funciona para dublados <V> e nao-dublados de exploracao).
"""
import argparse
import json
import os
import re
import struct
import sys

HARD_PX = 247
SAFE_PX = 210

SPEAKERS = {
    "レイトン": "Layton",
    "ルーク": "Luke",
    "ナレーション": "Narration",
    "ドルガー": "Dolger/Alfie",
    "タイラー": "Tyler",
    "ニコラ": "Nicola",
    "アニータ": "Anita",
    "ヘイゼル": "Hazel",
    "ブッチ": "Butch",
    "アデリン": "Adeline",
    "マックス": "Max",
    "ベル": "Belle",
    "ベッキー": "Becky",
    "マーガレット": "Margaret",
    "クローンマフィア": "Family Goon",
    "バッカス": "Bacchus",
    "ウッズ": "Woods",
    "シャロン": "Sharon",
    "未来シュレーダー": "Future Schrader",
    "未来ルーク": "Future Luke",
    "ハロルド": "Harold",
    "デロイ": "Delroy",
}
STRICT_VOICE = {"Layton"}  # informal aqui = FAIL; resto = INFO (Luke e criança: oralidade e esperada)
# Falantes que tratam Layton com deferencia -> "voce" merece checagem (o senhor?)
TRATAMENTO_SPEAKERS = {
    "Future Luke", "Harold", "Anita", "Sharon", "Margaret",
    "Bacchus", "Adeline", "Woods", "Delroy",
}
# Calques de sintaxe/registro tipicos de traducao automatica (INFO p/ revisao)
CALQUE_PT = re.compile(
    r"chegar ao fundo|ao fundo de|plenamente operacional|ao usu[áa]rio"
    r"|cruza os \d+ anos|em termos de|fazer sentido|de volta ao",
    re.I,
)

TAG_RE = re.compile(r"<[^>]+>")
END_RE = re.compile(r"(.*?)((</V>)|(![-*]+!))", re.S)
VOICE_RE = re.compile(
    r"(?<![A-Za-zÀ-ÿ])tô(?![A-Za-zÀ-ÿ])|(?<![A-Za-zÀ-ÿ])tá(?![A-Za-zÀ-ÿ])"
    r"|(?<![A-Za-zÀ-ÿ])pra(?![A-Za-zÀ-ÿ])|(?<![A-Za-zÀ-ÿ])né(?![A-Za-zÀ-ÿ])"
    r"|(?<![A-Za-zÀ-ÿ])bora(?![A-Za-zÀ-ÿ])|(?<![A-Za-zÀ-ÿ])mano(?![A-Za-zÀ-ÿ])"
    r"|\bdá pra\b|\ba gente\b",
    re.I,
)
EN_RESIDUAL = re.compile(
    r"\bpuzzle\b|\bhint coin\b|\bInspector\b|\bConstable\b|\bGranny\b", re.I
)
PT_WRONG = re.compile(
    r"quebra-cabeça|quebra-cabeca|moeda de pista|Índice de Enigmas|Inspector|Constable|Granny",
    re.I,
)
NEG_EN = re.compile(r"\b(not|n't|no\b|none|never|nothing|neither|nor)\b", re.I)
NEG_PT = re.compile(r"\b(não|nao|nem|nunca|nenhum\w*|nada|tampouco)\b", re.I)
NUM_RE = re.compile(r"\d+")
HYPHEN_RE = re.compile(r"[A-Za-zÀ-ÿ]-\s*\n\s*[A-Za-zÀ-ÿ]")
# Watchlist semantica (heuristica -> revisao manual, nao veredito). Casos vindos
# da analise do cap. 01 + bullets da skill (from temporal, soft sciences, etc).
IDIOM_WATCH = [
    (re.compile(r"on the same page", re.I), "idiom 'same page' (calque? 'de acordo')"),
    (re.compile(r"\bWELL\?", re.I), "'WELL?' interjeicao (ENTÃO?/E AI? nao 'BEM?')"),
    (re.compile(r"Tee hee", re.I), "onomatopeia identitaria (preservar?)"),
    (re.compile(r"\bmy boy\b", re.I), "'my boy' -> 'Meu jovem' (Layton) / 'meu rapaz' (Future Schrader)"),
    (re.compile(r"\bRoom \d+", re.I), "'Room N' hospitalar (Quarto? Sala?)"),
    (re.compile(r"\bOld \d+", re.I), "'Old N' refere pessoa (do N, masc.)"),
    (re.compile(r"Unless\.\.\.", re.I), "'Unless...' suspensao preservada?"),
    (re.compile(r"ne'er-do-well", re.I), "registro ('suspeito' vs pejorativo)"),
    (re.compile(r"\bwhizz\b", re.I), "'whizz' (gênio/esperto?)"),
    (re.compile(r"\bold dear\b", re.I), "'old dear' carro (tom afetivo)"),
    (re.compile(r"\bfrom \d+ years in the future\b", re.I), "pleonasmo temporal?"),
    (re.compile(r"things.+I mean", re.I | re.S), "ameaca 'things... I mean' omitida?"),
    (re.compile(r"get ugly", re.I), "'get ugly' traduzido ('feia')?"),
    (re.compile(r"bright as a button", re.I), "'bright as a button' (esperto que só?)"),
    (re.compile(r"brass neck", re.I), "'brass neck' (cara de pau?)"),
    (re.compile(r"spill the.{0,4}beans", re.I), "'spill the beans' (abrir o bico?)"),
    (re.compile(r"fight fire with fire", re.I), "'fight fire with fire' (combater fogo com fogo)"),
    (re.compile(r"one-way trip", re.I), "'one-way trip to nowhere' (viagem só de ida?)"),
    (re.compile(r"hotbed", re.I), "'hotbed' (antro?)"),
    (re.compile(r"not my scene", re.I), "'not my scene' (não é minha praia?)"),
    (re.compile(r"on the house", re.I), "'on the house' (por conta da casa)"),
    (re.compile(r"keep your hair on", re.I), "'keep your hair on' (calma!)"),
    (re.compile(r"whippersnapper", re.I), "'whippersnapper' (moleques?)"),
    (re.compile(r"strapping", re.I), "'strapping' (robusto/cheio de energia?)"),
    (re.compile(r"pearl of wisdom", re.I), "'pearl of wisdom' (dica de ouro?)"),
    (re.compile(r"in a pickle", re.I), "'in a pickle' (em apuros)"),
    (re.compile(r"on my watch", re.I), "'on my watch' (enquanto eu estiver de olho?)"),
    (re.compile(r"didn't half", re.I), "'didn't half' (intensificador britanico)"),
    (re.compile(r"get to the bottom", re.I), "'get to the bottom' (chegar à verdade?)"),
]
PLEO_RE = re.compile(r"daqui a .*no futuro|futuro.*futuro", re.I)


def load_widths(nftr_path):
    """Retorna funcao largura(texto)->px somando adv (Spec/Fontes_NFTR.md:4)."""
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
    except (OSError, struct.error):
        return None


def parse_blocks(text):
    """Extrai blocos <T> com join implicito; retorna lista de dicts.

    Cada bloco: raw (entre <T> e </V>|!---!|!***!), start_line (1-indexed da
    linha do <T>), tags, clean (sem tags).
    """
    out = []
    # localiza cada <T> e seu fim
    for m in re.finditer(r"<T>", text):
        start = m.end()
        tail = text[start:]
        em = END_RE.match(tail)
        raw = em.group(1) if em else tail
        start_line = text[: m.start()].count("\n") + 1
        tags = TAG_RE.findall(raw)
        clean = TAG_RE.sub("", raw)
        out.append(
            {"raw": raw, "start_line": start_line, "tags": tags, "clean": clean}
        )
    return out


def speaker_before(text, t_pos):
    """Detecta falante pela ultima tag JP antes da posicao do <T>."""
    head = text[:t_pos]
    names = re.findall(r"^ ?(.+)$", head, re.M)
    for line in reversed(head.splitlines()[-6:]):
        s = line.strip()
        if s in SPEAKERS:
            return SPEAKERS[s]
    return "?"


def content_lines(clean):
    """Linhas de dialogo (ignora delimitadores, headers LSCR, vazias)."""
    lines = []
    for l in clean.split("\n"):
        s = l.strip()
        if not s:
            continue
        if set(s) <= set("*!-"):
            continue
        if s.startswith("[") and s.endswith("]"):
            continue
        lines.append(s)
    return lines


def check_file(en_path, ia_path, hu_path, wfunc):
    en_txt = open(en_path, encoding="utf-8", errors="replace").read()
    findings = []
    en_blocks = parse_blocks(en_txt)
    t_poses = [m.start() for m in re.finditer(r"<T>", en_txt)]

    targets = []
    if ia_path and os.path.exists(ia_path):
        targets.append(("IA", ia_path))
    if hu_path and os.path.exists(hu_path):
        targets.append(("HU", hu_path))
    if not targets:
        findings.append(
            {"sev": "INFO", "cat": "cobertura", "msg": "sem par HUM/IA (cap. nao traduzido?)"}
        )
        return en_blocks, findings

    for label, path in targets:
        txt = open(path, encoding="utf-8", errors="replace").read()
        blocks = parse_blocks(txt)
        # bloco-count
        if len(blocks) != len(en_blocks):
            findings.append(
                {
                    "sev": "FAIL",
                    "cat": "tecnico",
                    "target": label,
                    "line": 1,
                    "msg": f"block-count EN={len(en_blocks)} vs {label}={len(blocks)} (truncamento?)",
                    "rule": "REGRAS_TRADUCAO.md:69 (estrutura identica)",
                }
            )
        # encoding: so acusa replacement char (arquivos no git sao UTF-8;
        # windows-1252 vale no build da ROM). Decode estrito gerava falso FAIL
        # em bytes 0x81/0x90/0x9D presentes ate nos Originais.
        if "�" in txt:
            findings.append(
                {"sev": "FAIL", "cat": "tecnico", "target": label,
                 "line": 1, "msg": "replacement char U+FFFD (encoding?)",
                 "rule": "REGRAS_TRADUCAO.md:5/windows-1252"}
            )
        for i, (eb, b) in enumerate(zip(en_blocks, blocks)):
            sp = speaker_before(
                txt, [m.start() for m in re.finditer(r"<T>", txt)][i]
                if i < len(re.findall(r"<T>", txt)) else 0,
            )
            # tags: multiset + ordem
            if sorted(eb["tags"]) != sorted(b["tags"]):
                findings.append(
                    {"sev": "FAIL", "cat": "tecnico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"tags EN={eb['tags']} vs {label}={b['tags']}",
                     "rule": "REGRAS_TRADUCAO.md:68"}
                )
            elif eb["tags"] != b["tags"]:
                findings.append(
                    {"sev": "WARN", "cat": "tecnico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"ordem de tags difere EN={eb['tags']} vs {label}={b['tags']}",
                     "rule": "REGRAS_TRADUCAO.md:68"}
                )
            # 3 linhas por pagina
            cl = content_lines(b["clean"])
            if len(cl) > 3:
                findings.append(
                    {"sev": "FAIL", "cat": "tecnico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"{len(cl)} linhas na pagina (max 3): {cl[:4]}",
                     "rule": "REGRAS_TRADUCAO.md:69"}
                )
            # hifenizacao
            if HYPHEN_RE.search(b["raw"]):
                findings.append(
                    {"sev": "FAIL", "cat": "tecnico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": "possivel hifenizacao (palavra quebrada com '-')",
                     "rule": "REGRAS_TRADUCAO.md:71"}
                )
            # largura real por linha
            if wfunc:
                for ln, line in enumerate(b["clean"].split("\n")):
                    s = line.strip()
                    if not s or set(s) <= set("*!-") or (
                        s.startswith("[") and s.endswith("]")
                    ):
                        continue
                    px = wfunc(re.sub(r"\{[^}]*\}", '"', s))
                    # linha do arquivo: aproxima (start_line + offset)
                    fline = b["start_line"] + ln
                    if px > HARD_PX:
                        findings.append(
                            {"sev": "FAIL", "cat": "tecnico", "target": label,
                             "block": i, "line": fline,
                             "msg": f"largura {px}px > hard {HARD_PX}: {s[:80]}",
                             "rule": "Fontes_NFTR.md:4/Screen01"}
                        )
                    elif px > SAFE_PX:
                        findings.append(
                            {"sev": "WARN", "cat": "tecnico", "target": label,
                             "block": i, "line": fline,
                             "msg": f"largura {px}px > safe {SAFE_PX}: {s[:80]}",
                             "rule": "REGRAS_TRADUCAO.md:73"}
                        )
            # glossario
            if EN_RESIDUAL.search(b["clean"]):
                findings.append(
                    {"sev": "FAIL", "cat": "glossario", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"ingles residual: {EN_RESIDUAL.search(b['clean']).group(0)}",
                     "rule": "REGRAS_TRADUCAO.md:2"}
                )
            m = PT_WRONG.search(b["clean"])
            if m:
                findings.append(
                    {"sev": "FAIL", "cat": "glossario", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"termo PT proibido: {m.group(0)}",
                     "rule": "REGRAS_TRADUCAO.md:2"}
                )
            # voz (com falante)
            vm = VOICE_RE.search(b["clean"])
            if vm:
                sev = "FAIL" if sp in STRICT_VOICE else "INFO"
                findings.append(
                    {"sev": sev, "cat": "voz", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"informal '{vm.group(0).strip()}' em falante {sp}",
                     "rule": "dossie Layton/Luke (_INDICE.md:40)"}
                )
            # tratamento (deferencia) — 'voce' para quem trata Layton por 'o senhor'
            if sp in TRATAMENTO_SPEAKERS and re.search(r"\bvoc[êe]\b", b["clean"], re.I):
                findings.append(
                    {"sev": "INFO", "cat": "tratamento", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"'você' em falante {sp} (para Layton deve ser 'o senhor'?)",
                     "rule": "dossie do falante + _INDICE.md:40"}
                )
            # calque sintatico
            cm = CALQUE_PT.search(b["clean"])
            if cm:
                findings.append(
                    {"sev": "INFO", "cat": "calque", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"possivel calque: '{cm.group(0)}'",
                     "rule": "Skill layton-qa (naturalidade idiomatica)"}
                )
            # pleonasmo
            if PLEO_RE.search(b["clean"]):
                findings.append(
                    {"sev": "WARN", "cat": "pleonasmo", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": "possivel pleonasmo temporal (validar contra EN)",
                     "rule": "Capitulo_XX + contexto"}
                )
            # numero EN vs PT
            en_nums = NUM_RE.findall(TAG_RE.sub("", eb["raw"]))
            pt_nums = NUM_RE.findall(b["clean"])
            if en_nums != pt_nums:
                findings.append(
                    {"sev": "WARN", "cat": "singular-plural", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"numeros EN={en_nums} vs {label}={pt_nums}",
                     "rule": "contexto/Capitulo_XX"}
                )
            # negacao: so uma direcao importa (EN nega e PT nao = possivel
            # inversao grave). O reverso (PT explicita 'não' onde EN usa
            # 'falta/impossible/un-') e parafrase normal -> nao acusar.
            # INFO, nao WARN: 'not polite' -> 'falta de educação' e valido.
            en_neg = bool(NEG_EN.search(TAG_RE.sub("", eb["raw"])))
            pt_neg = bool(NEG_PT.search(b["clean"]))
            if en_neg and not pt_neg:
                findings.append(
                    {"sev": "INFO", "cat": "semantico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": "EN nega e PT nao explicita (confira: falta/impossivel e OK)",
                     "rule": "back-translation"}
                )
            # razao de comprimento outlier (possivel omissao/invencao)
            en_len = len(TAG_RE.sub("", eb["raw"]).split())
            pt_len = len(b["clean"].split())
            if en_len >= 5 and (pt_len < en_len * 0.4 or pt_len > en_len * 2.2):
                findings.append(
                    {"sev": "WARN", "cat": "semantico", "target": label,
                     "block": i, "line": b["start_line"],
                     "msg": f"razao palavras EN={en_len} vs {label}={pt_len} (omissao/invencao?)",
                     "rule": "diff EN-PT"}
                )
    # watchlist semantica sobre EN (uma vez por bloco, fora do loop de targets)
    for i, eb in enumerate(en_blocks):
        for rx, why in IDIOM_WATCH:
            if rx.search(TAG_RE.sub("", eb["raw"])):
                findings.append(
                    {"sev": "INFO", "cat": "semantico", "target": "EN-ref",
                     "block": i, "line": eb["start_line"],
                     "msg": f"watchlist: {why}"}
                )
                break
    return en_blocks, findings


def main():
    ap = argparse.ArgumentParser(description="Harness QA layton-qa (generico por cap.)")
    ap.add_argument("--cap", required=True, help="ex. 01")
    ap.add_argument("--root", default=".", help="raiz do repo")
    ap.add_argument("--report", default=None, help="json de saida (default qa_<cap>.json)")
    ap.add_argument("--md", default=None, help="resumo markdown (default qa_<cap>.md)")
    args = ap.parse_args()

    cap = args.cap
    en_dir = os.path.join(args.root, "Textos Originais", "txt", "uk", cap)
    ia_dir = os.path.join(args.root, "Textos Traduzidos IA", "txt", "uk", cap)
    hu_dir = os.path.join(args.root, "Textos Traduzidos", "txt", "uk", cap)
    if not os.path.isdir(en_dir):
        print(f"cap dir nao encontrado: {en_dir}", file=sys.stderr)
        return 2

    wfunc = load_widths(
        os.path.join(args.root, "Previewer", "Fontes", "fontevent.nftr")
    )
    if wfunc is None:
        print("aviso: fontevent.nftr nao lido; cheque de largura desativado",
              file=sys.stderr)

    files = sorted(f for f in os.listdir(en_dir) if f.endswith(".lbin.txt"))
    all_findings = []
    total_blocks = 0
    for f in files:
        en_blocks, ffind = check_file(
            os.path.join(en_dir, f),
            os.path.join(ia_dir, f) if os.path.isdir(ia_dir) else None,
            os.path.join(hu_dir, f) if os.path.isdir(hu_dir) else None,
            wfunc,
        )
        total_blocks += len(en_blocks)
        for x in ffind:
            x["file"] = f
            all_findings.append(x)

    fails = [x for x in all_findings if x["sev"] == "FAIL"]
    warns = [x for x in all_findings if x["sev"] == "WARN"]
    # FAIL relevante = exceto glossario/voz INFO; conta tudo FAIL como gate
    report = {
        "cap": cap,
        "files": len(files),
        "blocks_en": total_blocks,
        "fails": len(fails),
        "warns": len(warns),
        "findings": sorted(
            all_findings, key=lambda x: (x.get("file", ""), x.get("line", 0))
        ),
    }
    rpath = args.report or f"qa_{cap}.json"
    with open(rpath, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    # markdown curto
    mpath = args.md or f"qa_{cap}.md"
    cats = {}
    for x in all_findings:
        cats[(x["sev"], x["cat"])] = cats.get((x["sev"], x["cat"]), 0) + 1
    with open(mpath, "w", encoding="utf-8") as fh:
        fh.write(f"# QA cap {cap} — {len(files)} arquivos, {total_blocks} blocos EN\n\n")
        fh.write(f"FAIL={len(fails)} WARN={len(warns)}\n\n")
        fh.write("## Por categoria\n\n")
        for (sev, cat), n in sorted(cats.items()):
            fh.write(f"- {sev}/{cat}: {n}\n")
        fh.write("\n## Achados (FAIL primeiro)\n\n")
        for x in sorted(all_findings,
                        key=lambda v: (0 if v["sev"] == "FAIL" else 1 if v["sev"] == "WARN" else 2,
                                       v.get("file", ""), v.get("line", 0))):
            where = f"{x.get('file','')}:{x.get('line','?')}"
            fh.write(f"- [{x['sev']}/{x['cat']}] {where} "
                     f"({x.get('target','')}) blk{x.get('block','?')}: {x['msg']}"
                     + (f" [{x['rule']}]" if x.get("rule") else "") + "\n")
    print(f"cap {cap}: {len(files)} arqs, {total_blocks} blocos EN, "
          f"FAIL={len(fails)} WARN={len(warns)} -> {rpath}, {mpath}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
