# Capítulo 02 — O Cassino Gilded 7 e o Luke do Futuro | Professor Layton and the Unwound Future

> **Capítulo 02 — O Cassino Gilded 7 e o Luke do Futuro (The Gilded 7 Casino / Future Luke)** — Análise de dump LSCR para `Textos Originais/txt/uk/02/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/02/`
> Total de arquivos escaneados: **31**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético

---

## 1. Arquivos Cobertos

Todos os 31 dumps `.lbin.txt` em `uk/02`:

```
02_000000.lbin.txt  — [vazio - apenas cabeçalho]
02_015020.lbin.txt  — Saída do Green Hospital - Layton/Luke decidem ir ao Gilded 7 Casino, Laytonmobile quebrada
02_015030.lbin.txt  — Sharon - pergunta sobre cassino na Flatstone Street
02_015040.lbin.txt  — Luke procura Dr. Schrader desaparecido
02_015050.lbin.txt  — Layton: é preciso pegar o trem de volta a Flatstone Street
02_015060.lbin.txt  — Retorno a Flatstone Street - não veem cassino, vão perguntar a local
02_015070.lbin.txt  — Family Goon hostil - Luke leva bronca, Layton brinca sobre animais selvagens
02_015080.lbin.txt  — Avistamento do homem nervoso (Hazel) visto anteriormente
02_015090.lbin.txt  — Hazel / Edgar em pânico com o chapéu - Layton tem sósia temido, Becky sugerida
02_015100.lbin.txt  — Family Goon - Boss Bostro odeia crianças, cassino perigoso
02_015110.lbin.txt  — Bacchus - ainda em preparação, voltem depois
02_015120.lbin.txt  — Max - BZZT sobre cassino, indica Becky
02_015130.lbin.txt  — Family Goon repreende levar criança a cassino
02_015140.lbin.txt  — Becky - indica Gilded 7 ao norte da praça da estação, Family haunt, Granny dormindo
02_015145.lbin.txt  — Margaret - despedida curta ao sair do hotel
02_015150.lbin.txt  — Max - tutorial de puzzles escondidos / hint coins (toque em pontos suspeitos)
02_015180.lbin.txt  — Guarda sumiu - confirmação da dica de Becky, seguir para norte
02_017000.lbin.txt  — Layton vê mulher que lembra alguém do passado (presságio Claire)
02_017010.lbin.txt  — Delroy (デロイ) bloqueia passagem - puzzle e aviso sobre perigo do chapéu
02_017020.lbin.txt  — Avistamento do Gilded 7 Casino
02_017030.lbin.txt  — Harold (ハロルド) - porteiro do Gilded 7, exige membership card, puzzle de entrada
02_018000.lbin.txt  — Interior do Gilded 7 - fontes e piso luxuosos, busca pelo Luke do futuro
02_019000.lbin.txt  — Primeiro encontro com Future Luke (未来ルーク) - teste de identidade, Don Paolo (dublado V0010-V0170)
02_020000.lbin.txt  — [vazio - apenas cabeçalho]
02_020010.lbin.txt  — Duelo de puzzles das 4 cartas - Future Luke vs Layton, loophole do naipe ausente
02_021000.lbin.txt  — Future Luke reconhece Layton genuíno - convite ao depósito nos fundos
02_021010.lbin.txt  — Revelação inicial: o gênio do mal é o próprio Hershel Layton ("devil in the top hat")
02_021020.lbin.txt  — Exposição longa: explosão da máquina, Stahngun vivo, Layton acolhe cientista, wormhole da relojoaria, sequestro de cientistas do passado, QG em Chinatown, nome falso de Stahngun
02_021030.lbin.txt  — Future Luke apressa retorno a Flatstone Street
02_022000.lbin.txt  — Bostro confunde Layton com o chefe - sequestro de Future Luke, fuga (dublado V0010-V0130)
02_023010.lbin.txt  — Coin Machine Gun Puzzle - placeholder de puzzle debug ("Quick! Throw those parts together!")
```

> **Nota:** 2 arquivo(s) contém(êm) apenas o cabeçalho LSCR sem blocos de texto: `02_000000.lbin.txt`, `02_020000.lbin.txt`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 02 |
|---|---|---|
| `ルーク` | **Luke Triton** | Aprendiz, co-protagonista, constrangido com Future Luke |
| `レイトン` | **Professor Hershel Layton** | Protagonista, alvo de pânico pelo chapéu, investiga sósia |
| `シャロン` | **Sharon (Hospital Receptionist)** | Recepcionista do Green Hospital, diz não conhecer cassino |
| `ヘイゼル` | **Hazel / Edgar (Nervous Man)** | Homem nervoso que revela nome Edgar, teme o "Layton do futuro" |
| `クローンマフィア` | **Family Goon / Clone Mafia** | Capangas idênticos da Family, bloqueiam ruas, avisam sobre Bostro |
| `バッカス` | **Bacchus (Restaurant Owner)** | Dono de restaurante em Flatstone, em preparação |
| `マックス` | **Max (Quiz Boy)** | Garoto quiz, tutorial de enigmas escondidos |
| `ベッキー` | **Becky (Hotel Duke Receptionist)** | Recepcionista, única que ajuda com direções ao cassino |
| `マーガレット` | **Margaret (Hotel Duke Manager)** | Gerente, breve despedida e bronca em Becky |
| `デロイ` | **Delroy / Deroy (Street Blocker)** | Bloqueador de rua ao norte da estação, adverte sobre chapéu |
| `ハロルド` | **Harold (Gilded 7 Doorman)** | Porteiro do Gilded 7, exige membership card |
| `未来ルーク` | **Future Luke (Older Luke)** | Luke 10 anos mais velho, convoca Layton para deter "evil Layton" |
| `ボストロ` | **Bostro (Gilded 7 Boss)** | Chefe do cassino, odeia crianças, sequestra Future Luke |

Tags de controle observadas: `<V0010>`–`<V0170>` em `02_019000` (encontro dublado), `<V0010>`–`<V0130>` em `02_022000` (Bostro), `<V0010>`–`<V0060>` em `02_021000`; restante não-dublado (`<T>` puro). `<W>` / `<W30>` pausas, `<A1/2>` etc. animações, `<K>` efeito cinético, `<S671>` efeito especial de acerto.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Saída do Green Hospital — Rumo ao Gilded 7 Casino (`02_015020`–`02_015050`)
No estacionamento atrás do Green Hospital, diante da Laytonmobile empoeirada e quebrada, Luke começa a aceitar a viagem ao futuro e Layton recentra a investigação no autor da carta, identificando-o como o próprio Luke e propondo irem ao Gilded 7 Casino para obter esclarecimentos face a face. Diante do carro inutilizável, Layton admite não ter habilidade para consertá-lo e decide seguir a pé, o que Luke aprova como melhor forma de investigação. Sharon, na recepção, confirma haver um cassino em Flatstone Street mas diz que não é lugar para crianças e afirma desconhecer a localização exata, sugerindo perguntar a um residente local. Luke então nota o sumiço de Dr Schrader, que Layton atribui a um passeio animado após a visita, e o grupo conclui que precisa pegar o trem de volta a Flatstone Street.
> Gancho: "The author of this letter is Luke Triton. In other words, Luke, the sender is you." / "Let's head to the Gilded 7 Casino."

### 3.2 Retorno a Flatstone Street — A Cidade Hostil (`02_015060`–`02_015130`)
De volta a Flatstone Street sem avistar o cassino, Layton e Luke tentam pedir informações e revelam o clima opressivo de Londres do futuro. Um Family Goon rosna e conta regressivamente para Luke parar de encarar, e Layton tenta aliviar a tensão brincando sobre o talento de Luke com animais selvagens. Em seguida encontram Hazel, que entra em pânico ao ver o chapéu, revela chamar-se Edgar e interpreta a pergunta sobre o Gilded 7 como teste para ver se vai entregar segredos, fugindo gritando; Layton deduz que um sósia seu tem reputação temível, recusa a sugestão de Luke para tirar o chapéu alegando que um gentleman não anda de cabeça descoberta, e decide pedir ajuda a Becky. Outros Goons reforçam o perigo avisando que Boss Bostro odeia crianças e que o cassino não é lugar para levar um garoto, enquanto Bacchus dispensa por estar em preparação e Max, em estilo quiz com BZZT/DING, confirma saber onde é mas redireciona a Becky por medo do pai.
> Gancho: "Boss Bostro hates kids, you see. Can't stand 'em." / "Nonsense, Luke. A gentleman can't very well walk around with a bare head now, can he?"

