# Capítulo 11 — Infiltração no Laboratório de Dimitri, Celeste e o Abraço do Velho Pai | Professor Layton and the Unwound Future

> **Capítulo 11 — Infiltração no Laboratório Subterrâneo / Celeste e o Segredo da Explosão** — Análise de dump LSCR para `Textos Originais/txt/uk/11/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/11/`
> Total de arquivos escaneados: **28**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão, `<J>` = jump

---

## 1. Arquivos Cobertos

Todos os 28 dumps `.lbin.txt` em `uk/11`:

```
11_000000.lbin.txt  — [vazio - apenas cabeçalho]
11_033310.lbin.txt  — Chegada ao facility, main gate indiscreto, busca por entrada discreta
11_033320.lbin.txt  — Luke acha fenda, Flora acha scrap de papel puzzle, quem deixou mensagem?
11_033330.lbin.txt  — Reencontro com Don Paolo nas sombras, como cruzou o Thames, flying machine ropey, puzzle J54
11_033340.lbin.txt  — Disputa da escada: quem desce primeiro, Captain Obvious vs nimblest/monkey, gentleman debate, puzzle decide Luke
11_033345.lbin.txt  — Flavor: ladder para dentro do facility
11_033350.lbin.txt  — Passagem subterrânea de materiais para o Thames, Don Paolo expert, Layton repara em materiais suspeitos
11_033360.lbin.txt  — Metal shutter trancado com puzzle lock, Flora avisa sobre life of crime
11_033370.lbin.txt  — Encontro com Hollis (Horace): rescue, Dimitri Allen, real Professor Layton, guards vindo
11_033380.lbin.txt  — Walmy/Walton de castigo no freeze, 10 hours shift, Bostro knock block off
11_033390.lbin.txt  — Neutralização dos guardas (não-violenta via puzzle), central research room, materiais não são da time machine - grupo separado com dangerous stuff
11_033400.lbin.txt  — Flavor: move on before regain consciousness
11_033410.lbin.txt  — Craig (Cuthbert) escocês, Horace apresenta real Layton, go back to our own time, infrared sensor, Bostro intruders
11_033420.lbin.txt  — Porta do central research room, puzzle lock de Dimitri
11_033500.lbin.txt  — Bostro armadilha dublado: 'Old it, sneaky sneaks, Narration Quickly Follow me! (resgate Celeste)
11_033510.lbin.txt  — Fuga: Through here, everyone!
11_033512.lbin.txt  — Revelação dublada: Who are you? Claire? No, Celeste younger sister
11_033514.lbin.txt  — Celeste estranged, tailing Layton, reputação solve any puzzle, split up Don Paolo escorta, segredo defies imagination, old father's embrace
11_033516.lbin.txt  — Celeste dublada: answer lies in the old father's embrace! meet next
11_033520.lbin.txt  — Bostro perseguição: Stay where you are!
11_033530.lbin.txt  — Flavor: need to leave facility immediately
11_033540.lbin.txt  — Flavor: can't head back that way
11_033545.lbin.txt  — Phew made it, Luke obcecado com last thing Celeste said
11_033550.lbin.txt  — Decodificação dublada: Old Father Thames, Thames Arms, embrace = arms
11_033555.lbin.txt  — Exposição longa: Layton conta explosão, lab em chamas, flats destruído, orphaned child, media suppressed, assault hospital month, office torn, one other person
11_033559.lbin.txt  — Pavel (Polo) perdido, compass kaputt, train tracks peril, mapa puzzle
11_033560.lbin.txt  — Pavel pós-puzzle: graças, compass, find way out
11_033565.lbin.txt  — We've given Family the slip, Thames Arms just up road
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `11_000000.lbin.txt`. `11_033345`/`11_033530`/`11_033540`/`11_033400` são flavors curtos de transição.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 11 |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Protagonista, deduz entrada discreta, repara em materiais suspeitos, resgata Hollis, neutraliza guardas sem violência, decodifica Old Father Thames, expõe explosão e perseguição política |
| `ルーク` | **Luke Triton** | Aprendiz, acha fenda, disputa escada com Paolo (nimblest), quebra enigma locks, reflete sobre Claire e old father's embrace |
| `アロマ` | **Flora Reinhold (Aroma)** | Encontra scrap de papel e resolve enigma, repreende Paolo sobre gentleman, avisa sobre life of crime, corre na fuga |
| `ドン・ポール` | **Don Paolo (Paul)** | Reaparece nas sombras à frente do grupo, nega revelar como cruzou o Thames (flying machine), disputa liderança da escada, defende secret research, quer escortar Celeste |
| `ホリス` | **Hollis / Horace (Scientist)** | Cientista cativo, assustado, aliviado ao saber real Layton, confirma Dimitri Layton fake, guia ao central research room, revela two research groups e dangerous stuff separado |
| `ワルートン` | **Walton / Barmey (Family - small)** | De castigo no freeze, lamenta school, reclama de rat |
| `ワルミー` | **Walmy (Family - large)** | Irmão maior, explica punishment, ameaça Bostro knock block off, 10 hours shift |
| `クレイグ` | **Cuthbert / Craig (Scottish)** | Escocês de sotaque (Whit's, doon, Ah'd), amigo de Horace, quer voltar a our own time, indica corridor, avisa Bostro + infrared sensor |
| `ボストロ` | **Bostro (Family lieutenant)** | Arma armadilha na central room, persegue intruders, grita 'Old it right there! |
| `サリアス` | **Celeste (Sarrias) — Claire's younger sister** | Resgatadora misteriosa, idêntica a Claire, revela ser irmã mais nova estranged, tailing Layton por reputação, dá pista codificada old father's embrace, split do grupo |
| `ナレーション` | **Narration** | Voz de resgate Quickly! Follow me! / Through here! |
| `ポーロ` | **Pavel / Polo (Explorer)** | Explorador poliglota perdido, compass kaputt, cavern exploration, train tracks viaje, pede ajuda com mapa enigma |
| `３号`/`オウム` | **Subject 3 / Parrot <N1>** | Ausentes neste capítulo (sem menção) |

Tags de controle observadas: `<V0010>`–`<V0060>` dublados em `11_033500`, `11_033512`, `11_033550`, `11_033516`; `<J54><Q><K>` enigma trigger em 11_033330; `<W>` pausas; `<A1/1>`–`<A7/0>` animações; `<K>` silêncio tenso em 033330 e 033390; placeholders `{''}` ausentes (exceto {''}ropey{''} implicito); `CELL NOT USED` em 11_033390 final.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Chegada ao Laboratório — A Entrada Discreta e o Bilhete de Flora (`11_033310`–`11_033320`)
O grupo chega à margem oposta do Thames após o túnel do Cap. 10 e Layton descarta a main portão como suicídio tático. Luke propõe procurar com cuidado e logo acha uma fenda para se espremer pela passagem, mas é Flora quem de fato entrega o avanço: nota um pequeno pedaço de papel preso na parede. O bilhete é um fechadura de enigma e Flora assume a solução com energia rara, comemorando quem sabe o que teria acontecido conosco se eu não tivesse resolvido aquele enigma?!. Layton agradece mas fecha com suspeita que ecoa todo o capítulo: quem poderia ter deixado aquela mensagem ali para facilitar a infiltração.
> Ganchos: "I don't think this is the kind of place we can stroll into through the main gate." / "Who could have left this message here?"

### 3.2 Don Paolo na Sombra — Como Ele Cruzou Primeiro (`11_033330`)
Do outro lado da fenda surge a voz conhecida de Don Paolo, que cobra ter resolveu meu enigma e reclama da falta de susto de Luke. Layton estranha a velocidade da travessia e Paolo ironiza sobre verdadeiros cavalheiros guardam seus segredos, bloqueando o assunto da flying machine ropey que Luke insinua. A cena estabelece que Paolo, agora aliado relutante, age em paralelo desde a fuga do Pagoda e já conhece o facility, preparando sua pose de expert no subterrâneo.
> Ganchos: "About time! I'm glad to see you had enough brains to solve your way through my puzzle." / "True gentlemen keep their secrets."

### 3.3 A Escada — Quem Desce Primeiro (`11_033340`–`11_033345`)
Na escada Paolo invoca Capitão Óbvio para ir à frente e Luke rebate ser mais jovem e mais ágil. Paolo devolve ser ágil te faz um macaco. Flora lembra que disfarçado Paolo foi educado e razoável e ele explica quando interpreto um papel eu imito cada nuance, inclusive phoney gentleman act do hypocrite Layton. Flora defende He's not acting like a gentleman. He IS a gentleman! e o impasse vira enigma: Luke vence e ouve Perhaps your head's not as empty as it looks. You can go down first.
> Ganchos: "He's not acting like a gentleman. He IS a gentleman!" / "If the brat solves it, he can go first."

### 3.4 No Subterrâneo — Passagem e Shutter (`11_033350`–`11_033360`)
Luke dá área livre e Paolo se gaba: clássica passagem subterrânea para transportar materiais de pesquisa que aposto que leva de volta até o Thames e Ninguém faz pesquisa secreta como Don Paolo!. Layton trava nos materiais: Os materiais que eles têm aqui. Parecem... Não, devo estar enganado. O shutter traz fechadura de enigma e Flora adverte I hope you didn't enjoy cracking that lock too much. It could lead you to a life of crime!
> Ganchos: "Nobody does secret research like Don Paolo!" / "The materials they have here. They look like..."

### 3.5 Hollis e os Guardas — Resgate e Dois Grupos de Pesquisa (`11_033370`–`11_033400`)
Atrás do shutter surge Hollis: Wh-what are you all doing down here?. Layton sussurra resgate e expõe capturado pela Family - ou melhor, por Dimitri Allen. Hollis só acredita ao ouvir I am the real Professor Layton e reage Goodness, you can't imagine how shocked I was when I found out that Layton was actually Dimitri. Teme what the Family would do se espalhar a verdade e manda Hide! quando ouve os guardas. Cut para Walmy/Walton de castigo no deep freeze por messed up, com 10 hours till shift ends sob ameaça de Bostro. Layton propõe turn a blind eye com método que não é seu usual style but desperate times; após enigma Hollis constata Crikey, I bet they didn't see that coming. They'll be out cold e Layton pondera Yes. I'm not one to condone violence, but needs must. Hollis revela o twist: ele é de polydimensional physics na máquina do tempo, mas os materiais do corredor pertencem a separate research group that tinker with some pretty dangerous stuff que Dimitri pouco liga, antes de guiar Well, if he's here, he'll probably be in the central research room.
> Ganchos: "I am the real Professor Layton. Dimitri has been using my good name" / "They belong to a separate research group... some pretty dangerous stuff."

### 3.6 Cuthbert/Craig — Voltar ao Nosso Tempo e o Sensor Infravermelho (`11_033410`–`11_033420`)
Hollis leva-os a Cuthbert (Craig), que irrompe em escocês Whit's with all this racket, Horace? Who are these folk?. Horace o abrevia para The real Professor Layton, Craig duvida com o que quer dizer, o verdadeiro Professor Layton?, e Horace corta por falta de tempo. Ao ouvir que vieram help us get out of here for good e You DO want to go back to our own time, Craig explode Oor own time?! Aye, Ah'd do anything tae get back there e indica que a central room é just a wee bit doon the corridor, pedindo que partam antes que Bostro and his boys, que gin about intruders, os peguem. Luke estranha a rapidez da detecção e Paolo, expert, deduz We probably tripped an infrared sensor. Basic secret base stuff. O último obstáculo antes da sala é a porta com strange lock: Another enigma, I suspect. Dimitri no doubt wishes to test the intelligence of all those who enter.
> Ganchos: "You DO want to go back to our own time, don't you?" / "We probably tripped an infrared sensor."

### 3.7 A Armadilha de Bostro e o Resgate por Celeste — A Irmã de Claire (`11_033500`–`11_033516`)
Porta aberta e Bostro encurrala: Aha! So this is where you sneaky sneaks 'ave been 'iding. There'll be no getting away! Luke grita Estamos presos! e voz sem nome corta Rápido! Sigam-me! / Por aqui, todos!. Na sala ao lado Layton balbucia Claire? Is it you?, Paolo confirma My eyes must be playing tricks on me! e ela corrige No. I'm Celeste, her younger sister. I've been trying to uncover what really happened to Claire. Layton estranha Claire never mentioned having a sister e Celeste explica greatest regret estranged e medo de attract unwanted attention from the Family, além de ter tailing a investigação dele porque great Professor Layton can solve any enigma. Interrompida por Oh no! The Family will be here any second!, Celeste impõe We can't move quickly in a big group e ordena split: Paolo a escolta, Layton you take the kids!. Antes de sumir deixa Professor, this city hides a secret so large it defies the imagination. The answer to everything lies in the abraço do velho pai! It is there we will meet next!
> Ganchos: "No. I'm Celeste, her younger sister." / "The answer to everything lies in the old father's embrace!"

### 3.8 Fuga, Decodificação e a Verdade da Explosão (`11_033520`–`11_033565`)
Bostro volta com Aha! Found you! e Layton ordena Luke, Flora, we have to run! / Precisamos deixar esta instalação imediatamente! Fora, Luke rumina last thing Celeste said e Layton decodifica o código como enigma: Celeste estava claramente tentando nos dar uma dica, Luke nota She used a code, e Layton conecta à flyer do Thames Arms: Rivers are often personified... Velho Pai Thames... The father she was talking about was Velho Pai Thames e Luke fecha And an embrace happens in someone's arms. In this case, the arms of the Thames!. Layton aposta ser também Family HQ. Em seguida Luke puxa o fio Claire - you, Dimitri and Don Paolo all have a personal tie... many mysteries lead back to that explosion? Layton cala com <K>... e entrega monólogo: lab em flames, block of flats destroyed, entire area devastated, I knew Claire was lost to me forever, orphaned child wailing for his parents, shocked grief, mas Despite the scale... there was no follow-up coverage e powerful political forces suppressed reports. Logo depois foi viciously assaulted, hospital for a month, office torn apart, information stolen. Conclui That explosion was no ordinary accident. Someone with serious political clout was involved, tentativas seguintes só deram resistance and threats, mas Claire is lost to me forever, I must know the truth. Há Dimitri and perhaps one other person que sabe, e encerra Everything will become clear at the Thames Arms. Epílogo traz Pavel perdido I...am lost, train tracks peril, compass kaputt e map enigma, fechando com We've given the Family the slip. Thames Arms is just up the road.
> Ganchos: "The father she was talking about was Old Father Thames." / "Despite the scale of the damage, there was no follow-up coverage" / "I was viciously assaulted."

> **Cliffhanger:** Celeste idêntica a Claire resgata o grupo e marca encontro no Thames Arms via código Velho Pai Thames; o facility revela dois projetos distintos - máquina do tempo e pesquisas perigosas que nem Dimitri controla - mas Layton revela que a explosão que matou Claire foi abafada por poder político e lhe custou um mês no hospital, apontando para um segundo conhecedor da verdade além de Dimitri.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag)` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes.

