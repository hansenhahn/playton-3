# Capítulo 04 — O Atalho para Midland Road e o Wormhole do Relógio | Professor Layton and the Unwound Future

> **Capítulo 04 — O Atalho para Midland Road e o Wormhole do Relógio (Return to the Clock Shop / The Wormhole)** — Análise de dump LSCR para `Textos Originais/txt/uk/04/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/04/`
> Total de arquivos escaneados: **26**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<J>` = centralizado

---

## 1. Arquivos Cobertos

Todos os 26 dumps `.lbin.txt` em `uk/04`:

```
04_000000.lbin.txt  — [vazio - apenas cabeçalho]
04_025125.lbin.txt  — Future Luke adia Chinatown - prioridade é ver o inspector, ida à relojoaria
04_025130.lbin.txt  — Farol no Thames - construído há 5 anos, localização peculiar no meio do rio
04_025131.lbin.txt  — Graham - pássaro roubou cufflinks
04_025132.lbin.txt  — Captura do papagaio com garnet - batismo <N1>, amizade com Luke (sequência longa)
04_025134.lbin.txt  — Recompensa: Parrot minigame desbloqueado
04_025136.lbin.txt  — Graham agradece - devolve garnet e cufflinks, elogio de cavalheirismo
04_025138.lbin.txt  — Graham planeja linha de roupas com Belle como musa, busca de cravat
04_025140.lbin.txt  — Atalho à esquerda para Midland Road - metade do tempo
04_025145.lbin.txt  — Incentivo para usar atalho rápido de Future Luke
04_025150.lbin.txt  — Observatório - vista, sem tempo para parar
04_025160.lbin.txt  — Porta para Midland Road trancada - puzzle numérico, Nicola dormindo contra a porta
04_025170.lbin.txt  — Chegada à relojoaria - secret knock de Future Luke
04_025180.lbin.txt  — Retorno à loja - Spring (Mrs. Cogg) escondida, Cogg no fundo
04_025190.lbin.txt  — Spring diz que Cogg está afinando o relógio grande
04_025200.lbin.txt  — Exposição longa de Cogg: invasão da Family (Gorocky/Piranch/Mr. Bostro), origem do wormhole no relógio de 100 anos, controle exclusivo, plano com Future Luke para voltar ao passado e falar com Chelmey
04_025215.lbin.txt  — Gate cumprido (30 puzzles) - Cogg pronto para ativar, Future Luke permanece no futuro
04_025216.lbin.txt  — Gate bloqueado - é preciso resolver 30 puzzles antes de voltar
04_025230.lbin.txt  — Salto temporal - time sickness, enjoo, instrução da batida secreta
04_025240.lbin.txt  — De volta ao presente - confirmação do retorno, ida ao escritório da Gressenheller University antes de Chelmey
04_025245.lbin.txt  — Lembrete: concluir investigação no presente antes de retornar ao futuro
04_025250.lbin.txt  — Hint Coach Stachenscarfen (ヒゲマフラー) - picarats
04_025260.lbin.txt  — David - serviço de ônibus confirmado no presente, puzzle do ônibus
04_025270.lbin.txt  — Flores (フローレス) / Flawless Florence - agradecimento por hint coins, gag de idade, puzzle
04_025280.lbin.txt  — Prompt: qual ônibus leva à Gressenheller University
04_025300.lbin.txt  — Recap no ônibus - OP Layton/OP Luke revisam caso: Big Luke, Layton do mal, Pagode, missão do inspector
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `04_000000.lbin.txt`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 04 |
|---|---|---|
| `未来ルーク` | **Future Luke (Big Luke)** | Luke 10 anos mais velho, guia, estrategista, conhece atalho e secret knock |
| `ルーク` | **Luke Triton (Little Luke)** | Aprendiz, co-protagonista, doma o papagaio, sofre time sickness |
| `レイトン` | **Professor Hershel Layton** | Protagonista, investiga farol, nomeia papagaio, planeja retorno ao presente |
| `OPルーク２` / `OPレイトン２` | **Past Luke / Past Layton (no ônibus, presente)** | Versões do presente em recap, revisam caso a caminho da universidade |
| `ジャック` | **Jack Cogg / Cogg (Clockmaker)** | Dono da relojoaria, guardião do wormhole, único que controla o relógio de 100 anos |
| `サマリー` | **Mrs. Cogg / Spring (Clock Shop Wife)** | Esposa de Cogg, esconde-se na loja, reconhece Future Luke, chama-o "Spring" |
| `グラハム` | **Graham (Dandy)** | Homem vaidoso de terno italiano, perde cufflinks para pássaro, planeja linha com Belle |
| `オウム` | **Parrot / <N1> (Parrot)** | Papagaio que rouba cufflinks, torna-se amigo de Luke, nomeável pelo jogador `<N1>`, minigame |
| `ニコラ` | **Nicola (Hat-fearing Man / Sleeping Man)** | Homem que dorme encostado na porta para Midland Road, acorda irritado com chapéu |
| `ゴロッキー` | **Gorocky (Family Goon)** | Capanga da Family que invade relojoaria com Piranchi |
| `ピランチ` | **Piranchi / Piranha (Family Goon)** | Capanga da Family, age com Gorocky, ameaça Cogg |
| `ボストロ` | **Bostro (Family Boss)** | Chefe da Family, ordena trabalho no relógio para "you-know-who" (Layton do futuro) |
| `ヒゲマフラー` | **Stachenscarfen / Moustache-Scarf Man (Dica Coach)** | Gag recorrente, explica picarats, auto-nomeia "Stachenscarfen" |
| `デビット` | **David (Passerby)** | Passante no presente, confirma que ônibus ainda circulam, fã de double-deckers |
| `フローレス` | **Flores / Flawless Florence (Tutorial Lady)** | Senhora do ponto de ônibus, cobra agradecimento, reage a ser chamada de velha |
| `ナレーション` | **Narration** | Narra recompensa do papagaio e chegada de Spring |

Tags de controle observadas: nenhum `<Vxxxx>` dublado neste capítulo (todo `<T>` não-dublado, exploração); `<W>` pausas; `<A1/2>` etc. animações; `<K>` efeito cinético em `04_025216`; `<J54>` bloco centralizado/jumping em `04_025180`; `<S310>` efeito sonoro de porta em `04_025160`; placeholders `<N1>` nome do papagaio; `<CR>` ausente.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Adiando Chinatown — Prioridade: o Inspector (`04_025125`–`04_025130`)
Future Luke interrompe o trajeto a Chinatown e redireciona o grupo para a relojoaria, argumentando que falar com o inspector é prioridade. No caminho, discutem o farol gigante visto no capítulo anterior às margens do Thames. Layton estranha a localização no meio do rio; Future Luke confirma que a construção tem cerca de 5 anos, mas adia explicações sobre Londres do futuro até depois do retorno.
> Gancho: "We'll return to Chinatown later, but our priorities lie elsewhere at the moment." / "About five years ago."

