---
name: layton-nazo
description: Use ao revisar, validar ou corrigir os enigmas (nazo) PT-BR de Professor Layton (playton-3) — preservação da resposta, tokens {#X}, estrutura lbin, largura fontq, teto de linhas, voz do falante vs dossiê e termos fixos (cartola/boné/Família). Aciona com enigma, nazo, revisar enigma, corrigir enigma, puzzle, dica, super dica, resposta do enigma, qa_nazo.
---

# Skill de QA — Enigmas (nazo)

Skill de **segunda iteração** para os 224 enigmas de Professor Layton PT-BR. Pressupõe que `Textos Traduzidos/rc/nazo` já está traduzido e atua como **revisor técnico-semântico**: o objetivo não é estilo, é garantir que **o enigma continue solucionável**.

> **Princípio:** um enigma traduzido errado não é "feio", é **quebrado**. Se um número, dia, cor, direção, ordem ou referência (`{#A}`) muda, o jogador não resolve ou resolve por engano. Toda decisão de revisão é subordinada à preservação da **resposta e das condições**.

> **Fidelidade semântica — nem mais, nem menos:** o enigma PT deve ter **o mesmo sentido** do original. Não é tradução literal, mas é proibido **acrescentar** fala, regra, dica ou condição que o EN não tem e **omitir** o que ele tem. Ex.: em `n160`, o PT antigo inventou na *pergunta* a regra de girar/virar (que só existe no bloco *erro* e na *dica 1*) e apagou o aviso `not to scale`.
>
> **Compreensão > literalidade:** a fidelidade se subordina ao entendimento. Quando a construção do EN for **trava-língua, ambígua ou de ordem impossível em PT** (ex. `n010`: *yesterday's day after tomorrow* / *tomorrow's day before yesterday*), é lícito **reordenar/parafrasear** para que o jogador entenda — desde que a **resposta e as condições fiquem idênticas** e nada seja acrescentado ou omitido. O que não se admite é o 1:1 ilegível que atrapalha a leitura do enigma.
>
> **Voz ≠ invenção:** localizar o sotaque pelo dossiê (escocês→caipira `ocê/ocês`, cockney, etc.) é **obrigatório** e **não** é conteúdo inventado. Conteúdo inventado é criar fala/regra/dica inexistente no original. Se o dossiê não cobre o falante, não invente sotaque: registre "falante não mapeado".

## Quando usar

- `enigma`, `nazo`, `puzzle`, `dica`, `super dica`, `revisar enigma`, `corrigir enigma`, `resposta do enigma`, `qa_nazo`
- Edição de `Textos Traduzidos/rc/nazo/uk/naz_df0..9/*.lbin.txt` comparando com `Textos Originais`
- Validação pré-`create_rom` dos enigmas

## Fontes de verdade

Compartilhadas (não duplicar — ler a fonte):

1. **Glossário e regras gerais:** `Spec/REGRAS_TRADUCAO.md` — `enigma` (nunca `quebra-cabeça`, salvo `jigsaw`), `Livro de Enigmas`, `moeda de dica`, frases fixas `Bem pensado!` (`Good thinking!`), `Bom trabalho!` (`Excellent work!`), `Excelente!` (`Brilliant!`), `REGRAS_TRADUCAO.md:32-33`.
2. **Métricas de fonte:** `Spec/Fontes_NFTR.md` — CWDH/CMAP, `adv`, encoding.
3. **Feedback fixo J2→J3:** `Spec/Analise_Traducao_Jogo2.md` (`Bem pensado!`, `Bom trabalho!`).
4. **Voz do falante (quando há fala entre `{''}`):** `Spec/Personagens/_INDICE.md` → dossiê do personagem (`Luke_Triton.md`, `Hershel_Layton.md`, `Bostro_Family.md`, `Secundarios_*.md`, …). O dossiê é a fonte do registro, sotaque e termos fixos; **não** fixe voz nesta skill.

Próprias do enigma (esta skill):

5. **Harness:** `.opencode/scripts/qa_nazo.py` — única ferramenta de medida.
6. **Comandos:** `review-puzzles` (revisão automatizada, corrige in-place) e `analyze-puzzles` (passe final em conversa, relatório + correção in-place após aprovação do usuário).

## Estrutura de um enigma (224/224 arquivos)

Cada arquivo tem **8 blocos** iniciados por uma linha `[...]`, e as linhas `[...]` (header/ponteiro) são **idênticas EN↔PT** — nunca mudam.

| Papel | Prefixo | Tela |
|---|---|---|
| `meta` | `ea0b…` | — (metadado + marcadores `nXXX`, `nXXXa`, `nXXXb`) |
| `question` | `eb0b…` | Screen03 Enigmas |
| `correct` | `ec0b…` | Screen03 |
| `wrong` | `ed0b…` | Screen03 |
| `hint1`/`hint2`/`hint3`/`super` | `ee0b…`/`ef0b…`/`f00b…`/`f10b…` | Screen08 Dicas |

## Tokens de controle `{...}`

- **Funcionais** (sumir/mudar = `FAIL`): `{#A}`…`{#E}` (referência a elemento/peça), `{po}` (símbolo de libra `£`), `{.}` (marcador de lista).
- **Estilísticos** (`INFO`): `{''}` (aspas) e `{9}` (apóstrofo, ex. `That{9}s right!`).
- Tokens **não contam** na largura: decodifique para um caractere antes de medir (`{...}`→`"`).

## Harness obrigatório (não inferir — executar)

```
python3 .opencode/scripts/qa_nazo.py --df N     # gera qa_nazo_dfN.json + .md
python3 .opencode/scripts/qa_nazo.py --all
python3 .opencode/scripts/qa_nazo.py --verify-font
```

Mecaniza: nº de blocos/marcadores/linhas `[...]` idênticas; tokens funcionais; tags (`<CR>`/`</C>`); encoding `U+FFFD`; glossário; hifenização; **largura real** via `fontq.nftr` (**hard 230px / safe 210px**); **nº de linhas** vs teto; números EN omitidos; dias da semana (`FAIL`) e cores (`WARN`); watchlist de termos críticos.

> **Ponto cego:** o harness **não** mede voz/registro nem termos fixos (`cartola`/`boné`, `Família` capitalizado, `Chefe`, sotaques). Esses dependem de leitura manual + dossiê — ver *Voz de personagem e termos fixos*.

### Largura — como é medida (auditado)

`decode_font` lê CWDH/CMAP do próprio `.nftr`: o avanço é o **3º byte do CWDH** (`cw[idx][2]`, coluna `Total`) e o CMAP começa em **`+16`**. `L+W+R` **não** é o avanço. `--verify-font` confere **147/147** glifos de `fontq` e `fontevent` contra `Spec/Fontes_NFTR.md`. Fallback = 4px para glifo não mapeado.

### Linhas — teto real da caixa

Derivado dos fundos + Configs (`NewLine 12`):

- **Screen03** (`Puzzle.png`, texto em `YPos 22`): **14 linhas** (pergunta/acerto/erro).
- **Screen08** (`Hints.png`, texto em `YPos 42`): **12 linhas** (dicas/super dica).

Os Originais respeitam exatamente esse teto. PT **> teto** = `WARN`; PT **> EN mas ≤ teto** = `INFO`.

## Voz de personagem e termos fixos (manual)

O harness não vê isto — leia os blocos com fala entre `{''}` e confira o **dossiê do falante** (`Spec/Personagens/`):

- **Narrador** (`ナレーション`, texto sem aspas de personagem) não tem voz de personagem — não coloquializar nem "caipirizar".
- **Sotaques:** escocês (Craig/Cuthbert) → caipira/interior leve (`ocê/ocês`, `viu?`, `bão` só afirmação, `briga`, `Quê?!`), **nunca** manter fonética `Ah/ye/nae/doon` (`Humor_Inventario.md:86`, `Secundarios_FutureLondon.md:69-72`); cockney (Bostro/Family) → urbano coloquial, sem formalizar (`Bostro_Family.md:45-47`); Layton → formal culto, frases completas, sem gíria (`Hershel_Layton.md:18-20,45`); Luke → oralidade infantil natural (`tá/pra/né`), sem gíria pesada (`Luke_Triton.md:18,46`).
- **Termos fixos de chapéu:** Layton → **`cartola`** (`REGRAS_TRADUCAO.md:34`); Luke → **`boné`** (`REGRAS_TRADUCAO.md:35`); chapéus de terceiros → `chapéu`. Um `hat` do Luke traduzido `chapéu` é defeito.
- **Organização:** `Family` → **`Família`** capitalizado (`Bostro_Family.md:48`); `Boss` → **`Chefe`**.
- **Localizar o sotaque conforme o dossiê é requisito** (não é invenção de conteúdo). O que é defeito: sotaque/localização ausente ou fora do dossiê. O que é proibido: acrescentar fala/regra/dica que o EN não tem (ver *Fidelidade semântica*).
- **Escopo:** divergência de voz/registro que descaracteriza o falante é achado (gravidade média/alta). Se o dossiê não cobrir o falante, registre como **"falante não mapeado"** e pergunte — nunca invente sotaque.

## Taxonomia de falha

| Categoria | Exemplos | Gravidade |
|---|---|---|
| `estrutura` | bloco/marcador/`[...]` divergente | FAIL |
| `referencia` | `{#A}`/`{po}`/`{.}` perdido | FAIL |
| `tecnico` | tag, `U+FFFD`, hifenização, largura `>230`, linhas `>teto` | FAIL/WARN |
| `glossario` | `quebra-cabeça`, frase fixa divergente, `cartola`/`boné`, `Família`/`Chefe` | FAIL/WARN |
| `resposta` | dia omitido/trocado, número omitido, cor divergente, direção invertida | FAIL/WARN/INFO |
| `voz` | registro/sotaque fora do dossiê do falante (ex. Craig neutro, Luke com `chapéu`) | WARN (manual) |

## Protocolo de análise crítica (obrigatório)

Para cada par `Originais ↔ Textos Traduzidos`, leia **pergunta + acerto + erro + 4 dicas** e responda:

1. **A resposta é a mesma?** dia, cor, número, direção, ordem/posição e referências `{#X}`/A-B-C-D.
2. **Alguma condição foi invertida, omitida ou inventada?** negação, `at least`/`exactly`, `clockwise`/`anticlockwise`, `before`/`after`, `double`/`half`, `odd`/`even`, `more`/`less`; e regra/dica/fala que o EN **não** tem.
3. **A dica conduz à resposta certa?** dica ambígua que induz erro é defeito.
4. **O feedback de acerto/erro mantém o sentido?** não precisa casar palavra a palavra.
5. **Cabe na caixa?** largura `fontq` e teto de linhas.
6. **Tokens/tags preservados?**
7. **Tem fala de personagem (`{''}`)?** Confira o **dossiê do falante** — registro, sotaque e termos fixos (`cartola`/`boné`, `Família`) — ver seção *Voz de personagem e termos fixos*.

Nunca julgue a frase isolada: o número na dica só faz sentido com a pergunta; a cor no acerto só faz sentido com o enunciado.

## Passe gramatical obrigatório (auto-correção, sem discussão)

> **Regra:** gramática é **no-brainer**. Todo desvio gramatical é **corrigido automaticamente**, não vira item de discussão. O relatório registra "já corrigido", nunca "proposta". A fonte da lista é `Spec/REGRAS_TRADUCAO.md` → *“Gramática PT-BR — correção automática”*.

O passe é **obrigatório duas vezes**:
1. **No fim da revisão autônoma** (`review-puzzles`), antes de entregar ao humano.
2. **No fim do passe interativo** (`analyze-puzzles`), **depois** de aplicar as correções aprovadas — edits e reflows introduzem erros novos.

Cobre, no mínimo: regência/crase (`chegar a/ao/à`, `páreo para`, `De que cor`, `olhar as`, `deslizar até`, `aplicar-se a`), subjuntivo após `supondo que`/`talvez`/`embora`, concordância verbal/nominal (sujeito composto → plural), gênero não inventado (`C deve ser o segundo`), ordem de advérbios (`que juntos formam`), `embaixo`, dupla negativa, `já que` causal, **continuidade de falas repetidas** (mesmo trecho EN `{''}` → PT idêntico), **naturalidade/não-literalidade** (EN literal não justifica PT-BR mecânico; calque/pleonasmo/idiom achatado = defeito) e voz do narrador (bloco sem falante não coloquializa).

## Reportar ≠ corrigir

Preservar estilo **não** autoriza omitir do relatório. **Todo** desvio — de fidelidade (adição/omissão/inversão), gramática/ortografia, voz/registro ou rótulo — deve ser **REPORTADO**, ainda que de gravidade baixa; só a **CORREÇÃO** é subordinada à solvabilidade e à aprovação do usuário. `gate=PASS`/`FAIL=0` **não** significa "sem achados": o harness cobre só o mecanizável.

- Varredura **bloco a bloco** via `qa_nazo.py --df N --exhaustive` (`qa_nazo_dfN.audit.md`), com veredito nas 7 dimensões do protocolo.
- **Priorizar só ordena; não filtra.** Tabela completa primeiro, síntese depois.
- Armadilhas que costumam escapar: `ou`↔`e`; `unknown`/`probably`→certeza; `only`/`at least`/`exactly` perdidos; palavras adicionadas (`ao redor`, `ou estranha`); interjeições omitidas; gênero/número inventado (`a nadadora C`); plural/subjuntivo (`18 ano`, `Embora vemos`); idiom→literal; regionalismo onde o EN é neutro.

## O que corrigir vs. preservar

- **CORRIGIR:** omissão/inversão de resposta (dia/cor/número/direção), **conteúdo inventado** (regra/dica/fala que o EN não tem), **omissão** de conteúdo do EN, token funcional perdido, tag/token quebrado, glossário (incl. `cartola`/`boné`, `Família`, `Chefe`), voz/registro fora do dossiê, largura `>230px`, hifenização, `�`, linhas acima do teto.
- **PRESERVAR:** paráfrase fluente em PT natural que mantém o **mesmo sentido e resposta**; **reordenação/paráfrase de trava-língua ou construção ambígua** (`n010`) que preserve resposta e condições; sinônimo de feedback aceitável; **sotaque localizado pelo dossiê** (requisito, não invenção); estilo do tradutor.

## Saída esperada

Cite `arquivo:linha` + regra (ex. `REGRAS_TRADUCAO.md:32`, `Fontes_NFTR.md:4`, teto 14/12, dossiê do falante). Liste arquivos tocados, nº de fixes por categoria (estrutura/token/técnico/glossário/resposta/voz) e se a estrutura permanece idêntica aos Originais. Se houver divergência que dependa da imagem do enigma (ex. cor do objeto) ou de falante sem dossiê, registre como ambiguidade — nunca invente.
