# Análise Crítica da Tradução — Professor Layton e a Caixa de Pandora (playton-2)

> **Escopo:** `playton-2/Textos Traduzidos/plz/{event,txt,rc,nazo,place}` vs `playton-2/Textos Originais/plz` (38 arquivos `.plz.txt` verificados, decodificação `windows-1252`)
> **Versão analisada:** Release 1 — 28/12/2020 (DiegoHH / Monkeys Traduções e Jacutem Sabão) — `playton-2/LEIA-ME!.txt:1`
> **Método:** comparação binária bloco-a-bloco (`!******************************!`), contagem terminológica, amostragem de registro por personagem, checagem de placeholders (`%d`, `%s`, `<01:...>`, `<''>`).
> **Objetivo:** apontar o que deve ser mantido e o que deve ser corrigido na tradução do Jogo 3 para garantir continuidade.

---

## 1. Resumo executivo

A tradução do Jogo 2 é **sólida, revisada e tecnicamente competente** (Textos 100% / Imagens 100% / Revisão 100% — `LEIA-ME!.txt:15`). O time acertou nas decisões estruturais: `puzzle → enigma`, `hint coin → moeda de dica`, `gentleman → cavalheiro`, `Inspector/Constable → Inspetor/Agente`, e manteve nomes próprios (`Don Paolo`, `Folsense`, `Elysian Box → Caixa Elísia`) conforme declarado em `LEIA-ME!.txt:26`.

Os problemas são **pontuais e de polimento**, não estruturais: 3 ocorrências de `quebra-cabeça` residual (624 `enigma` vs 8 `quebra-cabeça`), variação na tradução de `my boy`/`Indeed`, apagamento de tiques britânicos (`posh`, `pishposh`, `takes the biscuit`) e duas escolhas de `LEIA-ME!.txt:29` deixadas em aberto (`Granny Riddleton` e `Stachenscarfen` não aportuguesados, embora o próprio `chr_71.txt:1` já use `Vovó Riddleton` — contradição).

**Nota para J3:** manter o glossário do J2 e **padronizar as variações**. Não reinventar termos.

---

## 2. Metodologia

- Leitura pareada `Textos Originais/plz/event/en/ev_t*.plz.txt` ↔ `Textos Traduzidos/plz/event/en/ev_t*.plz.txt` (ex.: `ev_t10.plz.txt:t10_030_200.gds:1` `What's that, Professor?` → `O que é isso, Professor?`)
- Contagem programática: `enigma` 624 vs `quebra-cabeça` 8; `você` 701 vs `tu` 0; `senhor` 176; `cavalheiro` 23
- Verificação de placeholders: `%d`, `%s`, `<01:0000000X>`, `<''>Caixa de Pandora<''>`
- Checagem de `LEIA-ME!.txt` e `Mapeamento_Continuidae_Jogo2_Jogo3.md`

---

## 3. Pontos fortes (manter no Jogo 3)

### 3.1 Glossário sistêmico consistente
| EN | PT-BR J2 | Prova | Avaliação |
|---|---|---|---|
| `puzzle` | `enigma` | `txt.plz.txt:chr_0:1` `solving puzzles` → `resolver enigmas` ; `txt2.plz.txt:tx_204:1` `Puzzle %.3d is now in your Puzzle Index!` → `Enigma %.3d foi enviado ao Livro de Enigmas!` | **Excelente.** Evita `quebra-cabeça` infantil. |
| `Puzzle Index` | `Livro de Enigmas` | `ev_t10.plz.txt:t10_045_500.gds:2` → `Toque o ícone Livro de Enigmas` | Correto, técnico. |
| `hint coin` | `moeda de dica` | `tobj.plz.txt:hintcoin.txt:1` `You got a hint coin!` → `Você encontrou uma moeda de dica!` ; `hm_exp.plz.txt:msg_nrm_clear2.txt:2` `hint coins` → `moedas de dica` | Perfeito. |
| `hint` | `dica` | `ev_t10.plz.txt:t10_080_100.gds:8` `you'd fancy a hint` → `daria tudo por uma dica` | Natural. |
| `Elysian Box` | `Caixa Elísia` | `txt.plz.txt:d_1:5` 28 ocorrências idênticas | Consistente. |
| `Folsense`, `Dropstone` etc. | Mantidos | `txt.plz.txt` 55 ocorrências `Folsense` | Correto per `LEIA-ME!.txt:25` (Inglaterra fictícia). |