### `11_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `11_033310.lbin.txt` — Entrada discreta

*   **レイトン** (Professor Hershel Layton):  
    `<T>I don't think this is the kind of place we can stroll into through the main gate.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Perhaps there's a more discreet entrance.`
*   **ルーク** (Luke Triton):  
    `<T>Good idea, Professor. We might find another way in if we search the area carefully.`

### `11_033320.lbin.txt` — Mensagem de Flora

*   **ルーク** (Luke Triton):  
    `<T>I think we can squeeze through here!`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Hey look, you two. There's a message scrawled here.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Oh? Where?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Right there, on that little scrap of paper stuck on the wall. See it?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Hmm, this is a tough one.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Let me have another look at this.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Ha! I did it! Who knows what would have happened to us if I hadn't solved that puzzle?!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>Your help is greatly appreciated, Flora. I do wonder who could have left this message here, though.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Who could have left this message here?`

### `11_033330.lbin.txt` — Don Paolo nas sombras

*   **ドン・ポール** (Don Paolo):  
    `<T><J54><A6/2>About time!<W> I'm glad to see you had enough brains to solve your way through my puzzle.<Q><K></J>`
*   **ルーク** (Luke Triton):  
    `<T>Oh, hi there, Don Paolo.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A2/3>{''}Hi there, Don Paolo{''}?!`
