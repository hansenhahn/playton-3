# Capítulo 12 — O Segredo do Thames Arms, London Falso e a Vingança de Clive | Professor Layton and the Unwound Future

> **Capítulo 12 — O Thames Arms / A Verdade sobre o London do Futuro, Dimitri e Clive** — Análise de dump LSCR para `Textos Originais/txt/uk/12/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/12/`
> Total de arquivos escaneados: **21**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão, `<J>` = jump, `<S671>` = sistema de enigma

---

## 1. Arquivos Cobertos

Todos os 21 dumps `.lbin.txt` em `uk/12`:

```
12_000000.lbin.txt  — [vazio - apenas cabeçalho]
12_033590.lbin.txt  — Avistamento do inspector, convite ao Thames Arms
12_033593.lbin.txt  — Chelmey e o puzzle irrelevante, promessa do prime minister
12_033594.lbin.txt  — Flavor: Barton pede ajuda para o puzzle do inspector
12_033596.lbin.txt  — Flavor: Subject 3 (３号) - gang parade, blow the lid off mystery
12_033710.lbin.txt  — Flavor: avistamento de Big Luke
12_033720.lbin.txt  — Reencontro com Future Luke, shadowing Celeste até o restaurante
12_033730.lbin.txt  — Bartender do Thames Arms, welcome back
12_033740.lbin.txt  — Don Paolo impaciente no restaurante
12_033750.lbin.txt  — Celeste aliviada, all concerned parties em reunião
12_034500.lbin.txt  — REVELAÇÃO CENTRAL dublada: London fake, set, no time machine, lift do clock shop
12_035010.lbin.txt  — Exposição dublada: cavern subterrânea, largest film set, scientists enganados, bartender da Family
12_035020.lbin.txt  — Armadilha de Dimitri: minefield explosives, puzzle Find all the bombs, truque do infinito
12_035030.lbin.txt  — Backstory dublado de Dimitri: Bill Hawks, prototype, Claire test subject, flaw, venda do power source
12_035035.lbin.txt  — Flavor: Dimitri hasn't told us everything
12_036000.lbin.txt  — Cutscene: Movie de Dimitri correndo ao lab após explosão (Bill wounded, Claire dead)
12_037000.lbin.txt  — Continuação dublada: Bill greed, political ladder, amargura, pawn question
12_039000.lbin.txt  — Reviravolta dublada: Layton desmascara Clive, pawn de Dimitri
12_039010.lbin.txt  — Exposição dublada: Clive órfão da explosão, Constance Dove, newspaper, facsimile London, arma secreta
12_040010.lbin.txt  — Flavor: Flora refém, Layton look over there
12_041010.lbin.txt  — Flavor: mobile fortress revelada, Flora trapped up there
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `12_000000.lbin.txt`. `12_033594`/`12_033596`/`12_033710`/`12_035035`/`12_040010`/`12_041010` são flavors curtos de transição ou gags; `12_036000` é apenas marcador de cutscene `× / Movie of Dimitri rushing...`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 12 |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Protagonista, convoca Chelmey ao Thames Arms, revela London falso como set/cavern, desmonta minefield de Dimitri com truque do infinito, narra passado de Clive |
| `ルーク` | **Luke Triton** | Aprendiz, avista inspector e Big Luke, reage What?! ao London fake, decodifica 00 como infinity, alerta sobre Flora refém |
| `チェルミー` | **Inspector Chelmey** | Descrente mas atraído pela promessa do prime minister, preso ao enigma note irrelevante, reage underground right now e bumbling |
| `バートン` | **Constable Barton** | Gag de delicious smells no Thames Arms, flavor pedindo ajuda para Chelmey |
| `３号` | **Subject 3** | Gag curto gang parade |
| `未来ルーク` / `クラウス（帽子あり）` | **Future Luke / Big Luke / Clive (com chapéu)** | Shadowing Celeste, confirma todos no restaurante, depois desmascarado como Clive — órfão vingativo, dono do facsimile London |
| `バーテン` | **Bartender (Thames Arms / Family)** | Hospedeiro welcoming, depois revela-se Family hideout e ameaça I have no choice but to shut you up for good |
| `ドン・ポール` | **Don Paolo (Paul)** | Já dentro do restaurante, reclama de sweet time, testemunha revelação |
| `サリアス` | **Celeste (Sarrias)** | Irmã de Claire, aliviada, convoca reunião all concerned parties |
| `ディミトリー` | **Dimitri Allen** | Antagonista exposto, arma minefield, conta backstory de Bill Hawks/Claire/wormhole, descobre ter sido pawn de Clive |
| `アロマ` | **Flora Reinhold (Aroma)** | Ausente em diálogo direto, citada como refém trapped up there na mobile fortress |
| `ナゾバトル` | **Enigma Battle (System)** | Instruções do enigma Find all the bombs (grid bombs/row/col) |

Tags de controle observadas: `<V0010>`–`<V0290>` dublados em sequência contínua `12_034500`, `12_035010`, `12_035030`, `12_037000`, `12_039000`, `12_039010` (núcleo dublado mais denso do jogo); `<V00xx>` ausente em flavors e no minefield não-dublado parcial `12_035020`; `<W>` pausas longas em cheltenham e remembers; `<A1/1>`–`<A6/2>` animações; `<K>` silêncio Hmm em Future Luke e Layton; `<S671>` ausente neste capítulo (usado `<Q>` implícito no enigma bombs); placeholders `{''}` ausentes; `<×>` marcador de cutscene em `12_036000`.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Às Portas do Thames Arms — Chelmey e o Enigma Falso (`12_033590`–`12_033596`)
O grupo finalmente está a um passo do encontro marcado por Celeste e avista Chelmey. Layton convida-o para o Thames Arms e Chelmey, entre ceticismo e curiosidade, exige saber o que há no Thames Arms que seja tão urgente. Layton aposta que o que acontecerá lá levará você ao primeiro-ministro. Chelmey só resiste por estar preso a esse enigma complicado numa note que acredita ter relação com o caso, mas após Layton examinar e declarar esta carta não parece ter relevância, ele desiste do a pista se esgota e aceita seguir. Barton entremeia com cheiros deliciosos e Subject 3 faz gag parade que Luke responde com revelar o maior mistério que Londres já viu.
> Ganchos: "I need you to accompany me to the Thames Arms." / "I make no promises, but it's likely that what happens there will lead you to the prime minister."

### 3.2 Big Luke Volta — seguindo discretamente Celeste (`12_033710`–`12_033720`)
Olha! Lá está Big Luke! marca o reencontro. Future Luke explica que esteve seguindo uma mulher suspeita que seguindo você, Professor — Celeste — e que a perdeu e reencontrou entrando neste restaurante, seguida segundos mais tarde por Don Paolo. Luke adivinha o comparsa e Future Luke se diverte com I'm beginning to wonder whether I even need to explain. Com todos reunidos, Layton declara All the personagens do nosso mistério are here. I think it's time to reconvene with Celeste, e Big Luke estranha o termo Players in our mystery?.
> Ganchos: "I was doing a little investigating of my own, seguindo discretamente a suspicious woman" / "All the players in our mystery are here."

### 3.3 Dentro do Thames Arms — O Ponto de Encontro (`12_033730`–`12_033750`)
O bartender recebe com Ah, welcome back to the Thames Arms e pergunta pelo gentleman, Layton agradece. Don Paolo já instalado reclama Você certamente demorou para chegar aqui. Celeste irrompe aliviada É um alívio ver que vocês conseguiram sair all right e provoca Something tells me you've already worked most of it out, ao que Chelmey pressiona If you know something, Layton, spit it out!, e Layton inicia All concerned parties seem to be in attendance, so I'll try to explain things as best I can.
> Ganchos: "You certainly took your sweet time getting here, Layton." / "All concerned parties seem to be in attendance"

### 3.4 A Grande Revelação — London Falso, Cavern e o Lift (`12_034500`–`12_035010`)
Sequência dublada mais importante do jogo. Layton sentencia O London em que estamos, este London do futuro, é falso — Mais precisamente, é um cenário projetado para nos fazer acreditar que viajamos 10 anos para o futuro. Porque, veja, não há máquina do tempo. Não aqui, em lugar nenhum. Luke explode What?!, Future Luke silencia com Hmm, enquanto Layton explica que o back room do clock shop é no máquina do tempo, It's a lift leading down into the earth. Chelmey confirma You mean to say we're underground right now? e Layton teoriza cavernas subterrâneas que pepper the entire earth onde Dimitri built this false London — It's as if we're standing in the largest film set ever created. A motivação fecha o arco de cativeiro: He needed other cientistas to support his project, so he turned to the greatest minds, mas para mantê-los precisava que believed that they were stranded a decade from home e que a machine was their only hope of returning home. O bartender interrompe com Heh. I see you've caught on. Excellent work as always, Hershel, e Layton expõe The Family uses this establishment as a hideout, estranhando que o bartender didn't so much as raise an eyebrow. O bartender ameaça I have no choice but to shut you up for good, prenunciando Dimitri.
> Ganchos: "The London we are presently in, this London of the future, is a fake." / "The back room of the clock shop is no máquina do tempo. It's a lift leading down into the earth."

### 3.5 A Armadilha do Minefield — Bombas e o Infinito (`12_035020`)
Dimitri interrompe via voz do bartender e arma chantagem: Este restaurante está armado com explosivos suficientes para arrasar o local... E eles estão ticando. Ordena fiquem exatamente onde estão, avisa Um passo em falso e...BUM! e provoca Exato. Agora vou observar vocês se contorcerem um pouco mais. Layton finge rendição Well then, it would seem that you've bested me, Dimitri e aceita o paper que tells you all you need to know about the bombs. O enigma Find all the bombs (row/col numbers, red dots/tables sem bombas) é disfarce para o timer. Luke lê 00! The bombs are going to blow!, Dimitri silencia com <K>..., mas Layton corrige This isn't 00. This is the symbol for infinity. The bombs are never going to go off... because there are no bombs — It's true you've done some evil things, but you're not a killer. You just wanted to keep us busy. Dimitri insiste Before you take what might be your last step, I'd check my numbers again, Hershel.
> Ganchos: "This restaurant is rigged with enough explosives to level the place..." / "This is the symbol for infinity. The bombs are never going to go off... because there are no bombs."

### 3.6 O Passado de Dimitri — Bill Hawks, Claire e o Buraco de minhoca (`12_035030`–`12_037000`)
Dimitri cede Eu deveria saber que não te enganaria, Hershel e narra a origem há 10 anos: com Bill Hawks amigos...colegas pesquisando viagem no tempo, built prototype e debate sobre usar Claire as first test subject — I loved her too —, oposição veemente, flaw noticed, Bill refused to postpone. Revela que Unbeknownst to me, Bill had made a deal to sell the technology behind the machine's power source a large corporation por very impressive sum, sabendo que a máquina wasn't ready mas precisava demonstrate viability, com tragic results. Cutscene de Dimitri rushing to the lab com Bill wounded e Claire dead. Depois, Because of Bill's greed, Claire was lost to me forever. In the blink of an eye, I lost my life's work and love, enquanto Bill made full recovery, completed the deal e climbed the political ladder to the very top — He killed Claire and was rewarded with the most powerful seat. Amargo, voltou à pesquisa para travel to the past, rob Bill of all that he had won e save Claire. Layton fecha com Claire is no longer with us. There's nothing anyone can do, e lança a bomba Someone's been using you as a pawn.
> Ganchos: "Bill thought we should use Claire as the first test subject." / "He killed Claire and was rewarded with the most powerful seat in government."

### 3.7 O Verdadeiro Mentor — Clive Desmascarado (`12_039000`–`12_039010`)
Layton vira-se para Future Luke: Não, não há engano aqui. E não dá mais para esconder, Luke. Ou devo chamá-lo de Clive? Clive silencia <K>..., Dimitri balbucia Wh-what is he talking about, Clive?, e Layton acusa Você manteve suas verdadeiras intenções escondidas from everyone, Clive. Even your partner, Dimitri. Clive admite Tremendous work, Professor! You've found me out. Layton reconstrói: Clive lived next door to the lab que exploded, blast demolished half of the building, 10 people were killed, two of whom were your parents — In the span of a few segundos, you lost family and home, anger virou obsession com revenge. Adotado por kindly Constance Dove que possuia enormous fortune, herdou tudo após 5 years, trabalhou em prominent newspaper não por pocket money mas searching, hunted down both Bill Hawks and Dimitri. Concocted plan: befriended Dimitri e convinced resume research, used inheritance to set up this elaborate facsimile of London, used press contacts para lure brilliant men, mas unbeknownst to Dimitri, most staff were not working on the máquina do tempo. Clive had secretly reassigned many to a different project — his pet project. Chelmey cobra What was the second project? e Layton responde A weapon designed to cause destruction on an unimaginable scale. Dimitri gagueja A weapon?! Is this true, Clive?.
> Ganchos: "Or should I call you Clive?" / "A weapon designed to cause destruction on an unimaginable scale."

### 3.8 A Fortaleza Móvel — Flora Refém (`12_040010`–`12_041010`)
Revelação interrompida por urgência: Luke alerta Professor, o que vamos fazer? Ele está com Flora e Don Paolo grita Layton, look over there!. O horror materializa quando Luke pergunta Professor, o que é aquela coisa?! e Layton constata Parece que Clive esteve trabalhando em uma espécie de...fortaleza móvel. Luke fecha Flora's trapped up there. We've got to save her!.
> Ganchos: "It seems Clive's been working on some sort of...mobile fortress." / "Flora's trapped up there. We've got to save her!"

> **Cliffhanger:** Layton prova que o futuro é um set cavernoso acessado por lift, desarma o blefe infinito de Dimitri e expõe que Bill Hawks vendeu a máquina ainda falha para financiar ascensão ao poder; mas o fio revela o verdadeiro arquiteto — Clive, órfão da explosão adotado por Constance Dove, que usou Dimitri como pawn para erguer London falso e construir em segredo uma arma/fortaleza móvel onde agora mantém Flora refém.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag)` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes.

