# Capítulo 03 — O Caminho para Chinatown e o Pagode Imponente | Professor Layton and the Unwound Future

> **Capítulo 03 — O Caminho para Chinatown e o Pagode Imponente (Chinatown / Towering Pagoda)** — Análise de dump LSCR para `Textos Originais/txt/uk/03/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/03/`
> Total de arquivos escaneados: **25**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético

---

## 1. Arquivos Cobertos

Todos os 25 dumps `.lbin.txt` em `uk/03`:

```
03_000000.lbin.txt  — [vazio - apenas cabeçalho]
03_024010.lbin.txt  — Fuga do Gilded 7: apelidos Big Luke / Little Luke + restaurante no shopping arcade
03_024020.lbin.txt  — Bloqueio de retorno: Family ainda caça o grupo
03_024030.lbin.txt  — Hollis (ホリス) — pegadas molhadas sem chuva
03_024040.lbin.txt  — Future Luke explica a ética da máquina do tempo (analogia do bully)
03_024060.lbin.txt  — Margaret dormindo (Snoooozzzz)
03_024070.lbin.txt  — Becky — Chinatown e missão top-secret
03_024090.lbin.txt  — Chegada ao restaurante do arcade
03_024100.lbin.txt  — Family Goon ferido por Bostro — menção ao garoto do cassino
03_024110.lbin.txt  — Identificação do homem de preto — o portador da carta
03_024120.lbin.txt  — Bacchus — cardápio: fish and chips premiado e lamb stew
03_024125.lbin.txt  — Bacchus lamenta saída sem comer
03_024130.lbin.txt  — Reunião com Shipley/Butch: Pagode, cientistas escravizados, PM Hawks vivo, rota para Chinatown
03_025000.lbin.txt  — Reavistamento da mulher misteriosa — Layton suspeita ser Claire
03_025010.lbin.txt  — Estátua de bronze: autor famoso e menino doente (história comovente)
03_025030.lbin.txt  — Beco sujo a caminho de Chinatown — Luke escorrega
03_025040.lbin.txt  — Gyorack (ギョラック) — trabalhador que "perdeu a vida" cavando buraco
03_025050.lbin.txt  — Margem do Thames — farol gigante novo
03_025055.lbin.txt  — Graham — homem mais distinto e elegante de Londres, terno italiano
03_025060.lbin.txt  — Craig (クレイグ) — escocês, puzzle de passagem, pânico ao ouvir nome Layton, pegadas molhadas
03_025070.lbin.txt  — Colina arborizada e medo de fantasmas
03_025080.lbin.txt  — Segal (セガール) — bazar do mercado negro (black market bazaar)
03_025100.lbin.txt  — Portão de Chinatown — guardas sósias de Chelmey & Barton + reflexão sobre convite de Stahngun + retorno de Future Luke
03_025110.lbin.txt  — Área arborizada a oeste — wormhole da relojoaria como volta no tempo
03_025115.lbin.txt  — Sharon — oferta de vacina contra gripe (flu jabs)
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `03_000000.lbin.txt`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 03 |
|---|---|---|
| `ルーク` | **Luke Triton (Little Luke)** | Aprendiz, co-protagonista, batizado "Little Luke" |
| `未来ルーク` | **Future Luke (Big Luke)** | Luke 10 anos mais velho, guia e estrategista |
| `レイトン` | **Professor Hershel Layton** | Protagonista, mentor, obcecado pelo reavistamento de Claire |
| `ホリス` | **Hollis (Wet Shoes Man)** | Homem assustado com sapatos/pés molhados |
| `マーガレット` | **Margaret (Hotel Duke Manager)** | Gerente, gag recorrente dormindo |
| `ベッキー` | **Becky (Hotel Duke Receptionist)** | Recepcionista, comenta Chinatown/turismo |
| `クローンマフィア` | **Family Goon / Clone Mafia** | Capanga espancado por Bostro por causa do garoto no cassino |
| `バッカス` | **Bacchus (Restaurant Owner)** | Dono do restaurante do arcade, fish and chips premiado |
| `ブッチ` | **Butch / Shipley (Courier)** | Mensageiro da Family, verdadeiro nome Shipley, portador da carta, batedor de Chinatown |
| `グラハム` | **Graham (Dandy)** | Homem vaidoso de terno italiano sob encomenda, às margens do Thames |
| `クレイグ` | **Craig (Scottish Man)** | Escocês que bloqueia caminho com enigma, teme a Family |
| `ギョラック` | **Gyorack / Gyorakku (Hole Digger)** | Trabalhador enganado, cavou buraco escuro, perdeu casa e família |
| `セガール` | **Segal / Seagal (Black Market Dealer)** | Informante do bazar negro |
| `ワルミー` | **Warumy / Walmy (Pagoda Portão Guard - dupla)** | Dupla que barra o portão de Chinatown, sósias de Chelmey & Barton |
| `シャロン` | **Sharon (Green Hospital Receptionist)** | Recepcionista, gag de vacina |
| *(sem tag, referência)* | **Claire (mencionada)** | Mulher misteriosa reavistada, gatilho emocional de Layton |
| *(sem tag, referência)* | **Bill Hawks (PM)** | Primeiro-ministro desaparecido há 10 anos, supostamente no Pagode |
| *(sem tag, referência)* | **Chelmey & Barton (mencionados)** | Inspetor e assistente, sósias dos guardas do portão |

Tags de controle observadas: nenhum `<Vxxxx>` dublado neste capítulo (todo `<T>` não-dublado, exploração); `<W>` pausas; `<A1/2>` etc. animações; `<K>` efeito cinético em `03_024030` e `03_025100`; `<CR>`/`</C>` bloco de citação da estátua em `03_025010`.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Fuga do Gilded 7 — Big Luke e Little Luke (`03_024010`–`03_024020`)
O capítulo começa logo após a fuga do Gilded 7, ainda em Flatstone Street. A convivência de dois Lukes gera constrangimento sobre como se tratar; Little Luke tenta chamar o outro de "Mr Triton" e Future Luke pede para não ser chamado assim por si mesmo. Layton resolve o impasse propondo os apelidos Big Luke e Little Luke, aceitos com humor por ambos. Future Luke retoma o plano e marca encontro num restaurante do galeria comercial, perto da saída sul, onde um amigo os espera, mas alerta que não podem voltar pelo mesmo caminho porque a Family ainda os caça.
> Gancho: "I don't see why you can't both be called Luke." / "The Family is still on the hunt for us."

### 3.2 Pegadas Molhadas e a Ética da Máquina do Tempo (`03_024030`–`03_024040`)
No arcade, o grupo esbarra em Hollis, um homem assustado que se despede apressado após levar um susto. Layton manda Luke observar o chão e ambos notam pegadas molhadas apesar de não chover desde que chegaram — primeira pista do mistério hídrico, que se repetirá adiante como prenúncio de túneis alagados. Em seguida, Little Luke questiona por que impedir uma máquina capaz de melhorar vidas, e Future Luke responde com uma parábola moral: pergunta se ele usaria viagem no tempo para se vingar de um valentão aos 5 anos; diante da recusa indignada, conclui que alguém menos bondoso causaria estragos, convencendo Little Luke da necessidade de deter a máquina.
> Gancho: "Wet footprints... But it hasn't rained since we got here." / "Imagine the damage that someone less kind could do with a machine like that."

### 3.3 Hotel Duke e Chegada ao Restaurante (`03_024060`–`03_024090`)
De passagem pelo Hotel Duke, Margaret dorme ruidosamente e Luke sugere deixá-la descansar, enquanto Becky, em sussurro para não acordá-la, brinca que são turistas indo de cassino a Chinatown e pede segredo sobre a missão top-secret. Layton apressa a partida. Pouco adiante avistam o restaurante indicado por Future Luke no arcade e confirmam ser o ponto de encontro.
> Gancho: "Crikey, first the casino and now Chinatown? You two are proper tourists!" / "Yes, this is the one. Let's head in."

### 3.4 O Goon de Bostro e o Homem de Preto (`03_024100`–`03_024110`)
No caminho até o restaurante, encontram um Family Goon ferido que conta ter sido espancado por Bostro, furioso por um garoto ter entrado no cassino; Luke disfarça que não esteve lá e o goon, aliviado por não precisar dar lição, reclama do temperamento do chefe. Logo depois Future Luke aponta o homem de preto nas proximidades e Little Luke o reconhece imediatamente como o portador da carta que os trouxe ao futuro.
> Gancho: "Bostro just came by with all guns blazin'..." / "He's the one who brought us your letter!"

### 3.5 Bacchus e a Reunião com Shipley — O Pagode e o Primeiro-Ministro (`03_024120`–`03_024130`)
Dentro do restaurante, Bacchus os recebe com hospitalidade exagerada, gabando-se do premiado fish and chips com trocadilho "none batter/better" e do ensopado de cordeiro com batatas crocantes; Little Luke se empolga em pedir tudo, Layton o contém lembrando que não vieram para comer, e Bacchus lamenta na saída que percam o melhor cordeiro da cidade. O núcleo do capítulo ocorre em seguida com Shipley (apresentado como Butch, nome real Shipley), amigo de Future Luke e responsável por trazer a carta. Shipley relata reconhecimento em Chinatown: o Towering Pagoda abriga cientistas capturados trabalhando como escravos para o Layton do futuro e, segundo boato, também o primeiro-ministro Bill Hawks, desaparecido há 10 anos no dia do acidente. Future Luke explica que o Pagode é a fortaleza da Family num mar de armazéns e que toda Chinatown está sob controle dela, dificultando a aproximação; propõe então dividir o grupo para preparar infiltração segura, deixa Shipley com Layton e Little Luke e fornece a rota detalhada — subir Flatstone Street ao norte em direção ao cassino, escadas à direita, beco estreito no topo e trilha acima do rio até Chinatown — enquanto ele busca uma via segura.
> Gancho: "Evil Layton is holding them captured scientists there, apparently." / "The Towering Pagoda is the Family stronghold, situated among a sea of warehouses in Chinatown."

### 3.6 Claire Reaparece e a Estátua de Bronze (`03_025000`–`03_025010`)
Deixando o arcade, Layton se distrai ao reavistar a mulher misteriosa; Luke nota que é a mesma de antes, mas Layton disfarça o abalo. Em monólogo interno, ele se pergunta se realmente era Claire, cogita que Hawks possa ter sido enviado ao futuro como eles e oscila entre esperança e lógica ao lembrar que Claire não poderia estar ali após aquele dia. Na praça seguinte, Luke examina uma estátua de bronze de um autor de chapéu parecido com o de Layton; a placa conta que o autor, famoso por livros complicados, escreveu um romance de aventura para alegrar um menino doente, que morreu mas cuja amizade extraordinária perdurou, inspirando a inscrição em memória da amizade eterna — espelho temático da relação Layton/Luke.
> Gancho: "I could've sworn that was Claire. But that's impossible..." / "In memory of an extraordinary and everlasting friendship."

### 3.7 Rumo a Chinatown — Beco, Gyorack, o Farol e Encontros no Caminho (`03_025030`–`03_025060`)
Seguindo a rota de Shipley, o beco para Chinatown revela-se sujo e escuro; Luke corre, escorrega e Layton brinca com a queda. Encontram Gyorack, trabalhador entediado que conta ter aceitado um serviço supostamente tranquilo, foi jogado num buraco escuro para cavar dia e noite e, ao voltar, não encontrou mais casa nem família — oferece um enigma para passar o tempo e lembra do filho que adorava enigmas. Na margem do Thames, o farol gigantesco chama atenção por seu estado impecável e tamanho, evidência de construção recente no futuro. No caminho, Graham surge vaidoso de terno italiano sob medida, ofende-se ao ser associado à Family e se apresenta como o homem mais distinto de Londres; adiante, Craig, escocês de sotaque carregado, confirma o rumo a Chinatown mas admite nunca ter ido por medo da Family e bloqueia passagem com um enigma — ao ser resolvido prova que não são da Family, mas entra em pânico ao ouvir o nome Layton e foge, deixando como pista sapatos e calças encharcados, segunda ocorrência das pegadas molhadas.
> Gancho: "I've sort of lost my life, and now I can't find it." / "Course he's not a Family minion! He's the head honcho!"

### 3.8 Colina, Bazar Negro, o Portão de Chinatown e o Buraco de minhoca (`03_025070`–`03_025115`)
Na colina arborizada, Luke confessa medo de fantasmas e Layton brinca com o ceticismo científico do aprendiz. Logo depois Segal os aborda no meio do bazar do mercado negro, explica que ali se vendem itens raros e duvidosos sem perguntas e aconselha cautela com sapatos chamativos. No portão de Chinatown, dois guardas barrent a entrada — dupla que Layton nota ser sósia de Chelmey e Barton — o que o leva a refletir por que Dr Stahngun convidou justamente o inspetor e ele, exceções numa lista de mídia e alta sociedade, para a apresentação da máquina do tempo. Nesse momento Future Luke ressurge, ouve a questão e propõe falar com Chelmey no passado; conduz o grupo à área arborizada a oeste e revela que o único meio é o buraco de minhoca da relojoaria em Midland Road, ao qual tem acesso fácil via porta antes trancada, pedindo confiança e adiando a infiltração em Chinatown. De passagem pelo hospital, Sharon oferece flu jabs e Luke foge em pânico de agulhas.
> Gancho: "Why did Dr Stahngun, whoever he is, invite the inspector and me?" / "Indeed, Professor. But the only way to do it is to use the buraco de minhoca in the clock shop."
> **Cliffhanger:** O Towering Pagoda — fortaleza da Family onde cientistas e Bill Hawks estariam presos — fica em suspenso. Future Luke reorienta a investigação para voltar 10 anos pelo buraco de minhoca dos Cogg e interrogar Chelmey com memórias frescas, adiando a entrada em Chinatown.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag) — <Vxxxx> se dublado` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, mas esperas `<W>` e animações `<A>` anotadas quando presentes.