*   **ドン・ポール** (Don Paolo):  
    `<T>I'm lurking in the shadows here, boy! At least pretend to be startled, will you?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>How did you manage to get across the Thames ahead of us, Paul?`
*   **ドン・ポール** (Don Paolo):  
    `<T><A7/0>Nyeh heh heh.<A6/2> Let me tell you a little something about being a true gentleman, Layton.`
*   **ドン・ポール** (Don Paolo):  
    `<T>True gentlemen keep their secrets.<W> So don't think I'll be sharing them with you!`
*   **ルーク** (Luke Triton):  
    `<T>You probably just used that ropey flying machine of yours to-`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/1>It's not {''}ropey{''}, and I thought I'd made myself clear: the matter is not open for discussion.`
*   **ドン・ポール** (Don Paolo):  
    `<T>Tsk. Nosy brat.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Very well, Paul.<W> Now then, everyone, let's push on.`

### `11_033340.lbin.txt` — Disputa da escada

*   **ルーク** (Luke Triton):  
    `<T>This ladder's sure to take us down into the research facility.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/2>Ah yes, Captain Obvious to the rescue once again.<W> Stand aside. I'll lead the way.`
*   **ルーク** (Luke Triton):  
    `<T><A4/2>No way. I'm the youngest and the nimblest. I should go first.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/1>Being nimble doesn't make you first - it makes you a monkey!<W> Now stand aside!`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>Really, what kind of behaviour is that for an adult?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/4>Oh, Don Paolo, I'm so disappointed in you!`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>You were so polite and reasonable when you were disguised as the professor!`
