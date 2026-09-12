# Extras 20 — Sistema de Enigmas Perdidos, Tutoriais, Pós-Jogo e Transições Temporais | Professor Layton and the Unwound Future

> **Extras 20 — Sistema de Enigmas Perdidos / Tutoriais / Pós-Jogo (Não é Capítulo de História)** — Análise de dump LSCR para `Textos Originais/txt/uk/20/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/20/`
> Total de arquivos escaneados: **60** — **conteúdo extra, não capítulo narrativo**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão, `<J>` = jump, `<CR>` = controle de interface
> Natureza: **Extras / Sistema + Tutoriais + Pós-Jogo** — sem progressão linear; gerencia enigmas perdidos (flor/bee/house), explica minijogos, cobre arco do mural de Slate, transições de time travel via Cogg/Jack e mensagens de conclusão 100%

---

## 1. Arquivos Cobertos — Compendium Extra

Todos os 60 dumps `.lbin.txt` em `uk/20` — **conteúdo extra de sistema, não capítulo de história**. Organização por blocos numéricos (prefixo do nome do arquivo):

- **000000 — Cabeçalho vazio (1 arquivo):** `20_000000` sem blocos de texto — apenas `[7017010000000000:0000000000]`.
- **011xxx / 015xxx / 033xxx — Gatilhos pontuais de lore (3 arquivos com texto):** `011100` Granny Riddleton retirement + `015170` parrot + `033700` Subject 3 extendido dublado (rabbit turf / lab tests).
- **071xxx–073xxx — Sistema de enigmas perdidos: a casa/shack e a abelha (3 arquivos):** `071000` Beasly sigh + `072000` Nazoline/tiny house + `073000` Beasly magnetic personality/flower — tutoriais diegéticos do hub de enigmas esquecidos.
- **0750xx–0751xx — Cotidiano do London futuro: arco do mural de Slate/Damian + NPCs (18 arquivos):** `075000`–`075120` progressão completa do mural (de graffiti a work of art unrivalled) + `075130` Barton pork bun + `075140`/`075145` Cogg dica + `075150` Flora/Luke restaurante + `075160` Bostro dejected após Dimitri vansish.
- **0752xx — Transições, tutoriais de exploração e demo (14 arquivos):** `075200` demo conclusion + `075220` curious flower/insect + `075230` locked place + `075240`–`075248` 8 variações de Jack/Cogg time travel switch + `075250` Hidden Door bonus + `075260` enigmas que desaparecem/certain spot + `075270` quebra no casino/trespassing + `075280` door locked.
- **07529xx–07535xx — Pós-jogo e Bonuses (7 arquivos):** `075290` 153 enigmas + `075300` every enigma in story mode + `075310` every enigma in the game + `075320` livro ilustrados → Storyteller's House + `075330` toy car → Hotelier's House + `075340` parrot → Delivery Bird's House + `075350` save pós-fortress (resume inside mobile fortress).
- **07536xx–07539xx — Instruções de minijogos (5 arquivos):** `075360` livro ilustrado adesivos (14 blocos) + `075370` toy car tiles/bridges (21 blocos) + `075380`/`075385` parrot delivery ropes/perches (16–17 blocos duplicados) + `075390` Flora procura Luke + Beasly busting fourth wall no brick courtyard.
- **07540xx–07547xx — Flor de enigmas perdidos + fluxo temporal (8 arquivos):** `075400` Future Luke flower/attracts enigmas/Venus flytrap + `075410` Beasly 6 vozes ``Oi! That flower keeps hold of puzzles`` + `075420` Future Luke fica por anomalies + `075430`/`075440` Chelmey/Future Luke ficam com Jack switch + `075450`/`075460`/`075470` retornos Welcome back.

Lista completa:

```
20_000000.lbin.txt  — [vazio - apenas cabeçalho]
20_011100.lbin.txt  — Granny Riddleton se despede: holidays e puzzles perdidos vão para a flor
20_015170.lbin.txt  — Parrot no céu, Layton identifica e Luke tenta falar
20_033700.lbin.txt  — Subject 3 estendido dublado: rabbit turf, torture tests, light/dark room, heavy burden
20_071000.lbin.txt  — Beasly (bee) sigh: magnetic personality bloco inicial
20_072000.lbin.txt  — Nazoline e a tiny house dos puzzles perdidos
20_073000.lbin.txt  — Beasly explica: tap the flower, magnetic personality
20_075000.lbin.txt  — Slate/Damian: parede grafitada, plano de mural
20_075010.lbin.txt  — Slate se apresenta: big plans for this wall
20_075020.lbin.txt  — Progresso do mural: coming along nicely
20_075030.lbin.txt  — Mural: We're making real progress
20_075040.lbin.txt  — Mural: Hello friends, Swimmingly
20_075050.lbin.txt  — Mural: outline finished by next visit
20_075060.lbin.txt  — Mural: rough sketch, puzzle sobre painting
20_075070.lbin.txt  — Mural: kids will have coloured in some more
20_075080.lbin.txt  — Mural: spectator vs painter, kids doing great job
20_075090.lbin.txt  — Mural: Come back soon to have a look
20_075100.lbin.txt  — Mural: almost finished, paint pots puzzle
20_075110.lbin.txt  — Mural: My mural is nearly finished!
20_075120.lbin.txt  — Mural concluído: Perfect timing, work of art unrivalled in all of London
20_075130.lbin.txt  — Barton e pork bun: Scotland Yard solid meal
20_075140.lbin.txt  — Guide: If you're looking to do a little time travelling, talk to Cogg
20_075145.lbin.txt  — Guide duplicado: talk to Cogg (variante)
20_075150.lbin.txt  — Flora & Luke no restaurante: Victory meal, half the menu
20_075160.lbin.txt  — Bostro abatido: Mr Layton/Dimitri up and left, sensitive side
20_075200.lbin.txt  — Demo end: This concludes the demo of Lost Future
20_075220.lbin.txt  — Flor curiosa e insect buzzing
20_075230.lbin.txt  — Lugar trancado: This place is all locked up, try again later
20_075240.lbin.txt  — Jack: Want to travel back to your own time?
20_075241.lbin.txt  — Jack: Fancy a trip back to your London?
20_075242.lbin.txt  — Jack: Ready to go back to your own time?
20_075243.lbin.txt  — Jack: Are you wanting to travel back to your own time?
20_075245.lbin.txt  — Jack: Ready to leap forward into the future again?
20_075246.lbin.txt  — Jack: I take it you'd like me to help you return to the future?
20_075247.lbin.txt  — Jack: Want to go to the future again?
20_075248.lbin.txt  — Jack: So am I taking you back to the future again?
20_075250.lbin.txt  — Hidden Door bonus: outside The Hidden Door for this game, gift puzzle
20_075260.lbin.txt  — Tutorial de investigação: puzzles desaparecem, vão para certain spot
20_075270.lbin.txt  — Quebra no casino: Cripes! It broke! trespassing e damage
20_075280.lbin.txt  — Porta trancada: This door seems to be locked
20_075290.lbin.txt  — Pós-história: 153 puzzles, Bonuses section
20_075300.lbin.txt  — 100% story puzzles: solved every puzzle in story mode, Challenges/Weekly
20_075310.lbin.txt  — 100% total puzzles: solved every puzzle in the game, Weekly Puzzles
20_075320.lbin.txt  — Picture books complete: Storyteller's House added to Challenges
20_075330.lbin.txt  — Toy car complete: Hotelier's House added to Challenges
20_075340.lbin.txt  — Parrot delivery complete: Delivery Bird's House added to Challenges
20_075350.lbin.txt  — Save pós-fortress: resume inside mobile fortress, hunt for missed puzzles
20_075360.lbin.txt  — Instruções picture book: stickers, Place/Remove, 3 books
20_075370.lbin.txt  — Instruções toy car: tiles, bridges, jumps, arrows, Clear/Go
20_075380.lbin.txt  — Instruções parrot delivery: ropes, perches, Clear/Start/Quit
20_075385.lbin.txt  — Instruções parrot delivery (variante expandida) — duplicata de 075380
20_075390.lbin.txt  — Flora procura Luke + Beasly commentary: statue in brick courtyard, honey-grabbers
20_075400.lbin.txt  — Future Luke: peculiar flower in abandoned shop on Midland Road, Venus flytrap for puzzles
20_075410.lbin.txt  — Beasly dublado (6 vozes): Oi! That flower keeps hold of puzzles, tap it!
20_075420.lbin.txt  — Future Luke fica: fear anomalies, stay here until you return, Jack Let's be off!
20_075430.lbin.txt  — Chelmey fica: Heading back already? Jack flipping the switch now!
20_075440.lbin.txt  — Chelmey + Future Luke ficam: both stay behind, Jack Here we go!
20_075450.lbin.txt  — Future Luke retorno: Welcome back, Professor. Right, let's return to town
20_075460.lbin.txt  — Chelmey retorno: Ah Layton, good to see you made it back, Let's be on our way
20_075470.lbin.txt  — Chelmey + Future Luke retorno: Welcome back, ready to return to business
```

> **Nota (Extras):** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `20_000000.lbin.txt`. **Alta densidade de dublagem apenas em `20_033700` (Subject 3) e `20_075410` (Beasly com V0010–V0060)** — os demais são não-dublados ou com `<A>/<K>` pontuais. **Nenhum arquivo deste extra é enigma jogável** — todo o conteúdo são gatilhos de sistema/tutorial ou vinhetas de NPC. `20_011100` ancora a aposentadoria de Granny Riddleton; `20_075000`–`075120` formam arco serializado do mural de Slate (13 estados); `20_075240`–`075248` são 8 variações de uma mesma linha de Jack para time travel; `20_075400`/`075410` formam díptico da flor de Midland Road (Venus flytrap for enigmas); `20_075290`–`075350` concentram mensagens de 100% e unlocks de Layton's Challenges (Storyteller/Hotelier/Delivery Bird).

---

## 2. Personagens / NPCs / Sistema (Conteúdo Extra — Não Elenco de Capítulo Narrativo)

> **Aviso de template Extras:** esta seção lista **doadores de sistema / NPCs de tutorial e vinheta**, não elenco dramático de capítulo. Não há protagonista/antagonista ou arco narrativo jogável — cada personagem entrega instrução, flavor ou transição temporal no London extra. Mantida a tabela bilíngue JP→EN para referência de localização, com papel como *system/NPC giver*.