### `12_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `12_033590.lbin.txt` — Avistamento do inspector

*   **ルーク** (Luke Triton):  
    `<T>Hey look! There's the inspector!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>How fortunate. I would very much like him to join us at the Thames Arms.`

### `12_033593.lbin.txt` — Chelmey, o puzzle e o Thames Arms

*   **チェルミー** (Inspector Chelmey):  
    `<T>Ah, Layton. Any breakthroughs in your investigation?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Possibly, Inspector. In fact, I'm very glad to see you. I need you to accompany me to the Thames Arms.`
*   **チェルミー** (Inspector Chelmey):  
    `<T>The Thames Arms?`
*   **バートン** (Constable Barton):  
    `<T>My investigation of those premises revealed delicious smells, sir.`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A3/5>Be quiet for just a minute, will you, Barton?`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A3/1>What is there at the Thames Arms that's so amazing that I need to head there this very instant?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>I make no promises, but it's likely that what happens there will lead you to the prime minister.`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A2/5>Really now?<W> <A2/1>Hmm... Well, my interest is piqued. But there's the matter of this blasted puzzle...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>What puzzle?`
*   **チェルミー** (Inspector Chelmey):  
    `<T>It's in this note I found. I have a feeling it could have some bearing on the case.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Would you mind if I had a look at it, Inspector?`
