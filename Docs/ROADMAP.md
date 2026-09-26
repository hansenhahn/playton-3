# Roadmap — Tradução PT-BR | Professor Layton and the Unwound Future

> **Última atualização:** 2026-09-25
> **Base:** `master` @ `fef16d4c`
> **Métrica:** comparação `Textos Originais/txt/uk` × `Textos Traduzidos/txt/uk`
> (e `Textos Originais/rc/nazo/uk` × `Textos Traduzidos/rc/nazo/uk`). Uma unidade
> conta como traduzida quando o PT difere do EN (tags LSCR, headers `[...]` e
> delimitadores `!****!` são ignorados). Unidades curtas idênticas por natureza
> (`Hmm...`, tags de falante) aparecem como "não traduzidas" na métrica bruta.

---

## 1. Visão geral

| Frente | Feito | Total | % |
|---|---|---|---|
| História (caps 00–14) — capítulos | 15 | 15 | **100%** |
| História (caps 00–14) — unidades de texto | 4.848 | 4.915 | **99%** |
| Enigmas (naz_df0–df9) — grupos traduzidos | 10 | 10 | **100%** |
| Enigmas — grupos com QA | 1 (df0) | 10 | **10%** |
| Extras (18/19/20/30/40/50/90/99) | 2 | 8 | **25%** |
| Imagens localizadas | 403 | — | ver §3 |
| Harness / infra | texto + enigma | — | ver §4 |

---

## 2. Textos — capítulo a capítulo

### 2.1 História (00–14)

| Cap | Arquivos | Unid. EN | Tradução | QA |
|---|---|---|---|---|
| 00 | 34 | 283 | ~100% (279/281 blocos) | ✅ #27, #40 |
| 01 | 62 | 495 | 99% | ✅ #30 — caixas #41 aberto |
| 02 | 31 | 359 | 99% | ✅ #31 + #53 (revisão manual; caixa validada no Previewer; 2 falso-positivos de tela de enigma aceitos) |
| 03 | 25 | 325 | 98% | ✅ #34 |
| 04 | 26 | 301 | 98% | ✅ #37 |
| 05 | 31 | 317 | 99% | ✅ #39 |
| 06 | 37 | 348 | 99% | ✅ #21 |
| 07 | 52 | 574 | 99% | ✅ #22 |
| 08 | 17 | 149 | 96% | ✅ #23 |
| 09 | 32 | 427 | 98% | ✅ #24 |
| 10 | 47 | 421 | 98% | ✅ #26 |
| 11 | 28 | 257 | ~100% (257/257 blocos) | ✅ #43 — pair review pendente |
| 12 | 21 | 214 | ~100% (205/212 blocos; 7 idênticos por natureza) | 🔶 #44 — pair review pendente |
| 13 | 42 | 309 | ~100% (309/309 blocos) | 🔶 #46 — pair review pendente |
| 14 | 15 | 136 | ~100% (132/136 blocos; 4 idênticos por natureza) | 🔶 este PR — pair review pendente |

### 2.2 Extras

| Cap | Conteúdo | Arquivos | Unid. EN | Tradução |
|---|---|---|---|---|
| 18 | Compendium de Enigmas | 78 | 718 | 0% |
| 19 | Digest / recapitulação | 34 | 93 | ~100% (93/93 blocos) |
| 20 | Lost Puzzles / tutoriais / pós-jogo | 60 | 402 | 0% |
| 30 | Tap exploration / hint coins / flavor | 100 | 1.112 | 0% |
| 40 | Journal / Letter from the Future | 17 | 583 | 0%¹ |
| 50 | Epílogo / ending | 39 | 319 | 0% |
| 90 | Stachen / itens | 18 | 105 | ~100% (105/105 blocos) |
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

1. **História completa (caps 00–14)** — pair review dos caps 11–14 pendente.
2. **QA dos enigmas `naz_df1`–`df9`** (9 grupos) — tradução existe; falta passe
   semântico/voz/gramática do `layton-nazo`.
3. **Extras 18/20/30** — traduzir (Spec já existe para todos).
4. **caps 40/50/99** — decidir escopo (journal/ending/menus); cap. 40 está
   com placeholder em inglês.
5. **Fechar PRs abertos:** #41 (caixas cap. 01); #53 (revisão manual cap. 02).

---

## 6. Histórico de progresso

| Data | Marco |
|---|---|
| 2026-09-20 | Roadmap criado. Caps 00–10 traduzidos e com QA; cap. 00 fechado (PR #40). Enigmas df0 com QA; df1–df9 traduzidos sem QA. Extras e caps 11–14 pendentes. |
| 2026-09-20 | Cap. 11 traduzido (257 blocos) e QA automático (harness PASS); pair review pendente. Caps 12–14 pendentes. |
| 2026-09-20 | Cap. 12 traduzido (212 blocos) e QA semântico/voz (5 correções cirúrgicas); pair review pendente. Caps 13–14 pendentes. |
| 2026-09-20 | Cap. 13 traduzido (309 blocos) e QA semântico/voz/glossário (9 correções cirúrgicas); pair review pendente. Cap. 14 pendente. |
| 2026-09-20 | Cap. 14 traduzido (136 blocos; 132/136, 4 idênticos por natureza) e QA semântico/voz (4 correções cirúrgicas); pair review pendente. História 00–14 completa. |
| 2026-09-20 | Extras 19 (Digest) traduzido (93 blocos) e QA semântico/voz (8 correções cirúrgicas); pair review pendente. Narração neutra. |
| 2026-09-20 | Extras 90 (Stachen/itens/minijogo do papagaio) traduzido (105 blocos) e QA (4 correções de continuidade terminológica); pair review pendente. |
| 2026-09-25 | Cap. 02 — revisão manual (PR #53): QA semântico/voz/tratamento/gramática nos 359 blocos; correções de naturalidade (`está além das minhas habilidades`), tratamento (`o senhor` para Harold/Delroy) e precisão (`por que exatamente`, `carta de espadas`, `mais posso contar?`). Caixa validada no Previewer. Gate do harness fica em 2 FAIL de tela de enigma (`02_020010`), idênticos ao EN — falso-positivo aceito. |
