# Capítulo 13 — A Fortaleza Móvel de Clive, o Resgate de Flora e o Coração do Primeiro-Ministro | Professor Layton and the Unwound Future

> **Capítulo 13 — A Fortaleza Móvel / Infiltração, Gerador e o Relógio de Claire** — Análise de dump LSCR para `Textos Originais/txt/uk/13/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/13/`
> Total de arquivos escaneados: **42**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão, `<J>` = jump

---

## 1. Arquivos Cobertos

Todos os 42 dumps `.lbin.txt` em `uk/13`:

```
13_000000.lbin.txt  — [vazio - apenas cabeçalho]
13_041030.lbin.txt  — Reação de Chelmey à war machine sob London
13_041040.lbin.txt  — Celeste e Layton diante da arma, Layton decide resgatar Flora
13_041050.lbin.txt  — Don Paolo oferece o Laytonmobile da colina
13_041055.lbin.txt  — Flavor: Luke reconhece o Laytonmobile
13_041060.lbin.txt  — Puzzle do parafuso/screw do carro
13_042010.lbin.txt  — Prioridade dublado: encontrar Flora, find a way in
13_042020.lbin.txt  — Porta trancada com puzzle lock de Clive
13_042030.lbin.txt  — Lift/transport pod, Monitor revela ventilation room e puzzle de instruções codificadas
13_042040.lbin.txt  — Mapa da contraption, pod para ventilation room
13_042050.lbin.txt  — Porta grande da ventilation room
13_042060.lbin.txt  — Flora na glass cage
13_042070.lbin.txt  — Puzzle lock da glass cage
13_042080.lbin.txt  — Resgate dublado: mandar Luke/Flora ao carro, insistência em ficar
13_042090.lbin.txt  — Gorocky e Dolgan perdem a garota, pista da surveillance room
13_042099.lbin.txt  — Monitor avista o grupo, exige key code
13_042100.lbin.txt  — Puzzle do key code, Monitor foge (do a runner)
13_042110.lbin.txt  — Dolgan muscle com knife puzzle, ordens de Clive para não tocar
13_042120.lbin.txt  — Vista do alto da machine
13_042500.lbin.txt  — Confronto dublado com Clive: level and rebuild, little people vs government
13_042510.lbin.txt  — Armadilha pós-confronto, puzzle de fuga
13_042700.lbin.txt  — Clive sai para o main event
13_044000.lbin.txt  — Plano do gerador dublado: monitors ligados a cameras, cortar power na source
13_044010.lbin.txt  — Busca nos monitors, localização do generator room e coordenadas para o pod
13_044015.lbin.txt  — Flavor: usar monitors para achar generator
13_044020.lbin.txt  — Celeste bruxa, porta para o deck
13_044030.lbin.txt  — Flavor: ir ao deck
13_044040.lbin.txt  — Deck com flying machine de Don Paolo, Flora quer ficar, return underground
13_044050.lbin.txt  — Flavor: Don Paolo sobre a flying machine
13_044055.lbin.txt  — Device de coordenadas com green monitor puzzle
13_044060.lbin.txt  — Coordenadas inseridas, botão do generator lit up
13_044070.lbin.txt  — Coração da fortress, painel trancado, revelação do prime minister no pod
13_045000.lbin.txt  — Clive dublado: prime minister em special seat, fortress detonate, enough charge to level most of London
13_045020.lbin.txt  — Heartbeat monitor, pocket watch quebrado (10 minutos), troca de circuito
13_046000.lbin.txt  — 10 minutos para explodir, reverse energy flow (dublado)
13_046010.lbin.txt  — Gears core, reverse movement para overload
13_046020.lbin.txt  — Running out of time, puzzle final
13_047000.lbin.txt  — Energia reversa, fortress destroying itself dublado
13_047010.lbin.txt  — Transport pod falhando, fuga de carro
13_047020.lbin.txt  — Flavor: fortress destroying itself even faster
13_048010.lbin.txt  — Flavor: Clive...
13_048015.lbin.txt  — Belle no caos da cidade, aviso para correr ao clock shop em Midland Road
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `13_000000.lbin.txt`. `13_041055`/`13_044015`/`13_044030`/`13_047020`/`13_048010` são flavors de uma linha. `13_042030` e `13_045020` concentram os enigmas diegéticos mais longos do capítulo (instruções codificadas e troca do heartbeat).

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 13 |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Protagonista, decide resgatar Flora sozinho, decifra pods e instruções codificadas, liberta Flora, confronta Clive, formula plano do gerador/heartbeat e reversão de energia, ordena evacuação para Midland Road |
| `ルーク` | **Luke Triton** | Aprendiz, reconhece Laytonmobile, resolve enigma locks/key code, insiste em não deixar Layton sozinho, avisa sobre risco aos Londrinos, testemunha prime minister |
| `アロマ` | **Flora Reinhold (Aroma)** | Donzela na glass cage na ventilation room, liberta, recusa ir ao carro e exige ficar, apoia na fuga, quer ficar close to people you care about |
| `チェルミー` | **Inspector Chelmey** | Reação única: That maniac Clive has been building a war machine under London! |
| `サリアス` | **Celeste (Sarrias)** | Guia técnica, suspeitava de weapons behind Dimitri's back, explica gerador, propõe truque do pocket watch, brinca ser witch e revela flying machine, quer overload via gears |
| `ドン・ポール` | **Don Paolo (Paul)** | Benfeitor inesperado, roubou blueprints e construiu Laytonmobile melhorado na colina, confessa dúvida do screw, empresta carro e flying machine |
| `クラウス` | **Clive (Klaus)** | Antagonista central, justifica havoc para punir government, arma fortress com prime minister em pod detonador, sai para main event |
| `モニター` | **Monitor (Family - Screen)** | Capanga no vidro, guarda ventilation room e key code, perde instruções, foge após truque de Luke do a runner |
| `ゴロッキー` | **Gorocky / Lockjaw (Grocky)** | Capanga desastrado que told Layton where to find her, vai atrás do grupo |
| `ドルガン` | **Dolgan / Dorgan (Muscle)** | Músculo de Clive com knife, lança enigma em vez de atacar, obedece ordens de não tocar em ninguém, manda boss hates being made to wait |
| `ベル` | **Belle** | Cameo cômico no caos, recebe ordem de correr ao clock shop, pede kiss for good luck, Luke foge envergonhado |

Tags de controle observadas: `<V0010>`–`<V0130>` dublados em `13_042010`, `13_042080`, `13_042500`, `13_042700`, `13_044000`, `13_045000`, `13_046000`, `13_047000`; `<W>` pausas longas em surpresas (Wh-what?!, villain reveals); `<A1/1>`–`<A7/0>` animações frequentes em Layton/Luke; `<K>` silêncio tenso (Hmm, Hrm?); placeholders `{''}` para aspas internas little people, ropey; `<CR>...</C>` tag rara de condição de retorno em `13_044040`; `Placeholder text. Puzzle Cleared.` como marcador pós-enigma em `13_042100`/`13_042110`.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 O Choque da máquina de guerra e o Laytonmobile (`13_041030`–`13_041060`)
Chelmey sintetiza o pânico ao ver a fortress sob London e Celeste admite que suspeitava de armas behind Dimitri's back mas não desta escala. Layton decide buscar Flora mesmo sob risco e Don Paolo surge como aliado improvável ao oferecer seu "Laytonmobile aprimorado" a partir de plantas roubados, com último entrave num screw — "This is the one. I'm sure of it!" — resolvido por enigma. A cena sela a redenção prática de Paolo, que declara fazer tudo por Flora e libera o veículo na colina. O momento fecha o arco do carro-modelo do hospital e prepara a infiltração veicular.
> Ganchos: "That maniac Clive has been building a máquina de guerra under London all this time?!" / "I stole the plantas for it and made my own Laytonmobile aprimorado!"

### 3.2 Infiltração — Porta, Pod e o Monitor da Ventilation Room (`13_042010`–`13_042040`)
Com o carro, a prioridade é achar Flora e encontrar entrada. A porta exige fechadura de enigma — "I wouldn't expect anything less from Clive" — e revela lift de cápsulas de transporte. O Monitor delata que Flora foi jogada na sala de ventilação e que "Dimitri was just a puppet", gabando-se de código uncrackable que Layton decifra após duas falhas até liberar o mapa do 12th floor e autorizar o salto do pod. A revelação de que Dimitri era puppet amarra o retcon do Cap. 12.
> Ganchos: "Our first priority is finding where Clive has taken Flora." / "We chucked your little friend into the ventilation room."

### 3.3 Resgate de Flora — A Glass Cage e a Recusa de Recuar (`13_042050`–`13_042080`)
Atrás da porta grande, Flora está presa numa jaula de vidro com fechadura de enigma e grita "Help me, Professor!". O resgate dublado leva Layton a tentar dispensar as crianças ao carro — "head straight back to the car" — para parar a contraption sozinho, mas Luke e Flora recusam abandonar o mestre, selando o pacto de seguir juntos até Clive com urgência crescente.
> Ganchos: "I'm so glad to see you!" / "I'm your apprentice, which means I can't just let you plunge headlong into danger without me!"

### 3.4 Rumo à Surveillance Room — Gorocky, Dolgan e o Key Code (`13_042090`–`13_042120`)
Escondidos, ouvem Gorocky admitir "She's gone!" e Dolgan ir avisar Clive na surveillance room. O Monitor exige key code e Luke o manipula a fugir com "do a runner" até "I'm outta here.". Dolgan se apresenta como "I'm the muscle." que troca a faca por enigma por ordem expressa de não ferir ninguém, liberando passagem sob advertência de que ninguém pode deter Clive antes da vista do alto da machine, que impressiona pela escala vertical.
> Ganchos: "You need the key code to go to the surveillance room, fools!" / "Clive instructed me not to touch a single hair on any of your pretty heads."

### 3.5 Clive sem Máscara — Nivelar para Reconstruir (`13_042500`–`13_042700`)
O confronto opõe justiça institucional — "When the world learns of it, they'll be punished" — à tese de Clive de que sem "large-scale havoc" o governo não mudaria. Como repórter marcado por "countless tragedies", vê nos "little people" apenas "bumps on the road" e conclui que só force resolve, precisando nivelar London e reconstruir do zero antes de sair para o main event que já está em curso, deixando Layton com o dilema moral sem tempo.
> Ganchos: "But without large-scale havoc, those fools in government will never change their ways!" / "So you see, I have no choice but to level this place and rebuild it from the ground up."

### 3.6 O Coração da Fortaleza — Gerador, Monitores e a Flying Machine no Deck (`13_044000`–`13_044070`)
Celeste propõe achar o generator e "cut off the power at the source" usando "monitors linked to cameras". A busca rende coordenadas num esverdeada monitor para liberar o pod. Celeste brinca ser "witch" que voou de broom e manda ao deck, onde revelam a flying machine de Don Paolo controlada do solo, e Flora recusa evacuação com "No way! I'm staying here!" por lealdade ao grupo, enquanto a possibilidade de retorno subterrâneo permanece em aberto.
> Ganchos: "There has to be a generator somewhere here. All we need to do is find it and shut it down." / "Oh my gosh! That's Don Paolo's flying machine!"

### 3.7 O Coração que Bate — Prime Minister e o Relógio de Claire (`13_045000`–`13_045020`)
Clive avisa que o prime minister está num "very special seat" que "will detonate" com "enough charge to level most of London". Celeste identifica heartbeat com "two sets of wires" e propõe o "pocket watch I gave Claire", quebrado para só 10 minutes e exigindo troca em one fell swoop para ganhar janela mínima, com Luke alertando para o risco coletivo.
> Ganchos: "And should you try to move him from that pod, this whole fortress will detonate." / "That...is the pocket watch I gave Claire, long ago."

### 3.8 Reversão, Autodestruição e Fuga — Até o Clock Shop (`13_046000`–`13_048015`)
Com "10 minutes to get out", a saída é "reverse the energy flow" para "overload the power supply" via gears core. A reversão faz a fortress "start destroying itself" e inutiliza o pod — "systems go haywire" e risco de voltar ao deck — obrigando fuga de carro ainda mais rápida até o clock shop em Midland Road, onde o caos já se espalha com Belle como testemunha do pânico civil.
> Ganchos: "We need to reverse the energy flow. That will break the generator and shut down the fortress." / "Reversing the energy flow has caused the fortress to start destroying itself!"

> **Cliffhanger:** Clive expõe plano de nivelar London para punir o governo por negligenciar os little people, mas o grupo troca o heartbeat do primeiro-ministro pelo relógio quebrado de Claire para ganhar 10 minutos e reverte o gerador — a fortress começa a se autodestruir, o pod falha e a fuga tem de ser de carro até o clock shop em Midland Road, com Belle como testemunha do caos.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag)` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes.

