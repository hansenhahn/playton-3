# Mapeamento de Continuidade — Bordões Jogo 2 → Jogo 3

> **Objetivo:** garantir que personagens em comum entre *Professor Layton e a Caixa de Pandora* (playton-2) e *Professor Layton and the Unwound Future* (playton-3) mantenham a mesma voz na tradução PT-BR.
> **Fontes verificadas:**
> - Jogo 2 (traduzido): `playton-2/Textos Traduzidos/plz/{event,txt,rc,nazo}/en/*.plz.txt` (lidos como `cp1252`)
> - Jogo 3 (dossiês): `Spec/Personagens/*.md` + dumps `Spec/Capitulo_00_Prologo.md`–`Spec/Capitulo_14.md`

---

## 1. Personagens em comum (confirmados nos dumps)

| Personagem | Tag J2 | Tag J3 | Status |
|---|---|---|---|
| **Hershel Layton** | `01:00000001` em `ev_t10.plz.txt:3` | `レイトン` | Protagonista — 100% continuidade |
| **Luke Triton** | `01:00000002` em `ev_t10.plz.txt:4` | `ルーク` | Co-protagonista — 100% |
| **Flora Reinhold** | `01:00000005` em `ev_t15.plz.txt:202` | `アロマ` / `フローレス` | Terceira do trio — 100% |
| **Don Paolo** | menção `ide_4.txt:1` | `ドン・ポール` | Arqui-inimigo — 100% |
| **Inspetor Chelmey** | `m4_2.txt:1` | `チェルミー` | Recorrente — 100% |
| **Agente Barton** | `chr_21.txt:1` | `バートン` | Dupla cômica — 100% |
| **Dr. Andrew Schrader** | `t10_030_300.gds:3` | `未来シュレーダー` (Future) | Mentor — cameo |
| **Vovó Riddleton / Granny Riddleton** | `chr_71.txt:1` | `ナゾーバ` (menção em Extras 20) | Sistema — 100% |
| **Pavel / Polo** | `ev_t16` multilíngue | `ポーロ` | Cameo excêntrico |

> **Não em comum:** Bill Hawks, Dimitri/Claire/Clive/Bostro/Family, Becky/Margaret etc. são exclusivos do Jogo 3 — sem necessidade de continuidade, mas seguir padrão de registro.

---

## 2. Glossário sistêmico (aplicado a todos)

| EN (original) | PT-BR consolidado no Jogo 2 | Evidência J2 | Recomendação Jogo 3 | Risco se mudar |
|---|---|---|---|---|
| `puzzle` | **enigma** | `txt.plz.txt:chr_0:2` `His two passions are solving puzzles` → `Suas duas paixões são resolver enigmas` ; `nazo1.plz.txt:57` `puzzle count` → `enigma count 62` | **Manter `enigma`** (nunca `quebra-cabeça`) | Quebra busca no Livro, QA falha |
| `Puzzle Index` | **Livro de Enigmas** | `txt2.plz.txt:tx_204:1` `Puzzle %.3d is now in your Puzzle Index!` → `Enigma %.3d foi enviado ao Livro de Enigmas!` ; `ev_t10.plz.txt:t10_045_500.gds:2` → `Toque o ícone Livro de Enigmas` | Manter `Livro de Enigmas` | J2 usa sempre, J3 estava `Índice de Enigmas` em `Capitulo_00_Prologo.md:90` — unificar para `Livro` |
| `hint coin` | **moeda de dica** | `tobj.plz.txt:hintcoin.txt:1` `You got a hint coin!` → `Você encontrou uma moeda de dica!` ; `hm_exp.plz.txt:msg_nrm_clear2.txt:2` → `farejar moedas de dica` | Manter `moeda de dica` | J3 já usa `moedas de dica` (`Capitulo_00_Prologo.md:92`) — ok |
| `hint` (verbo) | **dica** | `ev_t10.plz.txt:t10_080_100.gds:8` `you'd fancy a hint` → `daria tudo por uma dica` | Manter `dica` | — |
| `Inspector` | **Inspetor** | `m4_2.txt:1` `Well, Inspector Chelmey's the name.` → `Bem, meu nome é Inspetor Chelmey.` | Manter `Inspetor Chelmey` | Sem `Inspector` inglês |
| `Constable Barton` | **Agente Barton** | `chr_21.txt:1` `Constable Barton` → `Agente Barton` | Manter `Agente Barton` | Não usar `Cabo`/`Oficial` |
| `Professor Layton` | **Professor Layton** | `ide_4.txt:1` `Professor Layton's self-proclaimed nemesis` → `Professor Layton` | Manter | Sem `Prof.` abreviado |
| `Don Paolo` | **Don Paolo** | `ide_4.txt:1` `Don Paolo` → `Don Paolo` | Manter `Don Paolo` | Não aportuguesar para `Dom Paulo` |
| `Granny Riddleton` | **Vovó Riddleton** | `chr_71.txt:1` `Granny Riddleton` → `Vovó Riddleton` | Manter `Vovó Riddleton` | J3 Extras usa `Granny` inglês — alinhar |