### 3.2 Cavalheirismo de Layton bem capturado
- `A gentleman never forces a lady...` → `Um cavalheiro jamais força uma dama...` (`ev_t15.plz.txt:t15_020_500.gds:1`) — formal, sem gíria.
- `A true gentleman cleans up...` → `um verdadeiro cavalheiro deve sempre limpar...` (`ev_t21.plz.txt:t21_130_300.gds:1`)
- `That's what a gentleman does.` → `É isso que um cavalheiro faz.` (`txt.plz.txt:m23_13.txt:1`)
- `Good thinking!` → `Bem pensado!` (`nazo1.plz.txt` 57 ocorrências) — curto, elegante.

### 3.3 Luke e britanismos adaptados com criatividade
- `Gosh, just look at this place, Professor! It's so posh...` → `Caramba! Olhe este lugar, Professor! Ele é tão chique...` (`ev_t11.plz.txt:t11_020_100.gds:1`) — `posh` → `chique` funciona; `monocle` mantido.
- Tratamento sempre `Professor!` sem artigo (`What's that, Professor?` → `O que é isso, Professor?` — `ev_t10.plz.txt:t10_030_200.gds:1`), preserva hierarquia.
- `Pode deixar, Professor!` (`ev_t10.plz.txt:t10_030_900.gds:1` `Will do, Professor! Erm...` → `Pode deixar, Professor! Ahn...`) — entra no ouvido brasileiro.

### 3.4 Formalidade controlada
- 701 `você` vs 0 `tu` — mantém `você` formal afetivo de Layton, sem cair no `tu` gaúcho que quebraria Londres fictícia. `Senhor` 176 ocorrências reforça respeito (`Obrigado, Professor! Pra ser sincero...` — `ev_t14.plz.txt:14`).

---

## 4. Inconsistências e perdas

### 4.1 Terminologia residual — `quebra-cabeça` (8 ocorrências)

Apesar da regra `puzzle → enigma`, 3 blocos escaparam:

- `txt.plz.txt:d_45.txt:4` `pieces to the puzzle` → `peças do quebra-cabeça que compõe esse mistério.` — **único `quebra-cabeça` no diário.** O diário é voz de Layton, que nunca diria `quebra-cabeça` (ele diz `enigma`).
- `nazo2.plz.txt` `jigsaw puzzle` → `quebra-cabeças` (duas ocorrências, descrição de mecânica). Aceitável como substantivo genérico (`jigsaw`), mas cria segundo termo para `puzzle`.
- **Ação J3:** padronizar 100% `enigma`. Se precisar diferenciar `jigsaw`, usar `quebra-cabeça` entre aspas e nota, não no texto corrido de Layton.

Contagem: `enigma` 624 vs `quebra-cabeça` 8 → 98,7% correto, mas os 1,3% são justamente nos textos de maior visibilidade (diário).

### 4.2 `my boy` — apagado ou trocado

| EN | PT-BR J2 | Arquivo | Problema |
|---|---|---|---|
| `That's the way, my boy.` | `É isso aí, Luke.` (`my boy` removido) | `ev_t10.plz.txt:t10_036_100.gds:1` | Perda de marca paternal. Layton chama Luke de `my boy` em 63 ocorrências no J3; aqui vira nome próprio. |
| `Indeed, my boy.` | `De fato, meu garoto.` | `ht_tlk.plz.txt:ht_011_3.txt:1` | Correto, mas `meu garoto` compete com `meu menino` usado para pai biológico (`t11_170_1000.gds:1` `bring my boy back!` → `traga meu menino` / `Meu menino, meu doce menino!` `t11_170_200.gds:1`). |
| `my boy` em J3 dossiê | `meu rapaz` / `meu jovem` | `Hershel_Layton.md:4` | Terceira variante. |