### `13_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `13_041030.lbin.txt` — Chelmey reage à war machine

*   **チェルミー** (Inspector Chelmey):  
    `<T>That maniac Clive has been building a war machine under London all this time?! It's madness!`

### `13_041040.lbin.txt` — Celeste e Layton diante da arma

*   **サリアス** (Celeste):  
    `<T>So this is the weapon that Clive was building...</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Did you know about this before?</T>`
*   **サリアス** (Celeste):  
    `<T>No! <A4/4>I suspected someone was developing weapons behind Dimitri's back...</T>`
*   **サリアス** (Celeste):  
    `<T><A1/1>But I never imagined that the product of all that research would be this atrocity!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>In any case, it's dangerous here. You need to leave at the double!</T>`
*   **サリアス** (Celeste):  
    `<T>But what about you?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>I'm going to get Flora.</T>`
*   **サリアス** (Celeste):  
    `<T>Are you mad? Look at that thing! You'll be killed!</T>`
*   **サリアス** (Celeste):  
    `<T>But I suppose I can't stop you, can I?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Flora's been abducted. I can't simply leave her there.</T>`

### `13_041050.lbin.txt` — Don Paolo e o Laytonmobile

*   **ドン・ポール** (Don Paolo):  
    `<T><A2/3>Isn't this usually when you like to show off? You are planning to rescue Flora, aren't you, Layton?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Of course. But how can I gain access to the fortress's interior?</T>`