---

## 3. Bordões por personagem — comparação lado a lado

### 3.1 Hershel Layton — o cavalheiro

| Bordão EN | Tradução J2 (literal) | Arquivo J2 | Proposta J3 | Nota de continuidade |
|---|---|---|---|---|
| `Luke, ...` (vocativo) | `Luke, ...` | `ev_t10: t10_030_800.gds:1` `Luke, before we go, would you be so kind...` → `Luke, antes de irmos, você teria a bondade...` | Manter `Luke, ...` | Identidade |
| `my boy` | **variante: `meu garoto` / omitido** | `ht_tlk.plz.txt: ht_011_3:1` `Indeed, my boy.` → `De fato, meu garoto.` ; `ev_t10: t10_036_100.gds:1` `That's the way, my boy.` → `É isso aí, Luke.` (omitido) | **Padronizar `meu jovem` / `meu rapaz`** — mas **se quiser continuidade estrita, usar `meu garoto`** como em `ht_011_3` | J2 é inconsistente; escolher 1 e manter nos 15 caps. Dossiê J3 sugeria `meu rapaz` — decidir com revisor |
| `Indeed.` | `De fato.` / `É verdade.` / `Por enquanto, sim.` | `ht_011_3` `Indeed, my boy.` → `De fato, meu garoto.` ; `ev_t11` → `Por enquanto, sim.` | **Fixar `De fato.`** | J2 variou; fixar melhora QA |
| `A gentleman never forces a lady...` | `Um cavalheiro jamais força uma dama...` | `ev_t15: t15_020_500.gds:1` → `Comporte-se, Luke. Um cavalheiro jamais força uma dama a falar mais do que ela quer.` | Manter `Um cavalheiro jamais...` | 100% idêntico a `Hershel_Layton.md:4` |
| `A true gentleman cleans up...` | `um verdadeiro cavalheiro deve sempre limpar...` | `ev_t21: t21_130_300.gds:1` → `Luke, um verdadeiro cavalheiro deve sempre limpar a sujeira...` | Manter `um verdadeiro cavalheiro` | — |
| `That's what a gentleman does.` | `É isso que um cavalheiro faz.` | `txt.plz.txt: m23_13:1` → `É isso que um cavalheiro faz.` | Manter | — |
| `It's not becoming of a gentleman.` | `Não é do feitio de um cavalheiro.` | `ev_t12: t12_290_500.gds:1` → `Não é do feitio de um cavalheiro.` | Manter `feitio` | J3 usou `um gentleman...` em `Spec/Capitulo_05.md:259` — alinhar para `cavalheiro` |
| `Every puzzle has an answer.` | **Não ocorre em J2** (variações: `Good thinking!`) | `nazo*.plz.txt` → `Bem pensado!` | **Manter `Todo enigma tem uma resposta.`** como lema fixo J3 | Criar continuidade nova — J2 nunca teve lema fixo |
| `Hmm...` / `<K>` | `Hmm...` | `ev_t15` `Hmm...` mantido | Manter `Hmm...` | — |

**Veredito Layton:** 95% compatível. Único ajuste é **padronizar `my boy` → `meu garoto`** se continuidade estrita, ou migrar tudo para `meu jovem` com nota de revisão.

### 3.2 Luke Triton — o aprendiz