### `03_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `03_024010.lbin.txt` — Apelidos Big/Little Luke e restaurante no arcade

*   **ルーク** (Luke Triton):  
    `So where are we headed to now then, um, Mr Triton?`
*   **未来ルーク** (Future Luke):  
    `Luke, please call me anything but Mr Triton. It's really strange being called that by myself.`
*   **ルーク** (Luke Triton):  
    `It's pretty awkward for me too, but what else am I supposed to call you?`
*   **レイトン** (Professor Hershel Layton):  
    `I don't see why you can't both be called Luke.`
*   **レイトン** (Professor Hershel Layton):  
    `Should the need to distinguish between you arise, you can be {''}Big Luke{''}, and you can be {''}Little Luke{''}.`
*   **ルーク** (Luke Triton):  
    `I'm not too keen on {''}Little Luke{''}, but it's better than all this confusion.`
*   **未来ルーク** (Future Luke):  
    `You're the boss, Professor. It's a pleasure to make your acquaintance, Little Luke!`
*   **ルーク** (Luke Triton):  
    `Oh no, the pleasure is all mine, Big Luke!`
*   **未来ルーク** (Future Luke):  
    `Heh heh. Now, where were we? Ah yes. There was something I needed to check up on.`
*   **未来ルーク** (Future Luke):  
    `Professor, did you pass a restaurant in the shopping arcade on the way to the casino?`