*   **ルーク** (Luke Triton):  
    `<T>We could try scaling one of its legs...</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>Foolish boy! You'd be squashed flatter than a pancake!</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T><A4/1>Hey Layton, how would you like to use your own car to get to the fortress?</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>You mean the one at the hospital? But that was just a model to make us believe we were in the future!</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T><A4/5>Hah! But I stole the blueprints for it and made my own improved Laytonmobile! Fully kitted out!</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>I was saving it for a special occasion, but too bad. I can always make another one.</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>The car is waiting for you on the hill over there. Get a move on!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>Many thanks, Paul.</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T><A5/5>Don't get all sappy on me, Layton. I'm only doing this for Flora!</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>I've parked your car up on that hill over there. What are you waiting for?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>My apologies, Paul. I'll go and fetch it immediately!</T>`

### `13_041055.lbin.txt` — Flavor Laytonmobile

*   **ルーク** (Luke Triton):  
    `<T>Don Paolo wasn't joking! This looks just like the real Laytonmobile!</T>`

### `13_041060.lbin.txt` — Puzzle do screw

*   **ドン・ポール** (Don Paolo):  
    `<T>Erm, there is one thing I need to confess, Layton...</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>What is it, Paul?</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>The truth is, the car's almost ready, but I don't know which screw to use on this last joint here.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>But the whole car could fall apart! What are we going to do now?</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>No need to get so shrill, brat!<W> We can work it out. One of these screws is sure to do the trick.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hmm, I can't seem to find the right one.</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>Stop messing around, Layton!</T>`
*   **ルーク** (Luke Triton):  
    `<T>It's not like YOU know which screw to use either!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Right, time to get this car running.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This is the one. I'm sure of it!</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/2>I've got to hand it to you this time, Layton. That was some fine work.</T>`
*   **ルーク** (Luke Triton):  
    `<T>So is the car ready to drive now?</T>`
*   **ドン・ポール** (Don Paolo):  
    `<T>You bet it is, boy.<W> Gentlemen, your chariot awaits!</T>`

### `13_042010.lbin.txt` — Prioridade dublado

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>Our first priority is finding where Clive has taken Flora.</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T>Aye aye, Professor!<W> <A4/4>But this place is huge! They could be anywhere!</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>First things first. Let's find a way in.</V>`

### `13_042020.lbin.txt` — Porta com puzzle lock

*   **ルーク** (Luke Triton):  
    `<T>The door is locked with a puzzle.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I wouldn't expect anything less from Clive.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It's clear that we're not getting inside without doing some thinking.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This puzzle isn't going down without a fight. I'll have to try again.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm confident I can find the solution this time.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Excellent! With the puzzle solved, we're free to go in.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Great! Then let's head in!</T>`

### `13_042030.lbin.txt` — Lift, Monitor e instruções codificadas

*   **レイトン** (Professor Hershel Layton):  
    `<T>This appears to be some sort of lift. I think we can use it to move around the fortress.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>But there are so many buttons, I don't have the slightest clue how to operate it.</T>`
*   **Narration**:  
    `<T>Oi, you two! Get away from that transport pod!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>Oh no! We've been spotted!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We've come here for the girl Clive kidnapped. Tell us where Flora is at once!</T>`
*   **モニター** (Monitor):  
    `<T>Flora, eh? You must mean that pretty thing the boss dragged back here.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>The boss? So you've been working for Clive all along...</T>`
*   **モニター** (Monitor):  
    `<T>Course we have!<W> Dimitri was just a puppet. Clive's been our gaffer from day one!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>Ah, it all makes sense now!</T>`
*   **モニター** (Monitor):  
    `<T>We chucked your little friend into the ventilation room. Not that you'll be able to get to her, mind!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>I wouldn't be so sure about that.</T>`
*   **モニター** (Monitor):  
    `<T><K>Hrm?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>What's to stop us from taking this transport pod to the ventilation room?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You've even been so kind as to leave us an explanation of how to use the device.</T>`
*   **モニター** (Monitor):  
    `<T>I did not!<W> Well, except for that note, but that's written in an uncrackable code.</T>`
