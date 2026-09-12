# Capítulo 00 — Prólogo | Professor Layton and the Unwound Future

> **Capítulo 00 — Prólogo** — Análise de dump LSCR para `Textos Originais/txt/uk/00/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/00/`
> Total de arquivos escaneados: **34**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação

---

## 1. Arquivos Cobertos

Todos os 34 dumps `.lbin.txt` em `uk/00`:

```
00_000000.lbin.txt  — [vazio - apenas cabeçalho]
00_001000.lbin.txt  — [vazio - apenas cabeçalho]
00_002000.lbin.txt  — Carta de Future Luke (dublada) + cena no apartamento de Layton/Luke
00_003000.lbin.txt  — [vazio - apenas cabeçalho]
00_004000.lbin.txt  — Banquete: Barton & Chelmey (comendo)
00_004005.lbin.txt  — Banquete: Barton & Chelmey continuação
00_004010.lbin.txt  — Banquete: Bill Hawks e sua esposa (Caroline Hawks)
00_004020.lbin.txt  — Layton & Luke no banquete, observando o guarda
00_004100.lbin.txt  — Guard Smith - puzzle tutorial do intruso
00_005000.lbin.txt  — Revelação da máquina do tempo - MC, Dimitri (como Dr. Stahngun), Bill Hawks
00_006000.lbin.txt  — [vazio - apenas cabeçalho]
00_007000.lbin.txt  — Debrief no apartamento pós-banquete (OP Layton/Luke v3)
00_008000.lbin.txt  — [vazio - apenas cabeçalho]
00_009000.lbin.txt  — "To my dear friend <N>," (placeholder de inserção de nome)
00_009005.lbin.txt  — Em Midland Road - puzzle do mapa + tutorial de movimentação
00_009010.lbin.txt  — Tutorial: Toque no carro (Flores)
00_009013.lbin.txt  — Tutorial: Flores repreende por sair
00_009016.lbin.txt  — Tutorial: Hint coins explicadas (Flores)
00_009020.lbin.txt  — Tutorial: Mala / Índice de Puzzles / Save / Diário
00_009030.lbin.txt  — David na rua - puzzle de memória para localização da relojoaria
00_009040.lbin.txt  — Observação de lojas fechadas
00_009050.lbin.txt  — Homem de Lenço e Bigode (ヒゲマフラー) cameo de hint coin
00_009055.lbin.txt  — Oferta de puzzle das escadas
00_009060.lbin.txt  — Puzzle da porta trancada da relojoaria
00_010000.lbin.txt  — [vazio - apenas cabeçalho]
00_010010.lbin.txt  — Dentro da relojoaria - puzzle de identidade da Mrs. Cogg (サマリー)
00_010015.lbin.txt  — Lembrete para ficar e esperar
00_010020.lbin.txt  — Inspecionando o relógio gigante
00_010030.lbin.txt  — Admirando a parede de relógios
00_010032.lbin.txt  — Esperando o marido voltar
00_010035.lbin.txt  — Ouvindo a porta
00_010040.lbin.txt  — Jack Cogg retorna - puzzle de engrenagem para o relógio gigante
00_010045.lbin.txt  — Lembrete da Mrs. Cogg para ajudar
00_011000.lbin.txt  — [vazio - apenas cabeçalho]
```

