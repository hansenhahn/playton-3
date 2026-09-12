# Capítulo 14 — A Queda da Fortaleza, Claire Revelada e a Carta de Luke | Professor Layton and the Unwound Future

> **Capítulo 14 — Colapso, Revelação e Epílogo / Fuga, Perdão e a Verdade sobre Celeste** — Análise de dump LSCR para `Textos Originais/txt/uk/14/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/14/`
> Total de arquivos escaneados: **15**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão, `<J>` = jump

---

## 1. Arquivos Cobertos

Todos os 15 dumps `.lbin.txt` em `uk/14`:

```
14_000000.lbin.txt  — [vazio - apenas cabeçalho]
14_048025.lbin.txt  — Fuga iminente: fortress crumbling, Layton ordena entrar no carro
14_048030.lbin.txt  — Escape by car com Prime Minister cético e Luke apressando
14_049010.lbin.txt  — Estrada bloqueada e puzzle de travessia (Luke find a way over)
14_050010.lbin.txt  — Chelmey/Barton no topside: all residents brought topside, Hurry up Layton
14_052000.lbin.txt  — Dublado: Celeste resgata Clive nos escombros, you can always start again
14_053010.lbin.txt  — Check pós-fuga: Is everyone all right?
14_054000.lbin.txt  — Dublado CORE: Clive preso, Bill Hawks manda apprehend, Layton defende victim of political agenda, flashback dos pais, second time saved, Chelmey vs Bill sobre blind ones
14_054050.lbin.txt  — Dimitri em remorso: love or pride, 10 years chasing impossible, one detail you got wrong
14_055000.lbin.txt  — Dublado CORE: Reveal Celeste é Claire, no younger sister, shot 10 years into future, molecular instability, flow of time must remain linear
14_057000.lbin.txt  — [vazio - apenas cabeçalho]
14_059000.lbin.txt  — Dublado epílogo: carta Dear Professor Layton, tailor-made mystery, please write back
14_060010.lbin.txt  — Sidequest evacuação: Chelmey Can you really stop that contraption? lead to clock shop
14_060020.lbin.txt  — Jack/Cogg confessa serviço à família Dove, I'll take them above ground using the lift
14_060030.lbin.txt  — Samara defende Clive: kind gentle person, not cold-hearted criminal
```

> **Nota:** 2 arquivos contêm apenas o cabeçalho LSCR sem blocos de texto: `14_000000.lbin.txt` e `14_057000.lbin.txt`. `14_048025`/`14_053010` são linhas únicas de urgência. `14_049010` concentra o enigma diegético da estrada. `14_052000`/`14_054000`/`14_055000`/`14_059000` são os blocos dublados centrais do final. `14_060010`–`14_060030` são flavors/sidequests de evacuação repetíveis do underground (Chelmey/Cogg/Samara) com estrutura quase idêntica de branching.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 14 |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Protagonista, ordena fuga de carro, pilota com PM, confia enigma a Luke, defende Clive como victim of political agenda, reconhece flashback do menino salvo, aceita revelação de Claire |
| `ルーク` | **Luke Triton** | Aprendiz, alerta road's blocked, resolve travessia (Yes! We did it!), apressa escape, checa todos a salvo, autor da carta epilogar tailor-made mystery |
| `ビル・ホーク` | **Prime Minister Bill Hawks** | Passageiro cético We're making our escape by car?! Is this some kind of joke? / This is madness..., manda apprehend Clive como imminent threat, chama criminosos de Despicable, alvo da réplica blind ones de Chelmey |
| `チェルミー` | **Inspector Chelmey** | Coordena evacuação topside (Is that the last of them?), pede Hurry up Layton, prende Clive, rebate Bill com blinded by own motivations, avisa no record of Claire having younger sister |
| `バートン` | **Constable Barton** | Confirma all residents brought topside, sir!, executa Barton take him back to headquarters |
| `クラウス` | **Clive (Klaus)** | Antagonista em ruínas Ngh... This is the end for me, resgatado por Celeste, confessa toying then enjoying time together, maybe wanted somebody to save me from madness, flashback I need to go back! parents inside, promete atone e se despede |
| `サリアス` | **Celeste (Sarrias)** | Salvadora de Clive You can always start again, I can't just leave you here, declara tragedy caused by mistakes we scientists made, revela-se Claire com You've taken good care of that hat I gave you / I don't have much longer here |
| `クレア` | **Claire (Foley)** | Identidade revelada It's me Hershel. It's Claire., explica I begged Dimitri to stop, flow of time must remain linear, broken laws of nature |
| `ディミトリー` | **Dimitri Allen** | Em remorso I don't know what to say... suffering in name of research, duvida love or pride, corrige Hershel there is one detail you got wrong, explica Claire shot 10 years into future e molecular instability trying to return to moment of blast, promete close the book on the time machine forever |
| `ジャック` | **Jack / Cogg (mordomo Dove)** | Servo dos Dove por anos, confessa knew Clive's identity, couldn't refuse when asked nicely, Had I known would never have agreed, oferece lift para evacuação |
| `サマリー` | **Samara / Summary (esposa de Jack)** | Defende Clive He was always such a nice boy / Deep down kind gentle person / not cold-hearted criminal, fica para help everyone out |
| `ナレーション` | **Narração / Flashback Boy** | Vozes do passado: I need to go back! My parents are still inside! / Pull yourself together / Nothing to be done. Jump back in there and you'll die too! |