*   **モニター** (Monitor):  
    `<T>Have a gander if you like, but you ain't never gonna work out the instructions!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hmm. I seem to have made an error somewhere.</T>`
*   **モニター** (Monitor):  
    `<T><A2/3>Hahahaaa! I told you that you wouldn't stand a chance!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I must decipher these instructions if we're to save Flora!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>There! The door should open any moment now.</T>`
*   **モニター** (Monitor):  
    `<T>Wh-what?!<W> Hey, stop! You ain't allowed to go in there!</T>`
*   **ルーク** (Luke Triton):  
    `<T>And how are you going to stop us? You're just a talking head!<W> <A3/1>C'mon, Professor! Let's find Flora!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>Let's see.<W> The ventilation room appears to be located on the 12th floor.</T>`
*   **モニター** (Monitor):  
    `<T>Don't you dare step inside there!<W> If you do, I'll make sure you regret it!</T>`
*   **ルーク** (Luke Triton):  
    `<T>How, exactly? You'll find it hard to make us regret anything from behind that glass! See you!</T>`

### `13_042040.lbin.txt` — Mapa da contraption

*   **レイトン** (Professor Hershel Layton):  
    `<T>This seems to be a map of the entire contraption.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Oh look! There's the ventilation room!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It seems this pod will take us there at the touch of a button.<W> Let's be off!</T>`

### `13_042050.lbin.txt` — Porta grande

*   **レイトン** (Professor Hershel Layton):  
    `<T>I think this is the room we're looking for.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Flora must be on the other side of this big door.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Yes. We can only hope that she's unharmed.<W> Let's go in.</T>`

### `13_042060.lbin.txt` — Flora na cage

*   **ルーク** (Luke Triton):  
    `<T><A1/6>Flora!</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Oh! Thank goodness you're here!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You poor thing... Hold on just a moment Flora! We'll soon get you out of there!</T>`

### `13_042070.lbin.txt` — Puzzle lock da glass cage

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Oh great. This weird glass cage has another one of those puzzle locks on it.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I simply can't stand to see Flora in that awful thing. Let's get this puzzle solved quickly.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>No, that won't do it.</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Help me, Professor!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Don't you worry, Flora. You'll be free before you know it.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hold on, Flora. I'll have you out of there in a matter of minutes.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>All right, Flora, I'm opening the cell.</T>`

### `13_042080.lbin.txt` — Resgate dublado e recusa de recuar

*   **アロマ** (Flora Reinhold (Aroma)) <V0010>:  
    `<V0010><T>I'm so glad to see you!</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>No need to worry. You're safe now, dear. But you can't stay here!</V>`
*   **アロマ** (Flora Reinhold (Aroma)) <V0030>:  
    `<V0030><T>Lead the way.</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T>Yeah, let's go.</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T><A2/1>You two head straight back to the car. I'll meet you there after I've put a stop to this contraption.</V>`
*   **ルーク** (Luke Triton) <V0060>:  
    `<V0060><T><A1/6>No way! <A1/3>I'm your apprentice, which means I can't just let you plunge headlong into danger without me!</V>`
*   **アロマ** (Flora Reinhold (Aroma)) <V0070>:  
    `<V0070><T><A1/3>Then I'm going too!</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T>I can't let you do this.</V>`
*   **ルーク** (Luke Triton) <V0090>:  
    `<V0090><T>And I can't let you do it alone!</V>`
*   **アロマ** (Flora Reinhold (Aroma)) <V0100>:  
    `<V0100><T>Yeah! What he said!</V>`
*   **レイトン** (Professor Hershel Layton) <V0110>:  
    `<V0110><T><A1/2>I see I can't change your minds. <A1/1>Come along if you must, but be careful.</V>`
*   **ルーク** (Luke Triton) <V0120>:  
    `<V0120><T><A1/1>Are we going to find Clive?</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T>Indeed. But our time is running out, so let's hurry.</V>`

### `13_042090.lbin.txt` — Gorocky e Dolgan perdem Flora

*   **レイトン** (Professor Hershel Layton):  
    `<T>Shh! Someone's coming.<W> Hide yourselves as best you can.</T>`
*   **ルーク** (Luke Triton):  
    `<T>But there's nowhere to hide!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Quick - duck behind that piece of machinery over there!</T>`
*   **ゴロッキー** (Gorocky / Lockjaw):  
    `<T>Aw great. She's gone!</T>`
*   **ドルガン** (Dolgan):  
    `<T>Yes... Do you think that might be because you told Layton where to find her? Hmm?</T>`
*   **ゴロッキー** (Gorocky / Lockjaw):  
    `<T><A2/3>Leave it out, will you? Yeah, I messed up, but you bangin' on about it ain't helpin'!</T>`
*   **ドルガン** (Dolgan):  
    `<T><A1/4>Hmm. Well, I have to go over to the surveillance room and tell Clive we've lost the girl...</T>`
*   **ゴロッキー** (Gorocky / Lockjaw):  
    `<T><A1/1>All right. While you're doin' that, I'll get after Layton and his cronies.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Did you hear that, Professor? Clive's in the surveillance room!</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>So are we going to go and talk to him?</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>Flora, the man just abducted you. We're not just going to have a pleasant chat!</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A2/5>You're right. That was quite ill-mannered of him!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let's just focus on getting to the surveillance room for now.</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>All right.<W> Still, it was an awful thing he did, wasn't it, Professor?</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Professor?</T>`

### `13_042099.lbin.txt` — Monitor exige key code

*   **モニター** (Monitor):  
    `<T>HA! I knew you couldn't hide from me!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/3>Oh no! We've been spotted again!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>Relax, Luke. There's little he can do from behind that monitor.<W> Now, let's go to the surveillance room.</T>`
*   **モニター** (Monitor):  
    `<T>Pfeh! Shows what you know! You need the key code to go to the surveillance room, fools!</T>`
*   **モニター** (Monitor):  
    `<T>You ain't going nowhere without that!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We'll be sure to decipher the key code beforehand, then.<W> Thanks for the tip.</T>`
*   **モニター** (Monitor):  
    `<T>You're welco-<W> Oi!</T>`