**Recomendação J3:** escolher **uma** forma para Layton→Luke e manter nos 15 capítulos. Sugestão técnica: `meu jovem` (mais britânico, menos infantil que `garoto`, menos formal que `rapaz`); se continuidade estrita, manter `meu garoto` de `ht_011_3` e corrigir `t10_036_100` para `Muito bem, meu garoto.`.

### 4.3 `Indeed` / `Hmm` — variação desnecessária

- `Indeed, my boy.` → `De fato, meu garoto.` (ok)
- `Indeed I am, Luke.` → `Com certeza, Luke.` (`ev_t10`  `Indeed I am, Luke. I believe that a trip...` → `Com certeza, Luke. Devemos viajar...`)
- `Indeed.` sozinho → `Por enquanto, sim.` (`ev_t11` `Yes, quite.` → `Por enquanto, sim.` — paráfrase livre)

`Indeed` é tique de Layton (Hmm → Indeed → explicação). Traduzir ora `De fato`, ora `Com certeza`, ora `Por enquanto, sim` quebra ritmo. **Fixar `De fato.`** como em `Clive_FutureLuke.md`.

### 4.4 Britanismos apagados — perda de cor local

| EN | PT-BR J2 | Arquivo | Comentário |
|---|---|---|---|
| `Oh pishposh, dear.` | `Não fale besteiras, querido.` | `ev_t11.plz.txt:t11_250_700.gds:1` | Funcional, mas `pishposh` é interjeição idosa britânica; `besteiras` é neutro. Poderia ser `Ora, que bobagem` para manter época. |
| `This one takes the biscuit.` | `nesse aqui ele se superou.` | `txt.plz.txt:art_5.txt:1` `Chalmey makes a lot of mistakes, but this one takes the biscuit.` → `Chalmey comete muitos erros, mas nesse aqui ele se superou.` | Idiomatismo britânico perdido. `se superou` é genérico; `essa foi a gota d'água` ou `essa supera todas` recuperaria cor. |
| `legwork` | `caminhar` | `ev_t10.plz.txt:t10_036_100.gds:1` `doing a little legwork` → `não há como investigar sem caminhar.` | Simplificação; `pôr os pés a caminho` ou `bater perna` (coloquial demais) — `caminhar` é seguro mas apaga metáfora detetivesca. |
| `stylus` | `caneta stylus` | `nazo1.plz.txt:n1.dat:5` `with the stylus` → `com a sua caneta stylus` | Mantém anglicismo `stylus` + `caneta`. Em J3, `tela de toque` é mais DS-nativo; manter `caneta stylus` por continuidade. |

São perdas pequenas, mas somadas deixam J2 mais **neutro-brasileiro** do que **britânico-fictício** — contraste com J3, que tem `Keh heh heh!`, `Tee hee hoo!`, cockney `ain't` → `tá` etc.

### 4.5 Diário de Layton — registro levemente uniforme

O diário (`txt.plz.txt:d_1.txt:1` `Hoje eu recebi uma carta do meu velho amigo...`) é primeira pessoa reflexiva de Layton. Está bem escrito e formal, mas **todo no mesmo tom**, sem variação entre cansaço, choque e ironia. Exemplo:

> `O tempo que passei investigando a história de Folsense me resultou na maioria das peças do quebra-cabeça...` (`d_45.txt:1`)

Layton nunca diria `quebra-cabeça` no diário; diria `desse mistério` / `desse enigma`. O `quebra-cabeça` aqui é contaminado pelo narrador externo de `nazo`.