*   **チェルミー** (Inspector Chelmey):  
    `<T>No luck? Well, I'm afraid I'm stuck here until I get this puzzle solved.`
*   **チェルミー** (Inspector Chelmey):  
    `<T>I'm sure there's a useful clue to be found in this note, if only I could solve the puzzle.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm sorry, Inspector, but this letter doesn't appear to have any relevance to your case.`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A2/5>Oh. Well, isn't that just wonderful! Another prospective lead fizzles out.<A3/5> I'm at my wits' end, I tell you.`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A3/1>Whatever you've got to show me at the Thames Arms, it has to be more useful than that note.`

### `12_033594.lbin.txt` — Flavor Barton

*   **バートン** (Constable Barton):  
    `<T>Please help the inspector with that puzzle. He's been stuck on it for ages and he's in a foul mood.`

### `12_033596.lbin.txt` — Flavor Subject 3

*   **３号** (Subject 3):  
    `<T>That's quite a gang you've got there. You starting a parade or something?`
*   **ルーク** (Luke Triton):  
    `<T>Nope. We're just on our way to blow the lid off the biggest mystery London's ever seen!`
*   **３号** (Subject 3):  
    `<T>Sounds great. You have fun with that.`

### `12_033710.lbin.txt` — Flavor Big Luke

*   **ルーク** (Luke Triton):  
    `<T>Look! There's Big Luke!`