### `13_042100.lbin.txt` — Puzzle do key code

*   **レイトン** (Professor Hershel Layton):  
    `<T>Oh dear. That's not right.</T>`
*   **モニター** (Monitor):  
    `<T>Ha haa!<W> You'll never work out the key code. Never!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We need that key code in order to proceed.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Well, that takes care of that.</T>`
*   **モニター** (Monitor):  
    `<T>Ohh... Clive is gonna have my hide for this!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>If you're so scared of Clive, why don't you just do a runner?</T>`
*   **モニター** (Monitor):  
    `<T><K>Hrm?<W></K> Wait, what did you say?</T>`
*   **ルーク** (Luke Triton):  
    `<T>I said you might as well run away if you're going to get punished either way.</T>`
*   **モニター** (Monitor):  
    `<T>You know, that ain't such a bad idea!<W> Yeah...<W> I'm outta here. Later, fellas!</T>`
*   **ルーク** (Luke Triton):  
    `<T>I can't believe that actually worked.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Placeholder text. Puzzle Cleared.</T>`

### `13_042110.lbin.txt` — Dolgan muscle e puzzle da faca

*   **ドルガン** (Dolgan):  
    `<T>Hmm. I've been waiting for you, Professor Layton. I was beginning to think that Clive had got it wrong.</T>`
*   **ドルガン** (Dolgan):  
    `<T>We lost you for a second when that idiot Lockjaw ran off...</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Clive certainly has it all worked out, doesn't he?<W> What did he send you here for?</T>`
*   **ドルガン** (Dolgan):  
    `<T><A1/2>Isn't it obvious?<W> I'm the muscle.</T>`
*   **ドルガン** (Dolgan):  
    `<T><A2/1>Now this is usually the point at which I show you just how good I am with a knife-</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/3>Watch out, Professor!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Get behind me, you two!</T>`
*   **ドルガン** (Dolgan):  
    `<T><A3/1>Hmm.<W> Now, now. No need to panic. The only thing I'm throwing your way today is this puzzle...</T>`
*   **ドルガン** (Dolgan):  
    `<T>Heh! Clive was right. You've bitten off more than you can chew this time, Professor.</T>`
*   **ドルガン** (Dolgan):  
    `<T>You think you can handle the cut and thrust of this puzzle I'm serving up?</T>`
*   **ドルガン** (Dolgan):  
    `<T><A1/2>Hmm. Looks like I was wrong about that puzzle cutting you down.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We can pass, then?</T>`
*   **ドルガン** (Dolgan):  
    `<T>Hmm. Yes, but only because Clive instructed me not to touch a single hair on any of your pretty heads.</T>`
*   **ドルガン** (Dolgan):  
    `<T>Otherwise I'd be showing you the pointy end of my knife collection.<W> If you know what I mean.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Everyone stay away from him! He could be lying!</T>`
*   **ドルガン** (Dolgan):  
    `<T><A2/1>Don't worry, boy. Orders are orders. Besides, no one can stop Clive.</T>`
*   **ドルガン** (Dolgan):  
    `<T>Now get moving. The boss hates being made to wait.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Just what is Clive planning with this machine of his?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Placeholder text. Puzzle Cleared.</T>`

### `13_042120.lbin.txt` — Vista do alto

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A2/5>Oh my gosh! We're so high up!</T>`
*   **ルーク** (Luke Triton):  
    `<T>You're not wrong there, Flora, this machine is enormous. Just what could Clive be planning?</T>`

### `13_042500.lbin.txt` — Confronto dublado com Clive

*   **クラウス** (Clive) <V0010>:  
    `<V0010><T>So nice of you to join me, Professor.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T><A1/1>Whatever it is you have planned, you can't go through with it.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>We know what Bill and Dimitri did. When the world learns of it, they'll be punished.</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>You said you wanted justice, and isn't that justice enough?</V>`
*   **クラウス** (Clive) <V0050>:  
    `<V0050><T>That's a nice sentiment.</V>`
*   **クラウス** (Clive) <V0051>:  
    `<V0051><T>But without large-scale havoc, those fools in government will never change their ways!</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T>Listen to yourself, Clive! You-</V>`
*   **クラウス** (Clive) <V0070>:  
    `<V0070><T><A2/5>Who are you to argue with me? As a reporter, I've witnessed countless tragedies first-hand.</V>`
*   **クラウス** (Clive) <V0080>:  
    `<V0080><T>And it's clear that my life isn't the only one that's been destroyed in the name of progress!</V>`
*   **クラウス** (Clive) <V0090>:  
    `<V0090><T>To those in power, the rest of us {''}little people{''} are all just bumps on the road to a brighter tomorrow.</V>`
*   **クラウス** (Clive) <V0100>:  
    `<V0100><T><A1/5>The only thing a bully understands is force.</V>`
*   **クラウス** (Clive) <V0101>:  
    `<V0101><T>So you see, I have no choice but to level this place and rebuild it from the ground up.</V>`
*   **レイトン** (Professor Hershel Layton) <V0110>:  
    `<V0110><T>What you're saying is unthinkable!</V>`
*   **クラウス** (Clive) <V0120>:  
    `<V0120><T><A1/1>This conversation is over.</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T>No, Clive!</V>`

### `13_042510.lbin.txt` — Armadilha pós-confronto

*   **クラウス** (Clive):  
    `<T>How do you intend to get out of this one, Professor? Do tell!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Blast!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I just need to calm down and think clearly...</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There! We're safe now!</T>`

### `13_042700.lbin.txt` — Clive sai para o main event

*   **クラウス** (Clive) <V0010>:  
    `<V0010><T>You never fail to impress. Sadly, I must leave you now, as the main event is about to start.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>What do you mean?</V>`

### `13_044000.lbin.txt` — Plano do gerador dublado

*   **サリアス** (Celeste) <V0010>:  
    `<V0010><T>There has to be a generator somewhere here. All we need to do is find it and shut it down.</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T><A4/1>I see! We'll cut off the power at the source.</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T><A4/4>But wait... This place is huge. We don't have time to scour it all!</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T>What are we going to do?</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T>Look around you. The monitors in this control room are linked to cameras throughout the fortress.</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T><A2/2>Perhaps they can offer us some clue as to the generator's location.</V>`