Tags de controle observadas: `<V0010>`–`<V0330>` dublados em `14_052000`, `14_054000` (mais longo do capítulo, 34 blocos com flashback V0160–V0190), `14_054050`, `14_055000` (30 blocos) e `14_059000` (carta V0010–V0090); `<W>` / `<W150>` pausa longa em madness e return to own time; `<A1/1>`–`<A5/0>` animações (hat de Layton em `055000`); `<K>` hesitação Ngh..., Hmm?; `<Q>` única em Barton Yes sir! `<A2/1>`; placeholders `{''}` ausentes; `14_049010` mantém padrão de retry de enigma (You'll have to try again / Come on I know you can do it) sem tag `<S671>` explícita.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Colapso e Fuga de Carro — A Estrada Bloqueada (`14_048025`–`14_049010`)
A fortress revertida no Cap. 13 entra em colapso acelerado e Layton corta qualquer hesitação com ordens secas de evacuação ao carro. Bill Hawks, ainda no pod do gerador, reage com incredulidade britânica à ideia de fugir de carro enquanto Luke insiste na urgência. Na rota de saída o caminho está bloqueado por escombros e Layton, fiel ao método, transfere a agência a Luke — "Don't panic, Luke. I'm sure you can find a way over this mess for us!" — até o Yes! We did it! do enigma e o alerta de que We're not out of the woods yet. Hold on tight sela a travessia como ponte entre a autodestruição do Cap. 13 e a evacuação civil que corre em paralelo no topside.
> Ganchos: "This place is crumbling at an incredible rate! Hurry everyone, into the car!" / "Don't panic, Luke. I'm sure you can find a way over this mess for us!"

### 3.2 Evacuação da Cidade Subterrânea — Chelmey, Barton, Cogg e Samara (`14_050010`, `14_060010`–`14_060030`)
Em contraponto à fuga do protagonista, Chelmey confirma com Barton que Todos os residentes da cidade subterrânea foram trazidos à superfície e murmura Depressa, Layton... como fio de tensão externa. Três flavors expansíveis detalham o esforço: Chelmey cobra Be straight with me... Can you really stop that contraption? e delega Lead everyone to the clock shop and get them above ground; Jack/Cogg revela que knew Clive's true identity from the start por servir a família Dove, lamenta I couldn't refuse when he asked so nicely e se redime oferecendo o lift; Samara insiste I just can't believe Clive would do something like this. He was always such a nice boy ao defender que Deep down Clive is a kind, gentle person. O conjunto ancora o tema do capítulo — evacuação como responsabilidade coletiva enquanto Layton ganha tempo no núcleo.
> Ganchos: "All residents of the underground city have been brought topside, sir." / "You knew Clive's true identity from the start, didn't you?"

### 3.3 O Resgate de Clive por Celeste nos Escombros (`14_052000`)
Antes do topside, Celeste encontra Clive resignado ao fim — "Ngh... This is the end for me." — e o puxa da auto-condenação com a tese moral do jogo: "That's not true, Clive. You can always start again and try to repair the damage you've done." Ao Why are you helping me? ela responde I can't just leave you here e, após o But don't you know what I've done?, sentencia Yes, but I would never leave you here to die porque so much of this tragedy was caused by the mistakes we cientistas made. A cena inverte o papel de Clive de carrasco para resgatado e introduz Celeste como consciência científica do desastre, preparando sua própria revelação.
> Ganchos: "That's not true, Clive. You can always start again and try to repair the damage you've done." / "After all, so much of this tragedy was caused by the mistakes we scientists made."

### 3.4 Superfície — Confronto com o Prime Minister, a Confissão e o Flashback (`14_054000`)
Já em superfície, Bill Hawks exige Alguém prenda esse homem imediatamente! e Chelmey cumpre Você vem comigo, garoto. Layton intervém com a defesa mais madura do jogo — "But we can't forget that he's also a victim of a political agenda for progress, no matter the cost." — provocando o You've got some audácia de Bill. Clive então responde à pergunta central de Layton — You knew full well I'd stand in the way... So why did you send for me? — admitindo que Dimitri precisava de Layton mas ele sabia da ameaça, que still led you to the heart of my base, que At first I was just toying with you... But I realised I was enjoying our time together e que Maybe part of me wanted somebody to save me from my all-consuming madness. As you did, all those anos atrás... O flashback dublado irrompe com I need to go back! My parents are still inside! / Pull yourself together! / There's nothing to be done. Jump back... you'll die too! e Layton reconhece That... was you? Clive fecha com This is the second time you've saved my life. Thank you, promete atone e troca o adeus And you too, Clive. Chelmey leva-o via Barton e encerra com a réplica política mais afiada do capítulo contra Bill: people can often be so blinded by their own motivations... criminals aren't the only blind ones.
> Ganchos: "But we can't forget that he's also a victim of a political agenda for progress, no matter the cost." / "Maybe part of me wanted somebody to save me from my all-consuming madness."

### 3.5 O Arrependimento de Dimitri — Amor ou Orgulho? (`14_054050`)
Dimitri, já sem Clive como escudo, faz mea culpa contido: "I don't know what to say. When I think of all the suffering I caused in the name of research...". Layton concede que Foi terrível. Mas você deve ter amado muito Claire, mas Dimitri duvida de si — the more unsure whether it was love...or pride — e resume For 10 long years, I chased after what so many called impossible. O gancho But, you know, Hershel, there is one detail that you got wrong. funciona como dobradiça direta para a revelação seguinte, mantendo Dimitri como ponte científica entre culpa e explicação temporal.
> Ganchos: "The more I reflect on it, the more unsure I am as to whether it was love...or pride that compelled me." / "But, you know, Hershel, there is one detail that you got wrong."

### 3.6 Celeste é Claire — Deslocamento Temporal e Instabilidade Molecular (`14_055000`)
O núcleo emocional do capítulo. Celeste avisa I don't think I have much longer here, Hershel e solta o teste do chapéu — "You've taken awfully good care of that hat I gave you." — que Layton não compreende até Chelmey trazer o laudo: Não há registro de Claire ter uma irmã mais nova. Dimitri confirma Yes, it was quite a shock when I first worked it out e Claire finalmente diz "It's me, Hershel. It's Claire." A explicação fecha o paradoxo plantado desde o Cap. 12: o experimento de 10 anos atrás wasn't a complete failure; Somehow Claire was shot 10 years into the future. To our present! funcionou por um único momento antes de explodir. Mas houve complicações — shortly after appearing, Claire's body showed signs of molecular instability. It was trying to return to its own time, ao momento do blast, por causa da natureza incompleta da máquina; Dimitri tentou stabilise her existence sem sucesso. Claire assume a posição ética: I begged Dimitri to stop his work. Tampering further with time can only result in more anomalies. The flow of time must remain linear. We all know the consequences of changing its course, e acusa What we did 10 anos atrás broke the laws of nature. And now we must pay. Dimitri encerra com Tonight, I will close the book on the máquina do tempo forever, selando o abandonment definitivo do projeto.
> Ganchos: "You've taken awfully good care of that hat I gave you." / "It's me, Hershel. It's Claire."

### 3.7 Epílogo — Todos a Salvo e a Carta do Novo Começo (`14_053010`, `14_059000`)
Após o turbilhão, Layton confere Is everyone all right? e Luke responde I think so, Professor! — pausa humana antes do salto temporal. O epílogo dublado entrega a carta que reabre o ciclo narrativo: "Dear Professor Layton, It's been a while since we said goodbye... I'm all settled in and making new friends here... something deeply puzzling happened here recently. It seems like the sort of mystery that's tailor-made for Professor Layton and his apprentice." O fecho I can't wait to start this new adventure... Your friend and apprentice, Luke transforma a resolução trágica de Claire/Clive/Dimitri em prólogo de uma nova aventura, ecoando o motivo gentleman/apprentice do jogo.
> Ganchos: "Is everyone all right?" / "It seems like the sort of mystery that's tailor-made for Professor Layton and his apprentice."

> **Cliffhanger/Fecho:** A fortress cai, a evacuação completa devolve a cidade subterrânea ao topside e Clive é preso após admitir que buscava ser salvo por Layton como na infância; Dimitri confronta que sua motivação pode ter sido orgulho e que errou um detalhe vital — Celeste nunca teve irmã porque ela é Claire, deslocada 10 anos pelo único sucesso instantâneo da máquina do tempo e agora em instabilidade molecular prestes a retornar ao blast; ela impõe que o fluxo do tempo deve permanecer linear e Dimitri jura fechar o livro da máquina para sempre, enquanto Luke, já distante, convoca Layton para um novo tailor-made mystery.

---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag)` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes.

### `14_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `14_048025.lbin.txt` — Fuga iminente da fortress