### `12_033720.lbin.txt` — Reencontro com Future Luke

*   **未来ルーク** (Future Luke / Big Luke):  
    `<T><A2/2>I'm so glad we're finally able to meet again.`
*   **ルーク** (Luke Triton):  
    `<T>Where did you run off to?`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T>I was doing a little investigating of my own, shadowing a suspicious woman I'd seen around town.`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T>I saw her tailing you, Professor, and decided someone had to find out who she was.`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>Oh! You must be talking about Celeste!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>And? Where did you last see her?`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T><A1/1>I lost her for a while, but I just saw her again, walking into this restaurant.`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T><A1/2>Seconds later, I saw a friend of ours go in as well.`
*   **ルーク** (Luke Triton):  
    `<T>Oh, let me guess. Don Paolo!`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T><A1/4>I'm beginning to wonder whether I even need to explain. You seem to know it all already!`
*   **ルーク** (Luke Triton):  
    `<T><A4/2>Well, we've been hard at work investigating too!`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T><A1/2>Of course. I never expected you to just wait idly for me to return.<W> So, now what?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>All the players in our mystery are here. I think it's time to reconvene with Celeste.`
*   **未来ルーク** (Future Luke / Big Luke):  
    `<T>Players in our mystery?<W> What does that mean...?`

### `12_033730.lbin.txt` — Bartender

*   **レイトン** (Professor Hershel Layton):  
    `<T>Hello there. We were in the area and thought we'd drop by again.`
*   **バーテン** (Bartender):  
    `<T>Ah, welcome back to the Thames Arms. Did you ever find the gentleman you were looking for?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Oh yes - thanks to you, of course.`
*   **バーテン** (Bartender):  
    `<T>Well, I'm glad to hear that.`

### `12_033740.lbin.txt` — Don Paolo no Thames Arms

*   **ドン・ポール** (Don Paolo):  
    `<T>You certainly took your sweet time getting here, Layton. I thought you'd got lost or something.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Come now, Paul. You surely haven't been waiting that long, have you?`

### `12_033750.lbin.txt` — Celeste e reunião

*   **サリアス** (Celeste):  
    `<T><A2/2>Professor Layton! It's such a relief to see you made it out all right.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>Why, I could hardly let myself get caught before hearing about that secret you mentioned, could I?`
*   **サリアス** (Celeste):  
    `<T>Something tells me you've already worked most of it out for yourself. Am I right?`
*   **ルーク** (Luke Triton):  
    `<T>Huh?!<W> Professor, is that true?`
*   **チェルミー** (Inspector Chelmey):  
    `<T>If you know something, Layton, spit it out!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>All concerned parties seem to be in attendance, so I'll try to explain things as best I can.`

### `12_034500.lbin.txt` — Revelação central dublada

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>The London we are presently in, this London of the future, is a fake.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>More precisely, it's a set designed to make us believe that we've travelled 10 years into the future.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>Because, you see, there is no time machine. Not here, not anywhere.</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T><A1/6>What?!</V>`
*   **未来ルーク** (Future Luke / Big Luke) <V0050>:  
    `<V0050><K><T>Hmm.</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T><A4/3>We were all led to believe that the clock shop was a portal to the future.</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><A1/1>But the truth about that shop is, in some ways, just as bewildering.</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T>The back room of the clock shop is no time machine.<W> It's a lift leading down into the earth.</V>`

### `12_035010.lbin.txt` — Exposição cavern e scientists dublada

*   **チェルミー** (Inspector Chelmey) <V0010>:  
    `<V0010><T><A4/2>You mean to say we're underground right now?</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T><A2/1>Precisely. You may have heard of subterranean caverns, as some of them house ancient ruins.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>Some experts theorise that these caverns pepper the entire earth.</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T><A1/1>What I've seen here leads me to conclude that Dimitri used one such cavern to build this false London.</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T>It's as if we're standing in the largest film set ever created.</V>`
*   **ルーク** (Luke Triton) <V0060>:  
    `<V0060><T><A1/1>What?! I don't believe it!</V>`
*   **チェルミー** (Inspector Chelmey) <V0070>:  
    `<V0070><T><A2/1>So Dimitri is behind all this then? But why?</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T><A4/3>That question stumped me as well.</V>`
*   **チェルミー** (Inspector Chelmey) <V0090>:  
    `<V0090><T>Why would he go to such pains to make us believe we're in the future?</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T>It doesn't make sense.<W> Unless convincing people of this is the key to achieving his ultimate goal.</V>`
*   **ルーク** (Luke Triton) <V0110>:  
    `<V0110><T><A4/1>What kind of goal requires a set-up like that?</V>`
*   **レイトン** (Professor Hershel Layton) <V0120>:  
    `<V0120><T><A4/1>It's simple.</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T>It seems that Dimitri never gave up his original dream of building a time machine.</V>`
*   **レイトン** (Professor Hershel Layton) <V0140>:  
    `<V0140><T><A1/1>But though he poured all his energy into achieving this feat, the task was too large for one man.</V>`