### 3.2 O Dândi e o Papagaio — Graham, Garnet e <N1> (`04_025131`–`04_025138`)
O grupo encontra Graham, um dândi vaidoso que teve seus cufflinks roubados por um papagaio. Future Luke quer seguir adiante, mas Little Luke invoca o código do cavalheiro e o grupo aceita ajudar. Graham oferece uma garnet brilhante para atrair a ave, mas ela caiu no fundo de sua maleta desorganizada — enigma de inventário. Após recuperá-la, usam a gema como isca e Luke doma o pássaro, que se mostra afeiçoado a ele. Layton sugere nomeá-lo; o próprio papagaio anuncia o nome escolhido pelo jogador (<N1>), formalizando a amizade. Narração premia o jogador com o minijogo Parrot. Graham recupera os cufflinks, agradece exaltando o cavalheirismo e recusa recompensa, e depois revela seu plano de propor a Belle uma parceria para uma linha de roupas, tendo-a como musa, precisando apenas de uma nova cravat para a ocasião.
> Ganchos: "Helping people in need is the duty of every gentleman." / "Hallo, hallo! Nice to meetchoo, meetchoo! I'm <N1>!"

### 3.3 O Atalho para Midland Road (`04_025140`–`04_025160`)
Guiados por Future Luke, pegam um atalho à esquerda que corta o tempo até Midland Road pela metade e dispensam parada no observatório apesar da vista. Ao fim do caminho, a porta para Midland Road está trancada com um enigma numérico embutido. Layton identifica os números, o enigma é resolvido, mas a porta continua emperrada. Ao empurrá-la em conjunto, descobrem Nicola dormindo encostado do outro lado, que acorda irritado e reclama do chapéu de Layton antes de ir embora. Layton lamenta tê-lo afugentado; Future Luke minimiza e segue para a relojoaria.
> Ganchos: "It will, and in half the time." / "Oi! What do you think you're doing, kicking down my napping door? You woke me up!"

### 3.4 Chegada à Relojoaria — O Secret Knock (`04_025170`–`04_025190`)
Diante da loja trancada, Future Luke revela conhecer uma batida secreta (batida secreta) que destranca a porta. Dentro, a loja parece vazia até Spring (Mrs. Cogg) surgir escondida com sua risada característica e reconhecer a batida. Future Luke a trata por "Spring", evidenciando aliança prévia; Spring confirma que Cogg está nos fundos afinando o grande relógio. Future Luke admite que o casal o tem ajudado e encaminha o grupo a Cogg para a explicação completa.
> Ganchos: "That's because you didn't know the secret knock." / "Tee hee hoo! Well, look who's back."

### 3.5 A Verdade sobre o Buraco de minhoca — Cogg Conta Tudo (`04_025200`)
Núcleo expositivo do capítulo (cerca de 400 linhas). Cogg apresenta o grande relógio com mais de 100 anos e conta que, enquanto fazia manutenção, a Family invadiu a loja: Gorocky e Piranchi arrombam e Bostro ordena preparar o relógio a tempo para "you-know-who" (o Layton do futuro). Cogg resiste e é arrastado para fora. Depois descobre que a Family financiava cientistas para construir uma máquina do tempo que abriria um vórtice/buraco de minhoca no fluxo temporal; o experimento saiu do controle e o ponto de dobra gravitacional acabou ancorado no relógio antigo por sua idade. Por ser o único capaz de mantê-lo funcionando, Cogg tornou-se o único operador do buraco de minhoca, coagido pela Family. Future Luke, ao saber da situação, propôs aliança a Cogg e Spring e usou o relógio para enviar a carta que trouxe Layton e Luke ao futuro. Layton reconhece o plano e promete voltar após falar com Chelmey para deter o responsável.
> Ganchos: "Which means, like it or not, I'm the only person who can open and close the buraco de minhoca." / "The only one who can stop Hershel Layton is Hershel Layton himself."

### 3.6 O Portão de 30 Enigmas e o Salto Temporal (`04_025215`–`04_025230`)
O retorno ao presente é condicionado a um portão clássico: Cogg só ativa o relógio se o jogador tiver resolvido ao menos 30 enigmas; caso contrário, pede mais investigação. Quando liberado, Future Luke opta por ficar no futuro para evitar paradoxos — Layton brinca que dois Lukes assustariam Chelmey. O salto causa "enjoo temporal" em Luke (enjoo, ouvidos tampados, chão de marshmallow), que Cogg normaliza como comum na primeira viagem. Antes da partida, Cogg reforça o uso da batida secreta para reabrir a loja no retorno.
> Ganchos: "Come back when you've solved 30 puzzles, and I'll return you to your own time." / "Are you going to be all right, Luke? You look positively pea-green."

### 3.7 De Volta ao Presente — Gressenheller e o Inspector (`04_025240`–`04_025300`)
De volta ao presente, o cenário ao redor da relojoaria já parece familiar. Layton, mesmo exausto, decide passar primeiro em seu escritório na Gressenheller University antes de procurar o Inspector Chelmey, para se preparar adequadamente. Há um lembrete explícito para concluir a investigação no presente antes de voltar ao futuro. No trajeto pela Midland Road, três reencontros cômicos marcam o contraste temporal: Stachenscarfen tenta reexplicar picarats e insiste num enigma; David confirma que os ônibus ainda circulam (ao contrário do futuro) e propõe enigma de ônibus; Flores/Flawless Florence cobra agradecimento por moedas de dica e, ofendida ao ser chamada de velha/elderly por Luke, desafia-o com um enigma, amolecendo com o cavalheirismo de Layton. Layton então pergunta qual ônibus vai para a universidade e, já a bordo, as versões "passadas" de Layton e Luke (OP) fazem um recap da missão — o chamado de Big Luke, o Layton do mal e sua pesquisa de máquina do tempo, o bloqueio de Chinatown e a necessidade de falar com o inspector — enquanto se aproximam da parada de Gressenheller.
> Ganchos: "Preparation, my boy, is the foundation upon which every good investigation is built." / "There is, and it's that something that we've come to investigate."

**Cliffhanger:** Com o buraco de minhoca da relojoaria como ponte estável, Layton e Luke têm uma janela curta no presente para coletar pistas em Gressenheller e com Chelmey antes de retornar para enfrentar o Layton do futuro no Pagode.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag) — <A/W> se houver` e então o texto em inglês conforme no arquivo. `<T>` limpo, esperas `<W>` anotadas.

### `04_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `04_025125.lbin.txt` — Adiando Chinatown