*   **レイトン** (Professor Hershel Layton):  
    `<T>This place is crumbling at an incredible rate! Hurry everyone, into the car!`

### `14_048030.lbin.txt` — Escape by car com Prime Minister

*   **レイトン** (Professor Hershel Layton):  
    `<T>There's no time to waste! Get in the car!`
*   **ビル・ホーク** (Prime Minister Bill Hawks):  
    `<T>We're making our escape by car?!<W> Is this some kind of joke?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'll do my best to drive safely, Prime Minister.`
*   **ルーク** (Luke Triton):  
    `<T>What are you waiting for? We've got to go!`
*   **ビル・ホーク** (Prime Minister Bill Hawks):  
    `<T>This is madness...`

### `14_049010.lbin.txt` — Estrada bloqueada e puzzle

*   **ルーク** (Luke Triton):  
    `<T><A1/3>Now what do we do? The road's blocked!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Don't panic, Luke. I'm sure you can find a way over this mess for us!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You'll have to try again, Luke!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Come on, Luke. I know you can do it this time!`
*   **ルーク** (Luke Triton):  
    `<T>Yes! We did it, Professor!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We're not out of the woods yet. Hold on tight, everyone!`

### `14_050010.lbin.txt` — Chelmey/Barton no topside

*   **チェルミー** (Inspector Chelmey) <V0020>:  
    `<V0020><T>Is that the last of them, then?</V>`