*   **レイトン** (Professor Hershel Layton) <V0150>:  
    `<V0150><T>He needed other scientists to support his project, so he turned to the greatest minds in London.</V>`
*   **レイトン** (Professor Hershel Layton) <V0160>:  
    `<V0160><T>But to keep the scientists working for him, they needed to believe that they were in the future.</V>`
*   **ルーク** (Luke Triton) <V0170>:  
    `<V0170><T><A1/6>Why?</V>`
*   **レイトン** (Professor Hershel Layton) <V0180>:  
    `<V0180><T><A2/1>Think about it, Luke. Dimitri couldn't imprison the scientists. Not in the conventional sense.</V>`
*   **レイトン** (Professor Hershel Layton) <V0181>:  
    `<V0181><T>After all, who knows what kind of work they would produce under those circumstances?</V>`
*   **レイトン** (Professor Hershel Layton) <V0190>:  
    `<V0190><T>No, Dimitri needed a different approach to compel the scientists to complete his research.</V>`
*   **レイトン** (Professor Hershel Layton) <V0200>:  
    `<V0200><T><A1/1>The scientists had to want the time machine to work as much as Dimitri did.</V>`
*   **レイトン** (Professor Hershel Layton) <V0210>:  
    `<V0210><T>So he told them that they had been shot forward 10 years in time, stranded a decade from home.</V>`
*   **レイトン** (Professor Hershel Layton) <V0220>:  
    `<V0220><T>Dimitri misled the scientists, telling them that the time machine was an unfinished project.</V>`
*   **レイトン** (Professor Hershel Layton) <V0230>:  
    `<V0230><T>They thought they were stranded, and that the machine was their only hope of returning home.</V>`
*   **チェルミー** (Inspector Chelmey) <V0240>:  
    `<V0240><T>Ah. So that's why they were so willing to follow orders.</V>`
*   **レイトン** (Professor Hershel Layton) <V0250>:  
    `<V0250><T><A3/1>That's all I've been able to work out.<W> Perhaps our friend here can fill us in on the rest.</V>`
*   **バーテン** (Bartender) <V0260>:  
    `<V0260><T>Heh. I see you've caught on. Excellent work as always, Hershel.</V>`
*   **レイトン** (Professor Hershel Layton) <V0270>:  
    `<V0270><T>The Family uses this establishment as a hideout.</V>`
*   **レイトン** (Professor Hershel Layton) <V0271>:  
    `<V0271><T>Therefore, it seemed a bit odd that the bartender didn't so much as raise an eyebrow when we walked in.</V>`
*   **バーテン** (Bartender) <V0280>:  
    `<V0280><T>I have to give credit where it's due. I never imagined you'd work out so much of the plan yourself.</V>`
*   **バーテン** (Bartender) <V0290>:  
    `<V0290><T><A2/1>I suppose I have no choice but to shut you up for good.</V>`

### `12_035020.lbin.txt` — Minefield e puzzle das bombas

*   **チェルミー** (Inspector Chelmey):  
    `<T><A>Dimitri Allen! You've been watching us the whole time?`
*   **ディミトリー** (Dimitri Allen):  
    `<T>I wish to issue a challenge to the professor. Bumbling lawmen have no part in this conversation.`
*   **チェルミー** (Inspector Chelmey):  
    `<T>B-bumbling!<W> I'll give you bumbling!`
*   **ディミトリー** (Dimitri Allen):  
    `<T>It would be wise for you all to stay exactly where you are.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>This restaurant is rigged with enough explosives to level the place... And they're ticking.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Are you out of your mind?! We'll all die. Even you!`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/5>Me? Hah! No, I'm going to stroll out of this place.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>You see, I know exactly how long we've got left, and I know the way out.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>Oh, and if you're thinking of running away, make sure you don't tread on a bomb.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>One false step and...BOOM!`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>This place is a minefield!`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A2/6>That's right.<W> Now, I'm going to watch you squirm a bit more...`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/5>And then leave you to your fate.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>Well then, it would seem that you've bested me, Dimitri.<W> There's nothing I can do...`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A1/1>Not exactly, Professor.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>Have a look at this piece of paper. It tells you all you need to know about the bombs in this room.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Fair enough. Let's see what we have here.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><S671>Oho, well done, Professor. I shouldn't have made it so easy for you.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>You've found all the bombs. I suppose you're going to avoid getting blown up after all.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>I'd say the same, unless, of course, there was something you weren't telling me.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>What?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Luke, this paper isn't just telling us where the bombs are. It's telling us how much time we've got left...`
*   **ルーク** (Luke Triton):  
    `<T>Hmm?<W> <A1/6>Oh!`
*   **ルーク** (Luke Triton):  
    `<T>00! <W>Zero, Professor! It's all over! The bombs are going to blow!`
*   **ディミトリー** (Dimitri Allen):  
    `<T><K>...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Not so fast, Luke...`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>Nooooo!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/5>Wait, Luke. Listen.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>This isn't 00.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This is the symbol for infinity. The bombs are never going to go off... because there are no bombs.`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>What?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>That's it, Dimitri, isn't it?<W> It's true you've done some evil things, but you're not a killer.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You just wanted to keep us busy so you could make your escape.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>Before you take what might be your last step, I'd check my numbers again, Hershel.`
*   **ナゾバトル** (Puzzle Battle - System):  
    `<T>Find all the bombs. The numbers above and to the left of the map indicate the number of bombs in each column and row. Red dots indicate people and squares indicate tables. There are no bombs in these squares. Derive the location of all bombs using the information provided, and mark them on your map.`

