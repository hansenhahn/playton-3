# Regras de Tradução — Professor Layton PT-BR (Jogo 3)

> **Vale para todo `playton-3/Textos Traduzidos` e deve manter continuidade com `playton-2/LEIA-ME!.txt:1` Release 1.**
> **Encoding:** `utf-8` sem BOM (igual a `layton.ini:8` e aos arquivos em `Textos Originais`). Nunca salvar com BOM — gera `�`.
> **Preview:** testar sempre em `Previewer/Configs/Screen01.ini` (`fontevent.nftr`, `ScreenNewLine = 16`).

---

## 1. Princípio

Tradução **não-mecânica**: cada personagem tem voz distinta (`Spec/Personagens/*.md`). Se trocar `meu garoto` por `cara`, quebra o Layton. Se trocar `enigma` por `quebra-cabeça`, quebra o `Livro`.

---

## 2. Glossário — PROIBIDO ALTERAR

| EN | PT-BR OBRIGATÓRIO | Prova J2 | Erro comum |
|---|---|---|---|
| `puzzle` | `enigma` | `txt.plz.txt:chr_0:1` `solving puzzles` → `resolver enigmas` (624 ocorrências) | `quebra-cabeça` só para `jigsaw` físico (`nazo2.plz.txt`) |
| `Puzzle Index` | `Livro de Enigmas` | `txt2.plz.txt:tx_204:1` → `foi enviado ao Livro de Enigmas!` | `Índice de Enigmas` |
| `hint coin` | `moeda de dica` | `tobj.plz.txt:hintcoin.txt:1` `You got a hint coin!` → `Você encontrou uma moeda de dica!` | `moeda de pista` |
| `hint` | `dica` | `ev_t10.plz.txt:t10_080_100.gds:1` `fancy a hint` → `daria tudo por uma dica` | `pista` |
| `gentleman` | `cavalheiro` | `ev_t15.plz.txt:t15_020_500.gds:1` `A gentleman never...` → `Um cavalheiro jamais...` | `cavalheiro` com `h`? `cavaleiro` |
| `Inspector` | `Inspetor` | `m4_2.txt:1` | `Inspector` |
| `Boss` (título, incl. `Boss Bostro` / `Boss!`) | `Chefe` / `Chefe Bostro` | `02_015100` `Boss Bostro hates kids` → `O Chefe Bostro odeia crianças`; `02_022000` `Boss!` → `Chefe!` | `Boss` residual |
| `Constable Barton` | `Agente Barton` | `chr_21.txt:1` | `Cabo`, `Constable` |
| `Professor Layton` | `Professor Layton` | `ide_4.txt:1` | `Prof.` abreviado |
| `Don Paolo` | `Don Paolo` | `ide_4.txt:1` | `Dom Paulo` |
| `Granny Riddleton` | `Vovó Riddleton` | `chr_71.txt:1` | `Granny`, `Vovó Charada` |
| `Elysian Box` | `Caixa Elísia` | `txt.plz.txt:d_1.txt:5` | `Caixa Elisíaca` |
| `Stylus` | `caneta stylus` / `toque` | `nazo1.plz.txt:n1.dat:1` | `stylus` sozinho, `caneta` |
| `Good thinking!` | `Bem pensado!` | `nazo1.plz.txt` | `Boa ideia!` |
| `Excellent work!` | `Bom trabalho!` | `nazo1.plz.txt` | `Excelente!` (reserve para `Brilliant!`) |
| `hat` (o do Layton, incl. `top hat`, `big hat`) | `cartola` | `01_012040` `matey in the top hat` → `camarada de cartola`; `02_017030` `fine top hat` → `bela cartola` | `chapéu` genérico (só para chapéus que NÃO são o do Layton, ex. `matching hats` dos capangas em `01_012150`) |
| `cap` / `hat` (o do Luke) | `boné` | `01_012040` `what's wrong with my hat?` (Luke) → `o que há de errado com meu boné?` | `chapéu`, `cartola` |
| `garnet` (gema-isca do papagaio + enigmas da maleta `n032`/`n218`) | `rubi` | `04_025132` `I always carry a garnet` → `sempre levo um rubi`; `n032` `red garnet` → `rubi vermelho` | `granada` (lê-se explosivo), `grená` (lê-se cor bordô) |

**Regra de ouro:** se o termo aparece em `Mapeamento_Continuidae_Jogo2_Jogo3.md:2`, copie idêntico.

---

## 3. Voz por personagem — RESUMO