*   **ドン・ポール** (Don Paolo):  
    `<T><A5/5>Of course I was. When I play a part, I mimic every nuance of the character!`
*   **ドン・ポール** (Don Paolo):  
    `<T>Right down to that hypocrite Layton's phoney gentleman act.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A3/3>That's a terrible thing to say. He's not acting like a gentleman. He IS a gentleman!`
*   **ドン・ポール** (Don Paolo):  
    `<T>Whatever.<W> Look, let's settle this debate with a puzzle. If the brat solves it, he can go first.`
*   **ドン・ポール** (Don Paolo):  
    `<T>This puzzle's too much for you, eh? Well, you are only Layton's apprentice. It makes sense.`
*   **ルーク** (Luke Triton):  
    `<T><A1/3>There's no way I'm going to admit defeat to that middling puzzle!`
*   **ルーク** (Luke Triton):  
    `<T>Let me try again!`
*   **ドン・ポール** (Don Paolo):  
    `<T>Hmph. Perhaps your head's not as empty as it looks. <A2/3>Well, a deal's a deal. You can go down first.`

### `11_033345.lbin.txt` — Flavor ladder

*   **レイトン** (Professor Hershel Layton):  
    `<T>We can make our way into the facility by climbing down this ladder.`

### `11_033350.lbin.txt` — Passagem subterrânea

*   **ルーク** (Luke Triton):  
    `<T>Okay, everyone, the coast is clear. Come on down.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A4/5>Ah, this looks like your classic underground passageway for transporting research materials.`
*   **ドン・ポール** (Don Paolo):  
    `<T>I'll bet you anything that this tunnel leads all the way back out to the Thames.`
*   **ルーク** (Luke Triton):  
    `<T>You sound awfully sure about that.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A5/2>Pfeh! Remember who you're talking to, boy.`
*   **ドン・ポール** (Don Paolo):  
    `<T>Nobody does secret research like Don Paolo!`
*   **ルーク** (Luke Triton):  
    `<T>I suppose everyone's got to have a hobby...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Oh my...`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>What is it?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>The materials they have here. They look like...<W> No. No, I must be mistaken. Never mind.`

### `11_033360.lbin.txt` — Metal shutter

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>This metal shutter is blocking our way. I'm starting to get the feeling we're not welcome here.`
*   **ルーク** (Luke Triton):  
    `<T>Of course not, Flora. That's how criminals work. The dirtier the deed, the more cautious they get!`
*   **ルーク** (Luke Triton):  
    `<T>See, they've even gone out of their way to fit a puzzle lock to the shutter.`
*   **ルーク** (Luke Triton):  
    `<T>Phew! This puzzle's a tough one all right!`
*   **ルーク** (Luke Triton):  
    `<T>Just watch. This time I'm going to crack this puzzle wide open!`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>You can do it, Luke.`
*   **ルーク** (Luke Triton):  
    `<T>Ha ha! That lock didn't stand a chance against me!<W> Stupid lock.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/5>I hope you didn't enjoy cracking that lock too much, Luke. It could lead you to a life of crime!`
*   **ルーク** (Luke Triton):  
    `<T><A1/1>Thanks, Flora. I'll, um, bear that in mind.`

### `11_033370.lbin.txt` — Hollis

*   **ホリス** (Hollis):  
    `<T>Wh-what are you all doing down here?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Shh!<W> Keep it down, sir. We've come to rescue you.`
*   **ホリス** (Hollis):  
    `<T>I...I don't know what you mean.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There's nothing to fear, my friend. We know the whole story.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You were captured by the Family - or rather, by Dimitri Allen.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>And now you're being forced to work on his research here, correct?`
*   **ホリス** (Hollis):  
    `<T>D-Dimitri Allen! You know his name! But who are you exactly?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I am the real Professor Layton. Dimitri has been using my good name for his own misguided purposes.`
*   **ホリス** (Hollis):  
    `<T>Ah, I see. <A2/4>I remember hearing that you worked in archaeology. Yes, it all makes sense now.`
*   **ホリス** (Hollis):  
    `<T>Goodness, you can't imagine how shocked I was when I found out that Layton was actually Dimitri.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Are any of the other scientists here aware of Dimitri's true identity?`
*   **ホリス** (Hollis):  
    `<T><A1/1>Some, yes. But I don't dare talk about it with the people here.`
*   **ホリス** (Hollis):  
    `<T>Imagine what the Family would do to me if they caught me spreading that kind of information around.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I see.<W> Well, is Dimitri here in the facility?`
*   **ホリス** (Hollis):  
    `<T>Well... He comes and goes...<W> Yikes! Quick! Hide! The guards are heading this way!`

### `11_033380.lbin.txt` — Walmy/Walton de guarda

*   **ワルートン** (Walton / Barmey):  
    `<T>Brr! This place is like a deep freeze. <A1/5>Why do we have to stand guard down here anyway?`