| Tag Japonês | Nome em Inglês | Papel no Extras 20 (Sistema / NPC) |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Em ~10 arquivos: reage a Granny Riddleton, parrot, mural, Hidden Door gift, time travel com Future Luke/Chelmey/Jack |
| `ルーク` | **Luke Triton** | Em ~18 arquivos: interlocutor principal — lugar bagunçado, papagaio amigável, Assunto 3, mural, Barton, Bostro, flor/inseto, invasão ao cassino |
| `未来ルーク` | **Future Luke** | Em `075400` planta carnívora para enigmas + `075420` teme anomalias e fica aqui + `075440` permanece para trás + `075450`/`075470` "Welcome back" |
| `アロマ` | **Flora Reinhold (Aroma)** | Em `075150` refeição da vitória ("What are you going to have, Luke?") e `075390` procura Luke ("Say, have you seen Luke?") |
| `チェルミー` | **Inspector Chelmey** | Em `075430`/`075440` "Heading back already, Layton? I've still got a few leads" + `075460`/`075470` retorno "Ah Layton, good to see you made it back" |
| `３号` | **Subject 3** | Em `033700` dublado extenso (V0011–V0281): "Mr Rabbit"? território do coelho, animal de laboratório, ID Assunto 3, sala escura/unhas, peso sobre Layton |
| `ナゾーバ` / `ナゾービー` | **Granny Riddleton / Beasly (Enigma Bee)** | `011100` Granny Riddleton linda/clarividente, aposentadoria/férias cuidando de enigmas ("beautiful and clairvoyant Granny Riddleton") + `071000`/`073000`/`075410` abelha Beasly personalidade magnética, Bzzzz, 6 vozes dubladas |
| `ナゾリーヌ` | **Nazoline (Enigma House Keeper)** | Em `072000` 13 blocos: casinha minúscula ali, enigmas perdidos, "Touch that tiny house" |
| `ダミアン` | **Damian / Slate** | Em `075000`–`075120` arco de 13 estados: grafite → parede branca → contorno do mural → crianças pintando → "Perfect timing, finished mural" (obra belíssima sem igual) |
| `バートン（食）` | **Constable Barton** | Em `075130` bolinho de porco: "Veteran officers can't fight crime on empty stomach" |
| `ボストロ` | **Bostro** | Em `075160` abatido sem Dimitri: "Hmm? Oh it's you" / "'E's my boss. And now 'e's gone" / "vanished with that Hawks bloke" |
| `サマリー` | **Summary / Guide** | Em `075140`/`075145` dica neutra: "If you're looking to do a little time travelling, you should talk to Cogg." |
| `ジャック` | **Jack (Cogg / Switch Operator)** | Em `075240`–`075248` (8 variações) + `075420`–`075440`: "Want to travel back" / "Fancy a trip" / "Ready to leap forward" / "Let's be off!" / "flipping the switch" |
| `ナレーション` | **Narration / System** | Em `075200` fim da demonstração + `075260` tutorial de enigmas que desaparecem + `075290`–`075360` 153 enigmas/Bônus + `075360`–`075385` instruções de minijogos (adesivos/ladrilhos/cordas) |

Tags de controle observadas: `<V>` dublado presente apenas em `033700` (V0011–V0281, rabbit torture monologue) e `075410` (V0010–V0060, Beasly flower); `<A1/*>`–`<A6/*>` animações frequentes em Luke/Layton/Beasly/Bostro (ex.: `<A1/5>` This place is a mess, `<A4/1>` magnetic personality); `<K>` apenas em `075160` Hmm?; `<W>` pausas curtas em B-beautiful?, Hmm?, etc.; placeholders `{''}` em `033700` {''}Mr Rabbit{''} / {''}Subject 3{''} e `072000` {''}Solve me{''}; `<CR>` interface em `075360` Place/Remove, `075370` Clear/Go!, `075380` Clear/Start!/Quit; `<Q><J>` apenas em `075300`–`075340` Congratulations unlocks.

---

## 3. Visão Geral do Conteúdo Extra (Organização do Compendium — Sistema e Pós-Jogo)

> **Este não é um capítulo de história.** Extras 20 é um **compêndio de sistema/tutoriais/pós-jogo**, jogável dentro e após o clímax narrativo mas sem progressão linear de plot. Os 59 arquivos com texto são gatilhos autocontidos que gerenciam enigmas perdidos, explicam minijogos e costuram transições temporais e estado de London. Não há ordem cronológica obrigatória — exceto o arco do mural de Slate (`075000`→`075120`) que progride por visitas.

### 3.1 Organização por Blocos Numéricos

| Bloco | Quantidade | Prefixo | Quem fala | Função no extra |
|---|---|---|---|---|
| **Cabeçalho** | 1 | `000000` | — | `[7017010000000000:0000000000]` sem blocos de texto |
| **Lore pontual dublado** | 3 | `011100`/`015170`/`033700` | Luke/Layton/Narration + Subject 3 + Granny Riddleton/Beasly | Vinhetas com dublagem: Granny aposentadoria + parrot + rabbit torture history (únicos `<V>` do bloco) |
| **Sistema enigmas perdidos** | 3 | `071000`–`073000` | Beasly / Nazoline | Tutoriais diegéticos: tiny house, flower, magnetic personality — hub onde enigmas esquecidos se reúnem |
| **London vivo: mural + NPCs** | 18 | `075000`–`075160` | Slate, Luke/Layton, Barton, Flora, Bostro, Guide | Arco serializado da parede grafitada ao mural + vinhetas gastronômicas/dejected |
| **Transições & tutoriais** | 14 | `075200`–`075280` | Narration, Luke/Layton, Jack | Demo end, locked places, Hidden Door gift, quebra no casino, e 8 variações de switch de viagem no tempo |
| **Pós-jogo & Bonuses** | 7 | `075290`–`075350` | Narration | Mensagens de 100% (153 enigmas), Weekly Enigmas, unlocks de Layton's Challenges, save pós-fortress |
| **Minijogos** | 5 | `075360`–`075390` | Narration + Flora/Beasly | Instruções detalhadas: livro ilustrado adesivos (14 blocos), toy car tiles (21 blocos), parrot ropes (16–17 blocos) |
| **Flor & fluxo temporal** | 8 | `075400`–`075470` | Future Luke, Beasly, Chelmey, Jack | Díptico da flor de Midland Road (Venus flytrap) + decisões de ficar/voltar com anomalies |

### 3.2 O Que Há em Cada Bloco (Amostra Fiel aos Arquivos — 1 a 2 Citações por Arquivo)

**011xxx/015xxx/033xxx — Lore pontual (únicos dublados):** Granny Riddleton se despede da gerência de enigmas perdidos (`011100` ``Before you stands the beautiful and clairvoyant Granny Riddleton.`` + ``I think it's time for me to retire... I'm getting tired.`` + ``I'm going off on a well-deserved holiday. I may never see you again``); Luke avista parrot (`015170` ``Look at the bird in the sky over there, Professor`` / ``That's no ordinary bird, Luke. It's a parrot.``); Subject 3 estendido dublado com backstory completo de lab (`033700` ``{''}Mr Rabbit{''}? Oh, puh-lease`` + ``This is my turf`` + ``I was kidnapped and sold as a lab animal.`` + ``There that the white coats started calling me {''}Subject 3{''}.`` + ``They'd throw me in a room and cut the lights. There'd be a loud noise, like nails on a blackboard.`` + ``The sooner you stop expecting good things to happen, the better off you'll be``).

**071xxx–073xxx — Hub de enigmas perdidos:** Beasly suspira por ser different from all the other bees (`071000` ``Ohh...`` / ``I'm different from all the other bees.`` + ``What's your story anyway, Beasly?``); Nazoline apresenta a tiny house (`072000` ``You know all those poor little enigmas you leave unsolved? ... They all live in that adorable little house over there`` + ``Touch that tiny house over there to say hello.`` + ``Can you hear all those poor enigmas crying, {''}Solve me{''}?``); Beasly duplo explica flower/magnetic personality (`073000` ``You know those enigmas you don't get around to solving? Well, they all come hang out with me.`` + ``I have what you might call one of them {''}magnetic personalities{''}.`` + ``Tap that flower over there to see a list of all the enigmas I've got.``).