### 3.3 Becky Entrega a Rota — O Norte da Estação (`02_015140`–`02_015180`)
Becky no Hotel Duke é a única fonte útil: alerta que o Gilded 7 é um Family haunt e, verificando que Granny dorme novamente, indica seguir ao norte da praça em frente à Flatstone Street Station. Luke associa a dica ao guarda que bloqueava o norte antes; Becky explica que os capangas rotacionam postos frequentemente e há boa chance de passagem agora. A conversa é interrompida por Margaret, que repreende Becky por tagarelice, mas Layton a defende e Becky repete a direção de forma concisa. Ao saírem, Margaret se despede brevemente e logo Luke confirma que o guarda sumiu, validando a intuição de Becky e liberando o avanço ao norte.
> Gancho: "Just head north from the square in front of the station. You'll see the casino eventually." / "Those thugs move around from post to post pretty often."

### 3.4 Interlúdio — Tutorial Escondido e Presságio (`02_015150` / `02_017000`)
Em interlúdio, Max oferece um tutorial de enigmas escondidos, contando que encontrou um enigma ao tocar num ponto suspeito e explicando que toques em áreas com splash de água ou puff de poeira podem revelar moedas de dica e enigmas. Pouco antes do cassino, Layton tem um momento de vulnerabilidade ao ver uma mulher passar que lhe lembra alguém do passado; Luke percebe o abatimento e Layton disfarça dizendo que deve ser engano, em forte presságio de Claire.
> Gancho: "I found it by touching a suspicious-looking spot." / "She just reminded me of someone I knew a long time ago."

### 3.5 Últimos Bloqueios — Delroy e o Porteiro Harold (`02_017010`–`02_017030`)
No último trecho até o cassino, Delroy barra a passagem, ironiza a desculpa de ir ao cassino encontrar alguém e os sussurros de Luke, exigindo enigma para liberar caminho; após a solução, lança aviso críptico sobre o perigo do chapéu e se recusa a revelar mais para manter o suspense. Logo adiante Luke avista o Gilded 7 e Layton confirma a chegada. Na porta, Harold exige membership card para filtrar a elite e propõe um teste de intelecto, elogiando o chapéu como prova de bom gosto; após o enigma resolvido, libera a entrada.
> Gancho: "Danger lurks about that hat of yours. You'd best watch yourself around here." / "Welcome to the Gilded 7."

### 3.6 Dentro do Gilded 7 — O Teste do Luke do Futuro (`02_018000`–`02_020010`)
No interior luxuoso com fontes e piso imponente, Layton pede discrição enquanto procuram Future Luke em meio ao espaço amplo. O encontro é totalmente dublado: Future Luke, mais alto, comenta o quanto era pequeno, Layton pergunta o motivo da convocação e Future Luke exige prova de identidade alegando muitos impostores em Londres do futuro e evocando o precedente de Don Paolo como mestre de disfarces; Luke jovem protesta mas Layton aceita. O duelo intelectual usa quatro cartas: Future Luke propõe achar o spade com três condições, Layton resolve e é elogiado; Layton retribui com variação contendo loophole intencional — nunca declarou que há um naipe de cada — e Future Luke inicialmente declara insolúvel até Layton revelar que não há spade na mesa, lição sobre premissas omitidas.
> Gancho: "How do I know the man before me now isn't Don Paolo in another of his costumes?" / "Tell me, did I ever state that the four cards on the table included one card from each suit?"

### 3.7 A Grande Revelação — O Layton do Futuro como Vilão (`02_021000`–`02_021020`)
Validado o duelo, Future Luke admite que já estava convencido mas quis duelar com o mentor, e leva o grupo ao depósito nos fundos para falar sem olhares. Lá dá as boas-vindas à London do futuro e, diante do ceticismo sobre mudanças da cidade e do estado de Schrader, revela que o gênio do mal que domina a cidade é o próprio Hershel Layton — o diabo da cartola que rege das sombras. Na exposição mais longa do capítulo, Future Luke explica que o artigo sobre a explosão é recente para Layton e Luke mas tem 10 anos ali, com primeiro-ministro desaparecido e caos parlamentar; Stahngun sobreviveu, escondeu-se e foi acolhido pelo próprio Layton, que se afastou de Luke, passou a frequentar o submundo, usou o intelecto para financiá-lo e ficou obcecado por viagem no tempo e mudar o passado. Com apoio financeiro, Stahngun construiu não uma máquina seletiva, mas um túnel/buraco de minhoca fixo de 10 anos ancorado na relojoaria de Midland Road, sem controle de destino; por isso o grupo usou relógio para se mover entre épocas. Future Luke pede ajuda para deter o outro Layton, que agora sequestra cientistas brilhantes do passado (pois muitos morreram na explosão) para construir máquina totalmente operacional; seu QG não é o cassino mas o coração de Chinatown, e Layton aceita ir até lá apesar das dúvidas, com Luke insistindo em acompanhar. Future Luke ainda solta a pista de que Stahngun é nome falso sem registro, e apressa o retorno a Flatstone Street.
> Gancho: "His name is Hershel Layton. The evil genius is you, Professor." / "It would be more accurate to describe it as a sort of tunnel between two periods in time."

### 3.8 Interrupção Brutal — Bostro Ataca (`02_022000`)
Quando tentam deixar o Gilded 7, Bostro intercepta o trio e confunde Layton com o chefe por causa do traje, ordenando interrogatório dos três. Future Luke grita para fugirem e é agarrado, enquanto Layton assume a liderança e ordena a fuga; o capítulo fecha em perseguição com Future Luke capturado e o QG de Chinatown como próximo destino, deixando em aberto o uso do buraco de minhoca e a identidade real de Stahngun. O arquivo adicional `02_023010` é apenas placeholder de enigma Coin Machine Gun sem integração narrativa.
> Gancho: "Oi, what are you doin', wearin' the boss's get-up? This your idea of a joke?" / "Professor, run away while you can!"
> **Cliffhanger:** Confronto com o Layton do futuro adiado; Future Luke capturado por Bostro obriga Layton e Little Luke a escapar do Gilded 7 rumo a Chinatown, com o mistério do buraco de minhoca e do falso Stahngun em aberto.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag) — <Vxxxx> se dublado` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, mas esperas `<W>` e animações `<A>` anotadas quando presentes.

### `02_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `02_015020.lbin.txt` — Saída do Green Hospital, decisão pelo Gilded 7

*   **ルーク** (Luke Triton):  
    `Professor, I'm starting to believe that we've really travelled to the future...`
*   **レイトン** (Professor Hershel Layton):  
    `Hmm... Let's focus on what we're sure of for now.`
*   **レイトン** (Professor Hershel Layton):  
    `The author of this letter is Luke Triton. In other words, Luke, the sender is you.`
*   **レイトン** (Professor Hershel Layton):  
    `We've been following his directives all this time.`
*   **レイトン** (Professor Hershel Layton):  
    `Perhaps meeting him face-to-face will shed some light on our current situation.`
*   **レイトン** (Professor Hershel Layton):  
    `Let's head to the Gilded 7 Casino.`
*   **ルーク** (Luke Triton) *(<W>)*:  
    `All right, Professor. It's a shame we can't drive there, though.`
*   **レイトン** (Professor Hershel Layton):  
    `Unfortunate as that may be, it doesn't look as though my car will be going anywhere soon.`