*   **ワルートン** (Walton / Barmey):  
    `<T>The most we're ever gonna find is a rat.`
*   **ワルミー** (Walmy):  
    `<T><A3/5>We're down here 'cause we messed up, ain't we?`
*   **ワルミー** (Walmy):  
    `<T>This is our punishment, and I'd say we got off lightly.`
*   **ワルミー** (Walmy):  
    `<T>If Bostro hears you harpin' on like that, he'll knock your block off.`
*   **ワルートン** (Walton / Barmey):  
    `<T><A4/0>I wish I'd stayed in school, bruv. I shoulda known no good would come from this line of work.`
*   **ワルミー** (Walmy):  
    `<T><A2/5>Shut it, mopey!<W> We've got 10 hours till our shift ends, and we've just gotta stick it out.`
*   **ワルミー** (Walmy):  
    `<T>If you really wanna make the time go faster, stop your moanin' and tell me a joke or something.`

### `11_033390.lbin.txt` — Plano para passar pelos guardas

*   **ホリス** (Hollis):  
    `<T>Psst! Did you hear that?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I did. Those two are going to stand guard there for the next 10 hours.`
*   **ホリス** (Hollis):  
    `<T><A2/4>I-I'm heading back. The guards know me. If I walk past on my own, they won't stop me.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Wait just a moment. I think we might be able to get these chaps to turn a blind eye to us.`
*   **ホリス** (Hollis):  
    `<T>But how?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It's not my usual style of problem solving, but you know what they say about desperate times...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Wait just a minute. I'm sure we can find a way past them.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We need to take care of the guards before they spot us.`
*   **ホリス** (Hollis):  
    `<T>Crikey, I bet they didn't see that coming. They'll be out cold for a while.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Yes. I'm not one to condone violence, but needs must, and at least now we can pass safely.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>I have something else to tell you before we move on.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We came here to prevent Dimitri from completing his time machine.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We also wish to liberate all the scientists that Dimitri is holding captive.`
*   **ホリス** (Hollis):  
    `<T>I'm listening.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm hoping we can speak directly to the man and end this whole mess.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Do you know Dimitri's current whereabouts?`
*   **ホリス** (Hollis):  
    `<T><K>Hmm.<W></K> Well, if he's here, he'll probably be in the central research room. I'll show you the way.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/1>Wonderful. But before we go, will you allow me one more question?`
*   **ホリス** (Hollis):  
    `<T>Go on.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>These materials lying around down here...<W> They aren't for building a time machine, are they?`
*   **ホリス** (Hollis):  
    `<T><K>...<W></K>No, they aren't.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>What exactly are you working on here?`
*   **ホリス** (Hollis):  
    `<T><A2/4>My speciality is polydimensional physics, so I've been assigned to work on the time machine.`
*   **ホリス** (Hollis):  
    `<T>The materials lying around here belong to a separate research group within the facility.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>And this group also work under Dimitri's supervision?`
*   **ホリス** (Hollis):  
    `<T><A1/1>Who knows? That group tinker with some pretty dangerous stuff.`
*   **ホリス** (Hollis):  
    `<T>I don't think Dimitri's that interested in what they do, though.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>CELL NOT USED`

### `11_033400.lbin.txt` — Flavor pós-guardas

*   **レイトン** (Professor Hershel Layton):  
    `<T>We'd best move on before these two regain consciousness.`

### `11_033410.lbin.txt` — Craig / Cuthbert

*   **クレイグ** (Craig / Cuthbert):  
    `<T><A2/8>Whit's with all this racket, Horace? Who are these folk?`
*   **ホリス** (Hollis):  
    `<T>Cuthbert, this is the real Professor Layton.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T><A1/1>Eh? Whit d'ye mean, {''}the real Professor Layton{''}?`
*   **ホリス** (Hollis):  
    `<T>Erm...<W> Look, I'll explain it all later, we don't really have time to go into it here.`
*   **ホリス** (Hollis):  
    `<T>All you need to know for now is that these people have come to help us get out of here for good.`
*   **ホリス** (Hollis):  
    `<T>You DO want to go back to our own time, don't you?`
*   **クレイグ** (Craig / Cuthbert):  
    `<T>Oor own time?!<W> Aye, Ah'd do anything tae get back there.<W> Whit can Ah do for ye, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>I have to find Dimitri, the man who's been using my name.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I hear he could be in the central research room. Do you know where that is?`
*   **クレイグ** (Craig / Cuthbert):  
    `<T>Aye, yer close! It's just a wee bit doon the corridor.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T>Wow, Ah still cannae believe yer the real deal! That's a right turn up for the books.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>As I recall, you were rather surprised to see me the last time we met as well.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T><A1/2>Eh, well aye. Ah'm awful sorry, but Ah wasnae tae know who Ah was talking tae.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T>Anyhoo, we can chit-chat later. Away ye go before yer spotted.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T><A1/1>Bostro and his boys were jist through here, gabbing something aboot intruders.`
*   **クレイグ** (Craig / Cuthbert):  
    `<T>Ye need tae get moving.`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>What?! <A1/1>But how did he pick up on us so quickly?`
*   **ドン・ポール** (Don Paolo):  
    `<T><A4/1>Bah, I should have known. We probably tripped an infrared sensor. Basic secret base stuff.`
*   **ドン・ポール** (Don Paolo):  
    `<T>No sense in standing around, Layton. Let's go!`
*   **クレイグ** (Craig / Cuthbert):  
    `<T><A1/3>Professor, Ah need tae get back to ma own time. Don't go letting me doon.`
*   **ホリス** (Hollis):  
    `<T>The central research room is just down this corridor.<W> Hurry, before the guards spot you!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Thank you. I'll take it from here.`

### `11_033420.lbin.txt` — Porta da central research room