*   **レイトン** (Professor Hershel Layton):  
    `The one near the arcade's southern exit?`
*   **未来ルーク** (Future Luke):  
    `That's the one. We'll head there first. A friend of mine is waiting for us.`

### `03_024020.lbin.txt` — Bloqueio da Family

*   **未来ルーク** (Future Luke):  
    `We can't go back that way, the Family is still on the hunt for us.`

### `03_024030.lbin.txt` — Hollis e pegadas molhadas

*   **ホリス** (Hollis):  
    `Yikes! What are you doing, sneaking up on me like that?! You almost gave me a heart attack!`
*   **ルーク** (Luke Triton):  
    `S-sorry, sir. I didn't think a simple hello would scare you so much.`
*   **ホリス** (Hollis):  
    `I was lost in thought and didn't see you coming. Anyway, I have things to do. Goodbye.`
*   **レイトン** (Professor Hershel Layton) *(<A4/1><K> Hmm...)*:  
    `Hmm...`
*   **ルーク** (Luke Triton):  
    `What's the matter, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `Look at the ground, Luke.`
*   **ルーク** (Luke Triton):  
    `Wet footprints... But it hasn't rained since we got here.`
*   **ルーク** (Luke Triton):  
    `How come his shoes are wet?`
*   **レイトン** (Professor Hershel Layton):  
    `I haven't the faintest idea.`

### `03_024040.lbin.txt` — A parábola do bully

*   **未来ルーク** (Future Luke):  
    `Just a little further, Luke. We're almost at the arcade now.`
*   **ルーク** (Luke Triton):  
    `I know. We walked through here earlier.`
*   **未来ルーク** (Future Luke):  
    `Oh right. Of course you did. You mentioned that before, didn't you?`
*   **ルーク** (Luke Triton):  
    `Yeah... Hey, you know, there's something I've been wondering about.`
*   **未来ルーク** (Future Luke):  
    `What's on your mind?`
*   **ルーク** (Luke Triton):  
    `Well, a machine that can take people to any point in time would really change the world.`
*   **ルーク** (Luke Triton):  
    `And not only that - it could improve people's lives!`
*   **未来ルーク** (Future Luke):  
    `Yes, it would certainly have the potential to do that.`
*   **ルーク** (Luke Triton):  
    `But even though this time machine could do so much for people, you want to stop it from being made?`
*   **未来ルーク** (Future Luke):  
    `Picture this scenario. Imagine there's this bully who's always giving you trouble.`
*   **ルーク** (Luke Triton):  
    `Go on.`
*   **未来ルーク** (Future Luke):  
    `Now, let's say you had that time machine we've been talking about.`
*   **未来ルーク** (Future Luke):  
    `Would you travel back in time to when that bully was a teensy five-year-old and get your own back?`
*   **ルーク** (Luke Triton):  
    `Of course not! That'd be cruel.`
*   **未来ルーク** (Future Luke):  
    `Of course you wouldn't, but that's because you've got a good heart.`
*   **未来ルーク** (Future Luke):  
    `Imagine the damage that someone less kind could do with a machine like that.`
*   **ルーク** (Luke Triton):  
    `Cor... I never thought of it like that. We've got to stop that machine from being built!`

### `03_024060.lbin.txt` — Margaret dormindo

*   **マーガレット** (Margaret):  
    `Snoooozzzz... Snoooozzzz...`
*   **ルーク** (Luke Triton):  
    `I think we should let her sleep, Professor.`

### `03_024070.lbin.txt` — Becky e Chinatown

*   **ベッキー** (Becky):  
    `Shh! Be quiet or you'll wake Granny up!`
*   **ルーク** (Luke Triton):  
    `Guess what, Becky? The professor and I are going to Chinatown.`
*   **ベッキー** (Becky):  
    `Crikey, first the casino and now Chinatown? You two are proper tourists!`
*   **ベッキー** (Becky):  
    `It does sound like fun though. What are you planning to do there?`
*   **ルーク** (Luke Triton):  
    `I can't tell you just yet. The professor and I are on a top-secret mission, you see.`
*   **レイトン** (Professor Hershel Layton):  
    `Come along, Luke. We need to get moving.`
*   **ベッキー** (Becky):  
    `Shh! Be quiet or you'll wake Granny up!`
*   **ベッキー** (Becky):  
    `Just promise you'll fill me in on all the juicy details when you come back!`

### `03_024090.lbin.txt` — Chegada ao restaurante

*   **ルーク** (Luke Triton):  
    `Look, there's the restaurant!`
*   **レイトン** (Professor Hershel Layton):  
    `Is this the place you had in mind, Big Luke?`
*   **未来ルーク** (Future Luke):  
    `Yes, this is the one. Let's head in.`

### `03_024100.lbin.txt` — Goon espancado por Bostro

*   **クローンマフィア** (Family Goon):  
    `Uggggh... Owww...`
*   **ルーク** (Luke Triton):  
    `Wow. You look terrible! What happened to you?`
*   **クローンマフィア** (Family Goon):  
    `Yeah, I'm in a right state to be honest with you. Bostro just came by with all guns blazin'...`
*   **ルーク** (Luke Triton):  
    `Oh dear. That's awful.`
*   **クローンマフィア** (Family Goon):  
    `You're tellin' me. He kept bangin' on about some brat who'd got into the casino.`
*   **クローンマフィア** (Family Goon):  
    `That brat wouldn't happen to be you, would it?`
*   **ルーク** (Luke Triton):  
    `M-me? Oh no, I wouldn't dream of going to an awful place like that.`
*   **クローンマフィア** (Family Goon):  
    `Good. I was afraid I was gonna have to teach you a lesson for being so daft.`
*   **クローンマフィア** (Family Goon):  
    `And I really ain't in no shape for teachin' right now, as you can see.`
*   **クローンマフィア** (Family Goon):  
    `Uggggh... I just don't get that Bostro. He's always losin' his rag for no reason.`

### `03_024110.lbin.txt` — O homem de preto

*   **未来ルーク** (Future Luke):  
    `Luke, do you see that man in black over there? Does he look familiar to you?`
*   **ルーク** (Luke Triton):  
    `Yes! He's the one who brought us your letter!`