*   **バートン** (Constable Barton) <V0030>:  
    `<V0030><T><A2/1>Yes, sir! All residents of the underground city have been brought topside, sir. Yes, sir!</V>`
*   **チェルミー** (Inspector Chelmey) <V0040>:  
    `<V0040><T>Hurry up, Layton...</V>`

### `14_052000.lbin.txt` — Celeste resgata Clive (dublado)

*   **クラウス** (Clive) <V0010>:  
    `<V0010><T><K>Ngh...<W></K> This is the end for me.</V>`
*   **サリアス** (Celeste) <V0020>:  
    `<V0020><T>That's not true, Clive. You can always start again and try to repair the damage you've done.</V>`
*   **クラウス** (Clive) <V0030>:  
    `<V0030><T>Huh?</V>`
*   **サリアス** (Celeste) <V0040>:  
    `<V0040><T>We can talk about that later. This place won't hold much longer.</V>`
*   **クラウス** (Clive) <V0050>:  
    `<V0050><T>...<W>Why are you, of all people, helping me?</V>`
*   **サリアス** (Celeste) <V0060>:  
    `<V0060><T>I can't just leave you here.</V>`
*   **クラウス** (Clive) <V0070>:  
    `<V0070><T><A2/5>But don't you know what I've done? What I tried to do?</V>`
*   **サリアス** (Celeste) <V0080>:  
    `<V0080><T><A4/4>Yes, but I would never leave you here to die.</V>`
*   **サリアス** (Celeste) <V0081>:  
    `<T><V0081>After all, so much of this tragedy was caused by the mistakes we scientists made.</V>`
*   **クラウス** (Clive) <V0090>:  
    `<V0090><T><A1/1>I...I see.</V>`
*   **サリアス** (Celeste) <V0100>:  
    `<V0100><T><A1/1>There will be time to talk more later. We need to leave now.</V>`

### `14_053010.lbin.txt` — Check pós-fuga

*   **レイトン** (Professor Hershel Layton):  
    `<T>Is everyone all right?`
*   **ルーク** (Luke Triton):  
    `<T>I think so, Professor!`

### `14_054000.lbin.txt` — Superfície, perdão e flashback (dublado)

*   **クラウス** (Clive) <V0010>:  
    `<V0010><T>Ugh...</V>`
*   **ビル・ホーク** (Prime Minister Bill Hawks) <V0020>:  
    `<V0020><T>Somebody apprehend that man at once!</V>`
*   **チェルミー** (Inspector Chelmey) <V0030>:  
    `<V0030><T>You're coming with me, boy, and I don't want any trouble!</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>Inspector, a moment please?</V>`
*   **ビル・ホーク** (Prime Minister Bill Hawks) <V0050>:  
    `<V0050><T>Just what do you think you're doing? This man poses an imminent threat to our national security!</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T>I cannot deny the damage that Clive has done to our city.</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T>But we can't forget that he's also a victim of a political agenda for progress, no matter the cost.</V>`