*   **ルーク** (Luke Triton) *(<A2/2>)*:  
    `Never mind. After all, the best way to do the legwork for an investigation is on foot.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `Ha ha! I couldn't agree with you more, my boy.`
*   **レイトン** (Professor Hershel Layton):  
    `Repairing this car requires more skill than I possess, unfortunately. Let's proceed on foot.`

### `02_015030.lbin.txt` — Sharon sobre o cassino

*   **シャロン** (Sharon):  
    `A casino on Flatstone Street?`
*   **シャロン** (Sharon):  
    `Yeah, there is one, but I'm not sure it's the kind of place you can take kids...`
*   **レイトン** (Professor Hershel Layton):  
    `Don't worry, madam. We're just meeting a friend there.`
*   **レイトン** (Professor Hershel Layton):  
    `Do you happen to know where on Flatstone Street the casino is located?`
*   **シャロン** (Sharon) *(<W>)*:  
    `Nah, sorry. Not my scene. You should ask someone in the area.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, I suppose a resident of Flatstone Street would be able to tell us. Thank you.`

### `02_015040.lbin.txt` — Onde está Dr. Schrader?

*   **ルーク** (Luke Triton):  
    `Hey, where's Dr Schrader gone?`
*   **レイトン** (Professor Hershel Layton):  
    `Well, our visit did seem to put him in high spirits. Perhaps he ventured out for a walk.`

### `02_015050.lbin.txt` — Trem de volta a Flatstone Street

*   **レイトン** (Professor Hershel Layton):  
    `We need to take the train back to Flatstone Street if we're to visit the casino, Luke.`
*   **ルーク** (Luke Triton):  
    `Okay, Professor.`

### `02_015060.lbin.txt` — De volta a Flatstone Street

*   **レイトン** (Professor Hershel Layton):  
    `Here we are, back on Flatstone Street.`
*   **ルーク** (Luke Triton) *(<A2/1>)*:  
    `Yes, but I can't see anything around here that looks like a casino.`
*   **レイトン** (Professor Hershel Layton):  
    `I think our best bet would be to ask a local.`
*   **ルーク** (Luke Triton) *(<A3/1>)*:  
    `Oh look! There's someone we can ask! Wait here, Professor.`

### `02_015070.lbin.txt` — Goon hostil

*   **クローンマフィア** (Family Goon) *(<W>)*:  
    `You've got exactly five seconds to stop gawpin', boy. One... Two...`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `I-I'm very sorry, sir!`
*   **レイトン** (Professor Hershel Layton):  
    `I gather that didn't go very well, Luke?`
*   **ルーク** (Luke Triton) *(<A1/3>)*:  
    `Let's ask someone else, Professor. I can't even look at that man without him snapping at me.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `And all this time I thought you had a talent for communicating with wild animals! Ha ha!`
*   **ルーク** (Luke Triton) *(<A1/5> <W>)*:  
    `Don't laugh, Professor! That man was scary!`
*   **レイトン** (Professor Hershel Layton):  
    `Now now, don't look so sour. I was only trying to lighten the mood a little.`
*   **レイトン** (Professor Hershel Layton):  
    `Why don't we find someone else to help us?`
*   **クローンマフィア** (Family Goon) *(<W>)*:  
    `I thought I told you to stop gawpin'?! Now get outta my face!`

### `02_015080.lbin.txt` — Avistamento de Hazel

*   **ルーク** (Luke Triton) *(<W>)*:  
    `Hey! It's that nervous-looking fellow we saw earlier.`

### `02_015090.lbin.txt` — Hazel / Edgar em pânico

*   **ヘイゼル** (Hazel / Edgar) *(<A2/5> <W>)*:  
    `What do you want from me? Don't hurt me! Please, I'm b-b-begging you!`
*   **ルーク** (Luke Triton):  
    `What? Why are you scared of me?`
*   **ヘイゼル** (Hazel / Edgar) *(<W> <A4/5>)*:  
    `You? No, it's your friend there with the b-b-big hat! Augh! He's looking right at me!`
*   **レイトン** (Professor Hershel Layton):  
    `Please calm down, sir. I mean you no harm. You must have me confused with someone else.`
*   **レイトン** (Professor Hershel Layton):  
    `The only thing I want to know is the location of the Gilded 7 Casino. It is around here, isn't it?`
*   **ヘイゼル** (Hazel / Edgar):  
    `The casino?`
*   **ヘイゼル** (Hazel / Edgar) *(<A5/1> <W>)*:  
    `Oh, I get it! You're testing me! You want to see if Edgar's going to spill the b-b-beans!`
*   **ヘイゼル** (Hazel / Edgar):  
    `And if I do, you're going to send me on a one-way trip to nowhere!`
*   **ルーク** (Luke Triton):  
    `What are you talking about?`
*   **ヘイゼル** (Hazel / Edgar) *(<W> <A6/0>)*:  
    `Augh! Somebody help meee!`
*   **ルーク** (Luke Triton):  
    `There he goes again...`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `Poor fellow. It sounds as though he's had a run-in with someone who looks like me.`
*   **ルーク** (Luke Triton):  
    `He's not the first person to react strangely to your hat.`
*   **レイトン** (Professor Hershel Layton):  
    `Hmm. Yes, it seems my doppelgänger has quite a fearsome reputation.`
*   **ルーク** (Luke Triton):  
    `Well... Maybe you should take your hat off for the time being. Just to avoid confusion, you know.`
*   **レイトン** (Professor Hershel Layton) *(<A3/2>)*:  
    `Nonsense, Luke. A gentleman can't very well walk around with a bare head now, can he?`
*   **ルーク** (Luke Triton) *(<W>)*:  
    `Er... I suppose not. Well, what's our next move?`
*   **レイトン** (Professor Hershel Layton) *(<A2/2>)*:  
    `That girl from the hotel, Becky, has been quite helpful. Let's try asking her for directions.`

### `02_015100.lbin.txt` — Goon alerta sobre Boss Bostro

*   **クローンマフィア** (Family Goon):  
    `Well well, look who it is.`
*   **ルーク** (Luke Triton):  
    `Hello, sir. Sorry to bother you mid-shift, but do you know where the Gilded 7 Casino is?`
*   **クローンマフィア** (Family Goon) *(<W>)*:  
    `The Gilded 7?! I ain't your dad or nothing, but ain't you a bit young to be hittin' the tables?`
*   **ルーク** (Luke Triton) *(<A1/5>)*:  
    `Oh, I'm not interested in gambling. I'm just meeting someone there.`
*   **クローンマフィア** (Family Goon):  
    `Whatever your excuse is, you're gonna have a hard time gettin' in.`
*   **クローンマフィア** (Family Goon):  
    `Boss Bostro hates kids, you see. Can't stand 'em.`
*   **クローンマフィア** (Family Goon) *(<W>)*:  
    `He'll have your hide if he sees you in his casino. I'd stay away if I was you.`
*   **ルーク** (Luke Triton):  
    `I see...`

### `02_015110.lbin.txt` — Bacchus

*   **バッカス** (Bacchus):  
    `Sorry fellas, we're still setting up here. Come back later!`

### `02_015120.lbin.txt` — Max sobre o cassino

*   **ルーク** (Luke Triton):  
    `Hiya Max. Do you know where the Gilded 7 Casino is?`
*   **マックス** (Max) *(<A3/0> <W> <A2/5>)*:  
    `BZZT! My dad says the casino's no place for children. We probably shouldn't even be talking about it.`
*   **ルーク** (Luke Triton):  
    `But you do know where it is?`
*   **マックス** (Max) *(<A1/1> <W>)*:  
    `DING DING DING! Correct! But I can't tell you. My dad would kill me!`
*   **マックス** (Max):  
    `Maybe Becky can tell you, though. Try asking her!`

### `02_015130.lbin.txt` — Goon repreende levar criança

*   **クローンマフィア** (Family Goon) *(<W>)*:  
    `The casino? With that kid? Are you barmy or what?`