### `03_024120.lbin.txt` — Bacchus e o cardápio

*   **バッカス** (Bacchus):  
    `Welcome, fellas.`
*   **バッカス** (Bacchus):  
    `If you're looking for the best home-cooked meal in London, you've come to the right place!`
*   **ルーク** (Luke Triton):  
    `Fantastic! What do you recommend?`
*   **バッカス** (Bacchus):  
    `I'm glad you asked! There's nothing I like better than an enthusiastic customer!`
*   **バッカス** (Bacchus):  
    `First things first: my fish and chips are award-winning. There's none batter! I mean better!`
*   **バッカス** (Bacchus):  
    `What kind of Englishman could say no to that, eh?`
*   **ルーク** (Luke Triton):  
    `Not me, that's for sure. I love fish and chips!`
*   **バッカス** (Bacchus):  
    `And if you fancy something warming on a cold day, I've got you covered.`
*   **バッカス** (Bacchus):  
    `My lamb stew with crispy potatoes will have you licking your chops... and the lamb's too! Har har!`
*   **ルーク** (Luke Triton):  
    `I'm sold! I'll have both!`
*   **レイトン** (Professor Hershel Layton):  
    `Don't get carried away now, Luke. The food sounds wonderful, but we didn't come here to eat, did we?`
*   **ルーク** (Luke Triton):  
    `Oh... That's right. I'm sorry sir, but we have business to attend to. I'll order something later, though!`
*   **バッカス** (Bacchus):  
    `Har har! Of course, little fella. You have a good think about which dish suits you.`
*   **バッカス** (Bacchus):  
    `Hello again, little fella. Are you ready to place your order?`
*   **ルーク** (Luke Triton):  
    `Yes! I'll have one of everything, please!`
*   **レイトン** (Professor Hershel Layton):  
    `Have patience, my boy. We can have something to eat once we've finished our business here.`
*   **バッカス** (Bacchus):  
    `Har har! Don't fret, little fella. When you do get to eat, it'll be a meal to remember, I promise.`

### `03_024125.lbin.txt` — Despedida de Bacchus

*   **バッカス** (Bacchus):  
    `You're not going to have a bite before you leave? That's a real shame, lad.`
*   **バッカス** (Bacchus):  
    `I don't mean to twist the knife, but you're missing out on the finest lamb you'll ever dig a fork into.`
*   **ルーク** (Luke Triton):  
    `If I could stay, I would, believe me. Next time I'm here, I'm ordering for two!`

### `03_024130.lbin.txt` — Reunião com Shipley (texto longo, 109 blocos)

*   **未来ルーク** (Future Luke):  
    `Sorry to keep you waiting, Shipley.`
*   **ブッチ** (Butch / Shipley):  
    `Not at all. I just got here a minute ago myself.`
*   **未来ルーク** (Future Luke):  
    `You've all met before, but I don't think you were properly introduced.`
*   **未来ルーク** (Future Luke):  
    `This is my good friend, Shipley.`
*   **未来ルーク** (Future Luke):  
    `He has played a vital role in bringing you and Little Luke here to our time.`
*   **レイトン** (Professor Hershel Layton):  
    `Pleased to meet you, Shipley.`
*   **ブッチ** (Butch / Shipley):  
    `Likewise, Professor. Sorry I had to be so brief with ya when we last met.`
*   **ブッチ** (Butch / Shipley):  
    `Luke here told me I shouldn't share any details until he had the chance to speak to ya himself.`
*   **レイトン** (Professor Hershel Layton):  
    `Don't give it another thought. Luke needed to test us before sharing the details of his plan.`
*   **未来ルーク** (Future Luke):  
    `Shipley, did you manage to do some reconnaissance work in Chinatown as I asked?`
*   **ブッチ** (Butch / Shipley):  
    `Certainly did, Luke. That filthy scumbag Layton-`
*   **ブッチ** (Butch / Shipley):  
    `Er, apologies, Professor. I'm talking about the evil Layton, of course.`
*   **未来ルーク** (Future Luke):  
    `The professor is aware of the situation. Do continue.`
*   **ブッチ** (Butch / Shipley):  
    `Right. Ya know the Towering Pagoda in Chinatown?`
*   **ブッチ** (Butch / Shipley):  
    `Evil Layton is holding them captured scientists there, apparently.`
*   **ブッチ** (Butch / Shipley):  
    `He's got them working like slaves on something or other.`
*   **未来ルーク** (Future Luke):  
    `So the scientists are in the Towering Pagoda... That's going to make things very difficult.`
*   **ブッチ** (Butch / Shipley):  
    `I heard another peculiar rumour while I was about town.`
*   **未来ルーク** (Future Luke):  
    `Yes?`
*   **ブッチ** (Butch / Shipley):  
    `Word has it that the prime minister who disappeared 10 years ago is being held up there too.`
*   **未来ルーク** (Future Luke):  
    `What?!`
*   **レイトン** (Professor Hershel Layton):  
    `Bill Hawks...`
*   **レイトン** (Professor Hershel Layton):  
    `He's been missing ever since the day of the accident.`
*   **未来ルーク** (Future Luke):  
    `It's been 10 years now...`
*   **未来ルーク** (Future Luke):  
    `Do you suppose evil Layton might have abducted the prime minister as well as all those scientists?`
*   **レイトン** (Professor Hershel Layton):  
    `We won't know until we check the facts for ourselves.`
*   **レイトン** (Professor Hershel Layton):  
    `Big Luke, you seemed apprehensive at the mention of the Towering Pagoda. What is this place?`
*   **未来ルーク** (Future Luke):  
    `The Towering Pagoda is the Family stronghold, situated among a sea of warehouses in Chinatown.`
*   **未来ルーク** (Future Luke):  
    `To complicate matters, all of Chinatown is under Family control.`
*   **未来ルーク** (Future Luke):  
    `Which means it'll be difficult just to get within walking distance.`
*   **レイトン** (Professor Hershel Layton):  
    `Be that as it may, we need to uncover the truth.`
*   **レイトン** (Professor Hershel Layton):  
    `Can you guide us safely to the pagoda?`
*   **未来ルーク** (Future Luke):  
    `Hmm... Infiltrating a place like that is going to require a bit of preparation.`
*   **未来ルーク** (Future Luke):  
    `Why don't we split up for a bit and I'll see if I can secure us a safe route there?`
*   **未来ルーク** (Future Luke):  
    `You go on and head for Chinatown without me. Shipley will tell you how to get that far. All right?`
*   **レイトン** (Professor Hershel Layton):  
    `Very well.`
*   **未来ルーク** (Future Luke):  
    `Good. Now I need to get moving. Be careful out there.`
*   **ルーク** (Luke Triton):  
    `Crikey, he didn't half leave in a hurry.`
*   **レイトン** (Professor Hershel Layton):  
    `We need to get to Chinatown, Shipley. What's the best way to get there?`
*   **ブッチ** (Butch / Shipley):  
    `Let's see... Yer best bet is to head back up Flatstone Street.`
*   **ブッチ** (Butch / Shipley):  
    `As ya head north towards the casino, there's a small set of stairs on the right.`