*   **ビル・ホーク** (Prime Minister Bill Hawks) <V0080>:  
    `<V0080><T>You've got some nerve, man!</V>`
*   **クラウス** (Clive) <V0090>:  
    `<V0090><T>Professor, I-</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T><A1/1>Answer me one question, Clive.</V>`
*   **レイトン** (Professor Hershel Layton) <V0101>:  
    `<T><V0101>You knew full well I'd stand in the way of your plot. So why did you send for me?</V>`
*   **クラウス** (Clive) <V0110>:  
    `<V0110><T><A3/5>Dimitri was sure he needed you for his project, but I knew full well of the threat you posed to my plan.</V>`
*   **クラウス** (Clive) <V0120>:  
    `<V0120><T>Though I suppose I still led you all the way to the heart of my base, didn't I?</V>`
*   **クラウス** (Clive) <V0130>:  
    `<V0130><T><A1/1>At first I was just toying with you. But at some point, I realised I was enjoying our time together.</V>`
*   **クラウス** (Clive) <V0140>:  
    `<V0140><T>Maybe part of me wanted somebody to save me from my all-consuming madness.</V>`
*   **クラウス** (Clive) <V0150>:  
    `<V0150><T>As you did, all those years ago...</V>`
*   **ナレーション** (Narration / Flashback) <V0160>:  
    `<V0160><T>I need to go back! My parents are still inside!</V>`
*   **ナレーション** (Narration / Flashback) <V0170>:  
    `<V0170><T>Pull yourself together, boy!</V>`
*   **ナレーション** (Narration / Flashback) <V0180>:  
    `<V0180><T>There's nothing to be done. Jump back in there and you'll die too!</V>`
*   **ナレーション** (Narration / Flashback) <V0190>:  
    `<V0190><T>No! No...</V>`
*   **レイトン** (Professor Hershel Layton) <V0200>:  
    `<V0200><T><A3/1>That...was you?</V>`
*   **クラウス** (Clive) <V0210>:  
    `<V0210><T><A1/4>Deep down inside, I hoped you might be able to talk me down from the edge of insanity again.</V>`
*   **クラウス** (Clive) <V0220>:  
    `<V0220><T>This is the second time you've saved my life now.<W150> Thank you.</V>`
*   **レイトン** (Professor Hershel Layton) <V0230>:  
    `<V0230><T>Clive...</V>`
*   **クラウス** (Clive) <V0240>:  
    `<V0240><T>Don't worry about me. I intend to atone for my crimes.</V>`
*   **クラウス** (Clive) <V0250>:  
    `<V0250><T>I look forward to the day we meet again. Until then, I hope life treats you well, Professor.</V>`
*   **レイトン** (Professor Hershel Layton) <V0260>:  
    `<V0260><T>And you too, Clive.</V>`
*   **チェルミー** (Inspector Chelmey) <V0270>:  
    `<V0270><T>Barton, take him back to headquarters.</V>`
*   **バートン** (Constable Barton) <V0280>:  
    `<V0280><T><Q><A2/1>Yes, sir!</V>`
*   **ビル・ホーク** (Prime Minister Bill Hawks) <V0290>:  
    `<V0290><T>Hah! Criminals like him make me think the whole world has gone mad. Despicable, just despicable.</V>`
*   **チェルミー** (Inspector Chelmey) <V0300>:  
    `<V0300><T><A1/5>Yes, people can often be so blinded by their own motivations that they lose sight of the damage they do.</V>`
*   **チェルミー** (Inspector Chelmey) <V0310>:  
    `<V0310><T>But criminals aren't the only blind ones.</V>`
*   **ビル・ホーク** (Prime Minister Bill Hawks) <V0320>:  
    `<V0320><T><A2/3>Just what are you implying, Inspector?</V>`
*   **チェルミー** (Inspector Chelmey) <V0330>:  
    `<V0330><T><A1/1>Nothing at all. Just stating the facts, sir. Now, if you'll excuse me, I still have work to do.</V>`

### `14_054050.lbin.txt` — Dimitri em remorso (dublado)

*   **ディミトリー** (Dimitri Allen) <V0010>:  
    `<V0010><T>I don't know what to say. When I think of all the suffering I caused in the name of research...</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>It was terrible. But I see you must have loved Claire very much to do what you did.</V>`
*   **ディミトリー** (Dimitri Allen) <V0030>:  
    `<V0030><T>The more I reflect on it, the more unsure I am as to whether it was love...or pride that compelled me.</V>`
*   **ディミトリー** (Dimitri Allen) <V0040>:  
    `<V0040><T>For 10 long years, I chased after what so many called impossible...<W> But I've come to my senses now.</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T><K><A4/3>Hmm.</V>`