**075000–075120 — Arco do mural de Slate/Damian (13 estados):** parede grafitada → lixa → branco → mural → kids painting → concluído (`075000` ``Tsk. Some people have no respect for others... Just look at this wall of mine`` + ``If I just paint this wall white again, I'm practically asking for it to be covered in graffiti.`` + ``maybe I should get someone to come by and paint a fancy mural``); `075010` ``I've got big plans for this wall... My name's Slate.``; `075060` ``I see you've managed to lay down a rough sketch of the whole mural.`` + ``Maybe this enigma about painting will help you pass the time.``; `075080` ``I'm more of a spectator than a painter... preparing paint, washing brushes``; `075100` ``one of the pots had this great enigma on the side...``; `075110` ``My mural is nearly finished!``; `075120` ``Perfect timing, fellows! We just finished the mural!`` + ``The mural is finished! It's a beautiful work of art unrivalled in all of London.``). Vinhetas paralelas: Barton (`075130` ``Oh pork bun! Om nom.`` + ``Veteran officers always say one can't possibly fight crime... on an empty stomach.``); Flora & Luke restaurante (`075150` ``We're finally going to have a meal here! Victory!`` + ``Oh Luke, you always order half the menu.``); Bostro dejected (`075160` ``That's 'cause Mr Layton - my boss - just levantou-se e saiu.`` / ``Well then 'e should 'ave taken me with 'im! I'm the best 'enchman 'e's ever 'ad!``). `075140`/`075145` dica Cogg duplicado (``If you're looking to do a little viagem no tempoling, you should talk to Cogg.``).

**075200–075280 — Demo / exploração / transições:** demo end (`075200` ``This concludes the demo of Professor Layton and the Lost Future.``); curiosidades de cenário (`075220` ``I can't stop looking at this curious flower and the strange little insect``; `075230` ``This place is all locked up.`` / ``It doesn't look as though anyone's there.``); Hidden Door bonus (`075250` ``We're standing outside The Hidden Door for this game.`` / ``Here's a little gift from us to you!`` + ``What a delightful enigma!``); tutorial de enigmas que somem (`075260` ``Some enigmas will disappear from their original locations`` + ``Most of your unsolved enigmas are sent off to a certain spot``); quebra no casino (`075270` ``Cripes! It broke!`` / ``Well what do you expect when you go around prodding everything?`` + ``Ah, so this is where it leads!``); porta fechada (`075280` ``This door seems to be locked.``); 8 variações de Jack/Cogg viagem no tempo switch (`075240` ``Want to travel back to your own time, do you?`` / `075241` ``Fancy a trip back to your London?`` / `075242` ``Ready to go back to your own time?`` / `075245` ``Ready to leap forward into the future again?`` / `075246` ``I take it you'd like me to help you return to the future?`` etc.).

**075290–075350 — Pós-jogo e unlocks:** fechamento de história → Bonuses (`075290` ``There are exactly 153 enigmas scattered throughout the story you've just completed.`` / ``A number of extra-challenging enigmas await you in the Bonuses section.``); 100% story (`075300` ``You've solved every enigma in the story mode... Congratulations!`` + ``try Layton's Challenges or the Weekly enigmas``); 100% total (`075310` ``You've solved every enigma in the game. Congratulations!``); unlocks (`075320` ``Congratulations! You've completed all the livro ilustrados! The Storyteller's House has been added...``; `075330` ``completed every course for your toy car! The Hotelier's House has been added``; `075340` ``With the help of your parrot, you've completed all delivery requests! The Delivery Bird's House has been added``); save pós-fortress (`075350` ``Since you've come to the end of the story, you will now have the chance to save the game.`` / ``you will resume play inside the mobile fortress.`` / ``you're free to return to town and hunt for items and enigmas that you may have missed.``).

**075360–075390 — Minijogos instruções:** livro ilustrado (`075360` ``Fill in the missing elements of the story by placing adesivos... Touch <CR>Place</C>`` / ``There are a total of three livro ilustrados``); toy car (`075370` ``Pick up all the items on the course and guide your car to the goal by placing tiles`` + ``When the car passes over a jump tile, it will leap over the next square`` + ``Touch <CR>Go!</C> to start your car.``); parrot delivery (`075380`/`075385` duplicado ``Your parrot has generously volunteered his services as a delivery bird.`` + ``Predict his flight path and use ropes to create perches`` + ``Ropes can't cross over each other...`` + ``Touch <CR>Start!</C> to send your parrot`` + ``if your parrot flies off the side of the screen or falls, you must start again.``); Flora procura Luke (`075390` ``Say, have you seen Luke around here?`` / ``Bzzzz bzzzzzzz`` + ``Luke? He's over by the statue in the brick courtyard! Hey! HEY! Are they even listening?``).

**075400–075470 — Flor de Midland Road + fluxo temporal:** Future Luke apresenta Venus flytrap for enigmas (`075400` ``Did you happen to notice that peculiar flower growing in the abandoned shop on Midland Road?`` / ``It supposedly attracts enigmas that have disappeared`` + ``Like a Venus flytrap for enigmas?!``); Beasly dublado com 6 vozes (`075410` ``Oi! Come by to dig into a few enigmas, did ya?`` + ``That flower keeps hold of enigmas you've left behind!`` + ``Leaving too many unsolved enigmas lying around can come back to sting you.`` + ``don't leave enigmas for tomorrow when you can solve them today!``); decisões de ficar (`075420` ``I fear that going back to your time could introduce additional anomalies`` / ``I've therefore decided to stay here until you return.`` + ``Let's be off!``; `075430` ``Heading back already, Layton? I've still got a few leads to chase`` + ``I'm flipping the switch now!``; `075440` ``I'm afraid I'll have to stay behind as well, Professor.`` + ``Here we go!``); retornos (`075450` ``Welcome back, Professor. Right, let's return to town.``; `075460` ``Ah Layton, good to see you made it back in one piece.``; `075470` ``Ah, there you are, Layton. I was beginning to wonder if you'd ever return.`` + ``Welcome back, Professor. Are you ready to return to our business here?``).

### 3.3 Como Usar Este Extra

- **Não é história linear:** pode ser jogado/consultado em qualquer ordem; o arco do mural (`075000`→`075120`) é o único com progressão visível por visitas sucessivas, mas sem pré-requisito rígido entre os demais arquivos.
- **Dublagem rara e pontual:** apenas `033700` (Subject 3, V0011–V0281) e `075410` (Beasly, V0010–V0060) têm voice acting; todos os outros 57 arquivos com texto usam apenas `<A>/<W>/<K>` ou narração pura.
- **Valor de sistema:** explica onde encontrar enigmas perdidos (flower/house/bee), como enigmas desaparecem (certain spot), e como tutoriais de minijogos funcionam — essencial para 100% e Bonuses.
- **Valor de construção de mundo:** fragmentos de London cenográfico pós-Fortaleza (mural comunitário, Barton com pork bun, Bostro órfão de Dimitri, Flora/Luke no restaurante, casino trespassing) + lore do lab de Subject 3 (white coats, dark room).
- **viagem no tempo hub:** as 8 variações de Jack + diálogos de Chelmey/Future Luke (`075420`–`075470`) são gatilhos de teleporte diegético via Cogg, sem enigma associado.

> **Fecho do extra:** sem fortress para derrubar nem Clive para desmascarar, Extras 20 devolve o jogo ao gesto essencial de cuidar dos deixados para trás — seja um enigma esquecido na flor de Midland Road, uma parede grafitada que vira mural comunitário, ou um carrinho e um papagaio à espera de tiles e cordas — reafirmando, fora da história, que o método gentleman também é manutenção cotidiana.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag)` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes. Cabeçalhos LSCR e separadores `!******************************!` omitidos por brevidade.

### `20_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `20_011100.lbin.txt` — Granny Riddleton se despede: holidays e puzzles perdidos vão para a flor

*   **ルーク** (Luke Triton):  
    `<T><A1/5>This place is a mess`

*   **ナレーション** (Narration / System):  
    `<T>Hold it right there, sonny boy`

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Augh`

*   **ナレーション** (Narration / System):  
    `<T>Ehee hee, oh yes. Wherever there
    are lost puzzles, there am I.`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Oh, it's you`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Have we met before?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>No? Well then, allow me to introduce
    myself`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Before you stands the beautiful and
    clairvoyant Granny Riddleton.`

*   **ルーク** (Luke Triton):  
    `<T><A1/6>B-beautiful?<W> Hmm, well you do
    look pretty good for your age, I
    suppose.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Watch your words, Luke`

*   **ナゾーバ** (Granny Riddleton):  
    `<T><A1/5>Have you ever noticed how many
    mysteries there are in the world?<W>
    How many puzzles?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Puzzles that tease your brain?
    Puzzles that bend your mind?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Puzzles that are just plain
    infuriating?`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Certainly.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>And what about the puzzles that you
    miss or leave unsolved? They've got
    to go somewhere, haven't they?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Where do they go, you ask?<W> Well,
    they come and stay with me`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>That's very good to know.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T><A1/1>Or I suppose I should say they used
    to come and stay with me. Things
    are about to change.`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>Are they?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>You might not be able to tell from
    my looks, but I'm no spring chicken.<W>
    Truth be told, I'm getting tired.`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Oh?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>I think it's time for me to retire
    from this puzzle-minding business.
    I've earned it.`

*   **ルーク** (Luke Triton):  
    `<T>But...`

*   **ルーク** (Luke Triton):  
    `<T><A1/3>You can't retire`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Are you saying that without me, you
    two would find yourselves in a
    pickle?`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>A huge pickle`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>How about the debonair gentleman
    in the top hat? What do you think?`

*   **レイトン** (Professor Hershel Layton):  
    `<T>I concur with my friend here.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Ehee hee.<W> Yep, I thought you might
    say that.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>But don't fret. I'll make sure you're
    taken care of.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>How?`

*   **ナゾーバ** (Granny Riddleton):  
    `<T><A1/6>Ehee hee`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Come back here when you've lost a
    few puzzles. It should all become
    clear then.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>Now, I know we just met, but you'll
    have to excuse me. I'm going off on
    a well-deserved holiday.`

*   **ナゾーバ** (Granny Riddleton):  
    `<T>I may never see you again, so
    ta-ta, and have a positively
    puzzly day`

*   **ルーク** (Luke Triton):  
    `<T>A...puzzly day?`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>What a strange conversation that
    was. Let's be sure to come back
    here later.`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Definitely.<W> Though that thing
    that's flying around is giving me the
    heebie-jeebies.`

*   **ルーク** (Luke Triton):  
    `<T>I wonder where Granny Riddleton is
    going on holiday?`

### `20_015170.lbin.txt` — Parrot no céu, Layton identifica e Luke tenta falar

*   **ルーク** (Luke Triton):  
    `<T><A3/2>Look at the bird in the sky over
    there, Professor`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>That's no ordinary bird, Luke. It's
    a parrot.<W> How do you suppose it got
    here?`

*   **ルーク** (Luke Triton):  
    `<T>Let's ask him`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>Ho ho`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>Aw.<W> I was just trying to be
    friendly...`

### `20_033700.lbin.txt` — Subject 3 estendido dublado: rabbit turf, torture tests, light/dark room, heavy burden

*   **ルーク** (Luke Triton):  
    `<T>Sorry, Mr Rabbit, I didn't mean to-</V>`

*   **３号** (Subject 3):  
    `<T>{''}Mr Rabbit{''}? Oh, puh-lease`

*   **３号** (Subject 3):  
    `<T><V0021>And don't get any stupid ideas
    about us being friends just
    because you know my name now`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>Of course not, Mr Subject 3. I
    don't mean to impose, but we really
    do need to pass through here.</V>`

*   **３号** (Subject 3):  
    `<T>Those puny ears of yours don't hear
    too well, do they, boy?</V>`

*   **３号** (Subject 3):  
    `<T><V0041>I thought I made it clear that this is
    my turf`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>But we just-</V>`

*   **３号** (Subject 3):  
    `<T><A3/5>Oh, shut your trap. Look, I'm not an
    unreasonable rabbit. But nothing's
    free, you know.</V>`

*   **３号** (Subject 3):  
    `<T><A3/5>If you want through that much,
    you're gonna have to solve this
    puzzle.</V>`

*   **３号** (Subject 3):  
    `<T><A2/5>You humans think you're so
    superior, but you can't even
    solve a simple puzzle`

*   **３号** (Subject 3):  
    `<T>Wipe that smug smile off your face`

*   **３号** (Subject 3):  
    `<T><A2/5>So, you solved it, eh?<W> Hmph. You're
    one of the cannier humans I've run
    into. I'll give you that.`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>So...how did you end up here anyway,
    Mr Subject 3? What's your story?`

*   **３号** (Subject 3):  
    `<T><A3/5>Wanna know more about this old
    rabbit, do you?`

*   **３号** (Subject 3):  
    `<T>Well get your hankie ready, 'cause
    my tale's a real tear-jerker`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Uh... All right.`

*   **３号** (Subject 3):  
    `<T><A3/5>I was born in the mean streets of
    London and separated from my
    parents at an early age.</V>`

*   **３号** (Subject 3):  
    `<T><V0101>I would never see them again.</V>`

*   **３号** (Subject 3):  
    `<T><A5/5>It wasn't long before I was
    kidnapped and sold as a lab animal.</V>`

*   **３号** (Subject 3):  
    `<T><V0111>I thought it couldn't get any worse.
    I was wrong.</V>`

*   **３号** (Subject 3):  
    `<T><A5/5>The research facility I was taken
    to was the most miserable place
    on earth.</V>`

*   **３号** (Subject 3):  
    `<T><V0131>It was there that the white coats
    started calling me {''}Subject 3{''}.</V>`

*   **ルーク** (Luke Triton):  
    `<T>That's a strange name.</V>`

*   **３号** (Subject 3):  
    `<T><A5/6>Yeah, that's 'cause it wasn't so
    much a name as an ID. I was a test
    subject, not a cuddly pet.</V>`

*   **３号** (Subject 3):  
    `<T><A5/1>There was a Subject 1 and a
    Subject 2 there, but who knows
    what happened to them?</V>`

*   **ルーク** (Luke Triton):  
    `<T><A2/1>I don't mean to stir up painful
    memories, but you said you were a
    test subject. So...</V>`

*   **３号** (Subject 3):  
    `<T><A3/5>You wanna know about the tests
    they did on me? Just thinking about
    it makes my fur stand on end.</V>`

*   **３号** (Subject 3):  
    `<T><V0181>Well, this was one of their
    favourite routines:</V>`

*   **３号** (Subject 3):  
    `<T><A3/5>They'd throw me in a room and cut
    the lights. There'd be a loud noise,
    like nails on a blackboard. </V>`

*   **３号** (Subject 3):  
    `<T>Next thing I know, I'm in a totally
    different room. Even now, I have
    no idea what they were doing.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>That sounds awful...</V>`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Have you two worked everything
    out?</V>`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>Did you hear Subject 3's terrible
    story?</V>`

*   **ルーク** (Luke Triton):  
    `<T><V0231>Apparently, he was forced to be a
    test subject in all these weird
    science experiments.</V>`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Our friend here carries a heavy
    burden on his shoulders.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>Poor little fellow...</V>`

*   **３号** (Subject 3):  
    `<T>{''}Poor little fellow{''}? Pah`

*   **３号** (Subject 3):  
    `<T><V0261>Life is hard, kid, and I've had it
    harder than most. None of it
    really matters.</V>`

*   **３号** (Subject 3):  
    `<T><V0262><A5/6>The sooner you stop expecting good
    things to happen, the better off
    you'll be`

*   **ルーク** (Luke Triton):  
    `<T><A1/3>What kind of attitude is that?
    You're free now and you've got
    your whole life ahead of you`

*   **３号** (Subject 3):  
    `<T><A1/1>Oh, so now you're gonna tell me how
    to live my life, eh?</V>`

*   **３号** (Subject 3):  
    `<T><V0281>Go on then, get outta my face
    before I bite the lot of you`

### `20_071000.lbin.txt` — Beasly (bee) sigh: magnetic personality bloco inicial

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/3>Ohh...`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>That's an awfully big sigh for such
    a small bee. What's the matter?`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/1>Well you know, even a honeybee
    like myself gets a little down in the
    dumps every now and then.`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>It must be awfully hard looking
    after of all those puzzles, being,
    you know, a bee.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Oh, that? No, that's a piece of
    cake, kid. My problem is that I'm
    different from all the other bees.`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>You can say that again. What's your
    story anyway, Beasly?`

### `20_072000.lbin.txt` — Nazoline e a tiny house dos puzzles perdidos

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>You know all those poor little
    puzzles you leave unsolved? Or
    the ones you just forget about?`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Well, there's no need to worry about
    them, because I give them a place
    to stay.`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T><A3/2>They all live in that adorable little
    house over there`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T><A3/2>All those lost little puzzles live in
    that teeny-weeny house over there.`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Isn't it just the cutest thing
    you've ever seen?</V>`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T><A3/2>See that tiny house over there?
    That's where all the darling little
    puzzles that you leave behind go.`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>You should definitely solve them
    when you get a chance, though. It
    hurts their feelings if you don't.</V>`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T><A3/2>The lost little puzzles would love
    to see you. Touch that tiny house
    over there to say hello.`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Go on`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T><A3/2>If you've missed any puzzles along
    the way, you can find them in that
    little house`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Just go and knock on the door`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Can you hear all those poor puzzles
    crying, {''}Solve me`

*   **ナゾリーヌ** (Nazoline (Puzzle House)):  
    `<T>Just touch the house to say hello
    to some of those lost puzzles.`

### `20_073000.lbin.txt` — Beasly explica: tap the flower, magnetic personality

*   **ルーク** (Luke Triton):  
    `<T><A1/2>Watch out, Professor`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>Now Luke, I'm sure he won't hurt us
    as long as we don't bother him.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>If you say so...</V>`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>You know, I've never seen a bee
    quite like this. Can you try talking
    to him, Luke?</V>`

*   **ルーク** (Luke Triton):  
    `<T>I suppose I can try.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/1>Well, look at Mr Tall Hat here.
    Clearly he knows a bee of
    distinction when he sees one.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Wow, you're not like any bee I've
    ever met.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/1>Isn't that what I just said? Well,
    it's true. I'm no run-of-the-hive
    bee, but I do try to blend in.</V>`

*   **ルーク** (Luke Triton):  
    `<T>You'd probably have better luck
    blending in if you didn't talk.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/2>Sure, whatever you say, smart guy.
    But listen, I've got something you
    should hear.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>You know those puzzles you don't
    get around to solving?<W> Well, they
    all come hang out with me.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>You see, I have what you might
    call one of them {''}magnetic
    personalities{''}.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>Wait, are you saying you've got the
    same job as Granny Riddleton?</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/1>Granny who? I don't know no
    grannies. But my name is Beasly.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/3>I'm going to tell you how to peruse
    those puzzles now, so listen good.</V>`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Oh, I'm all ears.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/2>Tap that flower over there to
    see a list of all the puzzles I've
    got. It's as simple as that.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>So, any time you get a craving to
    solve some of the puzzles you left
    behind, come here.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Did that all make sense? 'Cause
    people tell me I do tend to drone
    on.<W> Ha ha`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>It makes perfect sense.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/1>All right, then. You have fun with
    those puzzles, and I'll be here if
    you need me.</V>`

### `20_075000.lbin.txt` — Slate/Damian: parede grafitada, plano de mural

*   **ダミアン** (Damian / Slate):  
    `<T><A2/4>Tsk. Some people have no respect
    for others...`

*   **ルーク** (Luke Triton):  
    `<T>What seems to be the matter?`

*   **ダミアン** (Damian / Slate):  
    `<T>Just look at this wall of mine`

*   **ダミアン** (Damian / Slate):  
    `<T>I'm sure the little miscreant who did
    it is only having a laugh, but I'm the
    one who has to clean it up.`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>Hmm, that paint's completely dry.
    It looks like it would be really hard
    to strip it off.`

*   **ダミアン** (Damian / Slate):  
    `<T>I suppose I'll just have to paint
    over this mess.`

*   **ダミアン** (Damian / Slate):  
    `<T>While we're on the subject of
    painting, I might as well ask...<W>
    <A1/1>You ever heard this puzzle?`

*   **ダミアン** (Damian / Slate):  
    `<T>Giving you a little trouble, is
    it?`

*   **ダミアン** (Damian / Slate):  
    `<T>Let me tell you about that painting
    puzzle again.`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/5>Good thinking`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>Oh? What's that?`

*   **ダミアン** (Damian / Slate):  
    `<T>If I just paint this wall white again,
    I'm practically asking for it to
    be covered in graffiti.`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>So maybe I should get someone to
    come by and paint a fancy mural
    on it instead.`

*   **ダミアン** (Damian / Slate):  
    `<T>I mean, a white wall is one thing,
    but you'd have to be a real lout
    to graffiti a nice mural.`

*   **ルーク** (Luke Triton):  
    `<T><A4/2>That sounds like a good idea`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>Heh heh`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>A mural is exactly what this wall
    needs. Just thinking about it has
    got me all fired up`

### `20_075010.lbin.txt` — Slate se apresenta: big plans for this wall

*   **ダミアン** (Damian / Slate):  
    `<T>I've got big plans for this wall. I'm
    going to get someone to paint
    something amazing on here.`

*   **ダミアン** (Damian / Slate):  
    `<T>Oh, by the way, I don't think I
    introduced myself before. My
    name's Slate. Nice to meet you`

### `20_075020.lbin.txt` — Progresso do mural: coming along nicely

*   **ルーク** (Luke Triton):  
    `<T><A3/2>It looks like your mural is coming
    along nicely`

*   **ダミアン** (Damian / Slate):  
    `<T>Heh heh`

*   **ルーク** (Luke Triton):  
    `<T><A4/2>Well, it's looking great so far. I
    can't wait to see how it turns out`

### `20_075030.lbin.txt` — Mural: We're making real progress

*   **ダミアン** (Damian / Slate):  
    `<T>We're making real progress on this
    mural. Come by and have another
    peek at it later`

### `20_075040.lbin.txt` — Mural: Hello friends, Swimmingly

*   **ダミアン** (Damian / Slate):  
    `<T>Hello friends`

*   **レイトン** (Professor Hershel Layton):  
    `<T>How's the mural coming along?`

*   **ダミアン** (Damian / Slate):  
    `<T>Swimmingly`

### `20_075050.lbin.txt` — Mural: outline finished by next visit

*   **ダミアン** (Damian / Slate):  
    `<T>If everything stays on schedule,
    we'll have the outline finished by
    the next time you visit`

### `20_075060.lbin.txt` — Mural: rough sketch, puzzle sobre painting

*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>I see you've managed to lay down
    a rough sketch of the whole mural.
    It looks excellent.`

*   **ダミアン** (Damian / Slate):  
    `<T>Heh heh`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>So are you going to colour in the
    rest of the piece now?`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Of course`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/5>I bet you can hardly wait, eh?<W>
    Maybe this puzzle about painting
    will help you pass the time.`

*   **ダミアン** (Damian / Slate):  
    `<T>Was that puzzle too tough for you?
    Sorry about that`

*   **ダミアン** (Damian / Slate):  
    `<T>Ready to paint in an answer for this
    puzzle?`

*   **ダミアン** (Damian / Slate):  
    `<T><A2/1>You two certainly have a way with
    puzzles. I'm tickled pink.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Thank you, and good luck with the
    rest of your mural. I'm sure the
    finished work will be wonderful.`

*   **ダミアン** (Damian / Slate):  
    `<T><A4/6>Yep, you can count on that`

*   **ダミアン** (Damian / Slate):  
    `<T>I can hardly stand the wait myself`

### `20_075070.lbin.txt` — Mural: kids will have coloured in some more

*   **ダミアン** (Damian / Slate):  
    `<T>Next time you come by, the kids will
    have coloured in some more of the
    mural. I can't wait`

### `20_075080.lbin.txt` — Mural: spectator vs painter, kids doing great job

*   **ルーク** (Luke Triton):  
    `<T><A3/2>Wow`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/5>I'm pretty keen on them myself. Yep,
    the kids are doing a great job.`

*   **ルーク** (Luke Triton):  
    `<T><A4/1>The kids? You're not doing any of
    the painting yourself?`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Nah, I'm more of a spectator than
    a painter.`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>But I try to help the team as best
    I can by preparing paint, washing
    brushes and so on.`

*   **ルーク** (Luke Triton):  
    `<T><A3/2>Well, as long as you're having fun`

### `20_075090.lbin.txt` — Mural: Come back soon to have a look

*   **ダミアン** (Damian / Slate):  
    `<T>Come back soon to have a look at
    the mural`

### `20_075100.lbin.txt` — Mural: almost finished, paint pots puzzle

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>The mural looks as though it's
    almost finished`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Yep, we're pretty close now`

*   **ダミアン** (Damian / Slate):  
    `<T>Heh heh`

*   **ルーク** (Luke Triton):  
    `<T>Proud?<W> But didn't you say you have
    local children doing all the work?`

*   **ダミアン** (Damian / Slate):  
    `<T><A2/1>Well, they're doing the painting, but
    I've done a lot of the heavy lifting`

*   **ダミアン** (Damian / Slate):  
    `<T>Literally, in fact`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/5>You know, one of the pots had this
    great puzzle on the side of it.
    Here, have a look`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>My, you certainly have an affinity
    for paint, don't you?`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Couldn't solve it, eh? Yep, that
    puzzle's a real stumper.`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>This puzzle requires some serious
    thought.`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Wow, I think you two are the best
    puzzle solvers I've ever met`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>Well, we do get a lot of practice.`

*   **ダミアン** (Damian / Slate):  
    `<T><A4/6>Impressive stuff, though. Heh heh`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>You have to come back soon to see
    the greatest mural in London in its
    finished state.`

### `20_075110.lbin.txt` — Mural: My mural is nearly finished!

*   **ダミアン** (Damian / Slate):  
    `<T>My mural is nearly finished`

### `20_075120.lbin.txt` — Mural concluído: Perfect timing, work of art unrivalled in all of London

*   **ダミアン** (Damian / Slate):  
    `<T><A2/1>Perfect timing, fellows`

*   **ルーク** (Luke Triton):  
    `<T><A1/2>Oh great`

*   **ダミアン** (Damian / Slate):  
    `<T><A1/1>Thanks`

*   **ルーク** (Luke Triton):  
    `<T><A4/2>Don't forget to give yourself a
    pat on the back while you're at it`

*   **ルーク** (Luke Triton):  
    `<T>You may not have painted it, but
    you still put a lot of effort into
    that mural, Slate`

*   **ダミアン** (Damian / Slate):  
    `<T><A3/2>Heh heh`

### `20_075130.lbin.txt` — Barton e pork bun: Scotland Yard solid meal

*   **バートン（食）** (Constable Barton):  
    `<T>Oh pork bun`

*   **ルーク** (Luke Triton):  
    `<T>Aren't you supposed to be helping
    the inspector with his
    investigation, Constable?`

*   **バートン（食）** (Constable Barton):  
    `<T>Yes... But, well, there's an old
    saying in - chomp chomp -
    Scotland Yard.`

*   **バートン（食）** (Constable Barton):  
    `<T>Veteran officers always say one
    can't possibly fight crime - om
    nom - on an empty stomach.`

*   **バートン（食）** (Constable Barton):  
    `<T>A solid investigation begins with a
    solid meal.`

*   **ルーク** (Luke Triton):  
    `<T>I see... Well, if that's how they do
    it in Scotland Yard, who am I to
    argue?`

### `20_075140.lbin.txt` — Guide: If you're looking to do a little time travelling, talk to Cogg

*   **サマリー** (Summary / Guide (Cogg hint)):  
    `<T><A1/2>If you're looking to do a little time
    travelling, you should talk to Cogg.`

### `20_075145.lbin.txt` — Guide duplicado: talk to Cogg (variante)

*   **サマリー** (Summary / Guide (Cogg hint)):  
    `<T><A1/2>If you're looking to do a little time
    travelling, you should talk to Cogg.`

### `20_075150.lbin.txt` — Flora & Luke no restaurante: Victory meal, half the menu

*   **ルーク** (Luke Triton):  
    `<T><A4/2>We're finally going to have a meal
    here`

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>What are you going to have, Luke?`

*   **ルーク** (Luke Triton):  
    `<T>How about this?<W> Oh and this`

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Hee hee. Oh Luke, you always order
    half the menu.`

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Do you suppose the chef here would
    mind giving me a few cooking
    pointers?`

### `20_075160.lbin.txt` — Bostro abatido: Mr Layton/Dimitri up and left, sensitive side

*   **ボストロ** (Bostro):  
    `<T><A1/4><K>Hmm?<W></K> Oh, it's you.`

*   **ルーク** (Luke Triton):  
    `<T>Er... Hello there.<W> You seem quite a
    bit less, er, energetic than usual.`

*   **ボストロ** (Bostro):  
    `<T>That's 'cause Mr Layton - my boss -
    just up and left.`

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Oh, him?`

*   **ボストロ** (Bostro):  
    `<T>I don't care what 'is real name is.
    'E's my boss. And now 'e's gone.`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Is it really worth getting that
    upset over?`

*   **ボストロ** (Bostro):  
    `<T><A1/1>Course it is.<W> See, soon as we left
    the pagoda, 'e just vanished with
    that Hawks bloke.`

*   **ルーク** (Luke Triton):  
    `<T><A2/1>He was just trying to keep a low
    profile after his escape from here.`

*   **ボストロ** (Bostro):  
    `<T><A2/3>Well then 'e should 'ave taken me
    with 'im`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>Who would have guessed that Bostro
    had a sensitive side?`

### `20_075200.lbin.txt` — Demo end: This concludes the demo of Lost Future

*   **ナレーション** (Narration / System):  
    `<T>Nice work`

*   **ナレーション** (Narration / System):  
    `<T>This concludes the demo of
    Professor Layton and the Lost
    Future.`

*   **ナレーション** (Narration / System):  
    `<T>The adventure continues in the full
    version of the game`

### `20_075220.lbin.txt` — Flor curiosa e insect buzzing

*   **ルーク** (Luke Triton):  
    `<T><A3/1>I can't stop looking at this curious
    flower and the strange little insect
    that's buzzing around it.`

### `20_075230.lbin.txt` — Lugar trancado: This place is all locked up, try again mais tarde

*   **ルーク** (Luke Triton):  
    `<T>This place is all locked up.`

*   **レイトン** (Professor Hershel Layton):  
    `<T>It doesn't look as though anyone's
    there. Perhaps we should try again
    later.`

*   **ルーク** (Luke Triton):  
    `<T>Sounds good to me.`

### `20_075240.lbin.txt` — Jack: Want to travel back to your own time?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Want to travel back to your own
    time, do you?`

### `20_075241.lbin.txt` — Jack: Fancy a trip back to your London?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Fancy a trip back to your London?`

### `20_075242.lbin.txt` — Jack: Ready to go back to your own time?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Ready to go back to your own time?`

### `20_075243.lbin.txt` — Jack: Are you wanting to travel back to your own time?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Are you wanting to travel back to
    your own time?`

### `20_075245.lbin.txt` — Jack: Ready to leap forward into the future again?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Ready to leap forward into the
    future again?`

### `20_075246.lbin.txt` — Jack: I take it you'd like me to help you return to the future?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>I take it you'd like me to help you
    return to the future?`

### `20_075247.lbin.txt` — Jack: Want to go to the future again?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Want to go to the future again?`

### `20_075248.lbin.txt` — Jack: So am I taking you back to the future again?

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>So am I taking you back to the
    future again?`

### `20_075250.lbin.txt` — Hidden Door bonus: outside The Hidden Door for this game, gift puzzle

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Well, here we are, Luke. We're
    standing outside The Hidden Door
    for this game.`

*   **ルーク** (Luke Triton):  
    `<T><A2/2>Yep`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Itching to find out, are you?`

*   **ルーク** (Luke Triton):  
    `<T><A3/2>I certainly am`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>Well then, let's not keep you or our
    esteemed player in suspense any
    longer.`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Here's a little gift from us to you`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>What a delightful puzzle`

### `20_075260.lbin.txt` — Tutorial de investigação: puzzles desaparecem, vão para certain spot

*   **ナレーション** (Narration / System):  
    `<T>Are you getting used to moving
    around and investigating the city
    of London?`

*   **ナレーション** (Narration / System):  
    `<T>Well, here's some advice to keep
    your investigation running smoothly.`

*   **ナレーション** (Narration / System):  
    `<T>Some puzzles will disappear from
    their original locations as the
    story progresses.`

*   **ナレーション** (Narration / System):  
    `<T>But there's no need to worry`

*   **ナレーション** (Narration / System):  
    `<T>Most of your unsolved puzzles are
    sent off to a certain spot for
    you to solve at your leisure.`

*   **ナレーション** (Narration / System):  
    `<T>Visit there often to track down
    puzzles you missed, and try to
    complete every puzzle in the game.`

*   **ナレーション** (Narration / System):  
    `<T>Also, remember that some puzzles do
    not disappear from their original
    locations.`

*   **ナレーション** (Narration / System):  
    `<T>These puzzles can be solved at any
    time by returning to the place
    where you first found them.`

### `20_075270.lbin.txt` — Quebra no casino: Cripes! It broke! trespassing e damage

*   **ルーク** (Luke Triton):  
    `<T><A1/6>Cripes`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Well what do you expect when you
    go around prodding everything?`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>But Professor, I wasn't prodding
    it that hard`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/5>Luke...`

*   **ルーク** (Luke Triton):  
    `<T><A1/1>I'm sorry. I should probably be more
    careful.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Indeed you should.<W> Now let's see
    what kind of damage you've caused
    here.`

*   **レイトン** (Professor Hershel Layton):  
    `<T>What's this?<W> I do believe this leads
    somewhere interesting.<W><A2/2> Let's have
    a look at what's on the other side.`

*   **ルーク** (Luke Triton):  
    `<T><A1/6>But...isn't this trespassing,
    Professor?<W> P-Professor, wait
    for me`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Ah, so this is where it leads`

*   **ルーク** (Luke Triton):  
    `<T><A4/4>Can we leave now, Professor? The
    casino staff won't be happy if they
    find us in here...`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Ha ha`

*   **ルーク** (Luke Triton):  
    `<T>Maybe so, but I still think we should
    leave now`

### `20_075280.lbin.txt` — Porta trancada: This door seems to be locked

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>This door seems to be locked.`

### `20_075290.lbin.txt` — Pós-história: 153 puzzles, Bonuses section

*   **ナレーション** (Narration / System):  
    `<T>Did you enjoy Professor Layton and
    the Lost Future?`

*   **ナレーション** (Narration / System):  
    `<T>You have reached the end of the
    story, but the game is far from
    over`

*   **ナレーション** (Narration / System):  
    `<T>There are exactly 153 puzzles
    scattered throughout the story
    you've just completed.`

*   **ナレーション** (Narration / System):  
    `<T>See if you can complete each and
    every one of them`

*   **ナレーション** (Narration / System):  
    `<T>Be sure to check the Bonuses
    section. Unlock more bonus content
    by fulfilling certain conditions.`

*   **ナレーション** (Narration / System):  
    `<T>A number of extra-challenging
    puzzles await you in the Bonuses
    section.`

*   **ナレーション** (Narration / System):  
    `<T>See if you have what it takes to
    conquer some of the most baffling
    puzzles in the game.`

*   **ナレーション** (Narration / System):  
    `<T>Have fun with the rest of
    Professor Layton and the Lost
    Future`

### `20_075300.lbin.txt` — 100% story puzzles: solved every puzzle in story mode, Challenges/Weekly

*   **ナレーション** (Narration / System):  
    `<T>Did you enjoy Professor Layton
    and the Lost Future?`

*   **ナレーション** (Narration / System):  
    `<T>You've solved every puzzle in the
    story mode of this game.
    Congratulations`

*   **ナレーション** (Narration / System):  
    `<T>For more fun, try Layton's
    Challenges or the Weekly Puzzles
    in the Bonuses section.`

*   **ナレーション** (Narration / System):  
    `<T>Enjoy the rest of the game`

### `20_075310.lbin.txt` — 100% total puzzles: solved every puzzle in the game, Weekly Puzzles

*   **ナレーション** (Narration / System):  
    `<T>You've solved every puzzle in the
    game. Congratulations`

*   **ナレーション** (Narration / System):  
    `<T>For more fun, don't forget
    to try out the Weekly Puzzles`

*   **ナレーション** (Narration / System):  
    `<T>Enjoy the rest of the game`

### `20_075320.lbin.txt` — Picture books complete: Storyteller's House added to Challenges

*   **ナレーション** (Narration / System):  
    `<T>Congratulations`

*   **ナレーション** (Narration / System):  
    `<T>The Storyteller's House has been
    added to Layton's Challenges.`

### `20_075330.lbin.txt` — Toy car complete: Hotelier's House added to Challenges

*   **ナレーション** (Narration / System):  
    `<T>Congratulations`

*   **ナレーション** (Narration / System):  
    `<T>The Hotelier's House has been added
    to Layton's Challenges.`

### `20_075340.lbin.txt` — Parrot delivery complete: Delivery Bird's House added to Challenges

*   **ナレーション** (Narration / System):  
    `<T>Congratulations`

*   **ナレーション** (Narration / System):  
    `<T>The Delivery Bird's House has been
    added to Layton's Challenges.`

### `20_075350.lbin.txt` — Save pós-fortress: resume inside mobile fortress, hunt for missed puzzles

*   **ナレーション** (Narration / System):  
    `<T>Since you've come to the end of the
    story, you will now have the chance
    to save the game.`

*   **ナレーション** (Narration / System):  
    `<T>When you continue this saved game,
    you will resume play inside the
    mobile fortress.`

*   **ナレーション** (Narration / System):  
    `<T>From there, you're free to return
    to town and hunt for items and
    puzzles that you may have missed.`

*   **ナレーション** (Narration / System):  
    `<T>Since you've come to the end of the
    story, you will now have the chance
    to save the game.`

*   **ナレーション** (Narration / System):  
    `<T>When you continue this saved game,
    you will resume play inside the
    mobile fortress.`

### `20_075360.lbin.txt` — Instruções livro ilustrado: adesivos, Place/Remove, 3 books

*   **ナレーション** (Narration / System):  
    `<T>Fill in the missing elements of the
    story by placing stickers into each
    picture book.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Place</C> to display a bar
    containing all the stickers that
    you have collected for this book.`

*   **ナレーション** (Narration / System):  
    `<T>Touch a sticker and slide it to the
    position of your choice to stick
    it on the page.`

*   **ナレーション** (Narration / System):  
    `<T>To remove a sticker from the page,
    slide it back to the bar at the
    bottom of the Touch Screen.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Remove</C> to remove all the
    stickers from the picture book.`

*   **ナレーション** (Narration / System):  
    `<T>Touch the arrows on the left and
    right sides of the Touch Screen to
    turn the page.`

*   **ナレーション** (Narration / System):  
    `<T>The text on the top screen changes
    automatically to match the stickers
    you've placed.`

*   **ナレーション** (Narration / System):  
    `<T>Try to create a story that makes
    sense by placing all the stickers in
    the correct positions.`

*   **ナレーション** (Narration / System):  
    `<T>You'll collect more stickers as you
    play through the game and solve
    puzzles.`

*   **ナレーション** (Narration / System):  
    `<T>Solve as many puzzles as you can
    and try to collect every sticker.`

*   **ナレーション** (Narration / System):  
    `<T>There are a total of three picture
    books for you to complete.`

*   **ナレーション** (Narration / System):  
    `<T>Each picture book has its own set
    of stickers which can only be used
    in that book.`

*   **ナレーション** (Narration / System):  
    `<T>Complete the first picture book to
    unlock the second, and complete
    the second to unlock the third.`

*   **ナレーション** (Narration / System):  
    `<T>When you've successfully completed
    every picture book, something
    wonderful will happen`

### `20_075370.lbin.txt` — Instruções toy car: tiles, bridges, jumps, arrows, Clear/Go

*   **ナレーション** (Narration / System):  
    `<T>Pick up all the items on the course
    and guide your car to the goal by
    placing tiles in the correct spots.`

*   **ナレーション** (Narration / System):  
    `<T>The number and types of tiles
    available for you to use will be
    different for each course.`

*   **ナレーション** (Narration / System):  
    `<T>Place a tile by sliding it from the
    inventory on the right-hand side of
    the screen to the desired location.`

*   **ナレーション** (Narration / System):  
    `<T>You can put one tile on each square
    of the course.`

*   **ナレーション** (Narration / System):  
    `<T>You can only place tiles on standard
    terrain such as grass or sand.`

*   **ナレーション** (Narration / System):  
    `<T>Tiles can't be placed on squares
    that contain bridges, switches,
    trees, rocks or water.`

*   **ナレーション** (Narration / System):  
    `<T>When the car passes over a jump
    tile, it will leap over the next
    square no matter what it contains.`

*   **ナレーション** (Narration / System):  
    `<T>When the car passes over an arrow
    tile, it will turn and move in the
    direction of the arrow.`

*   **ナレーション** (Narration / System):  
    `<T>Once the car has passed over a
    tile, that tile will vanish from
    the course.`

*   **ナレーション** (Narration / System):  
    `<T>Touch your car to change the
    direction in which it will start
    moving.`

*   **ナレーション** (Narration / System):  
    `<T>Your car can only cross a bridge if
    there are no gaps in it.`

*   **ナレーション** (Narration / System):  
    `<T>Raise and lower bridges by guiding
    the car over the yellow switches
    on the course.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Clear</C> to return all the tiles
    you've placed to your inventory.`

*   **ナレーション** (Narration / System):  
    `<T>When all your tiles are in place,
    touch <CR>Go`

*   **ナレーション** (Narration / System):  
    `<T>If you've placed your tiles
    correctly, your car will zip around
    the course and reach the goal.`

*   **ナレーション** (Narration / System):  
    `<T>Just remember that reaching the
    goal alone isn't enough.`

*   **ナレーション** (Narration / System):  
    `<T>If you don't pick up every item on
    the course along the way, you won't
    clear the course.`

*   **ナレーション** (Narration / System):  
    `<T>If your car hits any obstacles
    along the way or drives off the
    course, you'll have to start again.`

*   **ナレーション** (Narration / System):  
    `<T>There are a total of 10 courses,
    which you can collect as you play
    through the game.`

*   **ナレーション** (Narration / System):  
    `<T>To collect every course, make sure
    you solve every puzzle you come
    across.`

*   **ナレーション** (Narration / System):  
    `<T>When you've conquered every course
    the game has to offer, something
    special will happen.`

### `20_075380.lbin.txt` — Instruções parrot delivery: ropes, perches, Clear/Start/Quit

*   **ナレーション** (Narration / System):  
    `<T>Your parrot has generously
    volunteered his services as a
    delivery bird.`

*   **ナレーション** (Narration / System):  
    `<T>Unfortunately, the heavy objects
    he has to carry make it hard for
    him to fly properly.`

*   **ナレーション** (Narration / System):  
    `<T>Predict his flight path and use
    ropes to create perches that
    will guide him to the recipient.`

*   **ナレーション** (Narration / System):  
    `<T>Create a perch for your parrot
    by connecting any two posts with a
    rope.`

*   **ナレーション** (Narration / System):  
    `<T>The number of ropes at your
    disposal changes with each delivery
    request.`

*   **ナレーション** (Narration / System):  
    `<T>The position and angle of each perch
    will affect your parrot's flight
    trajectory.`

*   **ナレーション** (Narration / System):  
    `<T>Build efficient perches that will
    help your parrot get to his
    destination as quickly as possible.`

*   **ナレーション** (Narration / System):  
    `<T>Ropes can't cross over each other.
    Also, you can't attach more than
    one rope to the same post.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Clear</C> to remove all the ropes
    you've drawn from the screen.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Start`

*   **ナレーション** (Narration / System):  
    `<T>If you want to cancel a delivery
    attempt while the parrot is flying,
    touch <CR>Quit</C>.`

*   **ナレーション** (Narration / System):  
    `<T>When the parrot lands on a flat
    perch, he will return to his basic
    flight path when he next takes off.`

*   **ナレーション** (Narration / System):  
    `<T>Using a number of well-placed
    perches, your parrot can fly to
    very high places.`

*   **ナレーション** (Narration / System):  
    `<T>Complete a course by guiding your
    parrot over to the delivery
    recipient.`

*   **ナレーション** (Narration / System):  
    `<T>During delivery, if your parrot
    flies off the side of the screen or
    falls, you must start again.`

*   **ナレーション** (Narration / System):  
    `<T>Your parrot must also reach the
    recipient before time runs out, so
    keep an eye on the time limit.`

### `20_075385.lbin.txt` — Instruções parrot delivery (variante expandida) — duplicata de 075380

*   **ナレーション** (Narration / System):  
    `<T>Your parrot has generously
    volunteered his services as a
    delivery bird.`

*   **ナレーション** (Narration / System):  
    `<T>Unfortunately, the heavy objects
    he has to carry make it hard for
    him to fly properly.`

*   **ナレーション** (Narration / System):  
    `<T>Predict his flight path and use
    ropes to create perches that
    will guide him to the recipient.`

*   **ナレーション** (Narration / System):  
    `<T>Create a perch for your parrot
    by connecting any two posts with a
    rope.`

*   **ナレーション** (Narration / System):  
    `<T>The number of ropes at your
    disposal changes with each
    delivery request.`

*   **ナレーション** (Narration / System):  
    `<T>The position and angle of each perch
    will affect your parrot's flight
    trajectory.`

*   **ナレーション** (Narration / System):  
    `<T>Build efficient perches that will
    help your parrot get to his
    destination as quickly as possible.`

*   **ナレーション** (Narration / System):  
    `<T>Ropes can't cross over each other.
    Also, you can't attach more than
    one rope to the same post.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Clear</C> to remove all the
    ropes you've drawn from the
    screen.`

*   **ナレーション** (Narration / System):  
    `<T>Touch <CR>Start`

*   **ナレーション** (Narration / System):  
    `<T>If you want to cancel a delivery
    attempt while the parrot is flying,
    touch <CR>Quit</C>.`

*   **ナレーション** (Narration / System):  
    `<T>When the parrot lands on a flat
    perch, he will return to his basic
    flight path when he next takes off.`

*   **ナレーション** (Narration / System):  
    `<T>Using a number of well-placed
    perches, your parrot can fly to
    very high places.`

*   **ナレーション** (Narration / System):  
    `<T>Complete a course by guiding
    your parrot over to the delivery
    recipient.`

*   **ナレーション** (Narration / System):  
    `<T>During delivery, if your parrot
    flies off the side of the screen or
    falls, you must start again.`

*   **ナレーション** (Narration / System):  
    `<T>Your parrot must also reach the
    recipient before time runs out, so
    keep an eye on the time limit.`

*   **ナレーション** (Narration / System):  
    `<T>When your parrot has completed
    every delivery request in the game,
    something cool will happen`

### `20_075390.lbin.txt` — Flora procura Luke + Beasly commentary: statue in brick courtyard, honey-grabbers

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Say, have you seen Luke around
    here?`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Bzzzz bzzzzzzz bzzzzz. Bzz bzzzzzz
    bzzzz bzzzzzz. Bzz bzz bzzzzzzzzzz.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>It doesn't look as though Luke is
    here. Let's search elsewhere, shall
    we?`

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/2>All right, Professor.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T><A1/3>Luke? He's over by the statue in
    the brick courtyard`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>They can't understand a word I'm
    saying, can they? And now they've
    buzzed off. Bah`

### `20_075400.lbin.txt` — Future Luke: peculiar flower in abandoned shop on Midland Road, Venus flytrap for puzzles

*   **未来ルーク** (Future Luke):  
    `<T>Tell me, did you happen to notice
    that peculiar flower growing in the
    abandoned shop on Midland Road?`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Erm... Why, what's so special about
    this particular flower?`

*   **未来ルーク** (Future Luke):  
    `<T>It supposedly attracts puzzles that
    have disappeared from their
    original locations.`

*   **ルーク** (Luke Triton):  
    `<T><A1/6>Like a Venus flytrap for puzzles?`

*   **未来ルーク** (Future Luke):  
    `<T><A2/2>That's what they say, anyway.
    I've never seen it for myself.`

*   **未来ルーク** (Future Luke):  
    `<T>But if those rumours are true,
    we'll be able to retrieve any
    puzzles we've left behind.`

*   **未来ルーク** (Future Luke):  
    `<T>I'd say that's reason enough to
    visit the shop.`

*   **ルーク** (Luke Triton):  
    `<T><A3/1>What do you say, Professor?`

*   **レイトン** (Professor Hershel Layton):  
    `<T>Well, we've nothing to lose, I
    suppose.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>The shop in question is just a quick
    stroll away and being able to visit
    lost puzzles would be very useful.`

*   **ルーク** (Luke Triton):  
    `<T>Then what's stopping us? Let's go`

*   **未来ルーク** (Future Luke):  
    `<T><A3/2>Don't you want to go and have a
    look at the flower that started all
    those rumours?`

*   **未来ルーク** (Future Luke):  
    `<T>It's growing not far from here, in
    the abandoned shop on Midland
    Road.`

### `20_075410.lbin.txt` — Beasly dublado (6 vozes): Oi! That flower keeps hold of puzzles, tap it!

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Oi`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>That flower keeps hold of puzzles
    you've left behind`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Puzzles you've left behind are
    packed inside that bloom.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>So go on`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Leaving too many unsolved puzzles
    lying around can come back to sting
    you.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>So don't just stand there with your
    mouth hanging open. Tap that
    flower and get solving`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Puzzles you left behind because they
    were too tough, or whatever,
    are hiding in that blossom.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>And they will not be ignored`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Flowers like that are fascinating
    plants. Puzzles just love to gather
    around them.`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>Sounds weird, I know, but if you
    want to see what I mean, just give
    it a tap.</V>`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>I wouldn't advise letting that
    flower get overburdened with
    puzzles, you follow?`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>All I'm saying is, don't leave puzzles
    for tomorrow when you can solve
    them today`

*   **ナゾービー** (Beasly (Puzzle Bee)):  
    `<T>...Bzzz?`

### `20_075420.lbin.txt` — Future Luke fica: fear anomalies, stay here until you return, Jack Let's be off!

*   **未来ルーク** (Future Luke):  
    `<T>I fear that going back to your
    time could introduce additional
    anomalies to the flow of time.`

*   **未来ルーク** (Future Luke):  
    `<T>I've therefore decided to stay
    here until you return.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>I was going to suggest the same
    thing myself. Please wait for us
    here. We'll be back before long.`

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Are you ready to go, then?<W> Good`

### `20_075430.lbin.txt` — Chelmey fica: Heading back already? Jack flipping the switch now!

*   **チェルミー** (Inspector Chelmey):  
    `<T>Heading back already, Layton?
    I've still got a few leads to chase,
    so I'm going to stay here for now.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Understood, Inspector. I'll see
    you when I return.`

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Right, would those who aren't
    coming please leave the room?
    <A3/0>I'm flipping the switch now`

### `20_075440.lbin.txt` — Chelmey + Future Luke ficam: both stay behind, Jack Here we go!

*   **チェルミー** (Inspector Chelmey):  
    `<T>Heading back already, Layton?
    I've still got a few leads to chase,
    so I'm going to stay here for now.`

*   **未来ルーク** (Future Luke):  
    `<T>I'm afraid I'll have to stay
    behind as well, Professor.`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>All right. We won't be long. Please
    wait for us here.`

*   **ジャック** (Jack (Cogg / Clock Shop Switch)):  
    `<T>Okay, now that they've left, let's
    get going.<W> <A3/0>Here we go`

### `20_075450.lbin.txt` — Future Luke retorno: Welcome back, Professor. Right, let's return to town

*   **未来ルーク** (Future Luke):  
    `<T><A2/2>Welcome back, Professor. Right,
    let's return to town.`

### `20_075460.lbin.txt` — Chelmey retorno: Ah Layton, good to see you made it back, Let's be on our way

*   **チェルミー** (Inspector Chelmey):  
    `<T>Ah Layton, good to see you made
    it back in one piece. Took you long
    enough`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>My apologies for keeping you
    waiting, Inspector. Let's be on our
    way.`

### `20_075470.lbin.txt` — Chelmey + Future Luke retorno: Welcome back, ready to return to business

*   **チェルミー** (Inspector Chelmey):  
    `<T>Ah, there you are, Layton. I was
    beginning to wonder if you'd ever
    return.`

*   **未来ルーク** (Future Luke):  
    `<T><A2/2>Welcome back, Professor. Are you
    ready to return to our business
    here?`

*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Certainly. Let's be off.`

---

## 5. Enigmas & Eventos Notáveis (Catálogo por Arquivo — Extras sem Enigmas Jogáveis)

| Arquivo | Evento / Sistema | Descrição |
|---|---|---|
| `20_000000` | **Cabeçalho vazio** | `[701701...0000]` sem `<T>` |
| `20_011100` | **Granny Riddleton retirement** | Luke: This place is a mess → Narration Hold it right there, sonny boy → Granny beautiful/clairvoyant → retire/holiday → puzzly day → heebie-jeebies bee |
| `20_015170` | **Parrot no céu** | Look at the bird → That's no ordinary bird, it's a parrot → Let's ask him → Ho ho |
| `20_033700` | **Subject 3 lore dublado** | {''}Mr Rabbit{''}? → rabbit turf/enigma portão → kidnapped/lab animal → white coats Subject 3 → Subject 1/2 → dark room/nails/blackboard → Layton heavy burden → kid free life ahead → bite the lot of you |
| `20_071000` | **Beasly sigh** | Ohh... → big sigh small bee → down in the dumps → I'm different from all other bees → What's your story, Beasly? |
| `20_072000` | **Nazoline tiny house** | poor little enigmas you leave unsolved → adorable little house over there (×4 variações) → Touch that tiny house → {''}Solve me{''} |
| `20_073000` | **Beasly magnetic personality** | Watch out, Professor → bee of distinction → magnetic personalities → Granny who? I'm Beasly → Tap that flower → drone on ha ha |
| `20_075000` | **Mural start** | Tsk wall disrespect → dry paint → paint over → painting enigma → white wall asks for graffiti → fancy mural idea → all fired up |
| `20_075010` | **Slate intro** | big plans for this wall → My name's Slate. Nice to meet you |
| `20_075020` | **Mural progress 1** | coming along nicely → Heh heh → looking great can't wait |
| `20_075030` | **Mural progress 2** | We're making real progress. Come by and have another peek mais tarde |
| `20_075040` | **Mural progress 3** | Hello friends → How's the mural? → Swimmingly |
| `20_075050` | **Mural progress 4** | outline finished by next visit |
| `20_075060` | **Mural progress 5** | rough sketch excellent → colour in rest? → painting enigma → You two have a way with enigmas |
| `20_075070` | **Mural progress 6** | kids will have coloured in some more |
| `20_075080` | **Mural progress 7** | Wow → kids doing great job → spectator not painter → preparing paint/washing brushes |
| `20_075090` | **Mural progress 8** | Come back soon to have a look at the mural |
| `20_075100` | **Mural progress 9** | almost finished → kids but I did heavy lifting literally → pots enigma → best enigma solvers I've ever met |
| `20_075110` | **Mural progress 10** | My mural is nearly finished! You'll soon see it in all its glory! |
| `20_075120` | **Mural finished** | Perfect timing, fellows! → work of art → Thanks! young artists → pat on the back Slate → Heh heh come anytime → unrivalled in all of London |
| `20_075130` | **Barton pork bun** | Oh pork bun! Om nom → investigation? → Scotland Yard saying → can't fight crime on empty stomach → solid investigation solid meal |
| `20_075140` | **Cogg dica** | If you're looking to do a little time travelling, talk to Cogg. |
| `20_075145` | **Cogg dica (duplicata)** | Idem `075140` — variante de gatilho duplicado |
| `20_075150` | **Restaurante** | Victory meal! → What are you going to have, Luke? → How about this? Oh and this! → you always order half the menu → chef pointers? |
| `20_075160` | **Bostro dejected** | Hmm? Oh it's you → less energetic → Mr Layton just levantou-se e saiu → Dimitri Allen impostor → vanished with Hawks bloke → best henchman → sensitive side |
| `20_075200` | **Demo end** | Nice work! → concludes demo of Lost Future → adventure continues in full version |
| `20_075220` | **Flor + insect** | can't stop looking at this curious flower and strange little insect buzzing around it |
| `20_075230` | **Locked place** | This place is all locked up → doesn't look as though anyone's there → try again mais tarde |
| `20_075240` | **Jack time travel 1** | Want to travel back to your own time, do you? |
| `20_075241` | **Jack time travel 2** | Fancy a trip back to your London? |
| `20_075242` | **Jack time travel 3** | Ready to go back to your own time? |
| `20_075243` | **Jack time travel 4** | Are you wanting to travel back to your own time? |
| `20_075245` | **Jack time travel 5** | Ready to leap forward into the future again? |
| `20_075246` | **Jack time travel 6** | I take it you'd like me to help you return to the future? |
| `20_075247` | **Jack time travel 7** | Want to go to the future again? |
| `20_075248` | **Jack time travel 8** | So am I taking you back to the future again? |
| `20_075250` | **Hidden Door bonus** | standing outside The Hidden Door → What enigma inside? → Itching to find out → Here's a little gift → What a delightful enigma! |
| `20_075260` | **Tutorial enigmas desaparecem** | moving/investigating London advice → enigmas disappear as story progresses → sent to certain spot → Visit there often → can be solved any time |
| `20_075270` | **Quebra no casino** | Cripes! It broke! → prodding everything → trespassing? → leads somewhere interesting → Ha ha! You worry too much, Luke! |
| `20_075280` | **Door locked** | This door seems to be locked. |
| `20_075290` | **153 enigmas** | Did you enjoy Lost Future? → end of story but game far from over → exactly 153 enigmas → Bonuses extra-challenging |
| `20_075300` | **Story 100%** | Did you enjoy → solved every enigma in story mode Congratulations! → Layton's Challenges/Weekly Enigmas |
| `20_075310` | **Total 100%** | solved every enigma in the game Congratulations! → don't forget Weekly Enigmas |
| `20_075320` | **Picture books 100%** | completed all livro ilustrados → Storyteller's House added to Layton's Challenges |
| `20_075330` | **Toy car 100%** | completed every course for toy car → Hotelier's House added |
| `20_075340` | **Parrot 100%** | parrot completed all delivery requests → Delivery Bird's House added |
| `20_075350` | **Salvar pós-fortress** | end of story save chance → resume inside mobile fortress → free to return to town hunt missed enigmas/items |
| `20_075360` | **Instruções livro ilustrado** | Fill missing elements adesivos → Place/Remove → arrows turn page → text changes with adesivos → 3 books unlock sequence → something wonderful |
| `20_075370` | **Instruções toy car** | Pick up items guide car tiles → tiles per course → Place slide → one tile per square → grass/sand only → bridges/switches/trees | jump/arrow vanish → direction bridge switches → Clear/Go! → reaching goal sozinha not enough |
| `20_075380` | **Instruções parrot 1** | parrot volunteered delivery → heavy objects hard to fly → ropes perches → number ropes changes → position angle affects trajectory → ropes can't cross → Clear/Start!/Quit → flat perch return flight |
| `20_075385` | **Instruções parrot 2 (duplicata)** | Idem `075380` — 17 blocos, texto expandido com ...Bzzz? |
| `20_075390` | **Flora + Beasly** | Say, have you seen Luke? → Bzzzz → It doesn't look as though Luke is here → Luke over by statue brick courtyard! HEY! → honey-grabbers buzzed off |
| `20_075400` | **Flor Venus flytrap** | peculiar flower abandoned shop Midland Road → attracts enigmas disappeared → Like Venus flytrap for enigmas?! → retrieve any enigmas left behind → quick stroll useful |
| `20_075410` | **Beasly flower dublado** | Oi! dig into enigmas? → flower keeps hold → packed inside bloom → So go on! Get to it! → Leaving too many unsolved can come back to sting → So don't just stand there... Tap that flower → ...Bzzz? |
| `20_075420` | **Stay: Future Luke** | fear anomalies going back → decide to stay here until you return → Please wait here → Jack Ready to go? Let's be off! |
| `20_075430` | **Stay: Chelmey** | Heading back already? still got leads → Understood → Jack would those not coming please leave room? flipping switch now! |
| `20_075440` | **Stay: ambos** | Chelmey leads → Future Luke stay behind as well → All right. We won't be long → Jack Okay, now that they've left, let's get going. Here we go! |
| `20_075450` | **Return: Future Luke** | Welcome back, Professor. Right, let's return to town. |
| `20_075460` | **Return: Chelmey** | Ah Layton, good to see you made it back → My apologies for keeping you waiting → Let's be on our way |
| `20_075470` | **Return: ambos** | Ah, there you are, Layton → Future Luke Welcome back, ready to return to our business? → Certainly. Let's be off. |

**Eventos narrativos sem enigmas diretos:** todos os 59 arquivos com texto são gatilhos de **sistema/tutorial/vinheta**; nenhum contém enigma offer→fail→retry→solve jogável — este é um **extra de hub e pós-jogo**, com lore leve e instruções mecânicas, servindo como gerenciamento de 100% e transições diegéticas. Diferentemente de Extras 18 (77 enigmas) e Extras 19 (digest narrativo), Extras 20 é 100% utilitário.

---

## 6. Notas de Localização & Observações Técnicas (Template Extras)

> **Template Extras 20:** este arquivo usa o prefixo **Extras** (good prefix para sistema/tutorial/pós-jogo, não capítulos de história). Mantém número 20 mas classifica como **sistema de enigmas perdidos + tutoriais + pós-jogo**. Linguagem PT-BR no entorno, diálogo em inglês UK original com " para sumário (seção 3) e ` para detalhado (seção 4). Outros blocos extras do dump (18, 19, 30, 40, 50, 90, 99) — se existirem — devem seguir o mesmo template Extras_XX.md quando forem documentados; por ora 18 (puzzles pós-Fortaleza), 19 (digest) e 20 (sistema/tutoriais) foram adaptados como exemplos.

*   **Extra sem puzzle jogável (não é capítulo):** Dos 60 arquivos, 59 contêm texto mas **0 contêm puzzles jogáveis com branching**; 1 é apenas cabeçalho. Como conteúdo de sistema pós-Cap. 14, a interatividade é de **gestão de coleção e tutorial**, não de desafio lógico — marca hub de serviço para 100%. Estrutura varia: vinhetas curtas de 1–6 blocos (Jack 1 bloco ×8, Slate 1–17 blocos) e instruções longas de 14–21 blocos (`075360`/`075370`/`075380`). **Não tratar como capítulo narrativo.**
*   **Dublagem concentrada em dois arquivos:** Apenas `033700` (Subject 3, ~20 `<V>` IDs V0011–V0281, rabbit monologue sobre lab/white coats/nails/blackboard) e `075410` (Beasly, 6 `<V>` IDs V0010–V0060, ``Oi! Come by to dig into a few puzzles, did ya?``) carregam voice acting — ambos ligados a **lore/mascote**. Todos os outros são não-dublados, usando `<A>`/`<W>`/`<K>` para ritmo (ex.: `<A1/5>` This place is a mess, `<A4/1>` magnetic personality, `<K>` Hmm? em `075160`).
*   **Arco do mural como serialização ambiental:** `075000`→`075120` (13 estados) é o **único arco com progressão visível** no extra — simula passagem de tempo comunitária (graffiti → white wall → outline → kids colouring → work of art unrivalled). Texto progride de ``Tsk. Some people have no respect...`` a ``Perfect timing, fellows! We just finished the mural!`` com puzzles temáticos de pintura em `075060`/`075100`. Reaparece como âncora geográfica do London futuro, similar à Pagoda em Extras 19.
*   **Hub de puzzles perdidos: flor/bee/house trifecta:** `071000`/`072000`/`073000` + `075400`/`075410` formam **sistema redundante** para o mesmo mecanismo (puzzles que desaparecem → vão para certain spot/flower/house/bee). Variações diegéticas: Granny Riddleton holiday (`011100`), Beasly magnetic personality (`073000`), Nazoline tiny house (`072000`), Future Luke Venus flytrap (`075400`) — todas apontam para **abandoned shop on Midland Road** como hub físico, com 8 variações de instrução de uso (tap flower/house). `075260` consolida regra em narração pura.
*   **Time travel como gatilho de teleporte:** `075240`–`075248` (8 linhas de Jack) + `075420`–`075470` (decisões de Future Luke/Chelmey ficar/voltar) são **variações de uma mesma cena de switch** com pequenas diferenças de formalidade (Want to travel back? / Fancy a trip? / Ready to leap forward?). Tags preservadas indicam escolha de quem viaja; Jack (Jack/Cogg) é operador com ``Let's be off!`` / ``flipping the switch now!``. Sem lore nova — apenas controle de fluxo.
*   **Pós-jogo e unlocks como recompensa mecânica:** `075290` fixa **153 puzzles** como total do story; `075300`/`075310` distinguem story mode vs total game; `075320`–`075340` vinculam 100% de cada minigame a **Layton's Challenges** (Storyteller's/Hotelier's/Delivery Bird's House) — padrão de recompensa por completude. `075350` explicita **save pós-fortress** (resume inside mobile fortress) permitindo hunt de missed puzzles — ponte direta para o hub de `075410`.
*   **Structure preservation:** Diálogo mantido em inglês UK original; nomes `Midland Road`, `Lost Future`, `The Hidden Door`, `Layton's Challenges`, `Storyteller's House`, `Hotelier's House`, `Delivery Bird's House`, `Bonuses`, `Weekly Puzzles`, `Cogg`, `Granny Riddleton`, `Beasly`, `Slate`, `Subject 3`, `Bostro`, `Dimitri Allen`, `Hawks` preservados; tags `<T>`/`<V>`/`<A>`/`<W>`/`<K>`/`<CR>`/`<Q><J>` preservadas no detalhado; placeholders `{''}` preservados em `033700` e `072000`; cabeçalho `[701701...]` e separadores `!****!` omitidos no detalhado por brevidade mas verificáveis no dump bruto.