> **Nota:** 7 arquivos contêm apenas o cabeçalho LSCR `[701701...]` sem blocos de texto: `00_000000`, `00_001000`, `00_003000`, `00_006000`, `00_008000`, `00_010000`, `00_011000`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 00 |
|---|---|---|
| `ナレーション` | **Narration / Future Luke (voiceover)** | Narra / lê a carta do futuro (`<V0000>`–`<V0060>`) |
| `OPレイトン` / `OPレイトン３` / `レイトン` | **Professor Hershel Layton** | Protagonista, destinatário da carta |
| `OPルーク` / `OPルーク３` / `ルーク` | **Luke Triton** | Aprendiz, autor da carta do futuro |
| `バートン（食）` | **Constable Barton (Eating)** | Alívio cômico no banquete |
| `チェルミー（食）` | **Inspector Chelmey (Eating)** | Gaba-se de sua influência, discute por causa da comida |
| `カレリナ首相夫人` | **Mrs. Caroline Hawks (PM's Wife)** | Reclama da comida e do evento |
| `ビル・ホーク` | **Prime Minister Bill Hawks** | Convidado de honra, voluntário da máquina do tempo |
| `スミス` | **Smith (Security Guard)** | Pede ajuda para encontrar o intruso |
| `披露会場司会者` | **Event MC / Master of Ceremonies** | Apresenta Dr. Stahngun e o PM |
| `変装ディミトリー` | **Dimitri Allen disfarçado como Dr. Alain Stahngun** | Antagonista, "criador" da máquina do tempo |
| `フローレス` | **Flora / Flores (Tutorial Lady)** | Tutorial de moedas de dica no ponto de ônibus |
| `デビット` | **David (Passerby)** | Esquece a localização da relojoaria até o enigma ser resolvido |
| `ヒゲマフラー` | **Moustache-Scarf Man (Dica Coach cameo)** | Gag recorrente - seu discurso sobre moedas de dica é roubado |
| `サマリー` | **Mrs. Cogg (Clock Shop Wife)** | Testa a identidade de Layton via enigma |
| `ジャック` | **Jack Cogg / Cogg (Clockmaker)** | Dono da relojoaria de Midland Road |

Tags de controle observadas: `<V0000>`–`<V0140>` indicam falas dubladas; `<T>` blocos de texto; `<W>` / `<W120>` esperas; `<A1/2>` etc. diretivas de animação; `<K>` efeitos cinéticos/de mão.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 A Carta do Futuro — Apartamento do Professor (`00_002000`)
O prólogo começa com a leitura dublada de uma carta endereçada ao professor, narrada por Future Luke. O remetente descreve uma Londres em caos dez anos no futuro e pede que Layton vá até a relojoaria da Midland Road, em Baldwin, assinando como Luke Triton. No apartamento, Layton deduz que o autor afirma ser o próprio Luke vindo do futuro; Luke reage com incredulidade e brinca sobre um carteiro que viaja no tempo, enquanto Layton observa que, mesmo no futuro, o aprendiz ainda precisaria de sua ajuda — e que essa constância é reconfortante. Diante da dúvida sobre a autenticidade, Layton admite ter poucas pistas, mas intui uma ligação com os acontecimentos terríveis da semana anterior. Mais tarde, após a explosão no banquete (`00_007000`), os dois revisitam a carta: Luke sugere que, se a máquina do tempo for real, a carta também pode ser, e Layton conecta o caso ao desaparecimento misterioso dos maiores cientistas de Londres, concluindo que o próximo passo é investigar a relojoaria.
> Gancho: "I am writing to you from 10 years in the future." / "We haven't much to go on yet."

### 3.2 O Banquete da Máquina do Tempo — Uma Semana Antes (`00_004000`–`00_005000`)
Em flashback para a semana anterior, acontece o banquete de apresentação da primeira máquina do tempo, com convidados ilustres. Na mesa de Chelmey e Barton, o tom é de alívio cômico: Barton come sem parar e questiona o convite, enquanto Chelmey atribui a presença à sua influência na polícia e reclama da comida salgada, comparando-a à de Amelie, o que gera disputa pela costeleta e ameaça de trabalho burocrático. Na mesa dos Hawks, Caroline classifica o evento como farsa e reclama da comida, enquanto Bill responde de forma distraída. Layton e Luke observam deslocados: Luke comenta o desconforto diante do primeiro-ministro e pergunta se a máquina é de verdade; Layton, cético, diz que só acreditará vendo funcionar e sente algo estranho ao notar um guarda procurando um intruso. O guarda Smith confirma o relato de comportamento suspeito e pede ajuda para encontrar o convidado não convidado, o que se resolve com um enigma e elogio a Luke, que então percebe que a apresentação vai começar. No palco, o mestre de cerimônias apresenta o Dr. Alain Stahngun — na verdade Dimitri Allen disfarçado — que agradece anos de pesquisa e reserva um lugar especial ao primeiro-ministro. Hawks se mostra cético, faz um discurso grandiloquente sobre superar limites e inaugurar uma nova era e hesita ao ser convidado para a demonstração; provocado por Stahngun por ter trocado as ciências exatas por uma área mais leve, acaba aceitando por orgulho, apesar do protesto da esposa, antes de Stahngun revelar a máquina e convidá-lo a entrar. O texto extraído não mostra a explosão, mas já antecipa os acontecimentos terríveis da semana seguinte.
> Gancho: "I won't be convinced until I've seen the contraption work for myself." / "Bill! Have you lost your mind?!"

### 3.3 A Caminho da Relojoaria — Midland Road, Baldwin (`00_009000`–`00_009060`)
Já no presente, após decidirem investigar, o grupo segue para Baldwin. Um bilhete com espaço para o nome do jogador marca o arquivo `00_009000`. Em Midland Road, Luke procura a loja e Layton lhe entrega o mapa que acompanhava a carta para que ele mesmo encontre o local por meio de um enigma; depois de resolvido, a narração introduz o tutorial de movimentação pelo ícone de sapato e pelas setas. Em seguida, Flora, no ponto de ônibus, conduz os tutoriais interativos: pede para tocarem no carro, que se desmonta, e explica as moedas de dica — para que servem, limite de uso e o fato de ficarem escondidas em pontos suspeitos — repreendendo o jogador caso saia no meio da explicação. Depois, Luke pergunta como acompanhar o progresso e a narração apresenta a mala, com índice de enigmas, opção de salvar e diário, que Layton diz que usarão bastante. No caminho encontram David, que finge não se lembrar da relojoaria até ter um enigma de memória resolvido e então foge com uma indicação vaga, o que Layton ironiza como maior interesse no enigma do que em ajudar. Observam lojas fechadas que só abririam à noite e o encontro com o Homem de Bigode e Lenço, que tenta repetir a explicação sobre moedas de dica já dada por Flora e lamenta ter perdido seu único momento de fala, confirmando que já se encontraram antes. Há ainda um enigma opcional das escadas que levam a casas vitorianas e, ao chegar à relojoaria, a porta trancada exige um enigma de abertura antes da entrada.
> Gancho: "Hint coins are tucked away all over the place, so touch anything that looks fishy." / "The door's locked."

### 3.4 Dentro da Relojoaria (`00_010010`–`00_010045`)
Dentro da loja, Mrs. Cogg recebe Layton e Luke após um longo período sem clientes, pede para ver a carta e confirma que ela indica a loja, embora não reconheça o remetente, mas diz conhecer Layton dos jornais que lê diariamente. Luke celebra a fama do professor, e ela finge ofensa ao comentário sobre a loja ser longe do centro, defendendo que o local é sim central. Para provar que não é um sósia, exige que ele resolva um enigma de identidade; convencida, afirma que o marido deve saber mais e pede que esperem explorando a loja. Enquanto aguardam, Luke se impacienta e Layton o acalma; ao explorarem, admiram o relógio gigante parado e a parede de relógios bem construídos, oportunidades para enigmas opcionais. O retorno de Jack Cogg acontece com entusiasmo por um achado, surpresa com os clientes e pedido de desculpas por não esperá-los tão cedo; Luke se apresenta como aprendiz, o que faz Cogg hesitar brevemente ao ouvir o nome. Cogg revela ter instruções para mostrar o maior relógio em funcionamento, mas não se lembra onde inserir a última engrenagem e pede que Layton resolva o enigma final do prólogo. Após o acerto, ele se prepara para acioná-lo, enquanto Mrs. Cogg reforça o convite para ficarem e ajudarem.
> Gancho: "I won't believe you're the real Professor Layton until you solve this puzzle!" / "That did the trick! Just wait here, and I'll go and start her up!"

> **Cliffhanger:** O relógio gigante, prestes a ser ativado como passagem disfarçada, encerra o prólogo e conduz diretamente à Londres do futuro do Capítulo 01.
## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag) — <Vxxxx> se dublado` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, mas esperas `<W>` anotadas.

### `00_002000.lbin.txt` — A Carta e o Apartamento

*   **ナレーション (Narration / Future Luke) `<V0000>`:**  
    `Professor, I hope this letter finds you well. As for me, I am in quite a predicament.`
*   **ナレーション `<V0010>`:**  
    `You see, the London we know and love has been thrown into absolute chaos.`
*   **ナレーション `<V0020>`:**  
    `To complicate matters, the calamity I speak of does not take place in your time.`
*   **ナレーション `<V0030>`:**  
    `This may be difficult to believe, but I am writing to you from 10 years in the future.`
*   **ナレーション `<V0040>`:**  
    `I know this is a lot to take in, but I'll explain it all soon.`
*   **ナレーション `<V0050>`:**  
    `For now, I ask that you head to the clock shop on Midland Road in Baldwin.`
*   **ナレーション `<V0060>`:**  
    `I look forward to seeing you again. Your student, Luke Triton`
*   **OPレイトン `<V0070>`:**  
    `Strange as it sounds, it seems that the author of this letter is none other than your future self, Luke.`
*   **OPルーク `<V0080>` / `<V0101>`:**  
    `From...my future self? But how is that even possible?`
*   **OPレイトン `<V0090>`:**  
    `I don't know, but it does raise the question: if this letter is indeed authentic, how did it get here?`
*   **OPルーク `<V0100>`:**  
    `Um... By time-travelling postman? Just joking, of course!`
*   **OPルーク `<V0101>`:**  
    `But seriously, I think this mystery might be the strangest we've ever encountered!`
*   **OPレイトン `<V0110>` / `<V0111>`:**  
    `Indeed. And even in the future, you seem to need my help in solving it. Your constancy can be quite a comfort in these uncertain times, my boy.`
*   **OPルーク `<V0120>`:**  
    `Er... Well, thank you, I think. But back to the letter - how do we know it's real?`
*   **OPレイトン `<V0130>` / `<V0135>`:**  
    `Hmm... Well, we haven't much to go on yet. But I can't help but think that this strange occurrence is connected to the terrible events of last week.`
*   **OPルーク `<V0140>`:**  
    `Hmm...`

### `00_004000.lbin.txt` — Chelmey & Barton (i)

*   **バートン（食） `<V0010>`:** `Chomp... Quite the, er, spread we have here, Inspector. Chomp...`
*   **バートン（食） `<V0020>`:** `Though it does make me wonder what we did to deserve invitations to such a feast.`
*   **チェルミー（食） `<V0030>` / `<V0031>`:** `It's obvious, Barton. I'm an influential man in the world of law enforcement. It's only natural I'd be invited to an important event such as this.`
*   **バートン（食） `<V0040>`:** `Er, I suppose that's possible...`
*   **チェルミー（食） `<V0050>`:** `Possible, you say?`
*   **バートン（食） `<V0060>`:** `Ummm - gulp - erm...probable! Highly probable, sir!`

### `00_004005.lbin.txt` — Chelmey & Barton (ii)

*   **チェルミー（食）:** `Hrm. Well, the food certainly isn't anything to write home about.`
*   **バートン（食）:** `Sorry you feel that way, sir. I think it's quite - chomp chomp - scrumptious, myself.`
*   **チェルミー（食）:** `Bah. This over-salted chop and pile of wilted greens have nothing on Amelie's cooking.`
*   **バートン（食）:** `If that's how you feel, sir, I'd be happy to relieve you of that, um, burden.`
*   **チェルミー（食）:** `Now see here, Barton! If you don't return my chop at once, I'll have you driving a desk next week!`
*   **バートン（食）:** `It would be worth it! Mmm... This crackling is, um, cracking!`
*   **チェルミー（食）:** `Hrm! They don't seem to be in any hurry to get this show started.`
*   **バートン（食）:** `Come on, sir, it's not all bad. At least there's - shlurp - food to enjoy while we wait.`
*   **チェルミー（食）:** `Honestly, I'm knee-deep in case work. I haven't got the time for fancy banquets.`
*   **バートン（食）:** `Chomp! Oh my, sir, you should try this. It's - chomp chomp - absolutely lovely.`

### `00_004010.lbin.txt` — Casal Hawks

*   **カレリナ首相夫人 `<V0010>`:** `Oh, this food is simply dreadful, Bill. Do get this over with quickly so we can leave.`
*   **ビル・ホーク `<V0020>`:** `Yes, dear...`
*   **カレリナ首相夫人:** `This event is a complete charade! Don't you agree, Bill?`
*   **ビル・ホーク:** `Hmmm? What's that? Oh yes, a complete charade.`
*   **カレリナ首相夫人:** `Well, I hope the presentation is brief. We do have places to be, you know.`

### `00_004020.lbin.txt` — Layton & Luke no Banquete

*   **ルーク `<V0010>`:** `I have to say, I feel a bit out of place here, Professor.`
*   **レイトン `<V0020>` / `<V0021>`:** `That's quite understandable, Luke. I'm sure most people would feel the same way in the presence of the prime minister.`
*   **ルーク `<V0030>`:** `Hey look! I think I see Inspector Chelmey over there!`
*   **レイトン `<V0040>`:** `Hmm...`
*   **ルーク `<V0050>` / `<V0051>`:** `So, Professor, what do you think about this whole event? Do you think that someone has really built a working time machine?`
*   **レイトン `<V0060>` / `<V0061>`:** `I'm not entirely sure. Still, if it proves to be true, can you imagine the stir it will cause in the scientific community?`
*   **ルーク `<V0070>`:** `Well, I think it's really exciting! Though you don't sound entirely convinced, Professor.`
*   **レイトン `<V0080>` / `<V0090>`:** `Anything's possible, Luke. But I won't be convinced until I've seen the contraption work for myself. And I must confess, something about this entire presentation seems a bit...off.`
*   **ルーク `<V0100>` / `<V0101>`:** `Why do you say that? Ah, of course. That must be your famous intuition talking, eh?`
*   **レイトン `<V0110>` / `<V0130>`:** `That's one way of putting it. But enough speculation. Look over there, Luke. He seems to be looking for a man who snuck into the event uninvited.`
*   **ルーク `<V0120>` / `<V0140>`:** `That guard? What about him? Ooh! So we have an intruder in our midst!`

### `00_004100.lbin.txt` — Guarda Smith

*   **スミス:** `Oh crumbs, I've really blown it this time...`
*   **レイトン:** `You look troubled, sir. Might we be of assistance?`
*   **スミス:** `Assistance? Oh yes, please! See, I've just received a report of some untoward behaviour... I'll never find this scoundrel on my own. I'm done for! You'll help me find that uninvited guest, won't you?`
*   **レイトン:** `Splendid work, my boy!` *(pós-puzzle)*
*   **スミス:** `Phew! Thanks so much for your help. There'll be no more scrounging on my watch!`
*   **ルーク:** `Did you see that, Professor? I just assisted in the apprehension of a suspect! Oh! Looks like the presentation is about to begin! Let's get back to our seats.`

### `00_005000.lbin.txt` — Revelação da Máquina do Tempo (24 falas, dubladas)

*   **披露会場司会者 `<V0010>` / `<V0011>`:** `Ladies and gentlemen! Thank you for taking part in an event that will undoubtedly go down in scientific history.`
*   **披露会場司会者 `<V0020>`:** `And here to demonstrate mankind's first time machine is its creator, Dr Alain Stahngun!`
*   **変装ディミトリー `<V0040>` / `<V0041>`:** `Thank you, my esteemed colleagues. After years of research in the field of time travel, I am pleased to share the fruits of my labour.`
*   **変装ディミトリー `<V0050>`–`<V0061>`:** `In just a few short moments, I will be moving on to our scheduled demonstration. But first, I am delighted to announce that Prime Minister Bill Hawks is in attendance today. As such, I have reserved a very special seat for our very special guest.`
*   **変装ディミトリー `<V0070>`:** `Please join me on stage, Prime Minister. No need to be shy!`
*   **ビル・ホーク `<V0080>`:** `Is this thing real?`
*   **変装ディミトリー `<V0090>`:** `What do you mean?`
*   **ビル・ホーク `<V0100>`:** `I mean, is this contraption a genuine, working time machine?`
*   **変装ディミトリー `<V0110>`:** `Why don't you have a seat and see for yourself?`
*   **披露会場司会者 `<V0120>`:** `Before we start, would you honour us with a few words, Prime Minister?`
*   **ビル・ホーク `<V0130>` / `<V0131>` / `<V0150>` / `<V0151>` / `<V0160>` / `<V0161>` / `<V0170>`:** `Good afternoon, everyone! Today is a monumental day not only for our great nation, but for the entire human race. Since the beginning of time, we humans have strived to transcend our natural limits. We have conquered the skies and the seas, and we have even travelled to outer space. But the one frontier that has always eluded us is time. Indeed, travelling through time is a dream many thought was out of reach for humanity...until now. Ladies and gentlemen, I hope you will join me in ushering in a new era for mankind!`
*   **披露会場司会者 `<V0190>` / `<V0200>`:** `Thank you for those words, Prime Minister. And now for the moment you've all been waiting for! Please take it away, Dr Stahngun!`
*   **変装ディミトリー `<V0210>` / `<V0211>` / `<V0220>`:** `I have just one more request before we start. I'd very much appreciate the prime minister's assistance in this demonstration. What do you say, Mr Hawks?`
*   **ビル・ホーク `<V0230>`:** `Wh-what?!`
*   **変装ディミトリー `<V0250>`:** `I assure you, there's no cause for concern.`
*   **ビル・ホーク `<V0260>`:** `But I was under the impression that I would merely be observing the proceedings...`
*   **変装ディミトリー `<V0270>` / `<V0280>` / `<V0281>`:** `Ah well, do forgive my presumption. It was never my wish to make you uncomfortable. I realise it's been some time since you traded in the hard sciences for the softer variety. Please feel free to return to your seat, Prime Minister.`
*   **ビル・ホーク `<V0290>`:** `Wait! What I mean to say is, of course I can assist you.`
*   **カレリナ首相夫人 `<V0320>`:** `Bill! Have you lost your mind?!`
*   **変装ディミトリー `<V0330>` / `<V0340>` / `<V0341>`:** `Ah, that's the courage we've come to expect from our fearless leader. You have my thanks. And now, without further ado, I give you my time machine! Mr Hawks, would you mind just stepping inside?`

### `00_007000.lbin.txt` — Debrief Pós-Banquete (Apartamento)

*   **OPルーク３ `<V0010>`:** `So, you think that what happened last week is somehow connected to this letter...`
*   **OPルーク３ `<V0020>`:** `Wait! Maybe if the time machine was real, this letter is real, too!`
*   **OPレイトン３ `<V0030>` / `<V0031>`:** `I don't know about that, but these two elements aren't the only puzzling issues. Tell me, Luke, have you heard about the recent disappearances occurring here in London?`
*   **OPルーク３ `<V0040>` / `<V0041>`:** `Oh yes, I read about it in the paper. Some of London's greatest scientists have been mysteriously vanishing.`
*   **OPレイトン３ `<V0050>` / `<V0060>`:** `Yes, and I can't shake the feeling that those disappearances are linked to this whole affair. In any case, it seems our best course of action is to head to the location mentioned in the letter.`
*   **OPルーク３ `<V0070>`:** `Good idea!`

### `00_009000.lbin.txt` — Inserção de Nome

*   **ルーク:** `To my dear friend <N>,` *(placeholder para nome do jogador)*

### `00_009005.lbin.txt` — Busca em Midland Road + Tutorial de Movimentação

*   **ルーク:** `Well, here we are. The clock shop that the letter mentioned should be around here somewhere. But where?`
*   **レイトン:** `This seems an ideal time to consult the map that accompanied the letter.`
*   **レイトン:** `Here, Luke. See if you can find the shop's location by yourself.`
*   **ルーク:** `Say no more, Professor!`
*   **ルーク:** `Hmm. This is more difficult than I expected.`
*   **ルーク:** `Let me give this puzzle another shot!` *(tentar novamente)*
*   **ルーク:** `Great! Getting to that clock shop should be a doddle now. Let's go, Professor!` *(resolvido)*
*   **ナレーション:** `All right. But before we head off, let's quickly review how to move around. Care to assist me, Luke? I know the drill, Professor. I can take it from here. Let's see... To start, touch the shoe icon. Once you've touched the shoe, arrows will appear. Touch an arrow to move in that direction.`
*   **レイトン:** `That's right. So just remember, whenever you want to move, start by touching the shoe.`

### `00_009010.lbin.txt` — Tutorial de Toque (Flores)

*   **フローレス:** `Well hello there, you strapping young things! I can tell from the looks on your faces that you're just dying to hear something useful! All right, here's my pearl of wisdom. Go and touch that car parked over there.`
*   **フローレス:** `Oi! Get your hands off me! Touch that car parked over there, I said!` *(se o jogador tocar em Flores)*
*   **ルーク:** `But...what about the car?`
*   **フローレス:** `Dear me, you've made quite a mess, haven't you? Now why did you go and do a thing like that?`
*   **ルーク:** `It wasn't m-my fault! You were the one who told me to touch it!`
*   **フローレス:** `Oh, did I now? I certainly don't recall saying anything of the sort.`

### `00_009013.lbin.txt` — Repreensão de Flores

*   **フローレス:** `Hey, you two! Don't go rushing off! I've got things to tell you! Important things!`
*   **フローレス:** `Hmph! Didn't anyone ever teach you any manners? You can't just walk off when I'm mid-lecture!`

### `00_009016.lbin.txt` — Hint Coins

*   **ルーク:** `Oh no! It just fell apart!`
*   **フローレス:** `Never mind that! Did you see the coin that just popped out? That's a hint coin, and it's yours to keep. If you ever find yourself stuck on a puzzle, you can spend one of those lovely coins to get a hint. Just remember that there's a limit to the number of hint coins you can find. If you use them willy-nilly, you may find yourself in a pickle later. Hint coins are tucked away all over the place, so touch anything that looks fishy. You might find a coin! Well, that's the end of my speech. Good luck with whatever it is you're doing round here. Ta-ta!`

### `00_009020.lbin.txt` — Tutorial da Mala

*   **ルーク:** `Say, Professor, how are we going to keep track of our progress?`
*   **ナレーション:** `Ah yes. I suspect we could both use a refresher on that subject. To start, touch the trunk icon located in the top-right corner of the Touch Screen. This will open the trunk, where you can access several useful options by touching their icons. This is the Puzzle Index. This option allows you to review puzzles you've found during the adventure. This is the Save option. Touch this option to save your progress throughout the adventure. This is the Puzzle Index. This option allows you to review puzzles you've found during the adventure. Solved puzzles are marked with a tick. Those you're yet to solve are blank. Any previously solved puzzle can be replayed from this menu. In order to have another go at an unsolved puzzle, however, you'll need to return to its location. Finally, this is the Journal. Touch the Journal to review the events of the story.`
*   **ルーク:** `Got it, Professor!`
*   **レイトン:** `That's good to hear, Luke. I imagine we'll be making good use of the trunk during our investigation.`

### `00_009030.lbin.txt` — David

*   **デビット:** `You're looking for a clock shop, you say? Hmm. Nah, can't say I know of one around here.`
*   **ルーク:** `All right. Well, thanks anyway.`
*   **デビット:** `Oh, wait a minute! On second thoughts, I think I passed a clock shop just the other day.`
*   **ルーク:** `Terrific! Do you remember where it was?`
*   **デビット:** `Hmm... That I'm not sure of. I have trouble remembering stuff when I have other things on my mind... Help me with this puzzle that's been bothering me and I might be able to remember where I saw that shop.`
*   **ルーク:** `You're in luck, sir! I happen to be a bit of a whizz when it comes to puzzles!`
*   **デビット:** `Yeah, until that puzzle gets solved, I don't think I'll be able to remember a thing. This puzzle's demanding all my attention. Solve it for me so I can remember where that clock shop is.`
*   **デビット:** `Hey, nice going, kiddo.` *(resolvido)*
*   **ルーク:** `Thanks. So, about that clock shop...`
*   **デビット:** `Right, the clock shop. It's somewhere on this road...I think. Well, got to dash! See you later!`
*   **ルーク:** `Wait! Oh. He ran off.`
*   **レイトン:** `Ha ha ha! Something tells me he was more interested in getting us to solve his puzzle than in helping us. Not to worry, though. I'm sure we'll be able to find the clock shop on our own. It's probably just a bit further down this road.`

### `00_009040.lbin.txt` — Lojas Fechadas

*   **ルーク:** `None of the shops around here seem to be open.`
*   **レイトン:** `They don't, do they? But many of them look as though they only open in the evening.`

### `00_009050.lbin.txt` — Homem de Bigode e Lenço

*   **ヒゲマフラー:** `Keh heh heh! Don't think I've seen you two whippersnappers before.`
*   **ルーク:** `Are you sure about that? I've got a feeling we've met somewhere...`
*   **ヒゲマフラー:** `Keh heh heh! Oh no, no, no, you must be thinking of someone else. But anyhoo, I've got some juicy information that you two might want to hear.`
*   **レイトン:** `Ah, if you're going to tell us about hint coins, then I should stop you now. A kind lady by the bus stop already gave us a comprehensive explanation.`
*   **ヒゲマフラー:** `What?! But...explaining hint coins is just about the only time we ever get to chat. How could you let someone else give my speech?`
*   **ルーク:** `You mean you've given us that talk before? So we HAVE already met!`
*   **ヒゲマフラー:** `Erm... Ahem. I'm suddenly not feeling too chipper. I'd better head home. I'll be seeing you 'round!`

### `00_009055.lbin.txt` — Escadas

*   **ルーク:** `Where do you suppose these stairs go to, Professor?`
*   **レイトン:** `I'd say they probably lead up to that row of charming Victorian houses. Say, Luke, all this talk of stairs has reminded me of a puzzle. Care to hear it?`
*   **ルーク:** `Would I ever!`
*   **ルーク:** `I suppose I'm not in the mood for a puzzle after all.` *(recusa)*
*   **レイトン:** `Let's give that stairs puzzle another go.` *(tentar novamente)* / `Exemplary thinking, Luke. Now let's get back on track.`
*   **レイトン:** `There probably aren't any clock shops in a quiet residential area like that.`

### `00_009060.lbin.txt` — Puzzle da Porta

*   **ルーク:** `This must be the place, Professor!`
*   **レイトン:** `Yes, finally.`
*   **ルーク:** `Let's go inside! Huh?`
*   **レイトン:** `What seems to be the matter, Luke?`
*   **ルーク:** `The door's locked. How are we supposed to get in?`
*   **レイトン:** `Let me have a look. Ah, it seems it's time for a puzzle. We have to solve this one to open the door.`
*   **ルーク:** `There's nothing wrong with taking a break, but we won't be able to enter until we solve that puzzle.` *(recusa)*
*   **レイトン:** `The door is fitted with a puzzle. We'll need to solve it to gain entry.` *(tentar novamente)*
*   **ルーク:** `That did the trick!`
*   **レイトン:** `There's no sense dawdling outside. Come now, in we go.` *(resolvido)*

### `00_010010.lbin.txt` — Entrevista com Mrs. Cogg

*   **サマリー:** `Oh gracious, customers! We haven't had any of those in ages. Welcome!`
*   **レイトン:** `Good day to you, madam. You'll have to excuse us, we're not here to buy anything, I'm afraid. I received a letter the other day, you see, instructing me to come here.`
*   **サマリー:** `Tee hee hoo. A letter, you say? Let me have a look at it, dearie. Hmm, yes. There's no mistake here. Whoever sent you this letter wanted you to visit our little shop.`
*   **レイトン:** `So you don't know who sent it to me?`
*   **サマリー:** `Unfortunately, I can't say that I do. But I do know who you are, Professor Layton!`
*   **ルーク:** `Oh really? And how do you know the professor?`
*   **サマリー:** `Tee hee hoo! Well, it's hard not to know a man who's in the papers so often. And I do so love my morning paper. I read it front to back, every day. So of course I know about the professor.`
*   **ルーク:** `Hey, did you hear that, Professor? Further proof that you're famous throughout London. Even all the way out here!`
*   **サマリー:** `Hey now! What do you mean, ''all the way out here''? Just because we don't fancy living in sardine-tin flats doesn't mean we're not central! Still, it is quite a shock to see the famous Professor Layton in the flesh. Such a shock, in fact, that I'm going to need some proof that you're not one of those lookalikes! They say there isn't a puzzle around that you can't solve, but I won't believe it until I see it! I won't believe you're the real Professor Layton until you solve this puzzle!`
*   **サマリー:** `Well, I must say that I'm thoroughly convinced. You certainly do live up to your reputation.` *(resolvido)*
*   **ルーク:** `Of course he does!`
*   **サマリー:** `Yes, well, about that letter... I can't say I've seen it before, but my husband might know something. He's out at the moment, but he should be back soon. Why not look around the shop while you wait?`
*   **サマリー:** `My husband will be back soon, so just have a look around the shop while you wait.` *(repetição se falar novamente)*

### `00_010015.lbin.txt` — Ficar no Local

*   **レイトン:** `We shouldn't wander off anywhere until we've got some answers.`

### `00_010020.lbin.txt` — Relógio Gigante

*   **ルーク:** `Wow, can you believe this clock?`
*   **レイトン:** `It certainly is impressive. Unfortunately, it doesn't appear to work.`
*   **ルーク:** `Then it's a good job there's so many other ways of telling the time here.`
*   **レイトン:** `Oh, you've just reminded me of a splendid puzzle, Luke.`
*   **レイトン:** `I suppose we can finish this puzzle later.` / `You know, Luke, you have yet to solve the clock puzzle I mentioned earlier.` *(recusa/tentar novamente)*
*   **ルーク:** `You know, I've never seen a clock this big up close. It's a real shame that it's not in working order.` / `This clock is just fantastic.` *(inspecionar)*

### `00_010030.lbin.txt` — Parede de Relógios

*   **ルーク:** `I've never seen so many clocks in one place!`
*   **レイトン:** `Yes, and they're all extremely well made. Whoever built them must be very talented.`
*   **ルーク:** `Really? How can you tell that just by looking at them?`
*   **レイトン:** `Ho ho! One gains an eye for these things with age, my boy. You know, this might be the ideal time for this clock puzzle of mine. Care to try it?`
*   **ルーク:** `You bet I would, Professor!`
*   **レイトン:** `Giving up, are you? Very well.` / `Let's revisit that puzzle about the clock, shall?` / `Spot on, Luke. Good work.` *(recusa/tentar novamente/resolvido)*

### `00_010032.lbin.txt` — Espera

*   **ルーク:** `We've been here for quite some time now. I do wish that lady's husband would hurry back.`

### `00_010035.lbin.txt` — Porta Ouvida

*   **ルーク:** `Oh, I think I just heard the door! Someone's here!`

### `00_010040.lbin.txt` — Jack Cogg

*   **サマリー:** `That'll be my husband.`
*   **ジャック:** `Wait till you see the little gem I picked up today, love... Oh my, customers!`
*   **サマリー:** `Welcome back, dear. This here is Professor Layton. He tells me he has some business in our shop.`
*   **ジャック:** `Layton? You're Professor Layton? My apologies! I wasn't expecting you so soon!`
*   **レイトン:** `No apology necessary, my good man. Oh, and allow me to introduce my-`
*   **ルーク:** `Apprentice! I'm the professor's apprentice, Luke! Pleased to meet you, sir!`
*   **ジャック:** `Luke, you say? Hmm... What I mean to say is, those are some fine manners, lad! It's nice to meet you too. The name's Cogg.`
*   **レイトン:** `You seemed a bit flustered by our arrival, Cogg. We certainly don't mean to impose...`
*   **ジャック:** `Oh no, no, no. It's no trouble at all. It's just that I had instructions to show you our biggest clock in action upon your arrival.`
*   **レイトン:** `It certainly is a beauty. Pity it's not in working order.`
*   **ジャック:** `Yes, I'd planned to give her a tune-up before you stopped by, so you could see her in all her glory. But I'm getting on a bit these days, and I have trouble keeping the old girl in good repair. I can't remember where to insert this last gear, and the clock won't work without it.`
*   **レイトン:** `Ah, I see. That does indeed sound problematic.`
*   **ジャック:** `Maybe you can help. The papers say you're a learned man. Can you work out where this gear goes?`
*   **レイトン:** `Hmm? Me? Well, I'd like to help, but I'm no expert in mechanics...`
*   **ジャック:** `Well, at least give it a try. Don't you want to see our biggest clock in its full working glory?`
*   **レイトン:** `I certainly do. Very well, I'll give it a shot.`
*   **ジャック:** `Sorry, Professor. Until we get that gear back in place, I can't show you the clock in motion. Can you work out where this gear goes, Professor?` *(recusa/tentar novamente)*
*   **ジャック:** `That did the trick! Just wait here, and I'll go and start her up! Here goes!` *(resolvido)*

### `00_010045.lbin.txt` — Lembrete

*   **サマリー:** `Tee hee hoo! Didn't you want to talk to my husband? Do stay and help my dear husband mend that big clock. We would both be very grateful!`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `00_004100` | **Find the Intruder** | Enigma tutorial do guarda Smith - dedução lógica para identificar o convidado não convidado. |
| `00_009005` | **Map to the Clock Shop** | Use o mapa da carta para localizar a loja. Tutorial de movimentação (ícone de sapato → setas). |
| `00_009010` + `00_009016` | **Touch / Moedas de Dica** | Tutorial interativo: tocar no cenário revela moedas de dica escondidas. |
| `00_009020` | **Maleta System** | Explica Salvar, Índice de Enigmas (visto para resolvidos), Diário. |
| `00_009030` | **David's Memory Enigma** | David não lembrará a localização da loja até o enigma ser resolvido - bloqueio clássico de NPC de Layton. |
| `00_009055` | **Stairs Enigma** | Enigma opcional acionado ao examinar as escadas para as casas vitorianas. |
| `00_009060` | **Locked Door Enigma** | Enigma de bloqueio para entrar na relojoaria. |
| `00_010010` | **Identity Verification Enigma** | Mrs. Cogg exige prova de que Layton é o verdadeiro professor. |
| `00_010020` / `00_010030` | **Clock Enigmas (opcional)** | Dois enigmas temáticos de relógios enquanto esperam por Cogg. |
| `00_010040` | **Gear Insertion Enigma** | Enigma final do prólogo: posicionar a engrenagem faltante para consertar o relógio gigante. O relógio então é ativado. |

**Eventos narrativos sem enigmas:** A demonstração catastrófica da máquina do tempo (a explosão de `00_005000` está *fora do texto* extraído, mas é prenunciada), e a construção gradual de mundo que estabelece: (a) viagem no tempo como espetáculo público, (b) desaparecimentos de cientistas, (c) os Coggs como guardiões da passagem para a London do Futuro.

---

## 6. Notas de Localização & Observações Técnicas

*   **Agrupamento de voz:** `00_002000` é totalmente dublado (`<V0000>`–`<V0140>`); `00_005000` é fortemente dublado (`<V0010>`–`<V0341>`); a maioria dos arquivos de exploração (`00_009xxx`, `00_010xxx`) não é dublada (apenas `<T>`), indicando conversas de gameplay fora de cutscene.
*   **Placeholder de nome:** `00_009000` contém literalmente `To my dear friend <N>,` — ponto confirmado de inserção do nome do jogador (consistente com convenções `<<NAME>>` em outros lugares).
*   **Texto repetido:** `00_009020` duplica a explicação do Índice de Enigmas literalmente (dois blocos consecutivos); provavelmente prompt duplo intencional no jogo.
*   **Dumps vazios:** Sete arquivos são apenas de cabeçalho e servem como separadores de segunda ordem para limites de capítulo (comum no LSCR da Level-5 para preencher fronteiras de capítulo).
*   **Codificação de personagens:** Tags como `ヒゲマフラー` (hige-mafurā = lenço-barba) e `サマリー` (samarī = summary) são codinomes internos; nomes externos mapeados para traduções de fãs em inglês / créditos do jogo (Mrs. Cogg, Beardy).

---

*Gerado a partir de dumps LSCR brutos — 34/34 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/00`. Próximo capítulo: `01` — Future London.*