### Layton (`Hershel_Layton.md`)
- **Forma:** `Você teria a bondade...` (`ev_t10:t10_030_800.gds:1`), nunca `pode pegar?` informal.
- **Tiques fixos:** `De fato.` (= `Indeed.`), `Hmm...`, `Meu jovem` (= `my boy` — padronizado; J2 usava `meu garoto` em `ht_tlk.plz.txt:ht_011_3:1` — escolher 1 e manter nos 15 caps), `Todo enigma tem uma resposta.`, `Um cavalheiro jamais/nunca...`, `É isso que um cavalheiro faz.` (`txt.plz.txt:m23_13:1`)
- **Proibido:** `tá`, `cara`, `bora`, `mano`, `a gente`.

### Luke (`Luke_Triton.md`)
- **Forma:** `O que é isso, Professor?` (`ev_t10:t10_030_200.gds:1`), `Pode deixar, Professor! Ahn...` (`ev_t10:t10_030_900.gds:1`), `Olhe, Professor!` (`ev_t11:t11_020_100.gds:1`), `Caramba!` (= `Gosh/Crikey`).
- **Hesitação:** `er...` / `Ahn...` com reticências, não `...` seco.

### Flora (`Flora_Reinhold.md`)
- `Ai! Que susto!` (`ev_t15:t15_020_200.gds:1`), `Quem, eu? Eu estava... er...` (`t15_020_400.gds:1`), `Só desta vez. Mas não me deixem sozinha de novo!` — manter `er...`.

### Don Paolo / Chelmey / Barton
- `Don Paolo` + `arqui-inimigo` (`ide_4.txt:1`), `Layton!` gritado.
- `Bem, meu nome é Inspetor Chelmey.` (`m4_2.txt:1`), `Agente Barton`.
- Barton faminto: `Chomp` → `Nhac` (J3) — manter onomatopeia.

### Mascotes
- `Keh heh heh!` (Stachenscarfen), `Tee hee hoo!` (Mrs. Cogg), `BZZT!/DING DING DING!` (Max) — **nunca traduzir efeito sonoro**.

---

## 4. Regras de estilo

1. **Formalidade:** sempre `você` (701 ocorrências J2), nunca `tu` (0). Layton trata estranhos com `senhor/senhora`, Luke com `Professor` sem artigo.
2. **Pontuação:** manter `!` e `?` do original. `Hmm...` com 3 pontos, `er...` com 3. Não normalizar `...` para `…` (fonte não tem).
3. **Travessão:** não usar. Quebra é `!------------------------------!` (continuação) e `!******************************!` (bloco).
4. **Aspas:** `<''>Caixa de Pandora<''>` → `''Caixa de Pandora''` (duas aspas simples) — não trocar por `“ ”`.
5. **Tags — instruções, não texto:** **todas as tags devem permanecer no texto traduzido, na mesma posição contextual do original, e não contam para o limite de caracteres/largura.** São instruções de jogo: ` <01:00000001><03:10>b1 normal<03:5>NONE<01:00000002><03:24>` (troca de falante/animação), `<W>` / `<W120>` (pausa), `<A>` (animação), `<T>`/`<V>` (bloco), `<K>` (efeito), `<CR>`, `<Q>`, `<J>`, `<S671>` etc. Traduza só o que está **fora** das tags. Ex.: original `<01:00000002><03:9>b1 shout<03:5>NONE<01:00000003><03:26>Is everything all right?!` → traduzido deve ser `<01:00000002><03:9>b1 shout<03:5>NONE<01:00000003><03:26>Está tudo bem com ele?` — tag antes de `Is` continua antes de `Está`. Nunca apagar, mover para fim da frase ou traduzir tag.
6. **Caixa de diálogo — REGRA DURA:** máximo **3 linhas por página** (1 página = 1 bloco entre `!------------------------------!` ou `!******************************!`). Verificado em `playton-2/Textos Traduzidos/plz/event/en/*.plz.txt`: 0 páginas com >3 linhas de diálogo. **Não criar linhas novas além de 3.** Se precisar mais, use nova página (`!------------------------------!`). Tags da regra 5 não contam nas 3 linhas.
7. **Largura — sem quebra de sílaba:** todas as palavras precisam encaixar inteiras na linha. **Proibido hifenizar** (`pala-\nvra`). O motor do DS não hifeniza — quebra só em espaço. Se a palavra não couber, reescreva a frase. Tags não entram na largura.
8. **Tamanho por linha — fonte de largura variável (`fontevent.nftr`):** **não é monoespaçada.** Caracteres finos `i I l L 1 ` `'` `!` `:` `;` ocupam ~4px; médios `a-z` ~6px; largos `W M` ~9px (`est_width` medido em `playton-2/Textos Traduzidos/plz/event/en/*.plz.txt`). Por isso **contagem de caracteres mente** (medir largura **sem tags**):
   - Medido no J2: **P50 = 30 chars (179px), P90 = 36 (212px), P95 = 38 (220px), máximo 44 (261px)** (`ev_t10.plz.txt:t10_030_500.gds:1` `Caro Hershel. Sendo o exímio arqueólogo` = 39 chars/~205px). Linha com muitos `i`/`l` cabe 42-44 chars; linha com `W`/`M` estoura com 32.
   - **Regra prática:** use **orçamento de largura, não de caracteres.** Alvo seguro = **~210px** (≈ 34 chars médios). **34 é média conservadora**, não limite fixo.
   - **Como validar:** `Previewer/Configs/Screen01.ini` (`Texts.png`, `ScreenXPos 9`, `ScreenYPos 141`, `ScreenNewLine 16`) — largura útil ≈ 240px. Teste sempre; se a linha tem `W`/`M`/`m` use 30-32 chars; se tem `i`/`l`/`1` pode ir a 40-42. J2 tem média PT/EN = 1.01 porque tradutores compensaram trocando palavras largas por finas — faça o mesmo (ex.: `investigar` (w=~42px) → `vasculhar` (w=~48px) — pior; prefira `ver` se precisar ganhar pixels).