### `13_044010.lbin.txt` — Busca nos monitors

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Look at all these monitors!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A3/2>We should be able to see all parts of the fortress from here.</T>`
*   **ルーク** (Luke Triton):  
    `<T>So we'll be able to find the location of the generator room!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>That's right, Luke. Now let's get searching.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Crikey. Maybe this isn't going to be as easy as I thought.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We mustn't stop searching, Luke. There are lives at stake.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>These monitors can help us pinpoint the location of the generator room.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Ah, there it is!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That's it, Luke!<W> Now all we have to do is feed these coordinates into the transport pod. Let's go!</T>`
*   **ルーク** (Luke Triton):  
    `<T>We're right behind you, Professor!</T>`

### `13_044015.lbin.txt` — Flavor generator

*   **サリアス** (Celeste):  
    `<T>We've got to use those monitors to work out the location of the generator room.</T>`

### `13_044020.lbin.txt` — Celeste bruxa

*   **ルーク** (Luke Triton):  
    `<T>Celeste, there's something I've been meaning to ask you.</T>`
*   **サリアス** (Celeste):  
    `<T>Oh? What's that?</T>`
*   **ルーク** (Luke Triton):  
    `<T>How in the world did you manage to get into the fortress?</T>`
*   **ルーク** (Luke Triton):  
    `<T>The professor and I had to do some pretty fancy manoeuvring to get here.</T>`
*   **ルーク** (Luke Triton):  
    `<T>What's more, this fortress is moving now. How did you catch up with us?</T>`
*   **サリアス** (Celeste):  
    `<T><A2/2>Heh heh. Didn't you know, Luke?<W> I'm a witch. I just hopped on my broom and flew up to the deck.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>Now you're just pulling my leg. Come on, I'm curious.</T>`
*   **サリアス** (Celeste):  
    `<T><A3/5>All right. If you're that interested, I suppose I can let you in on my secret.</T>`
*   **サリアス** (Celeste):  
    `<T>Just go through that door to the deck outside.</T>`

### `13_044030.lbin.txt` — Flavor deck

*   **サリアス** (Celeste):  
    `<T>You practically begged me to show you how I got here. Go on, go out onto the deck.</T>`

### `13_044040.lbin.txt` — Deck e flying machine

*   **ルーク** (Luke Triton):  
    `<T><A1/6>Oh my gosh! That's Don Paolo's flying machine!</T>`
*   **サリアス** (Celeste):  
    `<T>That's right. I begged him to fly me up here, so he loaded me in and sent me up.</T>`
*   **サリアス** (Celeste):  
    `<T>He controlled the machine from the ground. I didn't have to do anything. Amazing, isn't it?</T>`
*   **ルーク** (Luke Triton):  
    `<T>You can say that again!</T>`
*   **サリアス** (Celeste):  
    `<T>Funny, you don't seem so surprised, Professor.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Well, I already knew Paul had his machine with him.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>It's what he used to escape from the research facility that we infiltrated, isn't it, Celeste?</T>`
*   **サリアス** (Celeste):  
    `<T><A2/2>Nothing gets past you, does it, Professor?</T>`
*   **ルーク** (Luke Triton):  
    `<T><A3/1>So, now that we have Don Paolo's flying machine, we can come and go from here as we please.</T>`
*   **サリアス** (Celeste):  
    `<T>That's right, Luke.<W> <A2/6>Why, are you thinking of abandoning our mission?</T>`
*   **ルーク** (Luke Triton):  
    `<T>Never! I just thought it might be a good idea to drop Flora off somewhere safe before heading on.</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/5>No way! I'm staying here!</T>`
*   **サリアス** (Celeste):  
    `<T><A2/5>I can't say I blame you, Flora. You've got to stick close to the people you care about.</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Yes, but it is good to know we can <CR>return underground to continue exploring</C>.</T>`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Should we wish to, I mean.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>All right, everyone, we really shouldn't dawdle out here. We need to head to the generator room.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Oh yes, I'd nearly forgotten. Let's go, everyone!</T>`

### `13_044050.lbin.txt` — Flavor Don Paolo

*   **ドン・ポール** (Don Paolo):  
    `<T>How'd you like riding in my little flying machine, Layton? Jaw-dropping, isn't it?</T>`

### `13_044055.lbin.txt` — Device de coordenadas

*   **ルーク** (Luke Triton):  
    `<T>Um, Professor, how are we supposed to input the generator room coordinates?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><K>Hmm.</K><W> We should be able to enter them into one of these devices...</T>`
*   **ルーク** (Luke Triton):  
    `<T>Oh! What about that one on the wall over there? It's got numbers and things all over it.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Ah, the one with the green monitor? Yes, let's have a look at it.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm positive the small green screen over there is the device we're looking for.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Leave it to me, Professor. I'll investigate.</T>`

### `13_044060.lbin.txt` — Coordenadas no pod

*   **レイトン** (Professor Hershel Layton):  
    `<T>Punch in those coordinates, Luke. Once you do that, we should be able to go to the generator room.</T>`
*   **ルーク** (Luke Triton):  
    `<T>Look, Professor. The button for the generator room lit up!</T>`

### `13_044070.lbin.txt` — Coração da fortress e prime minister

*   **レイトン** (Professor Hershel Layton):  
    `<T>So this is the heart of the fortress.</T>`
*   **サリアス** (Celeste):  
    `<T>There's the control panel for the generator...<W> But it's locked away!</T>`
*   **ルーク** (Luke Triton):  
    `<T>The lock is a puzzle. Would you like to give it a shot, Professor?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'll do my best.</T>`
*   **サリアス** (Celeste):  
    `<T>You mustn't give up, Professor!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I've got to open this lock.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I think I've done it! Stand back, everyone.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>My word...</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>Is that...the prime minister?</T>`

### `13_045000.lbin.txt` — Ameaça dublado do pod

*   **クラウス** (Clive) <V0010>:  
    `<V0010><T>Ha ha ha ha!<W> <A2/6>I knew you'd find your way here sooner or later.</V>`