*   **未来ルーク** (Future Luke):  
    `We'll return to Chinatown later, but our priorities lie elsewhere at the moment.`
*   **未来ルーク** (Future Luke):  
    `Besides, you wanted to see the inspector, didn't you, Professor? Let's hurry to the clock shop.`

### `04_025130.lbin.txt` — O farol de 5 anos

*   **ルーク** (Luke Triton):  
    `Say, when was that lighthouse on the river built?`
*   **未来ルーク** (Future Luke):  
    `About five years ago.`
*   **レイトン** (Professor Hershel Layton) *(<A1/1>)*:  
    `Did anyone comment on its peculiar location?`
*   **レイトン** (Professor Hershel Layton):  
    `Building a structure like that in the middle of the river seems to serve little purpose.`
*   **未来ルーク** (Future Luke) *(<A3/5>)*:  
    `That's not untrue, Professor... But let's discuss the city later. We need to make for the clock shop.`

### `04_025131.lbin.txt` — Graham e o pássaro ladrão

*   **グラハム** (Graham):  
    `Oh, thank goodness you're here! London's most debonair man requires some assistance.`
*   **ルーク** (Luke Triton):  
    `Er... All right. What's the matter?`
*   **グラハム** (Graham) *(<A2/3>)*:  
    `It's that blasted bird over there!`
*   **グラハム** (Graham):  
    `The dreadful creature swooped down and plucked my best cufflinks right off my sleeves!`
*   **ルーク** (Luke Triton):  
    `What bird?`
*   **グラハム** (Graham):  
    `Look, there it is, flapping about! I think it's taunting me!`

### `04_025132.lbin.txt` — A captura do papagaio (sequência longa, 208 linhas)

*   **未来ルーク** (Future Luke):  
    `Oh, that must be the bird that fellow is talking about.`
*   **ルーク** (Luke Triton):  
    `Oh wow! A parrot!`
*   **グラハム** (Graham) *(<A2/3>)*:  
    `Don't just stand there staring! Grab the winged menace before it flaps off!`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `You may not have noticed, sir, but we're in a bit of a hurry here.`
*   **ルーク** (Luke Triton):  
    `Luke, listen to yourself! Don't you remember what the professor always says?`
*   **ルーク** (Luke Triton):  
    `Helping people in need is the duty of every gentleman.`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `A very good point, Luke. Very well then, let's think. This bird clearly likes shiny objects.`
*   **未来ルーク** (Future Luke):  
    `Excuse me sir, would you happen to have anything shiny we could borrow for a moment?`
*   **グラハム** (Graham) *(<A2/2>)*:  
    `Of course! What sort of gentleman would I be without the proper accoutrements?`
*   **グラハム** (Graham):  
    `Here, I always carry a garnet for when I need to accessorise with a little flash!`
*   **グラハム** (Graham) *(<A3/4>)*:  
    `Oh... Oh dear.`
*   **ルーク** (Luke Triton):  
    `What's wrong?`
*   **グラハム** (Graham):  
    `Curses! The garnet has fallen to the bottom of my case and I can't reach it!`
*   **未来ルーク** (Future Luke) *(<A4/4>)*:  
    `You're not making it very easy for us to help you.`
*   **未来ルーク** (Future Luke):  
    `He really should sort out the contents of this briefcase sometime. It's a bit of a mess.`
*   **未来ルーク** (Future Luke):  
    `Let me see if I can retrieve that garnet this time.`
*   **未来ルーク** (Future Luke):  
    `Aha! There we are!`
*   **未来ルーク** (Future Luke):  
    `With any luck, this flashy gem will attract the parrot.`
*   **未来ルーク** (Future Luke):  
    `See if you can tame him when he gets close.`
*   **ルーク** (Luke Triton) *(<A3/2>)*:  
    `Leave it to me!`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `Right then. Here goes!`
*   **オウム** (Parrot) :  
    `Awwwrk!`
*   **未来ルーク** (Future Luke) *(<A1/5>)*:  
    `Here he comes!`
*   **オウム** (Parrot) :  
    `Awwwrk! Skwaaarka skwaaaawk!`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `Don't worry, boy! We won't hurt you!`
*   **オウム** (Parrot) :  
    `Skwawk! Skwaaaark!`
*   **ルーク** (Luke Triton) *(<A4/2>)*:  
    `You don't say!`
*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `You know, that bird seems pretty fond of you, Luke. Are you friends now?`
*   **ルーク** (Luke Triton) *(<A2/2>)*:  
    `Of course!`
*   **レイトン** (Professor Hershel Layton):  
    `Well, now that you're friends, why don't you give him a name?`
*   **ルーク** (Luke Triton):  
    `Good idea, Professor! But what should I name him? Hmm...`
*   **オウム** (Parrot) :  
    `Hallo, hallo! Nice to meetchoo, meetchoo! I'm <N1>!`
*   **ルーク** (Luke Triton):  
    `Hello there! I'm Luke. It's nice to meet you too, <N1>!`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `Nice work, Luke! That was amazing!`
*   **ルーク** (Luke Triton) *(<A2/2>)*:  
    `Of course! What else would you expect from the apprentice of the great Professor Layton?`

### `04_025134.lbin.txt` — Recompensa do papagaio

*   **ナレーション** (Narration):  
    `You have a new feathered friend, <N1> the parrot!`
*   **ナレーション** (Narration):  
    `The Parrot minigame has been added to the trunk.`
*   **ナレーション** (Narration):  
    `First, have the parrot play with Luke to learn the basics.`
*   **ナレーション** (Narration):  
    `Once you've done that, you'll have the chance to do lots more with your parrot friend.`

### `04_025136.lbin.txt` — Graham agradece

*   **グラハム** (Graham) *(<A1/1>)*:  
    `Thank goodness you caught that fluffy fiend. What fine young men you two are!`
*   **グラハム** (Graham):  
    `Keep at it and one day you will each become a true gentleman, just like myself.`
*   **未来ルーク** (Future Luke):  
    `Glad we could help. Here's your garnet and...I believe these cufflinks are yours too.`
*   **グラハム** (Graham):  
    `Oh, yes. There we are. With these in place I'm even more devastatingly handsome than before.`
*   **グラハム** (Graham):  
    `Now I believe you two young men deserve something for your trouble.`
*   **未来ルーク** (Future Luke):  
    `Oh, there's really no need, sir.`
*   **ルーク** (Luke Triton):  
    `Helping people is reward enough for any gentleman!`

### `04_025138.lbin.txt` — Graham e Belle

*   **グラハム** (Graham) *(<A1/5>)*:  
    `Today's the big day! At last, I shall propose to the most enchanting woman in all of London.`