*   **ブッチ** (Butch / Shipley):  
    `Do ya know the ones I mean?`
*   **レイトン** (Professor Hershel Layton):  
    `Ah, yes. Now that you mention it, I do recall passing by an area that fits that description.`
*   **ブッチ** (Butch / Shipley):  
    `Good. Head up them stairs and follow the narrow alley at the top until ya hit a path above the river.`
*   **ブッチ** (Butch / Shipley):  
    `From there, just follow that path and it'll take ya straight into Chinatown.`
*   **ルーク** (Luke Triton):  
    `You're not coming with us, Shipley?`
*   **ブッチ** (Butch / Shipley):  
    `I wish I could, but I've got to stay here and wait for word from yer older self.`
*   **レイトン** (Professor Hershel Layton):  
    `Very well. Thank you for your assistance, Shipley. Come, Luke. We mustn't tarry here.`
*   **ブッチ** (Butch / Shipley):  
    `Be careful out there! If ya run into any trouble, ya can always find me here.`
*   **ブッチ** (Butch / Shipley):  
    `To get to Chinatown, head north up Flatstone Street.`
*   **ブッチ** (Butch / Shipley):  
    `Then climb the stairs on the right and go down the alley at the top.`
*   **ブッチ** (Butch / Shipley):  
    `After a while, ye'll come to a path above the river. Follow that path to get to Chinatown.`

### `03_025000.lbin.txt` — Reavistamento de Claire

*   **レイトン** (Professor Hershel Layton):  
    `Hmm...`
*   **ルーク** (Luke Triton):  
    `Did you see that, Professor? That was the same woman we saw earlier, wasn't it?`
*   **レイトン** (Professor Hershel Layton):  
    `I... I suppose it was.`
*   **ルーク** (Luke Triton):  
    `You seem distracted, Professor. Are you all right?`
*   **レイトン** (Professor Hershel Layton):  
    `What's that? Oh, I'm fine, Luke. Absolutely fine.`
*   **ルーク** (Luke Triton):  
    `If you say so, Professor. Hey look, I bet these are the stairs Shipley mentioned.`
*   **レイトン** (Professor Hershel Layton):  
    `I could've sworn that was Claire. But that's impossible...`
*   **ブッチ** (Butch / Shipley) *(eco de `03_024130` inserido como interlúdio)*:  
    `Word has it that the prime minister who disappeared 10 years ago is being held up there too.`
*   **レイトン** (Professor Hershel Layton):  
    `Perhaps that's what happened when the prime minister was abducted 10 years ago...`
*   **レイトン** (Professor Hershel Layton):  
    `Perhaps he was sent to the future, as we were... What if all this talk of time travel is real?`
*   **レイトン** (Professor Hershel Layton):  
    `If so, then maybe that really was Claire...`
*   **レイトン** (Professor Hershel Layton):  
    `No! It defies all logic. Claire can't be here. Not after that day...`

### `03_025010.lbin.txt` — Estátua de bronze e amizade eterna

*   **ルーク** (Luke Triton):  
    `Do you suppose that bronze statue depicts some sort of local hero? I'm going to have a quick look.`
*   **ルーク** (Luke Triton):  
    `Huh? Look, Professor, the man in the statue has the same hat as you!`
*   **レイトン** (Professor Hershel Layton):  
    `Ha ha! So he does! If I'm the man in the statue, does that make you that boy there?`
*   **ルーク** (Luke Triton):  
    `Hmm, well, I suppose he looks a bit like me...`
*   **ルーク** (Luke Triton):  
    `Oh, there's a description of the statue here. Let's see...`
*   **ルーク** (Luke Triton):  
    `It seems our friend here was some sort of famous author.`
*   **レイトン** (Professor Hershel Layton):  
    `An author, you say? Not a professor?`
*   **ルーク** (Luke Triton):  
    `Imagine if he was! Now that would be a coincidence! Let's see what else it says.`
*   **ルーク** (Luke Triton):  
    `The author used to write big, complicated books. But all that changed because of this boy.`
*   **ルーク** (Luke Triton):  
    `The boy was ill, and to cheer him up, the man wrote an adventure novel for people of all ages.`
*   **ルーク** (Luke Triton):  
    `I suppose the book was so successful that he went on to write more of them.`
*   **レイトン** (Professor Hershel Layton):  
    `What a heart-warming story.`
*   **ルーク** (Luke Triton):  
    `Oh, but that's not all, Professor. Here, I'll read you the rest.`
*   **ルーク** (Luke Triton):  
    `In the end, the little boy was taken by his illness.`
*   **ルーク** (Luke Triton):  
    `However, the extraordinary friendship between the author and the boy would last forever.`
*   **ルーク** (Luke Triton):  
    `I can't believe how sad that ending is.`
*   **レイトン** (Professor Hershel Layton):  
    `There, there. It's not all bad, my boy. It sounds as if the two found true friendship in each other.`
*   **レイトン** (Professor Hershel Layton):  
    `Some people go through their whole lives without experiencing such a thing.`
*   **ルーク** (Luke Triton):  
    `I suppose so. It's still terribly sad, though.`
*   **レイトン** (Professor Hershel Layton):  
    `Look here. It says, {''}In memory of an extraordinary and everlasting friendship.{''}`
*   **レイトン** (Professor Hershel Layton):  
    `Wouldn't it be wonderful if our friendship grew to those heights?`
*   **ルーク** (Luke Triton):  
    `What do you mean, {''}if{''}?! Our friendship is already extraordinary and everlasting.`
*   **レイトン** (Professor Hershel Layton):  
    `Now, now, Luke. I didn't mean to ruffle your feathers. You're right. We're very good friends.`
*   **レイトン** (Professor Hershel Layton):  
    `You're not upset, are you?`
*   **ルーク** (Luke Triton):  
    `Me? Upset? Of course not. Anyway, I think we should move on.`
*   **レイトン** (Professor Hershel Layton):  
    `Oh dear...`

### `03_025030.lbin.txt` — Beco para Chinatown

*   **ルーク** (Luke Triton):  
    `Is this really the way to Chinatown? It's awfully dirty...and dark.`
*   **レイトン** (Professor Hershel Layton):  
    `Does this place frighten you, my boy?`
*   **ルーク** (Luke Triton):  
    `Me? Scared? No way! I just want to get to Chinatown. Let's go!`
*   **レイトン** (Professor Hershel Layton):  
    `There's no need to dash off, Luke. Do be careful, you could sli-`
*   **ルーク** (Luke Triton):  
    `Whoa! Ow! Ow ow ow OW!`
*   **レイトン** (Professor Hershel Layton):  
    `Oh dear. What did I just tell you?`
*   **ルーク** (Luke Triton):  
    `Are you laughing at me, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `Laughing? Me? Certainly not! Are you quite all right?`
*   **ルーク** (Luke Triton):  
    `Of course I am. I just bumped my knee a little. I'll walk it off.`
*   **レイトン** (Professor Hershel Layton):  
    `Oh good. I was worried for a moment there. Let's go.`

### `03_025040.lbin.txt` — Gyorack e o buraco

*   **ギョラック** (Gyorack):  
    `Hello there, little chappie. Have you ever been so bored you could keel over? Me too.`
*   **ルーク** (Luke Triton):  
    `Why are you so bored?`
