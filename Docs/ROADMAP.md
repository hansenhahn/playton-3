# Roadmap — Tradução PT-BR | Professor Layton and the Unwound Future

> **Última atualização:** 2026-09-20
> **Base:** `master` @ `fa02a5ae`
> **Métrica:** comparação `Textos Originais/txt/uk` × `Textos Traduzidos/txt/uk`
> (e `Textos Originais/rc/nazo/uk` × `Textos Traduzidos/rc/nazo/uk`). Uma unidade
> conta como traduzida quando o PT difere do EN (tags LSCR, headers `[...]` e
> delimitadores `!****!` são ignorados). Unidades curtas idênticas por natureza
> (`Hmm...`, tags de falante) aparecem como "não traduzidas" na métrica bruta.

---

## 1. Visão geral

| Frente | Feito | Total | % |
|---|---|---|---|
| História (caps 00–14) — capítulos | 12 | 15 | **80%** |
| História (caps 00–14) — unidades de texto | 4.198 | 4.915 | **85%** |
| Enigmas (naz_df0–df9) — grupos traduzidos | 10 | 10 | **100%** |
| Enigmas — grupos com QA | 1 (df0) | 10 | **10%** |
| Extras (18/19/20/30/40/50/90/99) | 0 | 8 | **0%** |
| Imagens localizadas | 403 | — | ver §3 |
| Harness / infra | texto + enigma | — | ver §4 |

---

## 2. Textos — capítulo a capítulo

### 2.1 História (00–14)

| Cap | Arquivos | Unid. EN | Tradução | QA |
|---|---|---|---|---|
| 00 | 34 | 283 | ~100% (279/281 blocos) | ✅ #27, #40 |
| 01 | 62 | 495 | 99% | ✅ #30 — caixas #41 aberto |
| 02 | 31 | 359 | 99% | ✅ #31 |
| 03 | 25 | 325 | 98% | ✅ #34 |
| 04 | 26 | 301 | 98% | ✅ #37 |
| 05 | 31 | 317 | 99% | ✅ #39 |
| 06 | 37 | 348 | 99% | ✅ #21 |
| 07 | 52 | 574 | 99% | ✅ #22 |
| 08 | 17 | 149 | 96% | ✅ #23 |
| 09 | 32 | 427 | 98% | ✅ #24 |
| 10 | 47 | 421 | 98% | ✅ #26 |
| 11 | 28 | 257 | ~100% (257/257 blocos) | 🔶 harness PASS — pair review pendente |
| 12 | 21 | 214 | 0% | — |
| 13 | 42 | 309 | 0% | — |
| 14 | 15 | 136 | 0% | — |

### 2.2 Extras

| Cap | Conteúdo | Arquivos | Unid. EN | Tradução |
|---|---|---|---|---|
| 18 | Compendium de Enigmas | 78 | 718 | 0% |
| 19 | Digest / recapitulação | 34 | 93 | 0% |
| 20 | Lost Puzzles / tutoriais / pós-jogo | 60 | 402 | 0% |
| 30 | Tap exploration / hint coins / flavor | 100 | 1.112 | 0% |
| 40 | Journal / Letter from the Future | 17 | 583 | 0%¹ |
| 50 | Epílogo / ending | 39 | 319 | 0% |
| 90 | Stachen / itens | 18 | 105 | 0% |
| 99 | Menus / placeholders | 4 | 23 | 0% |

¹ Arquivos PT existem, mas o conteúdo está em inglês (placeholders).

---

## 3. Enigmas e imagens

| Frente | Feito | Total | % |
|---|---|---|---|
| Enigmas `naz_df0` | traduzido + QA | 22 arq. | ✅ |
| Enigmas `naz_df1`–`df9` | traduzido, **sem QA** | 202 arq. | QA ~0% |
| Imagens `ani/ani` | 52 | 908 orig. | — |
| Imagens `ani/menu` | 187 | 1.131 orig. | — |
| Imagens `ani/nazo` | 99 | 1.440 orig. | — |
| Imagens `bg/img` | 21 | 204 orig. | — |
| Imagens `bg/menu` | 21 | 150 orig. | — |
| Imagens `bg/nazo` | 23 | 737 orig. | — |
| **Imagens localizadas (total)** | **403** | 10.943 orig. uk | ~9% bruto² |

² Percentual bruto engana: a maioria dos originais são sprites/gráficos sem texto.
O número útil é **403 imagens efetivamente localizadas**.

---

## 4. Infra / build

| Item | Status |
|---|---|
| Harness `qa_chapter.py` (texto) | ✅ — fix de largura por caixa no PR #42 |
| Harness `qa_nazo.py` (enigmas) | ✅ #29 |
| Spec / dossiês / glossário / humor | ✅ caps 00–10 + extras 18/19/20/30 |
| Fontes NFTR (`fontevent`, `fontq`, `font18`) | ✅ |
| `create_rom` / `manifest` | ✅ |
| Weekly Puzzles (ASM) | ✅ #25 |

---

## 5. Próximos passos (ordem de impacto)

1. **Caps 12–14** — história final (3 caps / ~659 unidades). Maior vazio narrativo.
2. **QA dos enigmas `naz_df1`–`df9`** (9 grupos) — tradução existe; falta passe
   semântico/voz/gramática do `layton-nazo`.
3. **Extras 18/19/20/30** — traduzir (Spec já existe para todos).
4. **caps 40/50/90/99** — decidir escopo (journal/ending/menus); cap. 40 está
   com placeholder em inglês.
5. **Fechar PRs abertos:** #41 (caixas cap. 01) e #42 (harness).

---

## 6. Histórico de progresso

| Data | Marco |
|---|---|
| 2026-09-20 | Roadmap criado. Caps 00–10 traduzidos e com QA; cap. 00 fechado (PR #40). Enigmas df0 com QA; df1–df9 traduzidos sem QA. Extras e caps 11–14 pendentes. |
| 2026-09-20 | Cap. 11 traduzido (257 blocos) e QA automático (harness PASS); pair review pendente. Caps 12–14 pendentes. |