*   **グラハム** (Graham):  
    `Propose a business partnership, that is!`
*   **ルーク** (Luke Triton):  
    `Gosh, how exciting!`
*   **グラハム** (Graham) *(<A3/4>)*:  
    `Oh yes. At last Belle, radiant goddess that she is, will help me realise my life's ambition!`
*   **グラハム** (Graham):  
    `I plan to start...a clothing line!`
*   **グラハム** (Graham):  
    `As you can see, I am no stranger to style myself.`
*   **グラハム** (Graham):  
    `But no one has their finger on the pulse of fashion like that girl.`
*   **グラハム** (Graham):  
    `Every genius needs a muse. Belle is mine!`
*   **ルーク** (Luke Triton):  
    `Oh... Well, um, good luck with that.`
*   **グラハム** (Graham):  
    `Perhaps a new cravat is what I need to seal the deal. Hmm...`

### `04_025140.lbin.txt` — Atalho à esquerda

*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `Let's take the path on the left up here.`
*   **ルーク** (Luke Triton):  
    `The left? Will that way take us back to Midland Road as well?`
*   **未来ルーク** (Future Luke):  
    `It will, and in half the time.`

### `04_025145.lbin.txt` — Pressa

*   **未来ルーク** (Future Luke):  
    `There's no time to waste! We should use my short cut to get back to the clock shop as fast as possible.`

### `04_025150.lbin.txt` — Observatório

*   **ルーク** (Luke Triton):  
    `I bet the view from the observatory is out of this world!`
*   **未来ルーク** (Future Luke) *(<A3/5>)*:  
    `It is rather nice, but we don't have time to stop. We must press on to the clock shop!`

### `04_025160.lbin.txt` — Porta trancada e Nicola

*   **未来ルーク** (Future Luke):  
    `Midland Road is just on the other side of that door.`
*   **ルーク** (Luke Triton) *(<A3/1>)*:  
    `I'll go and open it!`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `...Hey! The door's locked!`
*   **未来ルーク** (Future Luke):  
    `Locked? It can't be. Budge over, Luke. I'll get it open.`
*   **未来ルーク** (Future Luke):  
    `How strange! It really is locked.`
*   **レイトン** (Professor Hershel Layton):  
    `Look at this, you two. There's an unusual set of numbers embedded in the door.`
*   **未来ルーク** (Future Luke):  
    `It doesn't make any sense. This door was supposed to be open.`
*   **レイトン** (Professor Hershel Layton):  
    `Try the puzzle lock on that door again. We're bound to solve this sooner or later.`
*   **レイトン** (Professor Hershel Layton):  
    `Wonderful work, Big Luke.`
*   **ルーク** (Luke Triton):  
    `I think it's a little early for congratulations, Professor. The door still won't open.`
*   **レイトン** (Professor Hershel Layton):  
    `If the puzzle isn't keeping the door shut, what is?`
*   **未来ルーク** (Future Luke) *(<A3/5>)*:  
    `Well, I suppose it's time for plan B.`
*   **未来ルーク** (Future Luke):  
    `This might seem too obvious, but would you two help me give this door a push?`
*   **レイトン** (Professor Hershel Layton):  
    `Certainly. It does seem we've run out of other options, after all.`
*   **未来ルーク** (Future Luke):  
    `Ready, everyone? All together on three. One. Two. Three!`
*   **ルーク** (Luke Triton):  
    `Aaah!`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `What's that man doing on the ground?!`
*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `Ha ha ha! This fellow must have fallen asleep against the door.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `It just goes to show that every puzzle has an answer.`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `Well think fast, Professor, because that answer is coming this way and he doesn't look happy.`
*   **ニコラ** (Nicola) *(<A2/5>)*:  
    `Oi! What do you think you're doing, kicking down my napping door? You woke me up!`
*   **レイトン** (Professor Hershel Layton) *(<A3/1>)*:  
    `We're terribly sorry, sir. Please understand, we had no idea you were there.`
*   **ニコラ** (Nicola) *(<A2/6>)*:  
    `Oh, not you again...`
*   **ニコラ** (Nicola):  
    `Look, I can't deal with that hat of yours right now. I'm out of here.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1>)*:  
    `Oh dear. I seem to have driven that poor man off.`
*   **未来ルーク** (Future Luke):  
    `I wouldn't pay it too much heed, Professor.`
*   **未来ルーク** (Future Luke):  
    `Besides, we need to keep moving towards the clock shop. We're nearly there now.`

### `04_025170.lbin.txt` — O secret knock

*   **ルーク** (Luke Triton):  
    `There's the shop. The door was locked earlier and no one would answer it when we knocked.`
*   **未来ルーク** (Future Luke):  
    `That's because you didn't know the secret knock. Watch this.`
*   **ナレーション** (Narration):  
    `Come on in!`
*   **未来ルーク** (Future Luke):  
    `Go on. Try the door now.`

### `04_025180.lbin.txt` — Spring escondida

*   **ルーク** (Luke Triton):  
    `It looks like no one's here.`
*   **ナレーション** (Narration) *(<J54>)*:  
    `Tee hee hoo! Well, look who's back.`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `Augh! What are you doing hiding there?!`
*   **サマリー** (Mrs. Cogg / Spring):  
    `I see you've learned the secret knock, dearie.`
*   **未来ルーク** (Future Luke):  
    `Actually, I was the one who did the knocking, Spring. Is Cogg around?`
*   **サマリー** (Mrs. Cogg / Spring):  
    `Ah, there you are, Luke. Cogg's in the back room.`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `Oh, so you know the owners of the clock shop, Luke?`
*   **未来ルーク** (Future Luke) *(<A2/5>)*:  
    `I must have forgotten to mention that earlier, but yes, Spring and Cogg have been helping me.`
*   **未来ルーク** (Future Luke):  
    `I think Cogg can explain better than I can, though. You should ask him.`
*   **ルーク** (Luke Triton):  
    `All right. Let's hear what he has to say.`
*   **未来ルーク** (Future Luke):  
    `Cogg's in the back room. He'll fill you in on how all this time travelling began.`
*   **未来ルーク** (Future Luke):  
    `Sorry for keeping you in the dark. It was never my intention to deceive you.`

### `04_025190.lbin.txt` — Cogg no fundo

*   **サマリー** (Mrs. Cogg / Spring):  
    `Cogg's tuning up the big clock in the back.`

### `04_025200.lbin.txt` — A exposição de Cogg (wormhole)

*   **ジャック** (Cogg):  
    `I thought I heard voices out front.`
*   **ジャック** (Cogg):  
    `Nice to see you again, Professor and er...`
*   **ルーク** (Luke Triton) *(<A3/2>)*:  
    `Luke! The professor's apprentice!`