*   **レイトン** (Professor Hershel Layton):  
    `No, sir. You misunderstand me. We aren't going there to gamble, merely to-`
*   **クローンマフィア** (Family Goon):  
    `A casino ain't no place to take a child! Even I know that!`
*   **ルーク** (Luke Triton):  
    `Wow! It's really nice of you to worry about me.`
*   **レイトン** (Professor Hershel Layton):  
    `Indeed, but you really needn't be concerned about the boy's well-being. Especially when-`
*   **クローンマフィア** (Family Goon):  
    `Look mate, you don't take kids into a place like that, and that's the end of it.`

### `02_015140.lbin.txt` — Becky dá a direção

*   **ベッキー** (Becky):  
    `Hmm? You're looking for the Gilded 7 Casino?`
*   **レイトン** (Professor Hershel Layton):  
    `Yes. We're supposed to meet someone there.`
*   **ベッキー** (Becky) *(<A1/5>)*:  
    `Well if you say so... But I think you ought to know that the place is a favourite Family haunt.`
*   **ルーク** (Luke Triton):  
    `We appreciate your concern, Becky, but we really do need to go there.`
*   **ベッキー** (Becky) *(<W>)*:  
    `All right... Oh good, Granny's asleep again.`
*   **ベッキー** (Becky) *(<A2/2>)*:  
    `I don't think she'd be too keen on me directing you to a hotbed of criminal activity like that.`
*   **ルーク** (Luke Triton) *(<W30> <W>)*:  
    `Oh... Er... We don't need to worry about our safety, do we? Not that I'm scared or anything.`
*   **ベッキー** (Becky):  
    `Tee hee! Good! Bravery is an admirable character trait, even if it can get you into trouble...`
*   **ベッキー** (Becky):  
    `So anyway, you know where Flatstone Street Station is, right?`
*   **ベッキー** (Becky) *(<W>)*:  
    `Just head north from the square in front of the station. You'll see the casino eventually.`
*   **ルーク** (Luke Triton):  
    `Ah, I had a feeling it was somewhere round there.`
*   **ベッキー** (Becky) *(<A1/1>)*:  
    `You did? How come?`
*   **ルーク** (Luke Triton):  
    `One of the Family's thugs was guarding the way north when we passed the station.`
*   **ルーク** (Luke Triton):  
    `I thought there might be something dodgy up there, but I couldn't get past him to see for myself.`
*   **ベッキー** (Becky) *(<A1/2>)*:  
    `Well, you might be all right this time.`
*   **ベッキー** (Becky):  
    `Those thugs move around from post to post pretty often.`
*   **ルーク** (Luke Triton) *(<A4/1>)*:  
    `Good to know.`
*   **ベッキー** (Becky):  
    `Yeah, it really doesn't sound like the best security plan, does it?`
*   **ベッキー** (Becky) *(<W>)*:  
    `Go and see for yourself, there's a good chance you'll be able to pass now. I... Uh-oh!`
*   **マーガレット** (Margaret) *(<W>)*:  
    `Becky! These are our guests! I'm sure they have better things to do than listen to you blather at them.`
*   **レイトン** (Professor Hershel Layton):  
    `No need to worry, madam. Becky was just giving us directions to our next destination.`
*   **マーガレット** (Margaret) *(<W>)*:  
    `Oh, is that so? Well, as long as she's being helpful.`
*   **ベッキー** (Becky):  
    `The establishment you're looking for is located at the north end of Flatstone Street.`

### `02_015145.lbin.txt` — Margaret ao sair

*   **マーガレット** (Margaret):  
    `Going out again, gentlemen? Do have a pleasant time about town.`

### `02_015150.lbin.txt` — Max - tutorial de puzzles escondidos

*   **マックス** (Max):  
    `Hey, listen to this! I came across a brilliant puzzle the other day. Want to hear it?`
*   **ルーク** (Luke Triton) *(<W>)*:  
    `A new puzzle, eh? Where'd you find it, Max?`
*   **マックス** (Max):  
    `It's a secret. But if you solve the puzzle, I'll tell you. What do you say? Want to try it?`
*   **ルーク** (Luke Triton):  
    `Sure!`
*   **マックス** (Max) *(<A3/0> <W> <A2/3>)*:  
    `BZZT! Invalid answer! Too bad. I've got a big secret to spill if you can get it right, you know.`
*   **マックス** (Max):  
    `If you can beat this puzzle, I'll tell you something really cool!`
*   **マックス** (Max) *(<W>)*:  
    `DING DING DING! Correct!`
*   **ルーク** (Luke Triton):  
    `So, where did you find that nice puzzle? You are going to tell me now, aren't you?`
*   **マックス** (Max) *(<A1/2> <W>)*:  
    `DING DING DING! Correct! I found it by touching a suspicious-looking spot.`
*   **ルーク** (Luke Triton):  
    `A suspicious-looking spot?`
*   **マックス** (Max) *(<W>)*:  
    `DING DING DING! Yeah, if something looks a little fishy, just give it a bit of a poke.`
*   **マックス** (Max):  
    `If you're lucky, a hint coin or puzzle will appear out of thin air!`
*   **ルーク** (Luke Triton) *(<W>)*:  
    `Wow! That's amazing!`
*   **マックス** (Max):  
    `Yeah. You need a sharp eye, though. Those hidden items could be anywhere.`
*   **マックス** (Max) *(<W> <A1/5>)*:  
    `If you touch an area and something happens, well...you could say that's a good sign.`
*   **ルーク** (Luke Triton):  
    `What kind of thing might happen?`
*   **マックス** (Max) *(<A1/2>)*:  
    `Oh you know, maybe you'll see a splash of water or a puff of dust.`
*   **マックス** (Max):  
    `If you see something like that, touch that same spot again. You never know what you might find...`
*   **マックス** (Max):  
    `Touch anything that looks suspicious. You might find something interesting!`

### `02_015180.lbin.txt` — Guarda sumiu

*   **ルーク** (Luke Triton):  
    `Look. The fellow who was standing guard over there is gone.`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `It seems Becky's guess was spot on. Let's keep moving north.`

### `02_017000.lbin.txt` — Presságio da mulher misteriosa

*   **ルーク** (Luke Triton):  
    `Professor?`
*   **ルーク** (Luke Triton):  
    `Is something the matter, Professor? You look dazed.`
*   **レイトン** (Professor Hershel Layton) *(<W2> <W>)*:  
    `I...I'm fine, Luke. I thought I saw... No, my eyes must have been playing tricks on me...`
*   **ルーク** (Luke Triton):  
    `Does it have something to do with that lady who just walked past?`
*   **レイトン** (Professor Hershel Layton) *(<A1/1> <W>)*:  
    `It's probably nothing. She just reminded me of someone I knew a long time ago.`

### `02_017010.lbin.txt` — Delroy bloqueia

*   **デロイ** (Delroy) *(<W>)*:  
    `Hmph. And just where do you two think you're going?`
*   **レイトン** (Professor Hershel Layton):  
    `We're on our way to meet someone at the Gilded 7 Casino.`
*   **デロイ** (Delroy) *(<W>)*:  
    `I see. Going to the casino to {''}meet someone{''}, are you? Interesting. Veeery interesting...`
*   **ルーク** (Luke Triton):  
    `Psst, Professor, I think this man is trying to intimidate us.`
*   **デロイ** (Delroy) *(<A6/0>)*:  
    `Stop that whispering, boy! I'm right here, you know!`
*   **ルーク** (Luke Triton) *(<W>)*:  
    `Oops! Um... Sorry, mister.`
*   **デロイ** (Delroy) *(<A3/1> <W>)*:  
    `Hmph. Well, since you've apologised, I suppose I can overlook your rudeness this time.`
*   **レイトン** (Professor Hershel Layton):  
    `I'm sorry to impose, sir, but would you be so kind as to let us pass? It's getting rather late.`