*   **ディミトリー** (Dimitri Allen) <V0060>:  
    `<V0060><T><A3/5>But, you know, Hershel, there is one detail that you got wrong.</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><A1/1>What are you referring to?</V>`

### `14_055000.lbin.txt` — Celeste é Claire, instabilidade molecular (dublado)

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T><K>Hmm?</V>`
*   **サリアス** (Celeste) <V0020>:  
    `<V0020><T>I don't think I have much longer here, Hershel.</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T>I don't know what you mean.</V>`
*   **サリアス** (Celeste) <V0040>:  
    `<V0040><T><A5/0>You've taken awfully good care of that hat I gave you.</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T>What did you say?</V>`
*   **チェルミー** (Inspector Chelmey) <V0060>:  
    `<V0060><T>Oi, there you are, Layton! I did a background check on Claire's family, like you asked.</V>`
*   **チェルミー** (Inspector Chelmey) <V0061>:  
    `<T><V0061>There's no record of Claire having a younger sister.</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><A1/1>Then...</V>`
*   **ディミトリー** (Dimitri Allen) <V0080>:  
    `<V0080><T>Yes, it was quite a shock when I first worked it out.</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T>But you... You can't really mean...</V>`
*   **クレア** (Claire) <V0100>:  
    `<V0100><T>It's me, Hershel. It's Claire.</V>`
*   **ディミトリー** (Dimitri Allen) <V0110>:  
    `<V0110><T>While it defies logic, it seems the experiment 10 years ago wasn't a complete failure.</V>`
*   **ディミトリー** (Dimitri Allen) <V0120>:  
    `<V0120><T>Somehow Claire was shot 10 years into the future.</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T>To our present!</V>`
*   **ディミトリー** (Dimitri Allen) <V0140>:  
    `<V0140><T>Yes. The time machine worked, if only for that single moment before it exploded.</V>`
*   **レイトン** (Professor Hershel Layton) <V0150>:  
    `<V0150><T>That's...that's not possible!</V>`
*   **ディミトリー** (Dimitri Allen) <V0160>:  
    `<V0160><T><A1/4>Unfortunately, however, there were more complications.</V>`
*   **ディミトリー** (Dimitri Allen) <V0170>:  
    `<V0170><T>Shortly after appearing in the present, Claire's body showed signs of...molecular instability.</V>`
*   **ディミトリー** (Dimitri Allen) <V0171>:  
    `<T><V0171>It was trying to return to its own time.</V>`
*   **ディミトリー** (Dimitri Allen) <V0180>:  
    `<V0180><T>I attribute that phenomenon to the incomplete nature of the time machine. She didn't have long here.</V>`
*   **ディミトリー** (Dimitri Allen) <V0190>:  
    `<V0190><T>I worked on the machine in the hopes of finding a way to stabilise her existence in the present.</V>`
*   **ディミトリー** (Dimitri Allen) <V0200>:  
    `<V0200><T>But it seems inevitable that she'll return to her own time...<W>to the moment of the blast.</V>`
*   **クレア** (Claire) <V0210>:  
    `<V0210><T><A4/4>I begged Dimitri to stop his work. Tampering further with time can only result in more anomalies.</V>`
*   **クレア** (Claire) <V0220>:  
    `<V0220><T>There's no telling what chaos we'd release upon the world if we tried to save the dead from their fate.</V>`
*   **クレア** (Claire) <V0230>:  
    `<V0230><T>The flow of time must remain linear.</V>`
*   **クレア** (Claire) <V0231>:  
    `<T><V0231>We all know the consequences of changing its course.</V>`
*   **クレア** (Claire) <V0240>:  
    `<V0240><T>But Dimitri wouldn't listen to me. That's when I knew the only way to stop him was through you, Hershel.</V>`
*   **クレア** (Claire) <V0250>:  
    `<V0250><T>What Dimitri, Bill and I did 10 years ago broke the laws of nature. And now we must pay.</V>`
*   **レイトン** (Professor Hershel Layton) <V0260>:  
    `<V0260><T><A5/1>This is all so...incomprehensible.</V>`
*   **クレア** (Claire) <V0270>:  
    `<V0270><T><A1/1>It's time to end this, Dimitri.</V>`
*   **ディミトリー** (Dimitri Allen) <V0280>:  
    `<V0280><T>Yes...it does seem that way.</V>`
*   **ディミトリー** (Dimitri Allen) <V0290>:  
    `<V0290><T><A1/1>My research has threatened our very existence and it could do so again.</V>`
*   **ディミトリー** (Dimitri Allen) <V0300>:  
    `<V0300><T>Tonight, I will close the book on the time machine forever.</V>`

### `14_057000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `14_059000.lbin.txt` — Carta de Luke (dublado epílogo)