*   **ジャック** (Cogg) *(<A2/1>)*:  
    `Yes, yes, Luke, of course.`
*   **未来ルーク** (Future Luke):  
    `Would you mind telling them about the wormhole and how it all started, Cogg?`
*   **未来ルーク** (Future Luke):  
    `I think it would help to have everyone on the same page.`
*   **ジャック** (Cogg):  
    `It'd be my pleasure. Now then, Luke! Erm...the smaller Luke, that is.`
*   **ルーク** (Luke Triton) *(<A3/1>)*:  
    `Yes?`
*   **ジャック** (Cogg):  
    `Tell me, lad. What does this contraption behind me look like to you?`
*   **ルーク** (Luke Triton):  
    `A big, old clock.`
*   **ジャック** (Cogg):  
    `Right you are. By my estimate, this clock is well over a hundred years old.`
*   **ジャック** (Cogg):  
    `The old girl needs a lot of TLC to keep chugging along, so I spend quite a bit of time on maintenance.`
*   **ジャック** (Cogg):  
    `I was right in the middle of oiling her gears one day when two Family thugs burst in...`
*   **ゴロッキー** (Gorocky):  
    `Here we go. This has gotta be the place the boss was talkin' about.`
*   **ピランチ** (Piranchi):  
    `Too right. Hey, boss! There's a big clock here, just like you said. It's a proper antique, look!`
*   **ジャック** (Cogg) *(<A1/1>)*:  
    `Hey you! What do you think you're doing, barging into my shop? Get your hands off my clock!`
*   **ゴロッキー** (Gorocky):  
    `Shut it, you old codger! You don't tell us what to do. Don't you know who you're dealin' with?`
*   **ジャック** (Cogg):  
    `I'm dealing with a load of clods who won't get out of my shop!`
*   **ピランチ** (Piranchi) *(<A3/3>)*:  
    `I'd keep a civil tongue in my head if I were you, grandad.`
*   **ピランチ** (Piranchi):  
    `Now get outta the way! We've got a schedule to keep here.`
*   **ボストロ** (Bostro) *(<A4/0>)*:  
    `What are you clowns waitin' for? Get to work!`
*   **ボストロ** (Bostro) *(<A2/3>)*:  
    `If we don't get a move on, things won't be ready in time for you-know-who!`
*   **ゴロッキー** (Gorocky):  
    `Sorry boss, we're doin' our best, but grandad here's got his knickers in a twist.`
*   **ボストロ** (Bostro):  
    `Then throw 'im out into the street, you numpty!`
*   **ジャック** (Cogg):  
    `Let me go, you villains!`
*   **ピランチ** (Piranchi):  
    `We're just gonna go for a little walk, all right, grandad?`
*   **ジャック** (Cogg):  
    `You keep your filthy hands off my clock! You hear me?`
*   **ボストロ** (Bostro):  
    `We're just about on schedule.`
*   **ボストロ** (Bostro):  
    `But we 'ave to wait until the exact time the boss said to turn this thing on.`
*   **ジャック** (Cogg) *(<A2/1>)*:  
    `That's all I heard before those brutes threw me out of my own shop.`
*   **ジャック** (Cogg):  
    `It wasn't until later that I found out what the thugs wanted from my little clock shop.`
*   **ジャック** (Cogg):  
    `See, the Family was funding the construction of a time machine by a group of scientists.`
*   **ジャック** (Cogg):  
    `I think the idea was to use it to create some kind of wormhole.`
*   **レイトン** (Professor Hershel Layton):  
    `But how could they do that?`
*   **ジャック** (Cogg):  
    `Search me. It was all mumbo-jumbo. Something about opening up a vortex in the flow of time.`
*   **ジャック** (Cogg):  
    `Anyway, things didn't go exactly to plan, for whatever reason.`
*   **レイトン** (Professor Hershel Layton):  
    `I see. So...somehow this hole in time appeared in this clock of yours.`
*   **ジャック** (Cogg):  
    `That's more or less it. This clock has been ticking away for over a hundred years.`
*   **ジャック** (Cogg):  
    `My guess is that something about the clock's age caused the warp point to gravitate to this spot.`
*   **ジャック** (Cogg):  
    `The wormhole, or whatever it's called, became a part of my clock.`
*   **ジャック** (Cogg):  
    `The thing is, I'm the only one who can keep the old girl running.`
*   **ジャック** (Cogg):  
    `Which means, like it or not, I'm the only person who can open and close the wormhole.`
*   **ルーク** (Luke Triton) *(<A4/1>)*:  
    `Wow, that's really weird!`
*   **ジャック** (Cogg):  
    `It's a burden, is what it is.`
*   **ジャック** (Cogg):  
    `Once the Family realised, they forced me to work the clock for them.`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `After a while, I caught wind of Cogg's situation.`
*   **未来ルーク** (Future Luke):  
    `It goes without saying that he's not a member of the Family.`
*   **未来ルーク** (Future Luke):  
    `In fact, the Family's been nothing but a source of trouble for him.`
*   **ルーク** (Luke Triton):  
    `It certainly sounds like it.`
*   **未来ルーク** (Future Luke):  
    `So I approached Cogg and Spring and explained my plan to them.`
*   **未来ルーク** (Future Luke):  
    `They agreed to help, and Cogg fired up the machine so that I could get my message to you.`
*   **レイトン** (Professor Hershel Layton):  
    `And upon receiving your letter, I let my curiosity take Luke and myself on a journey that led here.`
*   **レイトン** (Professor Hershel Layton):  
    `That's quite a plan you concocted, Big Luke.`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `Thank you... But it's about to get even more interesting.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1>)*:  
    `Oh?`
*   **未来ルーク** (Future Luke):  
    `Professor, with Cogg's help we can send you and Luke back to your own time.`
*   **未来ルーク** (Future Luke):  
    `You'll be able to speak to Inspector Chelmey there.`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `But you will come back to put a stop to what's going on here when you've finished, won't you?`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `You of all people should know the answer to that question, Luke.`
*   **レイトン** (Professor Hershel Layton):  
    `I keep my promises and I intend to solve the problem here. It's what a gentleman would do.`
*   **未来ルーク** (Future Luke):  
    `Thank you, Professor. That was exactly the answer I was hoping for.`
*   **レイトン** (Professor Hershel Layton):  
    `I wouldn't dream of leaving things here in this state.`
*   **レイトン** (Professor Hershel Layton):  
    `You said it yourself, Luke. The only one who can stop Hershel Layton is Hershel Layton himself.`
*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `Ha ha! That's true. My apologies. I should never have doubted you.`

### `04_025215.lbin.txt` — Gate de 30 puzzles (liberado)