*   **ギョラック** (Gyorack):  
    `Well, I don't have anything to do. That's a big factor.`
*   **ギョラック** (Gyorack):  
    `But also, I've sort of lost my life, and now I can't find it.`
*   **ルーク** (Luke Triton):  
    `Uh... How does one lose one's life?`
*   **ギョラック** (Gyorack):  
    `A while back, this fella tells me I can earn a few bob doing this cushy job.`
*   **ギョラック** (Gyorack):  
    `I was out of work at the time, so I thought, why not, you know?`
*   **ルーク** (Luke Triton):  
    `Makes sense.`
*   **ギョラック** (Gyorack):  
    `Yeah, I thought so too, until I realised I'd been had.`
*   **ギョラック** (Gyorack):  
    `Fella threw me in a dark hole and had me digging all day and night. Working like a dog, I was.`
*   **ルーク** (Luke Triton):  
    `It sounds like whatever he was paying you, it wasn't worth it.`
*   **ギョラック** (Gyorack):  
    `I haven't even told you the worst bit yet! I finally finish the job and I head home, yeah?`
*   **ギョラック** (Gyorack):  
    `But everything's been switched around while I'm in the hole, and I can't find my house or my family!`
*   **ルーク** (Luke Triton):  
    `Oh gosh! Maybe you travelled through time like us!`
*   **ギョラック** (Gyorack):  
    `Who what where now? I don't really follow, but I do know I've been out here on my own for a while.`
*   **ギョラック** (Gyorack):  
    `The only thing I've got to pass the time are these puzzles I do. Here, try one.`
*   **ギョラック** (Gyorack):  
    `No luck? Don't feel bad, chappie. You can always come back and try again. I'm not going anywhere...`
*   **ギョラック** (Gyorack):  
    `Let me guess. You've got nothing to do. Me neither. Why don't you pass the time with a puzzle?`
*   **ギョラック** (Gyorack):  
    `Good job there, chappie. I can tell you're a thinker.`
*   **ギョラック** (Gyorack):  
    `You remind me of my son. A right know-it-all, he is, but he's a good boy really.`
*   **ギョラック** (Gyorack):  
    `He used to love it when I'd give him a puzzle to work on. I do wish I could see the little tyke again.`
*   **ギョラック** (Gyorack):  
    `I wish I could find my way back home. It'd be nice to see the family again.`

### `03_025050.lbin.txt` — Margem do Thames e farol

*   **ルーク** (Luke Triton):  
    `It looks like we're on the right track, Professor. Here's the Thames.`
*   **レイトン** (Professor Hershel Layton):  
    `Indeed, and it looks as majestic as ever.`
*   **ルーク** (Luke Triton):  
    `Mm hmm. I suppose some parts of London never change, even after 10 whole-`
*   **ルーク** (Luke Triton):  
    `Hey, that wasn't there before.`
*   **レイトン** (Professor Hershel Layton):  
    `You've noticed it as well then, Luke.`
*   **ルーク** (Luke Triton):  
    `That has to be the biggest lighthouse I've ever seen, and I'm sure it wasn't there before.`
*   **レイトン** (Professor Hershel Layton):  
    `Judging by its almost pristine condition, it must have been erected fairly recently.`

### `03_025055.lbin.txt` — Graham, o dândi italiano

*   **グラハム** (Graham):  
    `Good day, fine gents. Isn't the view from here absolutely glorious?`
*   **レイトン** (Professor Hershel Layton):  
    `It most certainly is, sir.`
*   **グラハム** (Graham):  
    `Truly, it's nothing short of breathtaking.`
*   **ルーク** (Luke Triton):  
    `Psst, Professor. Look at this man. Do you suppose he could be part of the Family?`
*   **グラハム** (Graham):  
    `What's that, boy? I'm standing right here! If you have something to say, say it to my face!`
*   **グラハム** (Graham):  
    `What's more, I don't appreciate being associated with those drably clad ruffians.`
*   **グラハム** (Graham):  
    `Look at this suit! See the stitching? This was custom-made in Italy! Italy, I say!`
*   **ルーク** (Luke Triton):  
    `I'm ever so sorry, sir. I meant no offence! I never thought you were one of them really.`
*   **グラハム** (Graham):  
    `Well, as long as you acknowledge your outrageous mistake, I'm willing to let bygones be bygones.`
*   **グラハム** (Graham):  
    `Just to assuage any lingering doubts as to my identity, however, allow me to introduce myself.`
*   **グラハム** (Graham):  
    `Before you stands London's most distinguished, dashing and debonair man. The name's Graham.`
*   **グラハム** (Graham):  
    `I would tell you to remember the name, but I know you can't possibly forget!`
*   **ルーク** (Luke Triton):  
    `Got it! Graham, London's most distinguished, dashing and, um... I forgot the last one.`
*   **ルーク** (Luke Triton):  
    `But I won't forget the name, I promise!`
*   **グラハム** (Graham):  
    `Graham's the name. Those in search of London's most debonair man need look no further!`

### `03_025060.lbin.txt` — Craig, o escocês

*   **クレイグ** (Craig):  
    `Oh, hullo there.`
*   **ルーク** (Luke Triton):  
    `Say, do you happen to know if this is the way to Chinatown?`
*   **クレイグ** (Craig):  
    `Ah reckon this path'll most likely take ye there, aye.`
*   **ルーク** (Luke Triton):  
    `You reckon? Haven't you taken this path before?`
*   **クレイグ** (Craig):  
    `Nae chance! Ah've a feeling something could happen tae me doon that way. Something bad.`
*   **クレイグ** (Craig):  
    `Like, Ah could get intae a rammy with that Family lot.`
*   **クレイグ** (Craig):  
    `Ah'm better off jist staying here and solving puzzles.`
*   **クレイグ** (Craig):  
    `Aye, it's a tough one, eh?`
*   **クレイグ** (Craig):  
    `Ah don't think ye should be going doon there then.`
*   **クレイグ** (Craig):  
    `Ye'll need to prove that yer on the ball by solving that wee puzzle first.`
*   **クレイグ** (Craig):  
    `Ah've a feeling that Chinatown place is bad news. Much safer tae stay here and do a bit of puzzling.`
*   **クレイグ** (Craig):  
    `Huh, ye've solved ma puzzle. Looks like yer nae part of that Family lot then. They're not too bright, see.`
*   **ルーク** (Luke Triton):  
    `Of course not! We're no Family minions! I'm Luke, and this here is the famous Professor Layton!`
*   **クレイグ** (Craig):  
    `Whit?! L-Layton, ye say? Course he's not a Family minion! He's the head honcho!`
*   **クレイグ** (Craig):  
    `Help! Somebody help me!`
*   **ルーク** (Luke Triton):  
    `Oops. I forgot how the name Layton scares the living daylights out of people in this time.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, it's unfortunate, but people do seem to think I'm a criminal.`
*   **レイトン** (Professor Hershel Layton):  
    `On a more interesting note, have a look at the ground, Luke.`
*   **ルーク** (Luke Triton):  
    `Those footprints must belong to the man who just ran off.`
*   **ルーク** (Luke Triton):  
    `Come to think of it, his shoes and trousers were soaking. But why?`