*   **クラウス** (Clive) <V0020>:  
    `<V0020><T>Though if you're hoping to find our fearless leader, I'm afraid he's indisposed at the moment.</V>`
*   **クラウス** (Clive) <V0030>:  
    `<V0030><T><A2/6>I know how you like to play the hero, but I'd advise you not to get any foolish ideas.</V>`
*   **クラウス** (Clive) <V0031>:  
    `<V0031><T>You see, the prime minister is perched on a very special seat.</V>`
*   **クラウス** (Clive) <V0040>:  
    `<V0040><T>And should you try to move him from that pod, this whole fortress will detonate.</V>`
*   **クラウス** (Clive) <V0050>:  
    `<V0050><T>Also, you should know that there's enough charge in here to level most of London.</V>`
*   **クラウス** (Clive) <V0060>:  
    `<V0060><T>Of course, London's getting levelled either way. He he he!</V>`
*   **クラウス** (Clive) <V0070>:  
    `<V0070><T>Now, I do hate to run, but I have work to do.</V>`

### `13_045020.lbin.txt` — Heartbeat e pocket watch

*   **サリアス** (Celeste):  
    `<T>Look at this device. It seems to be monitoring the prime minister's heartbeat.</T>`
*   **サリアス** (Celeste):  
    `<T>It will detonate the charge if the sound of his heartbeat disappears.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Perhaps we can sever the connection somehow.</T>`
*   **サリアス** (Celeste):  
    `<T>I wouldn't do that, Professor.</T>`
*   **サリアス** (Celeste):  
    `<T>See how there are two sets of wires in the circuit?</T>`
*   **サリアス** (Celeste):  
    `<T>I don't think we'll be able to cut both sets before the device reacts.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Amazing, Celeste. You obviously possess a better understanding of mechanics than I do.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Your sister would be very proud.</T>`
*   **サリアス** (Celeste):  
    `<T>Hey, I've just had an idea.<W> <A2/2>What if we use this?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>That...is the pocket watch I gave Claire, long ago.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>And here I thought it had been lost in the explosion.</T>`
*   **サリアス** (Celeste):  
    `<T><A2/6>No... I actually found it when going through Claire's things after the accident.</T>`
*   **サリアス** (Celeste):  
    `<T>Unfortunately, the watch has been broken since I found it.</T>`
*   **サリアス** (Celeste):  
    `<T>No matter how much I wind it up, it never seems to run for more than 10 minutes.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I see where you're going with this, Celeste.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>You're suggesting we replace the sound of the prime minister's heart with that of the pocket watch?</T>`
*   **サリアス** (Celeste):  
    `<T><A1/1>Exactly. It's risky, but it seems to be the only option we've got.</T>`
*   **サリアス** (Celeste):  
    `<T>We'll need to disconnect the circuit from the prime minister and attach the watch in one fell swoop.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>But even if we succeed, the watch will stop running in 10 minutes and the fortress will explode anyway!</T>`
*   **ルーク** (Luke Triton):  
    `<T>We could end up putting the people of London in real danger!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Luke, if we take no action, London will face a greater danger than any explosion.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This is our only chance to stop Clive. The chances of success are slim, but we must try.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Argh. I'll have to try again.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I must get it right this time.</T>`
*   **サリアス** (Celeste):  
    `<T>Professor, that's it! The watch is connected now!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Yes, but our work here is far from over.</T>`

### `13_046000.lbin.txt` — 10 minutos e reverse energy

*   **ルーク** (Luke Triton) <V0010>:  
    `<V0010><T>We've got 10 minutes to get out of here before the fortress explodes! Now what?!</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>We need to reverse the energy flow. That will break the generator and shut down the fortress.</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T>How are we going to do that?</V>`
*   **サリアス** (Celeste) <V0040>:  
    `<V0040><T>I have an idea! Look over here!</V>`

### `13_046010.lbin.txt` — Gears core

*   **サリアス** (Celeste):  
    `<T>These gears form the core of the generator. If we can just reverse their movement...</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We can effectively overload the fortress's power supply, thus putting a halt to Clive's plan.</T>`
*   **サリアス** (Celeste):  
    `<T><A4/4>I see you've been thinking about this too, Professor. Is there anything you don't know about?</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>A gentleman must have his hobbies. It just so happens that I have an interest in machines.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A2/2>Amazing, Professor!</T>`
*   **サリアス** (Celeste):  
    `<T><A1/1>It's too early to celebrate, Luke. If we fail here, many lives may still be lost.</T>`
*   **サリアス** (Celeste):  
    `<T>Are you up to the challenge, Professor?</T>`
*   **サリアス** (Celeste) <V0010>:  
    `<V0010><T>It's all up to you now, Professor.</V>`

### `13_046020.lbin.txt` — Running out of time

*   **サリアス** (Celeste):  
    `<T><A2/6>We're running out of time!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Not to worry, Celeste.<W> I won't fail again.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This time I'll get it right!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It's done!</T>`

### `13_047000.lbin.txt` — Autodestruição dublado

*   **サリアス** (Celeste) <V0010>:  
    `<V0010><T><A2/2>You did it!</V>`
*   **サリアス** (Celeste) <V0020>:  
    `<V0020><T><A1/1>What was that?</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>Reversing the energy flow has caused the fortress to start destroying itself!</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T>Oh no!</V>`
*   **サリアス** (Celeste) <V0050>:  
    `<V0050><T>We've got to get out of here right now!</V>`

### `13_047010.lbin.txt` — Pod falha, fuga de carro

*   **ルーク** (Luke Triton):  
    `<T>The transport pod doesn't seem to be working.</T>`
*   **サリアス** (Celeste):  
    `<T>The fortress is tearing itself apart and causing some of the systems to go haywire.</T>`
*   **サリアス** (Celeste):  
    `<T>I don't think we can risk going back up to the deck!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Then we'll just have to use the car to escape. This way!</T>`

### `13_047020.lbin.txt` — Flavor autodestruição rápida

*   **レイトン** (Professor Hershel Layton):  
    `<T>There's no time to go back. The fortress is destroying itself even faster than I anticipated!</T>`

### `13_048010.lbin.txt` — Flavor Clive