*   **デロイ** (Delroy) *(<A5/5> <W>)*:  
    `But of course, my good man. As soon as you solve this puzzle of mine, that is.`
*   **デロイ** (Delroy):  
    `Hmph. What's the matter? Has my puzzle stumped you?`
*   **デロイ** (Delroy):  
    `Back to pit your wits against my puzzle, I see. Very well then. Prepare yourself!`
*   **デロイ** (Delroy) *(<A2/5>)*:  
    `Well done. You've proven yourself worthy, so I will provide you with a cryptic but valuable warning.`
*   **デロイ** (Delroy) *(<A2/6>)*:  
    `Danger lurks about that hat of yours. You'd best watch yourself around here.`
*   **レイトン** (Professor Hershel Layton):  
    `Why is everyone so fixated on my hat? Do you know someone else with a hat like mine?`
*   **デロイ** (Delroy):  
    `If I told you, it would kill all the suspense, wouldn't it? I'll leave that little mystery for you.`

### `02_017020.lbin.txt` — Chegada ao Gilded 7

*   **ルーク** (Luke Triton):  
    `Wow! Now that's a casino!`
*   **レイトン** (Professor Hershel Layton):  
    `I think it's safe to say that we've found the Gilded 7.`
*   **ルーク** (Luke Triton):  
    `I can't wait to see what it looks like up close!`

### `02_017030.lbin.txt` — Harold, porteiro do Gilded 7

*   **ハロルド** (Harold) *(<W>)*:  
    `Good evening, sir. May I see your membership card, please?`
*   **レイトン** (Professor Hershel Layton):  
    `Membership card?`
*   **ハロルド** (Harold) *(<A1/2>)*:  
    `The Gilded 7 Casino is a haven where society's finest ladies and gentlemen can gather.`
*   **ハロルド** (Harold):  
    `We check membership cards upon entry to ensure that less savoury types are kept out.`
*   **レイトン** (Professor Hershel Layton):  
    `Hmm... This is certainly the first I've heard of such a policy.`
*   **レイトン** (Professor Hershel Layton):  
    `I don't suppose you'd be willing to make an exception for us?`
*   **ハロルド** (Harold) *(<A2/2>)*:  
    `Well, your hat does show you to be a man of impeccable taste. Now we just need to test your intellect.`
*   **ハロルド** (Harold):  
    `If you can solve this puzzle, I'll let you in without a card - just this once, mind.`
*   **ルーク** (Luke Triton) *(<A4/1>)*:  
    `This fellow seems awfully focused on your hat as well.`
*   **レイトン** (Professor Hershel Layton):  
    `Naturally. Is there any greater proof of one's gentlemanly nature than a fine top hat?`
*   **ハロルド** (Harold) *(<A2/1>)*:  
    `Come now, sir. Don't tell me a gentleman of your calibre is incapable of solving a quick puzzle.`
*   **ハロルド** (Harold) *(<A2/1> <W> <A2/2>)*:  
    `Back to try again, sir? Perhaps you can find the correct answer this time.`
*   **ハロルド** (Harold) *(<A1/1>)*:  
    `Expertly solved, sir.`
*   **ハロルド** (Harold) *(<W> <A1/2>)*:  
    `You've certainly earned the right to enjoy our exclusive facilities. Welcome to the Gilded 7.`

### `02_018000.lbin.txt` — Interior do cassino

*   **ルーク** (Luke Triton):  
    `Just look at these fountains! And this floor! The owner must be filthy rich!`
*   **レイトン** (Professor Hershel Layton):  
    `I know you're excited, Luke, but do try to keep your voice down.`
*   **ルーク** (Luke Triton):  
    `Sorry, Professor. This place is just so impressive.`
*   **レイトン** (Professor Hershel Layton):  
    `I understand the feeling. It's also quite large. Finding your future self in here may prove difficult.`

### `02_019000.lbin.txt` — Encontro com Future Luke (dublado)

*   **レイトン** (Professor Hershel Layton) `<V0010>`:  
    `Hello, Luke.`
*   **ルーク** (Luke Triton) `<V0020>` *(<W>)*:  
    `Um, hi, Professor. Oh, you're talking to him.`
*   **ルーク** (Luke Triton) `<V0030>`:  
    `This is going to take some getting used to.`
*   **未来ルーク** (Future Luke) `<V0040>` *(<A2/2>)*:  
    `I can't believe how small I used to be.`
*   **ルーク** (Luke Triton) `<V0050>` *(<A1/5>)*:  
    `Hey! I'm not that small!`
*   **レイトン** (Professor Hershel Layton) `<V0060>`:  
    `So, tell me, why exactly did you go through such pains to bring us here?`
*   **未来ルーク** (Future Luke) `<V0070>`:  
    `I'll be happy to tell you in just a moment.`
*   **未来ルーク** (Future Luke) `<V0080>` *(<A4/3>)*:  
    `But before that, I'd just like to verify that I'm dealing with the real Professor Layton here.`
*   **レイトン** (Professor Hershel Layton) `<V0090>`:  
    `Who else would I be?`
*   **未来ルーク** (Future Luke) `<V0100>` *(<A4/4>)*:  
    `Allow me to explain.`
*   **未来ルーク** (Future Luke) `<V0101>`:  
    `In my London, it's rare to find someone who doesn't know the name Hershel Layton.`
*   **未来ルーク** (Future Luke) `<V0110>`:  
    `In fact, many impostors have come forth recently, claiming to be him.`
*   **ルーク** (Luke Triton) `<V0120>`:  
    `Are you saying you think the professor is a fraud?!`
*   **未来ルーク** (Future Luke) `<V0130>` *(<A4/1>)*:  
    `Professor, if you think back on our adventures together, you may recall a man named Don Paolo.`
*   **未来ルーク** (Future Luke) `<V0131>`:  
    `As you know, he was a master of disguise.`
*   **未来ルーク** (Future Luke) `<V0140>`:  
    `How do I know the man before me now isn't Don Paolo in another of his costumes?`
*   **ルーク** (Luke Triton) `<V0150>` *(<A1/3>)*:  
    `Now that's just rubbish, and you know it!`
*   **未来ルーク** (Future Luke) `<V0160>` *(<A4/2>)*:  
    `Is it now? He's tricked us before. Who's to say he couldn't do it again?`
*   **レイトン** (Professor Hershel Layton) `<V0170>`:  
    `Very well. I'll play along. How do you propose I prove my identity?`

### `02_020000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `02_020010.lbin.txt` — Duelo dos cartões

*   **レイトン** (Professor Hershel Layton):  
    `What exactly do you have in mind?`
*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `As a cautious man, I'm sure you have questions about my identity as well.`
*   **未来ルーク** (Future Luke):  
    `I therefore suggest that we each prove our identity to the other's satisfaction.`
*   **未来ルーク** (Future Luke):  
    `To this end, I propose that we demonstrate the power of our respective intellects.`
*   **未来ルーク** (Future Luke):  
    `I've prepared a puzzle that can only be solved by someone as insightful as Professor Layton.`
*   **未来ルーク** (Future Luke):  
    `Should you find the solution, I will give you the chance to present me with a similar challenge.`
*   **未来ルーク** (Future Luke):  
    `If I am who I say I am, I should have no trouble solving whatever you throw my way, should I?`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `Let's get started. Before us are four cards arranged according to the following set of conditions:`
*   **未来ルーク** (Future Luke) *(<A3/5>)*:  
    `First, a heart is next to a diamond.`
*   **未来ルーク** (Future Luke):  
    `Second, a club is not next to a spade.`
*   **未来ルーク** (Future Luke):  
    `Finally, a heart is directly to the right of a club.`
*   **未来ルーク** (Future Luke):  
    `Using just these three conditions, I challenge you to find the spade amongst these four cards.`
*   **未来ルーク** (Future Luke):  
    `Are you quite sure about your answer, Professor? I'd reconsider it if I were you.`