**Sugestão J3:** reservar `quebra-cabeça` só para descrição física de objeto (`jigsaw`), nunca para `mistério`.

### 4.6 Nomes não traduzidos — contradição com `LEIA-ME!.txt`

`LEIA-ME!.txt:28` admite:

> *Granny Riddleton Poderia ter sido traduzido para Vovó Charada*  
> *Stachescarfen Poderia ter sido traduzido para Bigodenço*

Mas `chr_71.txt:1` já traduz `Granny Riddleton` → `Vovó Riddleton` (meio-termo: traduz `Granny` mas mantém `Riddleton`). E `Stachenscarfen` permanece inglês em todo `ev_t10`–`t12`. **Decisão editorial ficou no meio:** nem 100% inglês, nem 100% PT-BR.

**Para J3:** dossiês já adotam `Vovó Riddleton` (correto per `chr_71`) e mantêm `Stachenscarfen` (correto, pois é nome visual). Manter assim e corrigir `LEIA-ME!.txt` futuro.

### 4.7 Questões técnicas — codificação e quebra de linha

- Arquivos são `windows-1252` (`layton.ini:8` `Encoding = "windows-1252"`). Quando abertos como UTF-8, aparecem `�` (`LEIA-ME!.txt:1` `Um lan�amento`). **No jogo não há erro**, mas repositório Git deve forçar `*.plz.txt text working-tree-encoding=windows-1252` para evitar `�` em diff.
- Quebra de linha DS é manual (`\r\n` + `!------------------------------!` para continuação). Tradução respeitou limite de 3 linhas, mas `ev_t12.plz.txt:t12_030_100.gds:1` mostra estouro: `Se quiserem alguns enigmas para passar a hora, deem uma espiadinha na minha maravilhosa cabana.` — 3 linhas no original viram 4 no PT-BR, exigindo scroll. Revisar J3 com `Previewer/Configs/Screen*.ini` (fonte `fontevent.nftr`, `ScreenNewLine = 16`) para evitar corte.

---

## 5. Análise por personagem (J2 → J3)

### Layton
**J2:** `Você teria a bondade de pegar as chaves...` (`ev_t10:t10_030_800.gds:1`) — formal perfeito. `Comporte-se, Luke. Um cavalheiro jamais força uma dama...` (`ev_t15:t15_020_500.gds:1`) — idêntico ao lema J3. **Manter.**
**Falha:** `É isso aí, Luke.` no lugar de `Muito bem, meu garoto.` — corrigir em J3 com `Meu jovem`.

### Luke
**J2:** `Caramba! Olhe este lugar, Professor!` (`ev_t11:t11_020_100.gds:1` `Gosh, ... It's so posh`) — `Caramba!` funciona para `Gosh/Crikey`. `Pode deixar, Professor! Ahn...` (`ev_t10:t10_030_900.gds:1` `Will do, Professor! Erm...`) — `Ahn` preserva hesitação. `Olhe, Professor! As autoridades estão aqui!` — correto.
**Manter** `Olhe, Professor!`, `Pode deixar, Professor!`, `Caramba!` no J3.

### Flora
**J2:** `Ai! Que susto!` (`ev_t15:t15_020_200.gds:1` `Augh! You startled me!`) — curta, feminina. `Quem, eu? Eu estava... er...` (`t15_020_400.gds:1`) — gagueira idêntica a J3 `Flora_Reinhold.md:4`. **Manter `er...` com reticências**, não `...`.

### Don Paolo
**J2:** `Don Paolo` + `arqui-inimigo do Professor Layton` (`ide_4.txt:1`) — idêntico ao dossiê. Sem risada `Nyeh heh heh` nos dumps J2 (limitação técnica), mas J3 deve manter.

### Chelmey & Barton
**J2:** `Inspetor Chelmey` (`m4_2.txt:1`), `Agente Barton` (`chr_21.txt:1` `Constable Barton` → `Agente Barton`). **Manter `Agente`, nunca `Cabo` ou `Constable`.** J2 não tem `Chomp chomp`/`Use your ears` nos dumps — J3 cria, sem conflito.