*   **ルーク** (Luke Triton):  
    `It's a bit chilly to go out for a swim, don't you think?`
*   **レイトン** (Professor Hershel Layton):  
    `Indeed. So how did he get so wet? Hmm...`

### `03_025070.lbin.txt` — Colina assombrada

*   **ルーク** (Luke Triton):  
    `You know, Professor, what with all the trees and stuff, this hill is a bit...creepy.`
*   **レイトン** (Professor Hershel Layton):  
    `What's the matter, Luke? You're not afraid of seeing a ghost, are you?`
*   **ルーク** (Luke Triton):  
    `C-come on, P-Professor! I know y-you would n-never believe in something s-so unscientific!`
*   **レイトン** (Professor Hershel Layton):  
    `Unscientific, you say?`
*   **ルーク** (Luke Triton):  
    `Yeah! Th-there's no p-proof that ghosts exist!`
*   **レイトン** (Professor Hershel Layton):  
    `And a man of science like you would never fear something as silly as ghosts, eh, Luke?`
*   **ルーク** (Luke Triton):  
    `Well...maybe just a little.`

### `03_025080.lbin.txt` — Segal e o mercado negro

*   **セガール** (Segal):  
    `Psst. Oi oi, you two, look sharp. Ye've got a lost look about ya. Do ya know where ye are?`
*   **レイトン** (Professor Hershel Layton):  
    `I must confess we do not. It's our first time in this area.`
*   **セガール** (Segal):  
    `Listen. I could be wrong, but it looks like you two are a couple of fine, upstandin' citizens.`
*   **セガール** (Segal):  
    `I'm a nice fella, so I'll clue ye in. Yer standin' right in the middle of the black market bazaar.`
*   **ルーク** (Luke Triton):  
    `Black market?! Wow!`
*   **セガール** (Segal):  
    `Wow is right, sonny. We sell a lot of dodgy stuff out here and no one questions where it comes from.`
*   **セガール** (Segal):  
    `If it was me in those shiny loafers of yours, I'd keep me head down and leg it, quick as I could.`
*   **レイトン** (Professor Hershel Layton):  
    `That would seem prudent indeed.`
*   **ルーク** (Luke Triton):  
    `Before we go, though, I've got a question. Why do people come all the way out here to shop?`
*   **セガール** (Segal):  
    `Listen, son. The things for sale here... Let's just say ya won't find them at the local corner shop.`
*   **セガール** (Segal):  
    `But come to the bazaar and who can say what treasures ye'll find?`
*   **ルーク** (Luke Triton):  
    `Oh, I suppose you mean antiques and other rare items?`
*   **レイトン** (Professor Hershel Layton):  
    `I think we've asked enough questions for one day, Luke. Let's move on, shall we?`
*   **セガール** (Segal):  
    `You two be careful! Oh and if yer ever in the market for somethin'... hard to find, swing by.`
*   **セガール** (Segal):  
    `You two still hoverin' around here? I'd get goin' if I was you.`

### `03_025100.lbin.txt` — Portão de Chinatown e sósias de Chelmey & Barton

*   **ワルミー** (Warumy / Gate Guard):  
    `Oi! Just what do you two think you're doing? No one passes through this here gate!`
*   **ワルミー** (Warumy / Gate Guard):  
    `Now clear off or we'll be having more than words with each other.`
*   **レイトン** (Professor Hershel Layton):  
    `I see...`
*   **ルーク** (Luke Triton):  
    `What nerve! They're just a pair of brutes, don't you agree?`
*   **ルーク** (Luke Triton):  
    `Um...Professor? What are you thinking about?`
*   **レイトン** (Professor Hershel Layton):  
    `Tell me, Luke. Did those two remind you of anyone we know?`
*   **ルーク** (Luke Triton):  
    `Hmm?`
*   **レイトン** (Professor Hershel Layton):  
    `It's not an exact match, but they do bear an odd resemblance to a certain pair of fellows.`
*   **ルーク** (Luke Triton):  
    `Hmm...`
*   **ルーク** (Luke Triton):  
    `Of course! You're talking about Inspector Chelmey and Barton!`
*   **レイトン** (Professor Hershel Layton):  
    `I am. The similarities are quite striking, don't you think?`
*   **ルーク** (Luke Triton):  
    `Big guy in charge, check. Small assistant, check!`
*   **ルーク** (Luke Triton):  
    `But something tells me the inspector wouldn't take kindly to being told he resembles a criminal!`
*   **レイトン** (Professor Hershel Layton):  
    `Speaking of the inspector, did his presence at that event seem at all odd to you?`
*   **ルーク** (Luke Triton):  
    `Event? Do you mean the time machine presentation?`
*   **レイトン** (Professor Hershel Layton):  
    `Yes. Why do you suppose a police inspector was invited to an event like that in the first place?`
*   **ルーク** (Luke Triton):  
    `Well... He's cracked quite a few tough cases. Maybe his celebrity status got him invited.`
*   **レイトン** (Professor Hershel Layton):  
    `Yes, I assumed the same thing. After all, pseudo-celebrity status is what got you and me our tickets.`
*   **ルーク** (Luke Triton):  
    `Pseudo-celebrity? Nonsense! You're the great Professor Layton.`
*   **ルーク** (Luke Triton):  
    `The model modern-day English gentleman!`
*   **レイトン** (Professor Hershel Layton):  
    `Ha ha! I hate to say it, Luke, but I think you're the only one who'd heap that kind of praise on me.`
*   **レイトン** (Professor Hershel Layton):  
    `From what I saw, almost everyone there was either from the media or London high society.`
*   **レイトン** (Professor Hershel Layton):  
    `The inspector and I were clear exceptions to an otherwise homogenous list of names.`
*   **ルーク** (Luke Triton):  
    `So?`
*   **レイトン** (Professor Hershel Layton):  
    `So, the question looms before us. Why did Dr Stahngun, whoever he is, invite the inspector and me?`
*   **レイトン** (Professor Hershel Layton):  
    `What I wouldn't give to hear the inspector's take on the event...`
*   **ルーク** (Luke Triton):  
    `Yeah, it's too bad we'd have to go back to our own time to ask him.`
*   **ルーク** (Luke Triton):  
    `Wait a second! What if the inspector is still working here in the future?`
*   **未来ルーク** (Future Luke):  
    `Professor, there you are!`
*   **ルーク** (Luke Triton):  
    `Ah, hello Luke.`
*   **未来ルーク** (Future Luke):  
    `I couldn't help but overhear you as I ran up. Did you say you'd like to meet the inspector?`
*   **レイトン** (Professor Hershel Layton):  
    `Yes. Ideally, we would meet him back in our time, while the events of that time are still fresh.`
*   **未来ルーク** (Future Luke):  
    `I think we can make that happen.`
*   **ルーク** (Luke Triton):  
    `But how?!`
*   **未来ルーク** (Future Luke):  
    `Let's continue this conversation where we can't be seen or heard, shall we?`
*   **未来ルーク** (Future Luke):  
    `Why don't we head over to the wooded area to the west?`
*   **未来ルーク** (Future Luke):  
    `There's a way to go back to your time, but let's go to the wooded area so we can talk in private.`