*   **未来ルーク** (Future Luke) *(<S671> <A2/2>)*:  
    `Yes, that is indeed the location of the spade. Impressive, Professor.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1> <W>)*:  
    `Thank you. Now, if I may present you with a puzzle of my own design?`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `Nothing would please me more.`
*   **レイトン** (Professor Hershel Layton):  
    `Good. I appreciated the idea behind your puzzle, so if you don't mind, I'd like to do something similar.`
*   **レイトン** (Professor Hershel Layton) *(<A2/1>)*:  
    `Here are the conditions for my four cards:`
*   **レイトン** (Professor Hershel Layton):  
    `A club lies directly to the right of a heart.`
*   **レイトン** (Professor Hershel Layton):  
    `A diamond is on the far left or far right and has a heart next to it.`
*   **レイトン** (Professor Hershel Layton):  
    `Finally, a club is also the far left or far right card.`
*   **レイトン** (Professor Hershel Layton) *(<A1/1>)*:  
    `Are you able to find the spade using these conditions?`
*   **未来ルーク** (Future Luke) *(<A2/4> <W>)*:  
    `You almost had me there, Professor. But as you know, this puzzle is flawed. It's unsolvable.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1>)*:  
    `Is that so?`
*   **未来ルーク** (Future Luke) *(<A2/4>)*:  
    `Yes. I tried several solutions, but none work, given the conditions you've set forth.`
*   **レイトン** (Professor Hershel Layton):  
    `Oh really?`
*   **レイトン** (Professor Hershel Layton):  
    `Tell me, did I ever state that the four cards on the table included one card from each suit?`
*   **未来ルーク** (Future Luke) *(<A3/5> <W>)*:  
    `Hmph. So the answer is...there is no spade?`
*   **レイトン** (Professor Hershel Layton) *(<A2/1>)*:  
    `Precisely. This was a trick question, but it makes a pertinent point.`
*   **レイトン** (Professor Hershel Layton):  
    `In the puzzle you issued me, you failed to specify that the four cards included one from each suit.`
*   **レイトン** (Professor Hershel Layton):  
    `Leaving in a loophole like that can make the puzzle unsolvable.`
*   **レイトン** (Professor Hershel Layton):  
    `The same omission can also open the door to alternate solutions.`
*   **レイトン** (Professor Hershel Layton) *(<A1/1>)*:  
    `You intentionally presented me with a puzzle that, when examined closely, is actually incomplete.`
*   **レイトン** (Professor Hershel Layton):  
    `That was the real test you set out for me, was it not? To see if I would spot the loophole?`
*   **未来ルーク** (Future Luke):  
    `Four cards sit in a line: {.}A heart is next to a diamond. {.}A club is not next to a spade. {.}A heart is directly to the right of a club. Can you work out which one is the spade, Professor? Touch that card.`
*   **レイトン** (Professor Hershel Layton):  
    `Four cards sit in a line: {.}A club sits directly to the right of a heart. {.}One of the cards on the far left or far right is a diamond, and next to it is a heart. {.}The other card on the far left or far right is a club. Can you find the spade, Luke?`

### `02_021000.lbin.txt` — Reconhecimento e convite ao depósito

*   **未来ルーク** (Future Luke) `<V0010>` *(<A2/2>)*:  
    `It seems you're the genuine article, Professor.`
*   **レイトン** (Professor Hershel Layton) `<V0020>` *(<A1/2>)*:  
    `I'm glad to see that I've finally convinced you.`
*   **未来ルーク** (Future Luke) `<V0030>`:  
    `To be honest, I was convinced from the beginning.`
*   **未来ルーク** (Future Luke) `<V0040>`:  
    `But I just couldn't pass up the opportunity to pit myself against my mentor in a battle of wits.`
*   **レイトン** (Professor Hershel Layton) `<V0060>`:  
    `Hmm. I'm flattered...I suppose.`
*   **ルーク** (Luke Triton) `<V0050>` *(<A1/6>)*:  
    `So? Out with it! Why did you call us here?`
*   **未来ルーク** (Future Luke):  
    `There are too many eyes on us in here. There's a storeroom in the back where we can talk. Follow me.`

### `02_021010.lbin.txt` — A revelação: o vilão é Layton

*   **未来ルーク** (Future Luke):  
    `Professor Layton, Luke, welcome to the London of the future.`
*   **レイトン** (Professor Hershel Layton) *(<K>)*:  
    `Hmm.`
*   **未来ルーク** (Future Luke):  
    `Still not convinced?`
*   **未来ルーク** (Future Luke):  
    `You saw Dr Schrader, didn't you?`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `You must have noticed the toll that time has taken on your mentor.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, we saw him...`
*   **未来ルーク** (Future Luke):  
    `And what of fair London? You've walked around enough now to see how she's changed.`
*   **未来ルーク** (Future Luke):  
    `Could you imagine there being a casino in this sleepy part of town back in your time?`
*   **ルーク** (Luke Triton):  
    `Yeah, everything's changed! What's happened to this city?`
*   **未来ルーク** (Future Luke) *(<A1/5> <W>)*:  
    `A genius appeared...an evil genius who turned the city on its head.`
*   **ルーク** (Luke Triton) *(<A1/3> <W>)*:  
    `Oh, I know where this is going. Don Paolo took over the city, didn't he?`
*   **未来ルーク** (Future Luke) *(<A1/1> <W> <A1/4>)*:  
    `Don Paolo? Oh no, I'm talking about a truly brilliant man.`
*   **未来ルーク** (Future Luke):  
    `Someone the three of us all know quite well.`
*   **ルーク** (Luke Triton) *(<A2/1>)*:  
    `Well, if it's not Don Paolo, then who is it?`
*   **未来ルーク** (Future Luke):  
    `What do you think, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `I really couldn't say.`
*   **未来ルーク** (Future Luke):  
    `Hmm... Really?`
*   **ルーク** (Luke Triton):  
    `Who is it? I've just got to know!`
*   **未来ルーク** (Future Luke) *(<W>)*:  
    `His name is Hershel Layton. The evil genius is you, Professor.`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `WHAAAAT?!`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `I...was afraid you'd say that.`
*   **ルーク** (Luke Triton):  
    `That can't possibly be right!`
*   **未来ルーク** (Future Luke):  
    `I'm sorry to say that it is.`
*   **未来ルーク** (Future Luke):  
    `They call him {''}the devil in the top hat{''}, and he rules London from the shadows.`
*   **未来ルーク** (Future Luke):  
    `It's common knowledge for people in this part of London.`
*   **レイトン** (Professor Hershel Layton):  
    `Tell me more, Luke.`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `What? I don't know any more than you do, Professor.`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `No, I meant the other Luke. Goodness, this is getting rather complicated, isn't it?`
*   **レイトン** (Professor Hershel Layton):  
    `Tell me, Luke, how did I rise to rule over all of London?`
*   **未来ルーク** (Future Luke):  
    `Where to begin...? Here, Professor, surely you remember this?`

### `02_021020.lbin.txt` — Exposição completa: explosão, Stahngun, wormhole, Chinatown

*   **ルーク** (Luke Triton) *(<A4/1>)*:  
    `Of course. This is an article about the accident that happened just the other day.`
*   **未来ルーク** (Future Luke) *(<A2/5>)*:  
    `Ha ha! Yes, to you, I suppose it was a recent event.`
*   **未来ルーク** (Future Luke):  
    `But here it's been a full 10 years since that fateful day.`
*   **ルーク** (Luke Triton):  
    `Whoa...`
*   **未来ルーク** (Future Luke) *(<A2/4>)*:  
    `It was the start of a dark period for London.`
*   **未来ルーク** (Future Luke):  
    `With the prime minister missing, Parliament was in utter chaos, you see.`
*   **ルーク** (Luke Triton) *(<A4/4> <W>)*:  
    `Yes, everyone in Parliament is in a state of panic. Um, in our time, I mean.`
*   **未来ルーク** (Future Luke) *(<A3/5>)*:  
    `Professor, you witnessed with your own eyes the accident that changed London forever.`