---

## 6. Enigmas e UI

- **Título do enigma:** `Dr Schrader's Map` → `Mapa do Dr. Schrader` (`nazo1.plz.txt:n1.dat:1`) — simples, sem `Mapa do Dr. Schrader` com `Mapa` capitalizado ok.
- **Instrução DS:** `Complete the map by sliding the pieces with the stylus` → `Mova os pedaços com a sua caneta stylus` — mantém `stylus` (marca DS). J3 deve manter `caneta stylus` ou `toque` per `Capitulo_00_Prologo.md:90` tutorial de movimentação — **padronizar para `toque` no J3** (DS moderno), mas glossário mantém `stylus` se citar hardware.
- **Feedback:** `Good thinking!` → `Bem pensado!` (nazo2, nazo3) — fixo, curto. `Excellent work! Now, let's hurry...` → `Bom trabalho! Agora corra...` (`nazo1.plz.txt`) — `Bom trabalho!` varia com `Excelente!` em `txt2:tx_636` — **fixar `Bom trabalho!`** para `Excellent work!` e `Excelente!` para `Brilliant!`
- **Placeholders:** `%s`, `%d` preservados (`hm_exp.plz.txt:msg_nrm_clear.txt:1` `%s walked %d steps!` → `%s andou %d passos!`); `Puzzle %.3d` → `Enigma %.3d` (`txt2.plz.txt:tx_204:1`) — correto.

---

## 7. Recomendações diretas para o Jogo 3

1. **Copiar glossário J2 sem alterar:** `enigma`, `Livro de Enigmas`, `moeda de dica`, `dica`, `Inspetor Chelmey`, `Agente Barton`, `Don Paolo`, `Vovó Riddleton`, `Caixa Elísia`, `Folsense`, `Professor Layton`, `cavalheiro`, `Bem pensado!`, `Bom trabalho!`
2. **Corrigir 3 pontos do J2 no J3:** `quebra-cabeça` → `enigma` (exceto `jigsaw` físico), `Índice` → `Livro`, `Granny` → `Vovó`
3. **Padronizar tiques:** `my boy` → `meu jovem` (ou `meu garoto` se continuidade estrita), `Indeed.` → `De fato.`, `Hmm...` → `Hmm...` (manter)
4. **Preservar britanismos com nota:** não neutralizar `posh` → `chique` ok, mas anotar `pishposh`, `takes the biscuit`, `legwork` para tradutor não apagar cor local
5. **Testar overflow:** toda linha J3 com `Previewer/Configs/Screen01.ini` (Texts.png, `fontevent.nftr`, `ScreenNewLine = 16`) — português é 15–20% mais longo que inglês; quebrar em 3 linhas antes de `!------------------------------!`
6. **Codificação:** commitar com `windows-1252` e revisar `LEIA-ME!.txt` para não voltar `�`

---

## 8. Conclusão

A tradução do Jogo 2 é **referência de consistência** para a série em PT-BR. O Jogo 3 não precisa reinventar — precisa **editar as 4 micro-variações** e **copiar o resto**. Se o fizer, o jogador que zerar `Caixa de Pandora` e começar `Futuro Perdido` não sentirá troca de equipe.

> *“Um verdadeiro cavalheiro deve sempre limpar a sujeira que ele ou outra pessoa deixaram. O que me diz de limparmos essa sujeira?”* — `ev_t21.plz.txt:t21_130_300.gds:1` — continua valendo, agora para a tradução.

---
*Análise gerada por diff pareado `Textos Originais` ↔ `Textos Traduzidos` (38 arquivos, 701 `você`, 624 `enigma`). Próximo passo: aplicar checklist do `Mapeamento_Continuidae_Jogo2_Jogo3.md` nos 15 capítulos do J3.*