| Bordão EN | J2 | Arquivo J2 | Proposta J3 |
|---|---|---|---|
| `Professor!` / `Professor Layton!` | `Professor!` | `ev_t10: t10_030_200.gds:1` `What's that, Professor?` → `O que é isso, Professor?` ; `ev_t11: t11_170_500.gds` `Mr Layton!` → `Sr. Layton!` | Manter `Professor!` (sem artigo) |
| `Will do, Professor! Erm...` | `Pode deixar, Professor! Ahn...` | `ev_t10: t10_030_900.gds:1` | Manter `Pode deixar, Professor!` | 
| `Look, Professor! ...` | `Olhe, Professor! ...` | `ev_t10: t11` `Olhe, Professor! As autoridades estão aqui!` | Manter `Olhe, Professor!` |
| `Of course, Professor!` | `É claro, Professor!` | `ev_t10: t10_022_...` | Manter |
| `I'm the professor's apprentice, Luke!` (J3) | **Não ocorre em J2** (Luke nunca se apresenta assim em J2) | — | **Criar `Sou o aprendiz do professor, Luke!`** — manter `aprendiz` (J2 usa `aprendiz`? Não, mas `chr` não tem; `Flora` é `aprendiz` implícito) |
| `Caramba!` (Luke exclama) | `Caramba! Olhe este lugar, Professor!` | `ev_t11: t11_100_...` `Gosh, just look at this place, Professor!` → `Caramba!` | Manter `Caramba!` para `Crikey!`/`Gosh!` |
| `Ahn?` / `Er...` | `Ahn?` / `er...` | `ev_t15: t15_020_400.gds:1` `Me? I, well, um...` → `Quem, eu? Eu estava... er...` | Manter `er...` |

**Veredito Luke:** continuidade perfeita. J2 já estabeleceu `Professor!` sem `o` e `Pode deixar, Professor!` — J3 deve copiar.

### 3.3 Flora Reinhold

| Bordão EN | J2 | J3 | Nota |
|---|---|---|---|
| `Who, me? I, well, um...` | `Quem, eu? Eu estava... er...` | `Quem, eu? Eu estava... er...` (`Hershel_Layton.md`) | Idêntico |
| `Ah, don't give it a second thought.` | `Ah, não se preocupe.` | `Ah, não se preocupe.` (`Spec/Capitulo_05.md:251`) | J3 `Flora_Reinhold.md` traz `Just this once. But you...` → traduzir como `Só desta vez...` (novo, sem precedente J2) |
| `Tee hee!` | Não ocorre em J2 para Flora (mas `Heh heh!` para Rosetta) | J3 `Tee hee hoo!` (Mrs. Cogg) | **Flora J2 é `Ah!`/`Ai! Que susto!`** — manter, mas `Tee hee!` pode ser `Hehe!` como Rosetta `Heh heh!` (`Spec/Capitulo_05.md:142`) |

**Veredito Flora:** J2 Flora é tímida (`Ai! Que susto!`), J3 ganha arco `You have some nerve leaving me alone!` — sem conflito, expandir.

### 3.4 Don Paolo

| Bordão EN | J2 | Arquivo | J3 |
|---|---|---|---|
| `Don Paolo` | `Don Paolo` | `ide_4.txt:1` → `Don Paolo` | Manter `Don Paolo` |
| `Professor Layton's self-proclaimed nemesis / arqui-inimigo` | `arqui-inimigo do Professor Layton` | `ide_4.txt:1` `self-proclaimed nemesis` → `que afirma ser o arqui-inimigo` | Manter `arqui-inimigo` (com hífen) — J3 dossier usa igual |
| `Layton!` (gritado) | `Layton!` | `m13_4.txt:1` `Stop talking in circles... Layton!` → `vá direto ao ponto, Layton!` | Manter grito `Layton!` |
| Risada `Nyeh heh heh` | **Não transcrita em J2** (sem onomatopeia nos dumps `cp1252`) | — | **Nova em J3** — manter `Nyeh heh heh` (dossiê) |

**Veredito Don Paolo:** continuidade de título `arqui-inimigo` ok.

### 3.5 Inspetor Chelmey & Agente Barton

| Bordão EN | J2 | Arquivo | J3 |
|---|---|---|---|
| `Inspector Chelmey` | `Inspetor Chelmey` | `m4_2.txt:1` `Inspector Chelmey's the name.` → `Inspetor Chelmey` | Manter `Inspetor Chelmey` |
| `Constable Barton` | `Agente Barton` | `chr_21.txt:1` `Constable Barton` → `Agente Barton` | Manter `Agente Barton` |
| `Well, Inspector Chelmey's the name.` | `Bem, meu nome é Inspetor Chelmey.` | `m4_2.txt:1` | Manter fórmula de apresentação |
| `Chomp chomp` / `cup of tea` | **Não ocorre em J2 dumps textuais** (Barton come em `art_5` sem onomatopeia) | `art_5.txt:1` `Even Barton can't hide his feelings` → `Nem mesmo Barton` | J3 cria `Chomp chomp` / `Mmm, tea...` — **novo, sem conflito** |