*   **未来ルーク** (Future Luke):  
    `The time machine presentation was a complete failure.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, both the prime minister and that scientist...`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `You mean Dr Stahngun?`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, that's right. Several people disappeared in the blast, including those two.`
*   **レイトン** (Professor Hershel Layton):  
    `It seems likely that they were killed by the force of the explosion.`
*   **ルーク** (Luke Triton):  
    `Didn't the papers say that a few of Dr Stahngun's assistants had also vanished in the blast?`
*   **未来ルーク** (Future Luke) *(<A3/3>)*:  
    `That's the story in the press. But what would you say if I told you Stahngun was still alive?`
*   **ルーク** (Luke Triton) *(<A1/6>)*:  
    `I'd say it's impossible!`
*   **未来ルーク** (Future Luke):  
    `Then you'd be wrong.`
*   **未来ルーク** (Future Luke):  
    `Dr Stahngun escaped the blast, but he went into hiding to avoid reprisals after the experiment.`
*   **レイトン** (Professor Hershel Layton):  
    `The man was responsible for the loss of our national leader, after all.`
*   **未来ルーク** (Future Luke) *(<W> <A3/5>)*:  
    `Desperate for a place to lie low, the doctor was given shelter by an unlikely person. You, Professor.`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `Me? Why would I aid the man responsible for this pandemonium?`
*   **未来ルーク** (Future Luke) *(<A4/3>)*:  
    `That is something I have never understood.`
*   **未来ルーク** (Future Luke):  
    `In the months that followed the explosion, you slowly grew distant from me.`
*   **未来ルーク** (Future Luke):  
    `You began consorting with figures from the criminal underworld.`
*   **ルーク** (Luke Triton) *(<A1/5>)*:  
    `The professor?! Never!`
*   **未来ルーク** (Future Luke) *(<A4/4>)*:  
    `Don't be so sure. Time has a way of changing people, Luke.`
*   **未来ルーク** (Future Luke):  
    `It was clear that something about Stahngun's research captivated you, Professor.`
*   **未来ルーク** (Future Luke) *(<A4/3>)*:  
    `You couldn't stop talking about time travel. You seemed obsessed with the idea of changing the past.`
*   **レイトン** (Professor Hershel Layton):  
    `Changing the past?`
*   **未来ルーク** (Future Luke):  
    `Dr Stahngun was very interested in continuing his research, but he needed financial backing to do it.`
*   **未来ルーク** (Future Luke):  
    `So you used your superior intellect to assume control of London's underworld.`
*   **ルーク** (Luke Triton) *(<A1/4>)*:  
    `No...`
*   **未来ルーク** (Future Luke):  
    `Of course, there were those who tried to stop you. But none were a match for Professor Layton.`
*   **未来ルーク** (Future Luke):  
    `Before long, you were raking in cash from all sorts of dodgy businesses.`
*   **未来ルーク** (Future Luke):  
    `With all the funding he needed, it wasn't long before Stahngun completed his time machine.`
*   **レイトン** (Professor Hershel Layton):  
    `Time machine? You mean...`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `That's right. The time machine in the clock shop on Midland Road.`
*   **未来ルーク** (Future Luke):  
    `Though I suppose {''}completed{''} is the wrong word, as the machine is far from complete.`
*   **レイトン** (Professor Hershel Layton):  
    `How so?`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `It doesn't allow the user to select a destination.`
*   **未来ルーク** (Future Luke):  
    `You can select neither the place nor the time you wish to travel to.`
*   **未来ルーク** (Future Luke):  
    `In fact, it would be more accurate to describe it as a sort of tunnel between two periods in time.`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `A wormhole!`
*   **未来ルーク** (Future Luke) *(<A1/2> <W>)*:  
    `Precisely. And by sheer chance...`
*   **未来ルーク** (Future Luke):  
    `This wormhole opened in the clock shop and crosses the 10 years between our two times.`
*   **未来ルーク** (Future Luke):  
    `This gives us the ability to move back and forth between your present and mine.`
*   **レイトン** (Professor Hershel Layton):  
    `So you used the wormhole to get the message to us and to bring us here.`
*   **レイトン** (Professor Hershel Layton):  
    `One thing is bothering me, though. This wormhole is obviously very important to my future self.`
*   **レイトン** (Professor Hershel Layton):  
    `Surely the Layton of this era must keep a close eye on it. How did you gain access?`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `I'll get to that, but right now there's more pressing business I'd like to attend to.`
*   **レイトン** (Professor Hershel Layton):  
    `Go on then. Tell us why you called us here.`
*   **未来ルーク** (Future Luke) *(<A2/5>)*:  
    `Always one step ahead of me, eh? You haven't lost your touch, Professor.`
*   **未来ルーク** (Future Luke):  
    `I wish to enlist your help in stopping Hershel Layton.`
*   **レイトン** (Professor Hershel Layton):  
    `You want me to stop myself?`
*   **未来ルーク** (Future Luke) *(<A2/4>)*:  
    `Even as we speak, the other Layton is working to build a fully operational time machine.`
*   **未来ルーク** (Future Luke):  
    `He's been ducking back into your time to gather every bright scientist working in time travel.`
*   **ルーク** (Luke Triton):  
    `But why bother going into the past to find scientists? There must be plenty here, in this era.`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `Actually, many of the experts in the field were lost when Stahngun's presentation went awry.`
*   **未来ルーク** (Future Luke):  
    `Layton had no choice but to travel back to the time before the blast in order to gather talent.`
*   **レイトン** (Professor Hershel Layton) *(<K>)*:  
    `Hmm...`
*   **未来ルーク** (Future Luke) *(<A1/4>)*:  
    `Things are already bad.`
*   **未来ルーク** (Future Luke):  
    `But if Layton manages to build a fully functional time machine, who knows what could happen?`
*   **未来ルーク** (Future Luke):  
    `Someone has to stop him from completing his scheme. But the only person who might succeed is-`
*   **レイトン** (Professor Hershel Layton) *(<W>)*:  
    `Me... That is what you are going to say, is it not?`
*   **未来ルーク** (Future Luke):  
    `Exactly. We have to fight fire with fire. No one else stands a chance against him.`
*   **レイトン** (Professor Hershel Layton):  
    `But how? I'm not familiar with this future London. I wouldn't even know where to start looking.`
*   **未来ルーク** (Future Luke) *(<A1/1>)*:  
    `That's one obstacle we'll have to overcome together. Layton's actions are shrouded in secrecy.`
*   **未来ルーク** (Future Luke):  
    `His base of operations, however, is well known. We can start our search for him there.`
*   **ルーク** (Luke Triton):  
    `You mean this casino isn't the future professor's headquarters?`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `No, this establishment is just one of the many ways he makes money.`
*   **未来ルーク** (Future Luke):  
    `His headquarters are in the heart of Chinatown.`
*   **レイトン** (Professor Hershel Layton):  
    `Well, let's visit the place and see if we can learn anything more.`
*   **レイトン** (Professor Hershel Layton):  
    `I must admit, Luke, there is still quite a bit about this situation that I find dubious.`
*   **レイトン** (Professor Hershel Layton) *(<A1/2>)*:  
    `However, I see that the only way to get to the bottom of this is to go and find this man claiming to be me.`
*   **未来ルーク** (Future Luke) *(<A2/2>)*:  
    `Heh heh. I thought you'd say that, Professor.`
*   **ルーク** (Luke Triton):  
    `Don't forget me! I'm coming too.`
*   **未来ルーク** (Future Luke) *(<W>)*:  
    `Of course you are. If I can't count on myself for help, who can I count on?`
*   **ルーク** (Luke Triton) *(<A4/4>)*:  
    `Thinking about what you just said makes me feel kind of...dizzy.`
*   **未来ルーク** (Future Luke) *(<W>)*:  
    `Ha ha! Well, I hope you get used to it soon. I'm going to need your help in stopping the evil Layton too.`