*   **ジャック** (Cogg):  
    `Let me see here. Yep, you've solved at least 30 puzzles.`
*   **ジャック** (Cogg):  
    `Seems you've done enough research to take your investigation back to your own time.`
*   **ジャック** (Cogg):  
    `Hopefully, you'll learn something there that will help us clear up the terrible situation here.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, I hope so. Now then, Cogg, if you would be so kind as to start up the clock...`
*   **未来ルーク** (Future Luke):  
    `I hope you'll understand if I stay here.`
*   **未来ルーク** (Future Luke):  
    `I don't wish to risk distorting the events of the past any more than necessary.`
*   **レイトン** (Professor Hershel Layton):  
    `I agree.`
*   **レイトン** (Professor Hershel Layton):  
    `Besides which, the poor inspector's eyes would likely pop out of his head if I turned up with two Lukes.`
*   **ルーク** (Luke Triton):  
    `Wow, that actually sounds quite funny... Too bad you can't come, Big Luke.`
*   **ジャック** (Cogg):  
    `Okay, she's all ready to go. Let's get going!`

### `04_025216.lbin.txt` — Gate bloqueado

*   **ジャック** (Cogg):  
    `Hrm? You two don't seem to have explored this London very thoroughly.`
*   **ジャック** (Cogg):  
    `If you want to make some real headway in your case, you'll have to do a bit more research.`
*   **レイトン** (Professor Hershel Layton):  
    `Exactly how much research do we need to do?`
*   **ジャック** (Cogg) *(<K> Hmm...)*:  
    `Hmm... Tell you what. Come back when you've solved 30 puzzles, and I'll return you to your own time.`
*   **レイトン** (Professor Hershel Layton):  
    `All right then, Cogg. You've been in on this plan longer than we have, so I bow to your judgement.`
*   **レイトン** (Professor Hershel Layton):  
    `We shall see if we can find a few more puzzles out there to solve.`
*   **ジャック** (Cogg):  
    `Hmm. You should probably do a bit more investigating here before returning to your own time.`
*   **ジャック** (Cogg):  
    `Come back when you've solved 30 puzzles and I'll take you back to your London.`

### `04_025230.lbin.txt` — Time sickness

*   **ジャック** (Cogg):  
    `Here we are.`
*   **ルーク** (Luke Triton):  
    `Ugh... I feel sick.`
*   **レイトン** (Professor Hershel Layton):  
    `Are you going to be all right, Luke? You look positively pea-green.`
*   **ルーク** (Luke Triton):  
    `I feel sort of seasick. My ears are all stuffy and the ground feels like it's made of marshmallow.`
*   **ジャック** (Cogg):  
    `Ah, that'll be time sickness. The first jump I made, I didn't feel very well either.`
*   **レイトン** (Professor Hershel Layton):  
    `Well Cogg, we're going to head off now and see what we can find out.`
*   **ジャック** (Cogg):  
    `Sounds good. I'll be here waiting for you. Just use that special knock and I'll let you in.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `Excellent. I was wondering how we'd contact you if you went back to your own time while we were out.`
*   **ジャック** (Cogg):  
    `Yep, that'd be a pain, all right.`
*   **ジャック** (Cogg):  
    `Now, you two should get moving. I'd like to get home in time for dinner.`
*   **ジャック** (Cogg):  
    `Have you finished your investigation here already?`
*   **レイトン** (Professor Hershel Layton):  
    `No, quite the opposite. We're just getting started.`

### `04_025240.lbin.txt` — De volta ao presente

*   **ルーク** (Luke Triton):  
    `There's no doubt about it, Professor. We're back in our time.`
*   **レイトン** (Professor Hershel Layton):  
    `The surroundings here certainly do seem familiar.`
*   **ルーク** (Luke Triton):  
    `Phew. All this time travel has really worn me out, you know.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `Yes, I could do with a rest myself. But we mustn't keep Cogg waiting.`
*   **ルーク** (Luke Triton) *(<A4/2>)*:  
    `You're right. So, shall we go and find Inspector Chelmey?`
*   **レイトン** (Professor Hershel Layton):  
    `That will be our second stop. I'd like to drop by my office at the university first.`
*   **ルーク** (Luke Triton):  
    `For a quick rest?`
*   **レイトン** (Professor Hershel Layton) *(<A2/2>)*:  
    `Not quite. I need to check a few things before our meeting with Inspector Chelmey.`
*   **レイトン** (Professor Hershel Layton):  
    `Preparation, my boy, is the foundation upon which every good investigation is built.`
*   **ルーク** (Luke Triton) *(<A4/2>)*:  
    `Right you are, Professor!`
*   **レイトン** (Professor Hershel Layton) *(<A4/2>)*:  
    `Now that we're back in our own time, we can reach the university in a matter of minutes by bus.`
*   **レイトン** (Professor Hershel Layton):  
    `Let's go, Luke.`

### `04_025245.lbin.txt` — Lembrete

*   **レイトン** (Professor Hershel Layton):  
    `I think it would be best to conclude our investigation here before returning to the future.`

### `04_025250.lbin.txt` — Stachenscarfen e picarats

*   **ヒゲマフラー** (Stachenscarfen) *(<A3/0>)*:  
    `Keh heh heh. And how are you doing, boy?`
*   **ルーク** (Luke Triton):  
    `I'm fine, thank you. It's always a surprise to see you again.`
*   **ヒゲマフラー** (Stachenscarfen) *(<A2/1>)*:  
    `Again? What's this 'again' business? Keh heh heh!`
*   **ヒゲマフラー** (Stachenscarfen) *(<A2/1>)*:  
    `I just thought I'd give you some advice, is all.`
*   **ルーク** (Luke Triton) *(<A4/2>)*:  
    `All right. What is it?`
*   **ヒゲマフラー** (Stachenscarfen):  
    `Not many folks know this, but when you solve puzzles, you can earn these-`
*   **ルーク** (Luke Triton) *(<A4/1>)*:  
    `Oh, if you're going to talk about picarats, we already know all about them.`
*   **ヒゲマフラー** (Stachenscarfen) *(<A3/0> <A2/5>)*:  
    `Well... Keh heh heh... Is that so? Well who cares? It's not all that great a secret anyway.`
*   **ルーク** (Luke Triton):  
    `Okay, well, thank you. We really should go now. We've got a lot to do.`
*   **ヒゲマフラー** (Stachenscarfen) *(<A2/3>)*:  
    `Wait! Don't just run off like that. I have, um...a puzzle! Yes, that's right! I have a puzzle for you.`
*   **ヒゲマフラー** (Stachenscarfen) *(<A3/0> <A2/1>)*:  
    `Keh heh heh. Bit of a stumper, eh?`