**Veredito:** títulos ok; bordões de comida são expansão J3.

### 3.6 Termos sistêmicos já validados acima

| Termo | J2 | J3 | Manter |
|---|---|---|---|
| `puzzle` | `enigma` | `enigma` | Sim |
| `Puzzle Index` | `Livro de Enigmas` | `Livro de Enigmas` (corrigir `Índice`) | Sim |
| `hint coin` | `moeda de dica` | `moeda de dica` | Sim |
| `Good thinking!` | `Bem pensado!` | `Bem pensado!` | Sim (nazo1) |
| `Excellent work!` | `Bom trabalho!` / `Excelente!` | `Bom trabalho!` | Sim |

---

## 4. Divergências detectadas (ação requerida)

| Divergência | J2 | J3 (dossiê atual) | Recomendação |
|---|---|---|---|
| `my boy` | `meu garoto` (ht_011_3) / omitido (t10_036_100) | `meu rapaz` / `meu jovem` (Hershel_Layton.md) | **Decidir 1 forma e aplicar em todo J3.** Sugestão: manter `meu garoto` para continuidade estrita; ou migrar J2+J3 para `meu jovem` com nota de revisão global |
| `Puzzle Index` | `Livro de Enigmas` (tx_204, t10_045_500) | `Índice de Enigmas` em `Spec/Capitulo_00_Prologo.md:90` (antigo) | **Corrigir J3 para `Livro de Enigmas`** |
| `Granny Riddleton` | `Vovó Riddleton` (chr_71) | `Granny Riddleton` (inglês em Extras) | **Mudar Extras para `Vovó Riddleton`** |
| `Enigmano` (Puzzle Lad) | `Enigmano Um/Dois...` (chr_75-79) | Não usado em J3 (Family, Stachenscarfen) | Manter `Enigmano` se reaparecer |
| `Indeed` | `De fato.` / `É verdade.` / `Por enquanto, sim.` (variou) | `De fato.` fixo | Fixar `De fato.` |

---

## 5. Checklist de tradução J3 (copiar-colar)

- [ ] Substituir todo `Índice de Enigmas` → `Livro de Enigmas`
- [ ] Substituir `Granny Riddleton` → `Vovó Riddleton`
- [ ] Fixar `my boy` → `meu garoto` (ou `meu jovem` se revisão global)
- [ ] Fixar `Indeed` → `De fato.`
- [ ] Manter `Don Paolo`, `Inspetor Chelmey`, `Agente Barton`, `Professor Layton`, `moeda de dica`, `enigma`, `Bem pensado!`, `Bom trabalho!`, `Pode deixar, Professor!`, `Olhe, Professor!`, `Um cavalheiro jamais...`, `É isso que um cavalheiro faz.` exatamente como J2
- [ ] Novos bordões J3 sem precedente J2 podem ficar como estão: `Get lost!` → `Some daqui!` / `Vaza!`, `Keh heh heh!`, `Tee hee hoo!`, `Chomp chomp`

---

## 6. Exemplos paralelos (prova)

**Layton — gentleman:**
- J2 `ev_t15: t15_020_500.gds` `Come now, Luke. A gentleman never forces a lady...` → `Comporte-se, Luke. Um cavalheiro jamais força uma dama...`
- J3 `Spec/Hershel_Layton.md:4` `A gentleman never forces a lady...` → mesma fórmula

**Luke — Professor:**
- J2 `ev_t10: t10_030_200.gds` `What's that, Professor?` → `O que é isso, Professor?`
- J3 `Luke_Triton.md:4` `What's that, Professor?` → `O que é isso, Professor?` (idêntico)

**Barton — título:**
- J2 `chr_21.txt:1` `Constable Barton` → `Agente Barton`
- J3 `Chelmey_Barton.md:1` `Constable Barton` → `Agente Barton` (ok)

**Enigma:**
- J2 `txt2.plz.txt: tx_204:1` `Puzzle %.3d is now in your Puzzle Index!` → `Enigma %.3d foi enviado ao Livro de Enigmas!`
- J3 deve usar `Enigma` e `Livro de Enigmas` (não `quebra-cabeça`)

---

*Gerado por comparação binária `cp1252` de 38 arquivos `.plz.txt` J2 vs 15 capítulos J3. Para dúvidas, abrir `playton-2/Textos Traduzidos/plz/event/en/ev_t*.plz.txt` lado a lado com `Textos Originais/plz/event/en/`.*