### `12_035030.lbin.txt` — Backstory de Dimitri dublado

*   **ディミトリー** (Dimitri Allen) <V0010>:  
    `<V0010><T>I should have known I wouldn't fool you, Hershel.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>I've worked things out on my own this far, but I need you to help make sense of the rest.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>You must have had some reason for concocting a scheme this wild.</V>`
*   **ディミトリー** (Dimitri Allen) <V0040>:  
    `<V0040><T><A1/4>I...I had a very good reason.</V>`
*   **ディミトリー** (Dimitri Allen) <V0050>:  
    `<V0050><T>It all started about 10 years ago. Bill Hawks and I were friends...colleagues.</V>`
*   **ディミトリー** (Dimitri Allen) <V0051>:  
    `<V0051><T>We worked in the same lab, researching time travel.</V>`
*   **ディミトリー** (Dimitri Allen) <V0060>:  
    `<V0060><T>Our research meant everything to us.</V>`
*   **ディミトリー** (Dimitri Allen) <V0061>:  
    `<V0061><T>We poured our hearts and souls into uncovering the secrets of space and time.</V>`
*   **ディミトリー** (Dimitri Allen) <V0070>:  
    `<V0070><T><A3/5>After months of progress, we had built ourselves a prototype time machine.</V>`
*   **ディミトリー** (Dimitri Allen) <V0071>:  
    `<V0071><T>It was finally time to test our work with a human subject.</V>`
*   **ディミトリー** (Dimitri Allen) <V0080>:  
    `<V0080><T>Bill thought we should use Claire as the first test subject. She was our lab assistant.</V>`
*   **ディミトリー** (Dimitri Allen) <V0081>:  
    `<V0081><T>I, of course, vehemently opposed this idea...<W><W><W> I loved her too, you see.</V>`
*   **ディミトリー** (Dimitri Allen) <V0090>:  
    `<V0090><T>And though she didn't return my feelings, I didn't want to risk her getting hurt in the experiment.</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T><K>Hmm.</V>`
*   **ディミトリー** (Dimitri Allen) <V0110>:  
    `<V0110><T><A1/1>Around this time, I noticed a flaw in the design of our machine.</V>`
*   **ディミトリー** (Dimitri Allen) <V0111>:  
    `<V0111><T>I begged Bill to postpone the experiment, but he wouldn't hear of it.</V>`
*   **ディミトリー** (Dimitri Allen) <V0120>:  
    `<V0120><T>Sometime after the accident, I made a startling discovery.</V>`
*   **ディミトリー** (Dimitri Allen) <V0121>:  
    `<V0121><T>Unbeknownst to me, Bill had made a deal to sell the technology behind the machine's power source.</V>`
*   **ディミトリー** (Dimitri Allen) <V0122>:  
    `<V0122><T>Apparently, a large corporation had offered him a very impressive sum.</V>`
*   **ディミトリー** (Dimitri Allen) <V0130>:  
    `<V0130><T>Bill knew the machine wasn't ready for a human subject, but he needed to demonstrate its viability.</V>`
*   **ディミトリー** (Dimitri Allen) <V0140>:  
    `<V0140><T><A1/4>We all know the tragic results of his decision.</V>`

### `12_035035.lbin.txt` — Flavor pós-backstory 1

*   **レイトン** (Professor Hershel Layton):  
    `<T>Dimitri hasn't told us everything. Let's hear what else he has to say.`

### `12_036000.lbin.txt` — Cutscene movie

*   **×** (System / Movie):  
    `Movie of Dimitri rushing to the lab after the explosion. Bill wounded and Claire dead.`

### `12_037000.lbin.txt` — Consequências e amargura dublada

*   **ディミトリー** (Dimitri Allen) <V0010>:  
    `<V0010><T>Because of Bill's greed, Claire was lost to me forever.</V>`
*   **ディミトリー** (Dimitri Allen) <V0020>:  
    `<V0020><T>Life is full of cruel twists.</V>`
*   **ディミトリー** (Dimitri Allen) <V0030>:  
    `<V0030><T>In the blink of an eye, I lost my life's work and the love of my life.</V>`
*   **ディミトリー** (Dimitri Allen) <V0031>:  
    `<V0031><T>To say I was a broken man would be an understatement.</V>`
*   **ディミトリー** (Dimitri Allen) <V0040>:  
    `<V0040><T><A4/3>Bill, on the other hand, made a full recovery from his injuries.</V>`
*   **ディミトリー** (Dimitri Allen) <V0041>:  
    `<V0041><T>He also completed the deal with the corporation, pocketing more money than most people see in a lifetime.</V>`
*   **ディミトリー** (Dimitri Allen) <V0050>:  
    `<V0050><T>He used his new-found fortune to climb the political ladder to the very top.</V>`
*   **ディミトリー** (Dimitri Allen) <V0060>:  
    `<V0060><T><A1/1>He killed Claire and was rewarded with the most powerful seat in government.</V>`
*   **ディミトリー** (Dimitri Allen) <V0061>:  
    `<V0061><T>If that's not a cruel joke, I don't know what it is.</V>`
*   **ディミトリー** (Dimitri Allen) <V0070>:  
    `<V0070><T>I can't pretend I wasn't bitter, and it was this bitterness that sent me back to my research.</V>`