*   **レイトン** (Professor Hershel Layton):  
    `<T>This door appears to lead to the central research room.`
*   **ルーク** (Luke Triton):  
    `<T>I hope Dimitri is in there, Professor!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>As do I. You heard him talking earlier, Luke. He can still be reasoned with, I'm sure of it.`
*   **ルーク** (Luke Triton):  
    `<T>Well, our first challenge is to get this door open. It's got some strange lock on it.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Another puzzle, I suspect. Dimitri no doubt wishes to test the intelligence of all those who enter.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Dimitri has set out a fearsome challenge for us. I need a moment to gather my thoughts.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm sure I'll be able to get it open this time.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There we are! The door's lock seems to have disengaged.`

### `11_033500.lbin.txt` — Armadilha de Bostro [dublado]

*   **ボストロ** (Bostro):  
    `<T>'Old it right there!`
*   **ボストロ** (Bostro) <V0010>:  
    `<V0010><T>Aha! So this is where you sneaky sneaks 'ave been 'iding. There'll be no getting away this time!</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>Oh!</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T>Oh no! We're trapped!</V>`
*   **ナレーション** (Narration) <V0050>:  
    `<V0050><T>Quickly! Follow me!</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T>Huh?</V>`

### `11_033510.lbin.txt` — Fuga imediata

*   **ナレーション** (Narration):  
    `<T>Through here, everyone!`
*   **ルーク** (Luke Triton):  
    `<T>Phew! That was too close!`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Oh! My heart's still racing.`

### `11_033512.lbin.txt` — Celeste aparece [dublado]

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>Who are you?</V>`
*   **ドン・ポール** (Don Paolo) <V0020>:  
    `<V0020><T>My eyes must be playing tricks on me!</V>`
*   **サリアス** (Celeste) <V0030>:  
    `<V0030><T>You're Professor Layton, are you not?</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>Claire? Is it you?</V>`
*   **サリアス** (Celeste) <V0050>:  
    `<V0050><T>No. I'm Celeste, her younger sister. I've been trying to uncover what really happened to Claire.</V>`
*   **サリアス** (Celeste) <V0060>:  
    `<V0060><T><A4/4>I...I know she was quite fond of you, Professor.</V>`

### `11_033514.lbin.txt` — Conversa com Celeste e split

*   **レイトン** (Professor Hershel Layton):  
    `<T>You're Claire's...younger sister?`
*   **ドン・ポール** (Don Paolo):  
    `<T><A3/5>You look exactly like her! It's uncanny...`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>We've crossed paths several times, haven't we?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>And yet it's strange. Claire never mentioned having a sister...`
*   **サリアス** (Celeste):  
    `<T>It is my greatest regret that we spent the last years of her life estranged from each other.`
*   **サリアス** (Celeste):  
    `<T>Forgive me for not getting in touch with you earlier, Professor.`
*   **サリアス** (Celeste):  
    `<T>I wanted to, but I was afraid it might attract unwanted attention from the Family.`
*   **サリアス** (Celeste):  
    `<T><A3/5>For your own safety, I decided it was best to avoid contact with you.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I see.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A5/5>You must have cared dearly for your sister to come to a place like this in search of the truth.`
*   **サリアス** (Celeste):  
    `<T>Well, if I'm honest, I haven't been running my own investigation so much as tailing yours, Professor.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>But why?`
*   **サリアス** (Celeste):  
    `<T><A2/2>Your reputation. Don't they say the great Professor Layton can solve any puzzle?`
*   **サリアス** (Celeste):  
    `<T>I thought that if anyone could get to the bottom of what happened that day, it would be you.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Celeste...<W> On the day of the explosion, I-</430>`
*   **サリアス** (Celeste):  
    `<T><A2/6>Oh no! The Family will be here any second! We've got to run!`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/2>Ah, now's my time to shine! No one makes a grand escape like Don Paolo!`
*   **サリアス** (Celeste):  
    `<T><A1/1>We can't move quickly in a big group like this. We need to split up.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/1>I couldn't agree more. My dear Celeste, please allow me to personally escort you to safety.`
*   **ドン・ポール** (Don Paolo):  
    `<T>Layton, you take the kids!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Celeste, wait! There's still so much we need to discuss!`
*   **ボストロ** (Bostro):  
    `<T>Aha! Found you!`
*   **サリアス** (Celeste):  
    `<T>Professor, this city hides a secret so large it defies the imagination.`

### `11_033516.lbin.txt` — Pista final de Celeste [dublado]

*   **サリアス** (Celeste) <V0010>:  
    `<V0010><T>The answer to everything lies in the old father's embrace! It is there we will meet next!</V>`

### `11_033520.lbin.txt` — Perseguição

*   **ボストロ** (Bostro):  
    `<T>Oi! Stay where you are, intruders!`
*   **ルーク** (Luke Triton):  
    `<T>Professor, look out!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Luke, Flora, we have to run!`

### `11_033530.lbin.txt` — Fuga flavor

*   **レイトン** (Professor Hershel Layton):  
    `<T>We need to leave this facility immediately!`

### `11_033540.lbin.txt` — Bloqueio

*   **レイトン** (Professor Hershel Layton):  
    `<T>We can't head back that way. We'll be caught for sure!`

### `11_033545.lbin.txt` — Fora do facility

*   **ルーク** (Luke Triton):  
    `<T>Phew. I can't believe the three of us made it out of there in one piece.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Don't let your guard down, Luke. We're not out of the woods yet.`
*   **ルーク** (Luke Triton):  
    `<T>Professor, I just can't stop thinking about the last thing Celeste said to us.`

### `11_033550.lbin.txt` — Decodificação do Thames Arms [dublado]