---

## 5. Regras técnicas

- Salvar como `utf-8` sem BOM (igual a `layton.ini:8` e aos arquivos em `Textos Originais`).
- Não deixar `puzzle`, `hint coin`, `Inspector` em inglês no `Textos Traduzidos` — grep deve retornar 0.
- Manter `...` e `<W>` (pausa) — não remover `<W>` de `ev_t10:t10_030_501.gds:1`.

---

## 6. Checklist antes de commit

- [ ] `enigma` 100% (grep `quebra-cabeça` deve dar 0, exceto `jigsaw`)
- [ ] `Livro de Enigmas` (não `Índice`)
- [ ] `moeda de dica` (não `moeda de pista`)
- [ ] `Inspetor`/`Agente`/`Vovó Riddleton`/`Don Paolo`
- [ ] Layton sem gíria; `De fato.` / `Meu jovem` / `Um cavalheiro` fixos
- [ ] Luke `Professor!` / `Pode deixar, Professor!` / `Caramba!`
- [ ] Placeholders intactos
- [ ] **3 linhas por página** (grep `!------------------------------!` conta) — nenhuma página >3
- [ ] **Nenhuma linha > ~210px** (≈ 34 chars médios; 38 = P95, 44 = máx com `i`/`l`) — `python3 est_width(linha_sem_tags) <= 210` e sem `palavra-\n` hifenizada. Linha com `W`/`M` deve ter ≤32 chars; com `i`/`l` pode até 42. **Tags não contam**
- [ ] **Toda palavra encaixa inteira** — testar no `Previewer/Screen01` (`Texts.png`); se estourar, reescrever, não forçar quebra
- [ ] `utf-8` sem BOM, sem `�`

---

## 7. Exemplos — CORRETO / INCORRETO

**CORRETO (J2):**
> `Comporte-se, Luke. Um cavalheiro jamais força uma dama a falar mais do que ela quer.` (`ev_t15:t15_020_500.gds:1`)

**INCORRETO:**
> `Se comporta, Luke. Um cavalheiro nunca força uma mina a falar.` — gíria, perde época.

**CORRETO:**
> `Você encontrou uma moeda de dica!` (`tobj.plz.txt:hintcoin.txt:1`)

**INCORRETO:**
> `Você ganhou uma hint coin!` — inglês residual.

**CORRETO (caixa 3 linhas, variável, sem hífen):**
> `Caro Hershel. Sendo o exímio` (23 chars, ~132px)  
> `arqueólogo que sei que é, estou` (31 chars, ~182px)  
> `certo de que está a par desse` (29 chars, ~168px) — `ev_t10.plz.txt:t10_030_500.gds:1` — 3 linhas, palavra inteira, <210px

**INCORRETO (caixa):**
> `Caro Hershel. Sendo o exímio arqueólogo` (39 — estoura P95)  
> `que sei que é, estou certo de que está` (38 — limite)  
> `a par desse objeto chamado Caixa` (32)  
> `Elísia.` (7 — 4ª linha criada) — **proibido**: criou 4ª linha. Reescreva ou quebre em nova página `!------------------------------!`.

**INCORRETO (hifenização):**
> `Você encontrou uma moeda de di-`  
> `ca embaixo do conjunto!` — motor não hifeniza, corta `di-`; escreva `moeda de dica` inteira na linha seguinte.

---
*Baseado em `Analise_Traducao_Jogo2.md` e `Mapeamento_Continuidae_Jogo2_Jogo3.md`. Dúvida? Abrir `Textos Originais` ↔ `Textos Traduzidos` lado a lado no par citado.*