*   **ディミトリー** (Dimitri Allen) <V0071>:  
    `<V0071><T>I thought that if I could travel to the past, I could rob Bill of all that he had won.</V>`
*   **ディミトリー** (Dimitri Allen) <V0080>:  
    `<V0080><T>Though of course, there was another reason why I wanted to go back in time.</V>`
*   **ディミトリー** (Dimitri Allen) <V0081>:  
    `<V0081><T>To save Claire from her fate.<W> Surely you understand, Hershel?</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T><K>...<W><W></K></T><TW><A1/1>Claire is no longer with us. There's nothing anyone can do to turn back time.</V>`
*   **ディミトリー** (Dimitri Allen) <V0100>:  
    `<V0100><T>Do you really believe that?</V>`
*   **レイトン** (Professor Hershel Layton) <V0110>:  
    `<V0110><T><A4/3>I don't want to, but I do.<W><W> <A4/1>I have just one more question for you.</V>`
*   **ディミトリー** (Dimitri Allen) <V0120>:  
    `<V0120><T><A4/3>What is it?</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T><A1/1>Someone's been using you as a pawn. <W>Are you aware of this?</V>`
*   **ディミトリー** (Dimitri Allen) <V0140>:  
    `<V0140><T>What are you talking about?</V>`

### `12_039000.lbin.txt` — Desmascaramento de Clive dublado

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>No, there's no mistake here. And there's no hiding it any more, Luke.<W><W> Or should I call you Clive?</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0020>:  
    `<V0020><T>Huh?!</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>It took some time to put together the pieces of your plan.</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>But when I finally understood it all, the sheer evil of it sent a chill down my spine.</V>`
*   **ディミトリー** (Dimitri Allen) <V0050>:  
    `<V0050><T>Wh-what is he talking about, Clive?</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0060>:  
    `<V0060><T><A1/4><K>...</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T>You kept your true intentions hidden from everyone, Clive. Even your partner, Dimitri.</V>`
*   **ディミトリー** (Dimitri Allen) <V0080>:  
    `<V0080><T>What are you saying, Hershel?</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0090>:  
    `<V0090><T><A1/1>Ahh...</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T>Clive was aiming for revenge on a massive scale and you were nothing more than a pawn, Dimitri.</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0110>:  
    `<V0110><T><A2/6>Tremendous work, Professor! You've found me out.</V>`
*   **チェルミー** (Inspector Chelmey) <V0120>:  
    `<V0120><T>Stop speaking in riddles, Layton! What's this all about?</V>`

### `12_039010.lbin.txt` — História completa de Clive dublada

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>Clive, you lived next door to the lab that exploded 10 years ago. You were just a child then.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>That blast demolished half of the building you lived in.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>Reports indicate that 10 people were killed in the explosion, two of whom were your parents.</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>It must have been a terrible shock.<W> In the span of a few seconds, you lost your family and your home.</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T>When the initial shock wore off, it was replaced with anger.</V>`
*   **レイトン** (Professor Hershel Layton) <V0051>:  
    `<V0051><T>You became obsessed with exacting revenge on those who had wronged you.</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0060>:  
    `<V0060><T><K><A4/1>...</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><A3/1>You were lucky enough to be adopted by a kindly woman in her golden years, Constance Dove.</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T>Miss Dove's extreme kindness was matched in scale only by the enormous fortune she possessed.</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T><A1/1>You two lived quite happily as a family for a time.<W> Sadly, it wasn't to last.</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T>Miss Dove departed from this world five short years later, leaving her fortune to you.</V>`
*   **レイトン** (Professor Hershel Layton) <V0110>:  
    `<V0110><T>Before long, you graduated from secondary school and took a part-time job at a prominent newspaper.</V>`
*   **レイトン** (Professor Hershel Layton) <V0120>:  
    `<V0120><T>Considering your sizeable inheritance, I don't think you took the job for pocket money.</V>`
*   **レイトン** (Professor Hershel Layton) <V0121>:  
    `<V0121><T>You were searching for something.</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T>Using the newspaper's resources, you finally hunted down the men responsible for your misery.</V>`
*   **レイトン** (Professor Hershel Layton) <V0140>:  
    `<V0140><T>You knew that both Bill Hawks and Dimitri Allen were responsible for the explosion.</V>`
*   **レイトン** (Professor Hershel Layton) <V0150>:  
    `<V0150><T>Armed with this information, you concocted a plan to avenge your parents.</V>`
*   **レイトン** (Professor Hershel Layton) <V0160>:  
    `<V0160><T><A2/1>First, you befriended Dimitri and convinced him to resume his research on the time machine.</V>`
*   **レイトン** (Professor Hershel Layton) <V0170>:  
    `<V0170><T>Then you used your inheritance to set up this elaborate facsimile of London.</V>`
*   **レイトン** (Professor Hershel Layton) <V0180>:  
    `<V0180><T>With your stage in place, you used your contacts in the press to find the best scientists in the country.</V>`
*   **レイトン** (Professor Hershel Layton) <V0190>:  
    `<V0190><T>After all, you would need quite a bit of help to complete this time machine.</V>`
*   **レイトン** (Professor Hershel Layton) <V0200>:  
    `<V0200><T>You then proceeded to lure these brilliant men into your trap.</V>`
*   **レイトン** (Professor Hershel Layton) <V0210>:  
    `<V0210><T>However, unbeknownst to Dimitri, most of your staff were not working on the time machine.</V>`
*   **ディミトリー** (Dimitri Allen) <V0220>:  
    `<V0220><T>Wh-what?</V>`