*   **サリアス** (Celeste) <V0010>:  
    `<V0010><T>The answer to everything lies in the old father's embrace! It is there we will meet next!</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>Celeste was clearly trying to give us a hint as to our next rendezvous point.</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T>Oh, of course. She used a code to hide our meeting place from the Family.</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T><A4/1>But what could that code possibly mean?</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T><A2/2>Think of it as a puzzle, Luke.</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T>Though I suspect the answer to this puzzle will be much more than our next meeting place.</V>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><V0061>I'd wager that it's also the Family's secret headquarters and where Dimitri's been hiding.</V>`
*   **ルーク** (Luke Triton) <V0070>:  
    `<V0070><T><A1/6>If that's the case, it's even more important that we find out where this place is!</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T><A1/1>Luke, do you remember seeing a flyer for a restaurant named {''}The Thames Arms{''} on the way here?</V>`
*   **レイトン** (Professor Hershel Layton) <V0085>:  
    `<V0085><T>That's where Celeste will be waiting for us.</V>`
*   **ルーク** (Luke Triton) <V0090>:  
    `<V0090><T><A1/1>At the Thames Arms? But how did you work that out?</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T><A1/2>Well, Luke, have you ever heard of Old Father Thames?</V>`
*   **レイトン** (Professor Hershel Layton) <V0110>:  
    `<V0110><T>Rivers are often personified in folklore and literature, and the River Thames is no exception.</V>`
*   **レイトン** (Professor Hershel Layton) <V0120>:  
    `<V0120><T>When Celeste said that the answer lies in the {''}old father's embrace{''}...</V>`
*   **レイトン** (Professor Hershel Layton):  
    `<T><V0121>The {''}father{''} she was talking about was Old Father Thames.</V>`
*   **ルーク** (Luke Triton) <V0130>:  
    `<V0130><T>Oh, I get it! And an embrace happens in someone's arms. In this case, the arms of the Thames!</V>`

### `11_033555.lbin.txt` — Exposição da explosão

*   **ルーク** (Luke Triton):  
    `<T>I've been thinking, Professor.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>What about, Luke?`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>About how you, Dimitri and Don Paolo all have a personal tie to poor Claire.`
*   **ルーク** (Luke Triton):  
    `<T>And all of you seem to question the circumstances surrounding her death. Even Celeste does.`
*   **ルーク** (Luke Triton):  
    `<T>Why do I get the feeling that many of the mysteries in this city lead back to that explosion?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><K><A4/5>...`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>The explosion that killed Claire didn't just destroy the lab in which she worked...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>By the time I got word of the accident and ran to the site, the whole place was in flames.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>A block of flats next to the lab had also been destroyed by the blast.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>The entire area was devastated.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A5/1>Looking upon that scene, I knew that Claire was lost to me forever.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>And I wasn't the only one who lost something that day. Many others were wounded or lost loved ones.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>To this day, I still remember an orphaned child I met wandering the street, wailing for his parents.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>For some time after the incident, I was in a state of shocked grief.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Then, when I came back to my senses, I noticed something curious.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Despite the scale of the damage, there was no follow-up coverage in the media.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Not one word about the incident was printed or broadcast after the initial reports.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I knew the only way I'd get answers about what happened was by running my own investigation.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I immediately set to work researching Claire's lab and the scientists she had worked with.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>During my investigation, I learned that powerful political forces had suppressed reports of the blast.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A>It was right after this discovery that I was viciously assaulted.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>My injuries were so severe that I was in hospital for a month. I was lucky to be alive.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>When I returned to work, my office had been torn apart.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>The majority of the information I'd gathered on the case had been stolen.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That explosion was no ordinary accident. Someone with serious political clout was involved.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>And this person abused his or her power to keep any facts about the event from ever coming to light.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/5>I tried to dig back into the case several times, but it was no use.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Every time I tried to make progress, I was met with resistance and threats of violence.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>Claire is lost to me forever, I know that. But I must know the truth of what happened that day.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It's a feeling I'm sure Don Paolo and Celeste share as well.`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>So you think Dimitri knows the truth?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Dimitri and perhaps one other person...`
*   **ルーク** (Luke Triton):  
    `<T>Who else do you mean, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Everything will become clear at the Thames Arms. Let's go.`

### `11_033559.lbin.txt` — Pavel perdido

*   **ポーロ** (Pavel / Polo):  
    `<T>I...<W>am lost.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A2/5>EEEK!`
*   **ルーク** (Luke Triton):  
    `<T>Flora, are you okay?`
*   **ポーロ** (Pavel / Polo):  
    `<T>Scusa, comrades. It wasn't my intention to scare the young fr{:a}ulein.`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>Pavel!<W> <A1/1>What are you doing down here?`
*   **ポーロ** (Pavel / Polo):  
    `<T><A1/5>I was exploring the area and somehow ended up here. Perdido.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Doing some of the cavern exploration you were talking about before, I take it?`
*   **ポーロ** (Pavel / Polo):  
    `<T><A1/1>Da. Earlier in my quest to find the great tunnels, I mistakenly wandered onto some train tracks.`
*   **ポーロ** (Pavel / Polo):  
    `<T>That little viaje put me in great peril, but danger is part and parcel of exploring el mundo, non?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I suppose you could say that.`
*   **ポーロ** (Pavel / Polo):  
    `<T>Naturalmente, most of my travel woes could've been avoided if my compass hadn't been broken.`
*   **ポーロ** (Pavel / Polo):  
    `<T><A2/1>Though I think this map might be able to show me which way to go. A bit of help, bitte?`

### `11_033560.lbin.txt` — Pavel pós-puzzle

*   **ポーロ** (Pavel / Polo):  
    `<T>C'est okay. I'll find my own way out of here eventually.`
*   **ポーロ** (Pavel / Polo):  
    `<T>My beloved compass is kaputt.`
*   **ポーロ** (Pavel / Polo):  
    `<T>Oh, double gracias, my monsieur. Thanks to you, I can now continue my travels.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Do be careful out there, Pavel.`
*   **ポーロ** (Pavel / Polo):  
    `<T>Bon! Now, which way should I go...?`

### `11_033565.lbin.txt` — Retorno ao Thames Arms

*   **ルーク** (Luke Triton):  
    `<T>We've made it this far, so I think it's finally safe to say we've given the Family the slip.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Things got rather chaotic back there, Flora. Are you feeling all right? Not too shaken?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>I'm fine, Professor. I'm just glad I had you both with me.`