*   **ルーク** (Luke Triton) <V0010>:  
    `<V0010><T>Dear Professor Layton,</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T>It's been a while since we said goodbye. How have you been?</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T>I'm all settled in and making new friends here.</V>`
*   **ルーク** (Luke Triton) <V0040>:  
    `<V0040><T>I am writing to you because something deeply puzzling happened here recently.</V>`
*   **ルーク** (Luke Triton) <V0050>:  
    `<V0050><T>It seems like the sort of mystery that's tailor-made for Professor Layton and his apprentice.</V>`
*   **ルーク** (Luke Triton) <V0060>:  
    `<V0060><T>I don't think anyone else could get to the bottom of this.</V>`
*   **ルーク** (Luke Triton) <V0070>:  
    `<V0070><T>I've enclosed a document with this letter that will tell you more about the situation.</V>`
*   **ルーク** (Luke Triton) <V0080>:  
    `<V0080><T>I can't wait to start this new adventure with you! Please write back as soon as you get this!</V>`
*   **ルーク** (Luke Triton) <V0090>:  
    `<V0090><T>Your friend and apprentice, Luke</V>`

### `14_060010.lbin.txt` — Flavor evacuação Chelmey

*   **チェルミー** (Inspector Chelmey):  
    `<T><A5/0>Be straight with me, Layton. Can you really stop that contraption?</T>`
*   **チェルミー** (Inspector Chelmey):  
    `<T><A4/2>If we let it carry on, there's no telling how much damage it could do to London!</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'll do my best to stop the machine. In the meantime, I need you to get everyone out of here.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Lead everyone to the clock shop and get them above ground as fast as possible.</T>`
*   **チェルミー** (Inspector Chelmey):  
    `<T>Don't worry, Layton. I'll make sure everyone is safe. You focus on stopping that machine.</T>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Thank you, Inspector.</T>`
*   **チェルミー** (Inspector Chelmey):  
    `<T>I'll make sure everyone evacuates the area safely. You just focus on stopping Clive and his machine.</T>`

### `14_060020.lbin.txt` — Jack/Cogg e o lift

*   **ジャック** (Jack / Cogg):  
    `<T>All this time, I never imagined the young sir was planning something so terrible.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You knew Clive's true identity from the start, didn't you?`
*   **ジャック** (Jack / Cogg):  
    `<T>Of course. The wife and I have served the Dove family and the young master for years.`
*   **ジャック** (Jack / Cogg):  
    `<T>He was always such a good boy. When he asked so nicely for my help, I couldn't refuse.`
*   **ジャック** (Jack / Cogg):  
    `<T>Had I known what he was up to, I would never have agreed.`
*   **ジャック** (Jack / Cogg):  
    `<T>It pains me to think that I might have prevented all of this.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Don't be too hard on yourself, Cogg. What's done is done.`
*   **ジャック** (Jack / Cogg):  
    `<T>Well, at the very least, I can try to make up for what I've done.`
*   **ジャック** (Jack / Cogg):  
    `<T>Tell everyone you meet to come here and I'll take them above ground using the lift.`
*   **ジャック** (Jack / Cogg):  
    `<T>I'll make sure everyone down here gets back to the surface safely.`
*   **ジャック** (Jack / Cogg):  
    `<T>Please, just stop the young sir and bring him back to us.`

### `14_060030.lbin.txt` — Samara defende Clive

*   **サマリー** (Samara / Summary):  
    `<T>I just can't believe Clive would do something like this. He was always such a nice boy.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It's clear that Clive took pains to hide his plan from you and your husband.`
*   **サマリー** (Samara / Summary):  
    `<T>You must believe me, Professor. Deep down, Clive is a kind, gentle person.`
*   **サマリー** (Samara / Summary):  
    `<T>I know what it looks like, but he's not a cold-hearted criminal.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I know. I'll do my best to put an end to this and bring him back.`
*   **サマリー** (Samara / Summary):  
    `<T>Thank you, Professor.<W> We'll stay here and help everyone out.`
*   **サマリー** (Samara / Summary):  
    `<T>Professor, don't let Clive do this. You've got to stop him before he goes any further.`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `14_048025`–`14_048030` | **Fuga em colapso (evento)** | Sequência não-enigma de escape: place crumbling + Prime Minister relutante by car; estabelece urgência do timer de 10 minutos herdado do Cap. 13 |