*   **クラウス（帽子あり）** (Clive (with hat)) <V0230>:  
    `<V0230><T><K>...</V>`
*   **レイトン** (Professor Hershel Layton) <V0240>:  
    `<V0240><T>Clive had secretly reassigned many of the scientists to a different project.</V>`
*   **レイトン** (Professor Hershel Layton) <V0250>:  
    `<V0250><T>You might think of it as his pet project.</V>`
*   **チェルミー** (Inspector Chelmey) <V0260>:  
    `<V0260><T>We don't have all day, Layton! What was the second project?</V>`
*   **レイトン** (Professor Hershel Layton) <V0270>:  
    `<V0270><T>A weapon designed to cause destruction on an unimaginable scale.</V>`
*   **ディミトリー** (Dimitri Allen) <V0280>:  
    `<V0280><T>A weapon?! Is this true, Clive?</V>`

### `12_040010.lbin.txt` — Flora refém

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Professor, what are we going to do? He has Flora and-`
*   **ドン・ポール** (Don Paolo):  
    `<T><A3/5>Layton, look over there!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Where?`

### `12_041010.lbin.txt` — Revelação da mobile fortress

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Professor, what is that thing?!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It seems Clive's been working on some sort of...mobile fortress.`
*   **ルーク** (Luke Triton):  
    `<T>Flora's trapped up there. We've got to save her!`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `12_033593` | **Chelmey's Note Enigma (irrelevante)** | Note que Chelmey acredita ser clue, Layton examina e declara no relevance; portão para aceitar ir ao Thames Arms |
| `12_034500`–`12_035010` | **London Fake Exposition (lore, sem enigma)** | Sequência dublada core: no time machine, clock shop lift, cavern, largest film set, scientists enganados 10 years como motivação |
| `12_035020` | **Find all the bombs — Minefield Enigma** | Grid enigma estilo Battleship com row/col numbers, red dots/tables sem bombas; twist narrativo: 00 é infinity, no bombs, bluff para fuga de Dimitri `<S671>` implícito |
| `12_035030`–`12_037000` | **Dimitri Backstory Exposition (lore)** | Explosão há 10 anos, Bill Hawks vende power source, flaw, Claire morte; movie `12_036000` mostra rushing; amarração com Cap. 11 (political suppression, hospital) |
| `12_039000`–`12_039010` | **Clive Reveal Exposition (lore)** | Desmascaramento: órfão, Constance Dove inheritance, newspaper hunt, befriended Dimitri, facsimile London, reassigned scientists para weapon |
| `12_040010`–`12_041010` | **Mobile Fortress Reveal (evento)** | Primeiro vislumbre da arma de Clive, Flora trapped up there, setup para dungeon final |
| `12_033720` | **Shadowing Celeste (evento)** | Big Luke explica ter seguido Celeste tailing Layton, conecta thread de Celeste do Cap. 11 |
| `12_035010` lore | **Thames Arms = Family Hideout** | Bartender sem reação revela Family establishment; payoff da decodificação Old Father's embrace do Cap. 11 |

**Eventos narrativos sem enigmas diretos:** convite a Chelmey (`033590`), Subject 3 parade gag (`033596`), reencontro Big Luke (`033710`), bartender welcome (`033730`), Don Paolo sweet time (`033740`), Celeste reúne all concerned parties (`033750`), flavor Dimitri hasn't told everything (`033535`), checagem de numbers again de Dimitri.

---

## 6. Notas de Localização & Observações Técnicas

*   **Capítulo mais dublado do endgame:** 7 dos 21 arquivos são totalmente dublados (`034500`, `035010`, `035030`, `037000`, `039000`, `039010` + parte de `035020` não-dublada quebra padrão). Densidade vocal só comparável ao Cap. 09 top-floor e marca virada de investigação para exposição — não há enigmas de exploração entre `034500` e `039010` além do minefield.
*   **London fake como retcon geográfico:** A solução `It's a lift leading down into the earth` recontextualiza todo o `future London` desde o Prólogo/Cap. 05 (clock shop) e usa caverns de ancient ruins como technobabble já plantado; largest film set amarra wet shoes/túnel do Cap. 10 e materials/dangerous stuff do Cap. 11 como cenografia cavernosa.
*   **Infinito vs 00:** O truque `00` → `infinity` do minefield (`035020`) é enigma diegético que prova tese de Layton de que Dimitri não é killer, reforçando arco moral de Dimitri desde o Pagoda (ends justify the means) e permitindo sua sobrevivência para confrontar Clive.
*   **Clive = Future Luke com chapéu:** Tag `クラウス（帽子あり）` (Clive com chapéu) confirma que Big Luke era identidade adotada por Clive; herança de Constance Dove explica escala da facsimile e newspaper job justifica acesso a scientists — elo direto com orphaned child wailing do Cap. 11 e suppressed reports do laboratório.
*   **Two projects payoff:** `12_039010` `most of your staff were not working on the time machine / weapon... unimaginable scale` fecha foreshadow de `11_033350` The materials they have here... e `11_033390` dangerous stuff separado, revelando que a time machine era isca para motivar scientists enquanto Clive construía mobile fortress.
*   **Structure preservation:** Diálogo mantido em inglês UK original; nomes `Thames Arms`, `Old Father Thames`, `Family`, `Bill Hawks`, `Constance Dove` preservados; `Hershel`/`Clive`/`Dimitri` usados conforme LSCR; `× / Movie` de `036000` mantido como cutscene marker sem texto jogável.