*   **ヒゲマフラー** (Stachenscarfen):  
    `Keh heh heh. Just say the word if you want to have another crack at my puzzle.`
*   **ヒゲマフラー** (Stachenscarfen):  
    `How was that for a fun puzzle? It's in your top ten, surely?`
*   **ルーク** (Luke Triton):  
    `It was okay, I suppose.`
*   **ヒゲマフラー** (Stachenscarfen) *(<A2/3>)*:  
    `Wh-what? Just okay?!`
*   **ヒゲマフラー** (Stachenscarfen) *(<A3/0> <A2/5>)*:  
    `Keh heh heh. Oh, I see. You're playing it cool.`
*   **ヒゲマフラー** (Stachenscarfen):  
    `You don't want to let on that my puzzle knocked your socks off.`
*   **ルーク** (Luke Triton):  
    `That's one way of putting it...`
*   **ヒゲマフラー** (Stachenscarfen) *(<A3/0> <A2/1>)*:  
    `Keh heh heh. Hello there, boy. Back to chat with your old mate Stachenscarfen, eh?`
*   **ルーク** (Luke Triton):  
    `Actually, we're in a bit of a hurry. Maybe another time.`

### `04_025260.lbin.txt` — David e os ônibus

*   **デビット** (David):  
    `Hi there, squirt. What can I do for you?`
*   **ルーク** (Luke Triton):  
    `I noticed there's a bus stop up ahead. London still has a bus service, doesn't it?`
*   **デビット** (David):  
    `Of course! We've got more buses than you can shake a stick at. What an odd question.`
*   **ルーク** (Luke Triton) *(<A3/2>)*:  
    `Brilliant! Did you hear that, Professor? The buses are running!`
*   **レイトン** (Professor Hershel Layton) *(<A4/2>)*:  
    `I heard, Luke. Your exuberance is appreciated, but we don't want to unsettle our friend here.`
*   **デビット** (David):  
    `Crikey, I've never seen someone so chuffed about taking the bus.`
*   **デビット** (David) *(<A3/5>)*:  
    `Well, if you like buses, you're going to love this little number.`
*   **デビット** (David):  
    `You know, if you really like buses, solving a puzzle like this should be a breeze.`
*   **デビット** (David):  
    `Back to take my bus puzzle out for another spin, eh?`
*   **デビット** (David):  
    `You know, I'm something of a bus aficionado myself.`
*   **デビット** (David):  
    `The old double-deckers, mind. None of that bendy business.`
*   **デビット** (David):  
    `Did you manage to get a bus?`

### `04_025270.lbin.txt` — Flores / Flawless Florence

*   **フローレス** (Flores):  
    `Well hello again, boys! I trust you've found yourselves some nice, shiny hint coins?`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `We have, thanks in no small part to your expert direction.`
*   **フローレス** (Flores):  
    `Delighted to be of assistance. So where's my thank you?`
*   **レイトン** (Professor Hershel Layton):  
    `Of course, madam. Please forgive me for not issuing proper thanks. We're very grateful for your help.`
*   **ルーク** (Luke Triton) *(<A3/2>)*:  
    `Yes, thank you. We never would have found them without the help of a wise old lady like yourself!`
*   **フローレス** (Flores) *(<A1/3>)*:  
    `Now, just a moment there, half-pint! Who are you calling old?`
*   **フローレス** (Flores):  
    `They don't call me Flawless Florence for nothing, you know! I'm as fit and nimble as a teenager!`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `I'm sorry, I didn't mean to call you old!`
*   **ルーク** (Luke Triton):  
    `I know how sensitive some elderly people can be about their age.`
*   **フローレス** (Flores):  
    `E-elderly?! Well, I never!`
*   **フローレス** (Flores):  
    `Looks like I'll have to teach you a lesson the old-fashioned way - with a puzzle!`
*   **フローレス** (Flores):  
    `What's the matter, boy? Do you need a rest?`
*   **フローレス** (Flores):  
    `If you're truly sorry about calling me old, you'll show me by solving this puzzle!`
*   **フローレス** (Flores):  
    `Hmph. You two are pretty sharp when it comes to puzzle solving, I'll give you that.`
*   **レイトン** (Professor Hershel Layton):  
    `The compliment means all the more coming from a lady such as yourself, Florence.`
*   **レイトン** (Professor Hershel Layton):  
    `I do hope our paths cross again sometime.`
*   **フローレス** (Flores):  
    `Tee hee! Now you're making me blush.`
*   **フローレス** (Flores):  
    `You can sweet-talk me all you like, but you should know I'm a married woman.`
*   **ルーク** (Luke Triton):  
    `I think that lady has taken a shine to you, Professor...`
*   **フローレス** (Flores):  
    `Such fine manners, and famous too! Maybe we should get to know each other better.`
*   **フローレス** (Flores):  
    `May I call you by your first name, Professor? Tee hee!`

### `04_025280.lbin.txt` — Ônibus para Gressenheller

*   **レイトン** (Professor Hershel Layton):  
    `Let's make our way back to my office. Now then, which bus goes to Gressenheller University?`

### `04_025300.lbin.txt` — Recap no ônibus

*   **OPルーク２** (Past Luke):  
    `I have to admit that all this time travelling has got me muddled.`
*   **OPルーク２** (Past Luke):  
    `What are we investigating now?`
*   **OPレイトン２** (Past Layton) *(<A2/2>)*:  
    `Ho ho! Feeling a bit disoriented, I see? I can hardly blame you.`
*   **OPルーク２** (Past Luke):  
    `It's not every day that I travel to the future and meet my older self, you know.`
*   **OPルーク２** (Past Luke):  
    `I think I could do with a bit of a recap of our case.`
*   **OPレイトン２** (Past Layton):  
    `Very well. Let's go back over it.`
*   **OPレイトン２** (Past Layton):  
    `Do you remember why Big Luke called us to the future?`
*   **OPルーク２** (Past Luke):  
    `To stop the evil Professor Layton.`
*   **OPレイトン２** (Past Layton):  
    `And what exactly are we stopping my future self from doing?`
*   **OPルーク２** (Past Luke):  
    `Er... Oh right! We want to stop you, I mean him, from completing his time machine research!`
*   **OPレイトン２** (Past Layton):  
    `Precisely. And that's why you and I were headed for Chinatown.`
*   **OPルーク２** (Past Luke):  
    `Oh yes. It's becoming a bit less jumbled now.`
*   **OPルーク２** (Past Luke):  
    `We couldn't get into Chinatown in the end.`
*   **OPルーク２** (Past Luke):  
    `It was at that point that you said it would be useful if we could talk to the inspector.`
*   **OPレイトン２** (Past Layton):  
    `Yes, but at the time I had no idea we'd be able to jump back to our own time to question him.`