| `14_049010` | **Road Blocked — Travessia Enigma** | Enigma diegético: Now what do we do? The road's blocked! — Luke deve find a way over this mess; retries You'll have to try again / Come on I know you can do it, sucesso Yes! We did it! |
| `14_050010` / `14_060010` | **Evacuação Topside / Clock Shop (evento)** | Chelmey confirma all residents brought topside; sidequest instrui Lead everyone to the clock shop and get them above ground — sem enigma, mas ponto de retorno para final |
| `14_052000` | **Resgate Moral de Clive (evento dublado)** | Sem enigma; Celeste inverte arco de Clive com you can always start again; tema mistakes we scientists made conecta culpa científica de Dimitri/Claire |
| `14_053010` | **Check pós-fuga (evento)** | Flavor Is everyone all right? / I think so — transição para topside |
| `14_054000` | **Confronto Final e Flashback (evento dublado)** | Núcleo dramático sem enigma: apprehend, victim of political agenda, Why did you send for me?, flashback pais inside, second time saved, Chelmey blind criminals / blind government; Barton Yes sir! |
| `14_054050` | **Love vs Pride (evento dublado)** | Exposição curta de Dimitri: suffering in name of research, love or pride, hook one detail you got wrong |
| `14_055000` | **Revelação Temporal de Claire (evento dublado)** | Lore central: hat I gave you, no younger sister, It's me Hershel, shot 10 years into future, molecular instability trying to return to blast, flow of time must remain linear, close the book on the time machine forever — sem enigma |
| `14_059000` | **Carta de Luke (evento dublado epílogo)** | Epílogo em carta: Dear Professor Layton, tailor-made mystery, please write back — gatilho para pós-jogo/sequência |
| `14_060020`–`14_060030` | **Cogg & Samara — Lift de Evacuação (evento)** | Flavors de branching: Cogg knew identity, lift duty I'll take them above ground; Samara kind gentle person — reforçam que Clive escondeu plano até dos tutores Dove |

**Eventos narrativos sem enigmas diretos:** crumbling fortress (`048025`), ceticismo do PM (`048030`), evacuação geral (`050010`), resgate Celeste-Clive (`052000`), confissão e adeus de Clive (`054000`), remorso Dimitri (`054050`), identidade Claire (`055000`) e carta (`059000`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Capítulo de resolução sem dungeon:** Dos 15 arquivos, apenas `14_049010` contém enigma jogável (road blocked); todo o resto é exposição dublada ou evento. É a inversão do Cap. 13, que era dungeon de infiltração — aqui o gameplay é epílogo e evacuação, com 5 arquivos dublados (`052000`, `054000`, `054050`, `055000`, `059000`) carregando o peso emocional.
*   **Celeste = Claire retcon:** A revelação replica estrutura do Cap. 12 (London fake): Layton teoriza, Chelmey traz dado factual verificável (background check no younger sister), Dimitri confirma e Claire confessa. O chapéu (that hat I gave you) é token físico plantado desde o Prólogo; molecular instability e trying to return to its own time dão technobabble para justificar por que Celeste aparece só no endgame e por que seu tempo é limitado — paying for breaking laws of nature.
*   **Duplo salvamento de Clive:** O flashback `14_054000` V0160–V0190 com I need to go back! parents inside ecoa o orphaned child wailing do Cap. 11 e o half building demolished / 10 people killed do Cap. 12; Layton salvou Clive criança do fogo e agora salva do madness — por isso second time you've saved my life estrutura o perdão gentlemanly e o I intend to atone.
*   **Chelmey vs Bill Hawks:** O diálogo `14_054000` V0290–V0330 (Despicable / blinded by own motivations / criminals aren't the only blind ones / Just what are you implying?) fecha o arco político aberto em `12_037000` (He killed Claire and was rewarded...) e `13_042500` (little people); Chelmey, antes bumbling, assume voz moral contra o PM.
*   **Cogg/Jack e Samara como tutores Dove:** `14_060020`/`060030` nomeiam os servidores que criaram Clive após Constance Dove; All this time I never imagined / He was always such a good boy / Please just stop the young sir... espelham a caracterização de Clive como nice boy desviado, reforçando que o plano foi hidden from you and your husband.
*   **Dois vazios intencionais:** `14_000000` e `14_057000` são cabeçalhos sem texto, provável reserva para movie/cutscene não dumpada (fortress collapse / Claire fading). `14_059000` como carta com 9 blocos `<V>` seguidos é marcador de pós-créditos, similar a `12_036000` movie mas com texto.
*   **Structure preservation:** Diálogo mantido em inglês UK original; nomes `Clive`, `Claire`, `Bill Hawks`, `Dimitri`, `Celeste`, `Cogg/Jack`, `Samara` preservados conforme LSCR; `Prime Minister` mantido; `Hershel` usado em falas íntimas de Dimitri/Claire; tags `<W150>` em Thank you e `<A5/0>` no hat preservadas para ritmo de voz.