### `03_025110.lbin.txt` — Área arborizada: volta no tempo

*   **未来ルーク** (Future Luke):  
    `There. Much better. I don't think anyone is likely to overhear us now.`
*   **レイトン** (Professor Hershel Layton):  
    `You mentioned that there is a way for us to visit the inspector in our own time.`
*   **レイトン** (Professor Hershel Layton):  
    `I can only imagine that this means going back to 10 years ago. Is such a thing possible?`
*   **未来ルーク** (Future Luke):  
    `Indeed, Professor. But the only way to do it is to use the wormhole in the clock shop.`
*   **ルーク** (Luke Triton):  
    `But the door to the clock shop is locked. How are we going to get in?`
*   **未来ルーク** (Future Luke):  
    `That shouldn't be a problem. I can get that door open for you.`
*   **レイトン** (Professor Hershel Layton):  
    `Strange... Why is it that you have such easy access to the wormhole?`
*   **未来ルーク** (Future Luke):  
    `I promise I'll explain everything when we get there. Please trust me on this.`
*   **未来ルーク** (Future Luke):  
    `But for now, let's return to the clock shop on Midland Road.`
*   **ルーク** (Luke Triton):  
    `But what about our plan to head into Chinatown?`
*   **未来ルーク** (Future Luke):  
    `That'll have to be put on the back burner for now. The situation has changed.`

### `03_025115.lbin.txt` — Sharon: flu jabs

*   **シャロン** (Sharon):  
    `Oh, you again. Back to visit someone else? Or are you feeling a bit under the weather?`
*   **シャロン** (Sharon):  
    `We're doing flu jabs now if you need one.`
*   **ルーク** (Luke Triton):  
    `J-jabs?! Oh no, I'm fit as a fiddle! Nope, no need to go poking at me with a needle!`
*   **シャロン** (Sharon):  
    `You sure? There's no waiting list, you know. You could have it done right now...`
*   **ルーク** (Luke Triton):  
    `P-Professor, I think our business here is finished! Let's go!`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `03_024030` | **Evento: pegadas molhadas (Hollis)** | Primeira pista visual das pegadas molhadas sem chuva; Layton pede para observar o chão. |
| `03_025040` | **Enigma de Gyorack (ギョラック)** | Trabalhador oferece enigma para passar o tempo; ramificações de falha (`No luck?`) e sucesso (`Good job`). Temática do buraco escuro. |
| `03_025060` | **Enigma de Craig (クレイグ)** | Escocês bloqueia caminho com "wee puzzle" para provar que não são da Family; fuga cômica ao ouvir nome Layton + segunda pista de pegadas molhadas. |
| `03_024130` | **Evento central: Exposição de Shipley** | Revelação do Towering Pagoda (fortaleza da Family), cientistas escravizados, boato de que Bill Hawks está vivo e preso lá. |
| `03_024130` + `03_025000` | **Navegação: rota para Chinatown** | Direções repetidas de Shipley: subir Flatstone Street norte, escadas à direita, beco, trilha acima do rio até Chinatown. |
| `03_025010` | **Evento: Estátua de bronze** | Lore paralela de autor que vira escritor de aventura por causa de menino doente; espelho temático da amizade Layton/Luke. |
| `03_025080` | **Evento: Black Market Bazaar (Segal)** | Introdução do bazar negro — mercado de itens raros/dodgy fora do controle da Family. |
| `03_025100` | **Evento: Portão de Chinatown (Warumy)** | Bloqueio narrativo; sósias de Chelmey & Barton; reflexão de Layton sobre lista de convidados de Stahngun. |
| `03_025110` | **Evento de virada: wormhole** | Future Luke revela que pode abrir a relojoaria e propõe voltar 10 anos para falar com Chelmey; Chinatown adiado. |
| `03_024040` | **Evento ético: parábola do bully** | Future Luke justifica impedir a máquina do tempo com analogia moral. |
| `03_025050` | **Evento ambiental: farol no Thames** | Farol gigante novo em estado impecável — prova visual da passagem de 10 anos. |
| `03_024010` | **Evento de nomenclatura** | Criação dos apelidos Big Luke / Little Luke para distinguir os dois Lukes. |

**Eventos sem enigma direto:** Conversas de Bacon/Bacchus (`03_024120`), susto de Claire (`03_025000`), colina assombrada (`03_025070`), Graham vaidoso (`03_025055`), gags de Margaret/Becky/Sharon, e o Goon espancado por Bostro (`03_024100`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Capítulo não-dublado:** Diferente do prólogo e de `02_019000`/`02_022000`, `uk/03` não contém nenhum bloco `<Vxxxx>`. Todo o capítulo é exploração/NPC talk (`<T>` puro), indicando transição de gameplay aberta antes do próximo set piece dublado.
*   **Shipley = Butch:** O arquivo `03_024130` confirma que `ブッチ` (Butch) e Shipley são a mesma pessoa — Butch era codinome da Family; Shipley é o nome real entre aliados de Future Luke. Coerente com `01_011130` onde Butch entregou a segunda carta "tailor-made puzzle".
*   **Pegadas molhadas:** Repetidas em `03_024030` (Hollis) e `03_025060` (Craig). O texto enfatiza ausência de chuva e roupas molhadas — foreshadowing de travessia por túneis/esgoto alagado rumo a Chinatown ou do próprio wormhole úmido. Layton explicitamente manda Luke olhar o chão duas vezes.
*   **Eco de texto em `03_025000`:** O bloco `Word has it that the prime minister who disappeared 10 years ago is being held up there too.` repete literalmente `03_024130:00370000` — inserção de flashback/lembrança de Layton ao ver Claire, não erro de dump. Reforça a ligação entre desaparecimento de Hawks e possível viagem temporal de Claire.
*   **Sósias Chelmey & Barton:** `03_025100` usa deliberadamente `ワルミー` duplicado (dois guardas idênticos) para espelhar a dupla policial. Layton explicita a analogia — pista de que Stahngun convidou deliberadamente figuras fora do circuito midiático/alta sociedade.
*   **Estátua como mise en abyme:** A história do autor e do menino morto (`03_025010`) espelha a amizade Layton/Luke e prenuncia o tema de perda e memória que culminará com Claire. O `<CR>` indica caixa de citação dentro do texto.
*   **Rota de Shipley como design de nível:** As direções são repetidas em 3 blocos finais de `03_024130` (`head north up Flatstone Street / stairs on the right / alley at the top / path above the river`) — padrão Level-5 para garantir que o jogador não se perca no hub aberto pós-Gilded 7.
*   **Contraste de tom:** O capítulo intercala exposição pesada (Pagode, Hawks, wormhole) com gags leves (Bacchus "none batter / better", Graham "Italy!", Sharon "flu jabs", Luke escorregando) — estrutura típica de respiro entre dungeons.
*   **Proposta de volta no tempo:** `03_025110` formaliza a mecânica de revisita ao passado via wormhole da relojoaria — primeiro uso narrativo reverso do portal (até então só ida). Future Luke admite acesso privilegiado mas adia explicação, criando cliffhanger de confiança.

---

*Gerado a partir de dumps LSCR brutos — 25/25 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/03`. Próximo capítulo: `04` — Chinatown / Infiltração no Pagode.*