*   **OPルーク２** (Past Luke):  
    `In that sense, I suppose we were pretty lucky, eh?`
*   **OPレイトン２** (Past Layton):  
    `Hmm. Perhaps.`
*   **OPルーク２** (Past Luke):  
    `Perhaps? Why, what's wrong? Is there something bothering you?`
*   **OPレイトン２** (Past Layton):  
    `There is, and it's that something that we've come to investigate.`
*   **OPレイトン２** (Past Layton):  
    `Oh! We've just about reached our stop.`
*   **OPレイトン２** (Past Layton):  
    `We'll drop by my office and then it's off to see the inspector.`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `04_025130` | **Lore do Farol** | Evento de diálogo - farol construído há 5 anos no meio do Thames, localização sem propósito, indica construção recente de Future London. |
| `04_025131` + `04_025132` | **Parrot / Briefcase Enigma** | Enigma de inventário - recuperar garnet do fundo da maleta desorganizada de Graham para atrair papagaio que roubou cufflinks. Gag de shiny objects. |
| `04_025134` | **Recompensa Parrot** | Minigame desbloqueado: Parrot - ter papagaio brincando com Luke para aprender o básico, placeholder `<N1>` para nome escolhido pelo jogador. |
| `04_025136` + `04_025138` | **Belle / Clothing Line** | Lore - Graham pretende propor parceria de linha de roupas a Belle (radiant goddess, muse), precisa de cravat nova. Conexão com Belle do Cap. 02. |
| `04_025140`–`04_025145` | **Atalho para Midland Road** | Navegação - Future Luke conhece atalho à esquerda que corta metade do tempo até a relojoaria. |
| `04_025160` | **Enigma da Porta Numérica + Nicola** | Enigma de bloqueio com números embutidos na porta; falha técnica resolvida com força bruta (empurrão) revelando Nicola dormindo contra a porta - gag de enigma com resposta física. |
| `04_025170`–`04_025180` | **Secret Knock** | Evento - batida secreta que abre a relojoaria; Spring/Mrs. Cogg reconhece e revela aliança com Future Luke. |
| `04_025200` | **Exposição do Wormhole** | Evento narrativo central (401 linhas) - Cogg explica origem do wormhole num relógio de 100 anos, invasão da Family financiando máquina do tempo (vortex), warps gravitam para o relógio antigo, Cogg como único operador coagido, aliança com Future Luke para enviar carta. |
| `04_025215` / `04_025216` | **Portão de 30 Enigmas** | Bloqueio de progressão clássico de Layton - exige 30 enigmas resolvidos para Cogg ativar o wormhole e retornar ao presente; caso contrário, "do a bit more research". |
| `04_025230` | **Time Sickness** | Evento - enjoo pós-salto (ouvidos tampados, chão de marshmallow); Cogg revela que primeira viagem também causou mal-estar; instrução de retorno via secret knock. |
| `04_025240`–`04_025280` | **Retorno ao Presente - Contraste Temporal** | Sequência de validação - ônibus voltam a circular (vs. futuro sem ônibus), David fã de double-deckers, Flores cobra agradecimento, prompt para Gressenheller University. Confirma salto bem-sucedido 10 anos atrás. |
| `04_025250` | **Picarats / Stachenscarfen** | Tutorial recorrente - Dica Coach tenta explicar picarats, é interrompido ("we already know"), insiste em enigma. |
| `04_025270` | **Flawless Florence Enigma** | Enigma punitivo - Flores desafia Luke por chamá-la de velha/elderly, exige resolver enigma como pedido de desculpas. |
| `04_025300` | **Recap no Ônibus** | Evento de recapitulação - OP Layton/Luke revisam missão (Big Luke, evil Layton, time machine, Chinatown, inspector Chelmey) a caminho de Gressenheller. |

**Eventos narrativos sem enigmas diretos:** adiamento do Pagode em Chinatown, discussão sobre o farol, observação do observatório, despedida de Future Luke que permanece no futuro para evitar paradoxo.

---

## 6. Notas de Localização & Observações Técnicas

*   **Agrupamento de voz:** Nenhum `<Vxxxx>` dublado neste capítulo; todo o texto é de exploração `<T>` não-dublado. Isso confirma que o Cap. 04 é majoritariamente transição / exposição via Cogg, sem cutscene dublada - contrastando com o prólogo e Cap. 02.
*   **Placeholder de nome:** `04_025132` / `04_025134` contêm `<N1>` - nome do papagaio escolhido pelo jogador (ex.: similar a `<N>` do prólogo). A frase `I'm <N1>!` é dita pelo próprio pássaro, e a recompensa repete "You have a new feathered friend, <N1> the parrot!" Duplicação intencional entre diálogo e narração de minigame.
*   **Nomes internos vs. externos:** `サマリー` (Samarī = Spring) é chamada "Spring" por Future Luke em inglês, mas "Mrs. Cogg" / "Summary" em outros arquivos; `グラハム` = Graham, `オウム` = parrot, `ゴロッキー` / `ピランチ` = Gorocky / Piranchi (grafias aproximadas de fan-translation, mantidas como Family Goons), `ヒゲマフラー` = Stachenscarfen (auto-batismo em `04_025250`).
*   **Texto repetido / gating:** `04_025215` e `04_025216` são variações condicionais do mesmo checkpoint (≥30 enigmas vs. <30 enigmas) - padrão Level-5 para bloquear retorno até o jogador estar suficientemente avançado no Índice de Enigmas. Ambos compartilham prefixos mas divergem em permissão/bloqueio.
*   **Bloco centralizado:** `04_025180` usa `<J54>Tee hee hoo! Well, look who's back.<Q><K></J>` - raro tag `<J>` de justificação/centro para fala misteriosa de Spring escondida.
*   **Efeitos sonoros:** `04_025160` usa `<S310>` para som de porta; `04_025132` usa múltiplos `Awwwrk!` / `Skwaaarka` sem tag de animação vocal, indicando efeitos sonoros de papagaio não-dublados.
*   **Continuidade:** O capítulo conecta diretamente o Cap. 03 (saída de Chinatown → relojoaria) ao Cap. 05 (investigação no presente com Chelmey/Gressenheller). O portão de 30 enigmas e a mecânica do secret knock estabelecem o wormhole como sistema de viagem recorrente para o resto do jogo.
*   **Dumps vazios:** Apenas 1 arquivo vazio (`04_000000`), menor taxa de padding que capítulos anteriores, indicando capítulo denso em conteúdo e sem muitos separadores.

---

*Gerado a partir de dumps LSCR brutos — 26/26 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/04`. Próximo capítulo: `05` — Investigação no Presente (Gressenheller / Chelmey).*