*   **レイトン** (Professor Hershel Layton):  
    `<T>Clive...</T>`

### `13_048015.lbin.txt` — Belle no caos

*   **ベル** (Belle):  
    `<T>My, what a commotion there is in town today!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>This place could be reduced to rubble at any moment. Go quickly to the clock shop on Midland Road!</T>`
*   **ベル** (Belle):  
    `<T>Really?<W> Fluke, my darling, did you hear that? We've got to run!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/3>Sorry, Belle. I'm going with the professor to try to stop the man responsible for this mess!</T>`
*   **ベル** (Belle):  
    `<T><A2/6>Oh Flukey... Your bravery makes me weak at the knees.</T>`
*   **ルーク** (Luke Triton):  
    `<T><A3/2>Belle, listen. You've got to get out of here now.</T>`
*   **ベル** (Belle):  
    `<T><A3/5>If you tell me it's for the best, Fluke, I'll do as you say. I trust you.</T>`
*   **ベル** (Belle):  
    `<T><A3/7>But before you go, come close and give your sweetheart a kiss for good luck!</T>`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>P-Professor! I think we should get moving!</T>`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `13_041060` | **Screw Selection Enigma (carro)** | Don Paolo não sabe which screw to use na última junta do Laytonmobile; Layton resolve com trial-error, resposta é This is the one. |
| `13_042020` | **Door Enigma Lock (infiltração)** | Porta com enigma lock padrão de Clive, portão para interior da fortress |
| `13_042030` | **Coded Instructions Enigma (pod)** | Nota com uncrackable code explicando transport pod; enigma diegético longo com múltiplas tentativas Hmm. I seem to have made an error |
| `13_042070` | **Glass Cage Enigma Lock** | Weird glass cage com enigma lock que prende Flora, "Help me, Professor!" |
| `13_042100` | **Key Code Enigma (surveillance room)** | Monitor guarda key code; enigma com tentativas Oh dear. That's not right.; fuga via manipulação psicológica do a runner |
| `13_042110` | **Dolgan's Knife Enigma (cut and thrust)** | Muscle troca knife por enigma, falha com "Looks like I was wrong about that puzzle cutting you down", revela ordem de não ferir |
| `13_042510` | **Clive's Escape Trap Enigma** | Após "How do you intend to get out of this one, Professor?" Layton resolve com "There! We're safe now!" |
| `13_044010` | **Monitor Search Enigma (generator)** | Busca nos monitors para pinpoint generator room, coordenadas para transport pod |
| `13_044055`–`13_044060` | **Green Monitor Coordinates Enigma** | Device com small green screen, enigma de input; "The button for the generator room lit up!" |
| `13_044070` | **Generator Panel Lock Enigma** | Control panel locked away, abre para revelar prime minister no pod |
| `13_045020` | **Heartbeat Swap Enigma (pocket watch)** | Troca do heartbeat por pocket watch em one fell swoop, 10 minutos de janela, enigma com Argh. I'll have to try again |
| `13_046010`–`13_046020` | **Gears Reverse Enigma (overload)** | Reverse movement das gears core para overload power supply, "We're running out of time!" |
| `13_042510`/`13_046020` lore | **Autodestruição (evento)** | Reversing energy flow causa fortress destroying itself, systems go haywire, transport pod falha |

**Eventos narrativos sem enigmas diretos:** reação de Chelmey war machine (`041030`), despedida técnica com Celeste (`041040`), oferta do carro na colina (`041050`), prioridade dublado (`042010`), mapa da contraption (`042040`), reencontro e recusa de recuar (`042080`), pista da surveillance room (`042090`), ameaça do Monitor (`042099`), vista do alto (`042120`), manifesto de Clive little people (`042500`), saída para main event (`042700`), plano do gerador e câmeras (`044000`), gag da witch/broom (`044020`), revelação da flying machine no deck (`044040`), aviso de Don Paolo flying (`044050`), ameaça do pod detonador (`045000`), fuga de carro vs deck (`047010`), aviso a Belle para clock shop Midland Road (`048015`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Capítulo de infiltração mais denso pós-Cap. 11:** 42 arquivos superam Cap. 12, mas com menos dublagem contínua; picos dublados são `042010`/`042080` (resgate), `042500`/`042700` (Clive), `044000`/`045000`/`046000`/`047000` (gerador). O restante é exploração com enigma locks em cadeia, típico de dungeon final.
*   **Don Paolo redimido via Laytonmobile:** O carro do hospital model vira real via blueprints roubados — payoff de `11_033330` ropey flying machine; gag do screw repete motivo de Paolo como inventor e bridge entre facility do Cap. 11 e fortress móvel. A flying machine reaparece no deck como Chekhov's gun plantada desde `11_033545` e paga em `13_044040` com controle remoto do solo.
*   **Family como fachada de Clive:** `13_042030` "Dimitri was just a puppet. Clive's been our gaffer from day one!" consolida retcon de `12_039010`; `Dolgan`/`Gorocky (Lockjaw)` são os únicos Family nomeados no capítulo e ambos neutralizados via enigma/psicologia, mantendo regra de Layton de non-violence.
*   **Pocket watch como timer narrativo:** O relógio quebrado de Claire (10 minutos) substitui o infinity trick do Cap. 12; mecanismo de two sets of wires justifica urgência e limita janela de 10 minutos que estrutura `046000`–`047020`. Frase "pocket watch I gave Claire, long ago" amarra Prólogo e hospital do Cap. 11.
*   **Prime minister como bomba humana:** "special seat" + "enough charge to level most of London" + "London's getting levelled either way" triplica threat; heartbeat monitor ecoa minefield do Cap. 12 mas agora com refém real, elevando stakes de bluff para dilema moral de Luke.
*   **Structure preservation:** Diálogo mantido em inglês UK original; nomes `Laytonmobile`, `Midland Road`, `Clive`, `Celeste`, `Dimitri`, `Belle/Flukey` preservados; `<CR>return underground to continue exploring</C>` de `044040` mantido como tag de condição de gameplay; `Placeholder text. Puzzle Cleared.` preservado como marcador pós-enigma em `042100`/`042110`.