*   **ルーク** (Luke Triton):  
    `<T><A3/2>Professor, the Thames Arms is just up the road from here. Let's go and meet Celeste!`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `11_033320` | **Flora's Scrap Paper Enigma** | Bilhete na parede que Flora resolve sozinha; Layton questiona autoria misteriosa (possível Celeste). |
| `11_033330` | **Don Paolo's Shadow Enigma (J54)** | Portão enigma com trigger `<J54><Q><K>` que Paolo usou para testar o grupo; precede gag da flying machine. |
| `11_033340` | **Ladder Order Enigma** | Disputa Captain Obvious vs nimblest/monkey resolvida por enigma; Luke vence e desce primeiro. |
| `11_033360` | **Metal Shutter Lock Enigma** | Enigma lock na shutter; Flora faz meta-piaga sobre life of crime. |
| `11_033390` | **Guards Non-Violent Neutralization Enigma** | Layton usa enigma/trick para deixar Walmy/Walton out cold sem violência: "not my usual style / needs must". |
| `11_033420` | **Central Research Room Door Enigma** | Strange lock / fearsome challenge de Dimitri; portão para confronto final. |
| `11_033500`–`11_033516` | **Bostro Trap → Celeste Rescue (dublado)** | Sequência dublado: armadilha, fuga guiada por Narration/Celeste, revelação irmã de Claire, split e pista Old Father. |
| `11_033550` | **Old Father's Embrace Word Enigma** | Decodificação: Old Father Thames + embrace = arms → Thames Arms; Layton aposta ser também Family HQ. |
| `11_033555` | **Explosão Exposition (lore)** | Sem enigma direto; monólogo revela abafamento midiático, assault e hospital month, office torn - indica conspirador político além de Dimitri. |
| `11_033559`–`11_033560` | **Pavel's Map/Compass Enigma** | Explorer multilíngue perdido por train tracks, compass kaputt, pede ajuda com map enigma; pós-solve agradece em 4 línguas. |
| `11_033390` lore | **Two Research Groups Reveal** | Evento: separate group com dangerous stuff não-interesse de Dimitri - foreshadow de segundo projeto (possível arma/mobile fortress). |

**Eventos narrativos sem enigmas diretos:** entrada discreta vs main portão (`033310`), passagem que volta ao Thames (`033350`), observação de materiais (`033350` Layton oh my), rotina freeze guards (`033380`), infrared sensor de Paolo (`033410`), corrida e separação (`033514`/`033520`), fuga imediata (`033530`/`033540`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Agrupamento de voz:** Apenas `11_033500`, `11_033512`, `11_033516`, `11_033550` são dublados (Bostro trap + Celeste); todo o restante é `<T>` de exploração/infiltração, similar ao Cap. 10 mas com pico dublado no resgate — marca virada de ato da mid-game para endgame.
*   **Celeste = Claire double:** `サリアス` (Celeste) usa sprite idêntico a Claire, explica ausência de menção anterior como estranged last years e tailing por medo da Family; espelha o fake Layton do Cap. 09 - não é fantasma mas irmã investiga.
*   **Old Father Thames enigma:** Jogo de palavras intraduzível preservado em inglês; solução depende de personificação folclórica "Old Father Thames" + arms/embrace = Thames Arms — já introduzido como restaurante riverside no Cap. 08. Repetição literal da pista em 3 arquivos (`033514`, `033516`, `033550`) fixa o código.
*   **Two facilities twist:** Diálogo Hollis `033390` confirma que materiais do corredor não são da time machine; dangerous stuff separado sob supervisão incerta sugere que o lab abriga dois experimentos paralelos - explicação para foreshadow "looks like..." de Layton em `033350` e para escala devastadora da explosão (flats destroyed).
*   **Volta ao our own time:** Hollis e Craig/Cuthbert repetem want to go back to our own time, reforçando que cientistas foram sequestrados de 10 anos atrás (London presente) para London futuro, não nascidos ali - amarra wormhole do Prólogo/Cap. 05 com Dimitri.
*   **Infrared sensor:** Don Paolo explica detecção rápida como basic secret base stuff, mantendo trait de gadget-knowledge e justificando por que Bostro aparece tão rápido na central room.
*   **Supressão política:** Exposição `033555` é mais longa do capítulo (34 blocos) e introduce antagonista invisível com political clout que abafou media, assaulted Layton e roubou office — além de Dimitri, preparando revelação do PM Oswald?/Claire's boss e motivo para Celeste temer attention.
*   **Pavel cameo:** `ポーロ` (Pavel) mantém poliglotismo (Scusa, Perdido, Da, viaje, el mundo, bitte, C'est, kaputt, Bon, gracias) e trait de great tunnels/cavern exploration, mas desta vez relata train tracks peril - callback ao Thames tunnel e ao próprio labyrinth subterrâneo.
*   **Continuidade Flora-gentleman:** Debate `033340` recicla credo "true gentleman" e distinção acting vs being, com Flora como defensora moral e Paolo como mimic cynico - eco direto do teste do falso Layton no Cap. 09.

---

*Gerado a partir de dumps LSCR brutos — 28/28 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/11`. Próximo capítulo: `12` — Thames Arms e o Segredo da Cidade.*