*   **未来ルーク** (Future Luke) *(<A2/6>)*:  
    `Oh yes, there's one more interesting fact I should mention, Professor.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1>)*:  
    `Yes?`
*   **未来ルーク** (Future Luke) *(<A1/2>)*:  
    `There's no record of a scientist matching Dr Stahngun's name and description. It's a false name.`
*   **レイトン** (Professor Hershel Layton):  
    `Is that so?`
*   **未来ルーク** (Future Luke):  
    `Whoever he was, he took pains to hide his real identity from the people at the presentation.`
*   **レイトン** (Professor Hershel Layton) *(<A4/5>)*:  
    `Now that you mention it, few of the guests seemed to know the man.`
*   **レイトン** (Professor Hershel Layton):  
    `What would motivate Stahngun to use a false name? What was he planning?`
*   **未来ルーク** (Future Luke):  
    `Another interesting question we may hope to answer along the way.`
*   **レイトン** (Professor Hershel Layton):  
    `It just doesn't make any sense...`
*   **ルーク** (Luke Triton) *(<A1/1>)*:  
    `What are you thinking, Professor?`
*   **未来ルーク** (Future Luke):  
    `We can talk more on the way. For now, we should head back to Flatstone Street.`

### `02_021030.lbin.txt` — Retorno a Flatstone Street

*   **未来ルーク** (Future Luke):  
    `Please hurry. We need to make our way back to Flatstone Street.`

### `02_022000.lbin.txt` — Bostro interrompe a fuga (dublado)

*   **ボストロ** (Bostro) `<V0010>`:  
    `Oh, there you are, Boss!`
*   **レイトン** (Professor Hershel Layton) `<V0020>`:  
    `Oh!`
*   **ボストロ** (Bostro) `<V0030>` *(<A2/3>)*:  
    `Oi, what are you doin', wearin' the boss's get-up? This your idea of a joke?`
*   **レイトン** (Professor Hershel Layton) `<V0040>` *(<Q>)*:  
    `No, no, not at all.`
*   **ボストロ** (Bostro) `<V0050>` *(<A3/1>)*:  
    `Come to think of it, I don't think I've seen any of you round 'ere before.`
*   **レイトン** (Professor Hershel Layton) `<V0060>`:  
    `Yes, well, we don't often get a chance to visit this fine establishment of yours.`
*   **ボストロ** (Bostro) `<V0080>` *(<A1/1>)*:  
    `Dunno about that, but I'm gonna need you to come with me for some questionin'. This way, you three.`
*   **未来ルーク** (Future Luke) `<V0090>` *(<A3/5>)*:  
    `Argh!`
*   **未来ルーク** (Future Luke) `<V0100>` *(<A1/5>)*:  
    `Professor, run away while you can!`
*   **未来ルーク** (Future Luke) `<V0110>`:  
    `Oof!`
*   **ルーク** (Luke Triton) `<V0120>` *(<A1/6>)*:  
    `Oh no!`
*   **レイトン** (Professor Hershel Layton) `<V0130>`:  
    `Quickly, you two! This way!`

### `02_023010.lbin.txt` — Coin Machine Gun Puzzle (debug)

*   **レイトン** (Professor Hershel Layton):  
    `Coin Machine Gun Puzzle`
*   **レイトン** (Professor Hershel Layton):  
    `Quick! Throw those parts together!`
*   **レイトン** (Professor Hershel Layton):  
    `Retry`
*   **レイトン** (Professor Hershel Layton):  
    `Correct`
*   **レイトン** (Professor Hershel Layton):  
    `Incorrect`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `02_015150` | **Enigmas Escondidos / Moedas de Dica** | Tutorial de Max: tocar pontos suspeitos revela enigmas/moedas de dica (splash de água, puff de poeira). |
| `02_017010` | **Delroy's Enigma** | Bloqueio de rua ao norte da estação; após resolver, aviso críptico sobre o chapéu. |
| `02_017030` | **Membership Card Enigma (Harold)** | Enigma de entrada do Gilded 7; sem card, teste de intelecto para provar ser gentleman. |
| `02_019000` + `02_020010` | **Duelo das 4 Cartas (Future Luke vs Layton)** | Enigma duplo: Future Luke propõe achar o espadas (spade) com 3 condições; Layton propõe variação com loophole — resposta é "não há espadas" pois premissa de 4 naipes distintos nunca foi declarada. Teste de atenção a lacunas lógicas. Touch that card / Can you find the spade, Luke? |
| `02_023010` | **Coin Machine Gun Enigma** | Placeholder/debug: "Quick! Throw those parts together!" — sem integração narrativa, provavelmente enigma cortado/teste. |
| `02_015070` etc. | **Bloqueios narrativos da Family** | Múltiplos Goons impedem passagem até enigma resolvido; sistema de rotatividade de guardas ("move around from post to post") explica por que caminho ao cassino se libera. |
| `02_017000` | **Presságio Claire** | Layton vê mulher que lembra alguém do passado — foreshadowing do motivo real ("changing the past") ligado à obsessão revelada em `02_021020`. |

**Eventos narrativos sem enigma:** Pânico generalizado com o chapéu (Hazel/Edgar, Anita ecoa no background, Delroy, Harold), revelação do "devil in the top hat", exposição do wormhole da relojoaria (túnel fixo de 10 anos, sem seleção de destino), QG em Chinatown, e sequestro de cientistas do passado para construir máquina completa — arco que explica os desaparecimentos prenunciados no Prólogo (`00_007000`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Voz e estrutura:** Apenas 3 blocos são fortemente dublados: `02_019000` (`<V0010>`–`<V0170>` encontro), `02_021000` (`<V0010>`–`<V0060>` reconhecimento) e `02_022000` (`<V0010>`–`<V0130>` Bostro). Todo o restante é exploração não-dublada, típica de LSCR de mid-chapter. `02_020010` — apesar de ser clímax lógico — é majoritariamente não-dublado, exceto prompts de enigma.
*   **Dumps vazios:** 2 arquivos vazios (`02_000000`, `02_020000`) funcionam como separadores de cena/loading — padrão da Level-5 para fronteiras de capítulo (`00` tinha 7, `01` tinha 1).
*   **Codificação de personagens:** `ヘイゼル` revela nome próprio `Edgar` em fala ("if Edgar's going to spill the beans"), indicando que Hazel é codinome genérico e Edgar o nome canônico no futuro. `デロイ` (Delroy) e `ハロルド` (Harold) são bloqueadores exclusivos do cap. 02. `未来ルーク` vs `ルーク` exigem desambiguação constante — Layton mesmo comenta "Goodness, this is getting rather complicated, isn't it?".
*   **Continuidade:** `02_015020` recicla a nota do banco do passageiro de `01_015000` ("Gilded 7 Casino on Flatstone Street") mas agora com decisão explícita de ir a pé. `02_015030` ecoa a estrutura de `01_012010` (Adeline) — NPC feminino que não conhece o destino exato. `02_021020` fecha o loop do `00_005000` (explosão da demonstração) com retcon: Stahngun sobreviveu.
*   **Wormhole vs máquina:** `02_021020` estabelece distinção crucial para spec: a relojoaria não é máquina do tempo completa, mas túnel/Wormhole sem controle de destino — explica por que Future London é acessada apenas via aquele relógio e por que o Layton do futuro precisa sequestrar cientistas para construir a versão controlável.
*   **Placeholder de nome falso:** `Stahngun` é explicitamente declarado falso ("There's no record of a scientist matching...") — gancho para revelação posterior de Dimitri Allen (já visto disfarçado em `00_005000` como `変装ディミトリー`).
*   **Arquivo `02_023010`:** Sequência de 5 linhas curtas com `Coin Machine Gun Puzzle` sugere asset de teste ou enigma reutilizado de outro capítulo; mantido no dump mas sem gatilho narrativo no capítulo 02.

---

*Gerado a partir de dumps LSCR brutos — 31/31 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/02`. Próximo capítulo: `03` — Chinatown e o Layton do Futuro.*
