# Capítulo 09 — Infiltração no Towering Pagoda, o Falso Layton e Dimitri | Professor Layton and the Unwound Future

> **Capítulo 09 — Infiltração no Towering Pagoda / O Falso Professor Desmascarado e a Verdade de Dimitri** — Análise de dump LSCR para `Textos Originais/txt/uk/09/*.txt`
> Caminho de origem: `/Textos Originais/txt/uk/09/`
> Total de arquivos escaneados: **32**
> Idioma: Inglês UK (texto original do jogo)
> Tags preservadas: `<Vxxxx>` = ID de voz, `<T>` = bloco de texto, `<W>` = espera, `<A>` = animação, `<K>` = efeito cinético, `<Q>` = questão

---

## 1. Arquivos Cobertos

Todos os 32 dumps `.lbin.txt` em `uk/09`:

```
09_000000.lbin.txt  — [vazio - apenas cabeçalho]
09_026490.lbin.txt  — Segal - aviso lion s den e puzzle de preparation
09_026500.lbin.txt  — Rudolph - hoo hoo, rendezvous com Pepper, Myrtle
09_026510.lbin.txt  — Vivian (ビビアン) - comentário sobre gentleman apressado
09_026520.lbin.txt  — Pepper (ポルテ) - Noodle Palace, noodle puzzles
09_026530.lbin.txt  — Deloy (デロイ) - guarda do portão, boss puzzle gate
09_026540.lbin.txt  — Desaparecimento do professor - bilhete nas costas de Flora
09_026545.lbin.txt  — Future Luke - press on without him
09_026550.lbin.txt  — Barmey/Walton (ワルートン) - casino rampage, puzzle de bloqueio
09_026560.lbin.txt  — Reencontro dublado - Sorry to keep everyone waiting
09_027010.lbin.txt  — Porta do dragão - olhos como chave, puzzle de Luke
09_027020.lbin.txt  — Goggles - personal projection device / memory recorder foreshadow
09_027030.lbin.txt  — Corredor sombrio - gloomy dragons
09_027040.lbin.txt  — Walmy (ワルミー) vs Future Luke - bullying Barmey, puzzle
09_027050.lbin.txt  — Sala de espelhos - porta oculta no escuro
09_027055.lbin.txt  — Top floor - Estamos perto
09_027060.lbin.txt  — Sliding block gigante - piso puzzle antes do falso Layton
09_027070.lbin.txt  — Abertura da porta - encontro iminente
09_029000.lbin.txt  — Falso Layton dublado - I demand an explanation, charlatan
09_029010.lbin.txt  — Teste do impostor - blocos, memória e caneta vazia
09_030010.lbin.txt  — Dimitri dublado - Hats off, time machine, Claire, memory recorder (42 blocos)
09_030020.lbin.txt  — Relevo de tropas - 5 vs 5 estrelas, empate estratégico
09_031010.lbin.txt  — Armadilha dupla dublado - two Laytons, genuine article
09_032010.lbin.txt  — Don Paolo como decoy - ace in the hole e fechadura
09_032030.lbin.txt  — Tables have turned - diversions, Bostro, fuga com PM, alarme
09_032035.lbin.txt  — Caminho bloqueado - Family waiting below
09_032040.lbin.txt  — Trapdoor e mapa de túneis - split em dois grupos
09_032050.lbin.txt  — Stairwell - parede que é porta
09_032060.lbin.txt  — Saída do pagoda - put some distance
09_032080.lbin.txt  — Aviso - foolish to return under heavy guard
09_032090.lbin.txt  — Exposição longa dublada - Don Paolo como Schrader/Delmona, Claire (61 blocos)
09_033010.lbin.txt  — Don Paolo arqui-inimigo - Paul da universidade, sleuthing, retorno ao hotel
```

> **Nota:** 1 arquivo contém apenas o cabeçalho LSCR sem blocos de texto: `09_000000.lbin.txt`.

---

## 2. Personagens Presentes

| Tag Japonês | Nome em Inglês | Papel no Cap. 09 |
|---|---|---|
| `レイトン` | **Professor Hershel Layton** | Protagonista, infiltra Pagoda, desmascara falso, confronta Dimitri, planta diversions e explica Don Paolo |
| `ルーク` | **Luke Triton** | Aprendiz, resolve porta do dragão, questiona sumiço, testemunha revelação de Claire |
| `未来ルーク` | **Future Luke (Big Luke)** | Guia, enfrenta Barmey/Walmy, propõe split nos túneis, avisa alarme |
| `アロマ` | **Flora Reinhold (Aroma)** | Alvo do bilhete nas costas, reagente ao goggles/ espelhos, separada no split |
| `セガール` | **Segal** | Reaparece em Chinatown, avisa lion's den e oferece enigma de preparação |
| `ルドルフ` | **Rudolph** | Gag de Pepper/Myrtle, libera grupo para pagoda |
| `ビビアン` | **Vivian** | Flavor line sobre gentleman apressado |
| `ポルテ` | **Pepper (Noodle Palace)** | Dono do restaurante, oferece noodle enigmas |
| `デロイ` | **Deloy (Portão Guard)** | Guarda do portão do Family, enigma portão a mando do boss |
| `ワルートン` | **Barmey / Walton (Family - small)** | Tenta bloquear casino rampage, enigma |
| `ワルミー` | **Walmy (Family - Barmey's brother)** | Irmão maior de Barmey, vicious enigma na subida |
| `にせレイトン` | **False Layton (Impostor)** | Antagonista do teste de blocos/memória, charlatan desmascarado |
| `ディミトリー` | **Dimitri Allen** | Vilão revelado, construtor da time machine, amava Claire, usa memory recorder |
| `ドン・ポール` | **Don Paolo (Paul)** | Ás na manga, decoy preso, revelado como Schrader/Delmona, calouro apaixonado por Claire |
| `レイトン（ゴーグル）` | **Layton (Goggles)** | Layton durante uso do projection device |
| `未来シュレーダー` | **Future Dr Schrader (Don Paolo)** | Flashback da saudação que entregou o disfarce |
| `ボストロ` | **Bostro** | Tenente da Family, resgata Dimitri com PM |
| `ナレーション` | **Narration** | Voz que anuncia falha da armadilha (two Laytons) |
| `ナゾバトル` | **Enigma Battle (System)** | Texto de sistema do enigma de tropas |

Tags de controle observadas: `<V0010>`–`<V0560>` dublados em `09_026560`, `09_029000`, `09_030010`, `09_031010`, `09_032010`, `09_032090`, `09_033010`; restante `<T>` não-dublado de exploração/enigma. `<W>` pausas; `<A1/1>`–`<A6/0>` animações; `<K>` silêncio tenso; `<Q>`/`<S671>` marcadores de sistema; placeholders `{''}` para aspas internas; `<CR>`/`<C>` em instruções de enigma.

---

## 3. Resumo Narrativo (Cronológico)

### 3.1 Chinatown Antes do Pagoda — Últimos Avisos (`09_026490`–`09_026530`)
O capítulo reaquece Chinatown como hub antes da infiltração. Segal confirma que o alvo voltou ao Towering Pagoda e oferece aviso de veterano da Family e ponto de apoio condicional, além de seu enigma de trocadilho sobre preparação. Rudolph encerra o gag doméstico ao ser pressionado por Flora sobre seu encontro com Pepper, negando escândalo e sendo liberado por Layton. Vivian resume-se a flavor sobre ritmo pouco gentleman, Pepper recebe com hospitalidade e engata enigma de noodles, enquanto Deloy fecha a rua ao Pagoda com a lógica de que só passa quem o boss espera que resolva seu enigma.
> Ganchos: "Yikes, jumpin' straight into the lion's den, eh?" / "Head down the street to the pagoda. I wouldn't keep him waiting."

### 3.2 O Professor Desaparece — O Bilhete em Flora (`09_026540`–`09_026560`)
Ao cruzar o portão de Deloy, Layton some sem aviso. Luke e Future Luke constatam o sumiço abrupto e Flora menciona ter visto o professor sorrir ao se desviar; só então o recado colado às costas dela revela a caligrafia de Layton para seguirem sem ele. Future Luke defende que há propósito em cada gesto do professor, mas o grupo avança desfalcado e Barmey tenta ocupar o vácuo cobrando o episódio do cassino, sendo dispensado com enigma. No reencontro dublado adiante Layton retorna comedido e Luke cobra a desaparição repentina, recebendo apenas a desculpa de que precisava checar algo — pista do plano do decoy que só se fecha adiante.
> Ganchos: "Go on without me. I'll catch up with you soon" / "Oh, sorry to keep everyone waiting. Let's be off."

### 3.3 Ascensão pelo Pagoda — Dragões, Goggles e Espelhos (`09_027010`–`09_027070`)
A subida é uma dungeon de enigmas ambientais sem dublagem. A porta do dragão exige ler os olhos como chave e é assumida por Luke, celebrada por Layton. Em seguida Layton experimenta os goggles e os descreve como televisão para uma só pessoa, provocando piada de Flora e custo físico de tontura, a ponto de jurar não querer usá-los de novo — objeto que só depois se revela ser captura de memória. Walmy cobra vingança pelo irmão Barmey e impõe seu enigma, superado por Future Luke. A sala de espelhos embaralha a orientação até de Luke, obrigando Layton a apontar a porta escondida no escuro, e o último andar impõe o piso inteiro como sliding block gigante notado por Flora.
> Ganchos: "Think of it as a television for one, Luke. Only the wearer can see the image displayed inside." / "Does anyone else think this floor looks like a giant sliding block puzzle?"

### 3.4 O Falso Layton Desmascarado — Blocos e Memória (`09_029000`–`09_029010`)
Confronto dublado seguido de teatro lógico. O impostor recebe o grupo com risada confiante e pose de velho amigo, mas Luke sente estranheza imediata e Layton o rotula como charlatão. Em vez de acusar direto, Layton pede a Luke que resolva um enigma e lança o teste da caneta, perguntando a cor no bolso. O falso recusa chutar sem lógica e Layton extrai daí a falha: se fosse seu eu futuro, teria vivido aquele instante e jamais o esqueceria. A metáfora dos blocos sustenta o argumento — blocos do meio não flutuam sem apoio e o mesmo vale para a memória, e remover um bloco inteiro destruiria a persona. A revelação final desmonta tudo ao mostrar que nunca houve caneta.
> Ganchos: "You've put on quite a show, but it's clear to me that you're nothing but a charlatan." / "My pockets are empty. There was never a pen there to begin with."

### 3.5 Dimitri Revelado — Máquina do Tempo e Claire (`09_030010`–`09_030020`)
Sequência mais longa dublada expõe o vilão. Dimitri cumprimenta com ironia, explica que construir sozinho uma máquina do tempo é tarefa hercúlea e que usar o nome de Layton deu disfarce perfeito e isca ideal, pois o bom nome de Layton o traria. Layton questiona a escolha e ouve que suas memórias são a peça que faltava. O retcon dos goggles vem em seguida: eram um cognitive capture unit, um memory recorder que já extraiu o que precisava. Dimitri precisa triangular com memórias de Layton e Bill sobre Claire o ponto de origem do buraco de minhoca logo antes da morte dela, assumindo risco de ficar preso para sempre. O motivo é então declarado como o dia em que perdeu tudo e o amor por Claire, mas Layton mantém o limite moral mesmo diante do luto.
> Ganchos: "Those glasses you put on were a cognitive capture unit of my own design." / "Nothing can excuse the kidnapping of all those scientists. Not even this, Dimitri."

### 3.6 Armadilha Dupla e o Ás na Manga (`09_031010`–`09_032030`)
Dimitri tenta superioridade numérica no próprio quartel, mas Layton já havia invertido o tabuleiro. Primeiro o grupo parece cair em armadilha e a narração ironiza a falha em capturar o artigo genuíno, revelando dois Laytons e o espanto dos oponentes. A explicação está no andar superior, onde Don Paolo, trancado com os Lukes, reclama de ter que fazer o papel de decoy e Layton lembra seu credo de só usar o ás na manga quando necessário, após resolver a fechadura. Em seguida Layton vira a mesa dizendo ter plantado diversions na subida, deixando os capangas ocupados por minutos. Bostro apressa a fuga do boss, que foge com o primeiro-ministro enquanto o alarme inunda o prédio de thugs.
> Ganchos: "I hate to disappoint you, but it seems you've failed to ensnare the genuine article." / "A true gentleman never plays his ace in the hole until absolutely necessary."

### 3.7 Fuga pelos Túneis — A Separação (`09_032035`–`09_032080`)
Com a entrada tomada e o caminho de baixo vigiado, a saída é emergencial. Luke encontra um trapdoor e Layton confirma o palpite; Don Paolo reclama do tamanho exíguo da escadaria para seu porte. Diante de mapa emaranhado de túneis, Layton tenta traçar rota e Future Luke impõe que precisarão se dividir porque as passagens são estreitas demais para todos ao mesmo tempo. Layton escolhe levar Don Paolo para vigiá-lo, Future Luke fica com Flora e Luke é orientado a ajudar na vigilância. Flora tenta trocar de grupo, mas Layton a despede prometendo reencontro no hotel. O trio restante força a porta que parecia parede, emerge do lado externo e decide ganhar distância, sabendo que voltar sob guarda pesada seria tolice.
> Ganchos: "The passages below are too narrow for all of us to move through at the same time." / "We'll see each other soon enough, Flora. Go with Big Luke, and we'll meet back at the hotel."

### 3.8 A Verdade sobre Don Paolo — Schrader, Delmona e Claire (`09_032090`–`09_033010`)
Epílogo dublado amarra os disfarces. Luke pergunta por que Don Paolo está ali e ouve veto irritado, até Layton explicar que o mestre do disfarce era o homem perfeito para o truque. A linha do pacto é reconstruída: Layton desconfiou de Schrader na saudação que não estranhou Luke criança quando no futuro Luke é adulto, e de Delmona pelo cabelo branco que entregou a peruca — detalhe que o verdadeiro Dean, careca há anos, jamais usaria. Confrontado, Paolo contou ter sido pago por Dimitri para guiá-los ao Pagoda e aceitou trocar de lado após Layton compartilhar os fenômenos. O motivo final é Claire, namorada de Layton e pesquisadora do mesmo lab de Dimitri vista a caminho da explosão cuja cobertura foi abafada, revelando que a obsessão de Dimitri é expiação distorcida e que Paolo também a amava desde a universidade.
> Ganchos: "Don Paolo, master of deception and disguise, seemed like the perfect man to employ for the task." / "Claire was my...girlfriend, back when I was just starting my academic career."

> **Cliffhanger:** O Pagoda revela Dimitri e seu motivo por Claire, o memory recorder já extraiu Layton, Don Paolo troca de lado por amor antigo, mas a Family leva o primeiro-ministro e o grupo precisa fugir dividido pelos túneis — retorno ao hotel para juntar Flora/Big Luke.



---

## 4. Diálogo Detalhado por Arquivo

> Formato: `Falante (Tag) — <Vxxxx> se dublado` e então o texto em inglês conforme no arquivo. `<T>`/`<V>` limpos, esperas `<W>` e animações `<A>` anotadas quando presentes.

### `09_000000.lbin.txt` — [vazio - apenas cabeçalho]

*   Cabeçalho: `[7017010000000000:0000000000]` — sem blocos de texto.

### `09_026490.lbin.txt` — Segal - aviso lion s den e puzzle de preparation

*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Hello there, friends. Did you find that fella ye were chasin'?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Unfortunately not, but I'm confident we'll corner him at the Towering Pagoda this time.`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T><A1/2>Yikes, jumpin' straight into the lion's den, eh? You be careful down there in Chinatown.`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>On the, um, off chance things get hairy, come and talk to me. I'll help ye out.`
*   **ルーク** (Luke Triton):  
    `<T>The way you say that makes me think there's more than an off chance things'll get hairy...`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T><A2/1>Not at all, my small friend. But ya know what they say: hope for the best, prepare for the not best.`
*   **ルーク** (Luke Triton):  
    `<T>The not best? Don't you mean the worst?`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Do I? I dunno.<W> Speakin' of preparation, have you fellas ever heard this one?`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Leaving a job half done? I didn't {''}prepare{''} for that possibility. Arf.`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Here to try that puzzle again?<W> Good! Here it is.`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Now that's out the way, I s'pose ye'll be headin' to the Towering Pagoda, eh?`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>Watch yerselves out there, all right?`
*   **セガール** (Segal (Black Market Dealer)):  
    `<T>That pagoda's a treacherous place. Keep an eye out for trouble, won't ya?`

### `09_026500.lbin.txt` — Rudolph - hoo hoo, rendezvous com Pepper, Myrtle

*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T>Well hello again, whippersnappers! Did you manage to find that nasty man from the Towering Pagoda?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>No, it seems we just missed him down by the river. But we believe he's back at the pagoda now.`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T>Hoo hoo hoo! All this coming and going must be taking it out of you!`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T>Good thing you're still young and full of beans!`
*   **ルーク** (Luke Triton):  
    `<T>And what about you, Rudolph? Have you resolved your little problem?`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T><A1/2>Hrm? P-problem? I don't know what you mean, lad...`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/3>Don't play innocent. Luke's talking about your clandestine lunchtime rendezvous with Pepper.`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T>Wh-what?<W> Oh no, no, no! My wife's mistaken about all of that. Really, it's nothing scandalous!`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T>Thanks for your concern, but it's all just a big misunderstanding. Please don't pay it any heed.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm pleased to hear that there's no reason to worry.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Now come along, everyone. We mustn't waste any more time in getting to the Towering Pagoda.`
*   **ルーク** (Luke Triton):  
    `<T>Okay, Professor.`
*   **ルドルフ** (Rudolph (Chinatown Elder)):  
    `<T><A1/1>I'd best head home myself...before Myrtle explodes.`

### `09_026510.lbin.txt` — Vivian (ビビアン) - comentário sobre gentleman apressado

*   **ビビアン** (Vivian):  
    `<T>You're always rushing about. That doesn't really seem very suitable for a gentleman...`

### `09_026520.lbin.txt` — Pepper (ポルテ) - Noodle Palace, noodle puzzles

*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Welcome to Pepper's Noodle Palace!`
*   **ルーク** (Luke Triton):  
    `<T>Hello there, Pepper!`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>And a big {''}hello there{''} to you too, gents. Thanks for stopping by again.<W> Hungry already, are you?`
*   **ルーク** (Luke Triton):  
    `<T><A3/1>I'm still quite full, actually.`
*   **ルーク** (Luke Triton):  
    `<T><A3/2>We do know one police officer who'd never turn down a bowl of noodles, mind...`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T><A2/1>Hungry customers are my favourite customers! I think I'll treat him to a bowl on the house.`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>It's not just the noodles that are good here, you know - the noodle puzzles aren't bad either. Here!`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Aww. Not to your taste?`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Hungry for a noodle puzzle?<W> Then dig your chopsticks into this!`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Nice work there!`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Hello there! What can I get you?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Nothing for now, thank you, but we're looking forward to coming by for another meal later.`
*   **ポルテ** (Pepper (Noodle Palace Owner)):  
    `<T>Oh, okay then. See you soon!`

### `09_026530.lbin.txt` — Deloy (デロイ) - guarda do portão, boss puzzle gate

*   **デロイ** (Deloy (Gate Guard)):  
    `<T>Hmph. Back again, I see.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Yes, we heard that Mr Layton had returned.`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>That...is not incorrect.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Then I assume you'll be letting us through?`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>Hmph. I have no objections.<W><A5/5> Well, that's not entirely true. There is one minor issue left.`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>When the boss got back, he ordered me to not let anyone through unless they solve this puzzle.`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>Sorry, but the boss said that the man wanting to pass through here would be able to solve this puzzle...`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T><A6/0>Therefore, I can only deduce that you're not the man he's expecting.`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>You know the score. If you want to get in, you have to solve this puzzle first. No exceptions.`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T>Hmph. It seems the boss was right about you. You must be the one he's been waiting for...`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>Does that mean we can enter?`
*   **デロイ** (Deloy (Gate Guard)):  
    `<T><A4/1>Head down the street to the pagoda. I wouldn't keep him waiting, if I were you.`

### `09_026540.lbin.txt` — Desaparecimento do professor - bilhete nas costas de Flora

*   **ルーク** (Luke Triton):  
    `<T>The Towering Pagoda's not far now.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/2>The Layton from your time and the one from mine are finally going to meet face-to-face...`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>That might be tricky, because our professor's not here...`
*   **ルーク** (Luke Triton):  
    `<T>Huh?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><K><A1/1>Hmm?`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>Where's the professor?!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>It's like he just disappeared.`
*   **ルーク** (Luke Triton):  
    `<T><A1/1>But he just solved that puzzle that got us through the gate!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>Yes, and then we walked through the gate together.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>He was a bit ahead of us by that point. I think he might've waved at me before he vanished.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/5>What?!<W> But where did he go?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>I'm not sure.<W> He was smiling as he dashed off, though.`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>But...why?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/4>I have no idea. The professor's actions always have some purpose, though...`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>Hey Flora, there's a piece of paper stuck to your back.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A2/5>Oh! How embarrassing! Someone must be playing a trick on me.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>There's something written on it - it's in the professor's handwriting!`
*   **ルーク** (Luke Triton):  
    `<T>Let's have a look. It says: {''}Go on without me. I'll catch up with you soon{''}.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/1>I think we should do as he says. The professor's never led us astray, after all.`
*   **ルーク** (Luke Triton):  
    `<T>I agree. This is probably all part of some brilliant plan that the professor's concocted.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>That's all very well, but will one of you Lukes please take this paper off my back?`

### `09_026545.lbin.txt` — Future Luke - press on without him

*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>The professor wouldn't leave us alone without good reason. Let's just press on without him for now.`

### `09_026550.lbin.txt` — Barmey/Walton (ワルートン) - casino rampage, puzzle de bloqueio

*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>H-hey! What are you lot doing back here?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>We're on our way to the Towering Pagoda. Not that it's any of your business.`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T><A2/5>N-not so fast!<W> You're the ones who went on the rampage in the casino, ain't you?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/2>What if we are? What are you going to do about it?`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>I-I...<W> My bruv Chelton'd give you a good hidin'...if he hadn't gone to erm...spend a penny.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/1>Looks like we're in luck then, eh? We'll just be on our way now.`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>If you run off, I'll make sure Chelton squishes you like an ant when he finds you!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>We'll bear that in mind.`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>Wait! One more thing! Um...<W> Solve this puzzle!`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>You ain't no match for my puzzle, so you ain't goin' nowhere!`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>If you can't cough up an answer to this puzzle, maybe I don't need Chelton after all!`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>Blast! You solved it.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/2>We really don't have any more time for this silliness. We'll be heading to the pagoda now.`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T><A1/1>F-fine! But remember, you got lucky!`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>If my bruv was here, you'd be the one gettin' bossed around!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/1>Are you finished?`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>Th-this ain't over! Mark my words! You're gonna get what's comin' to you!`

### `09_026560.lbin.txt` — Reencontro dublado - Sorry to keep everyone waiting

*   **ルーク** (Luke Triton) <V0010>:  
    `<V0010><T><A4/4>I hope we find the professor soon...</V>`
*   **アロマ** (Flora Reinhold (Aroma)) <V0020>:  
    `<V0020><T>Poor thing! You're just lost without him, aren't you, Luke?</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T><A4/1>You're a fine one to talk!</V>`
*   **レイトン** (Professor Hershel Layton) <V0050>:  
    `<V0050><T><A3/2>Oh, sorry to keep everyone waiting. Let's be off.</V>`
*   **ルーク** (Luke Triton) <V0060>:  
    `<V0060><T><A1/6>Where did you go?<A1/1> One minute you were there, and the next you'd vanished!</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T>My apologies, Luke. I just needed to check something.</V>`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><Q><K><A1/1>...`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T>But enough about that. Come along, everyone. The Towering Pagoda is just steps away.</V>`

### `09_027010.lbin.txt` — Porta do dragão - olhos como chave, puzzle de Luke

*   **ルーク** (Luke Triton):  
    `<T>I suppose it would be too much to expect the door to be open...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let's see. The eyes of this dragon seem to be the key that unlocks this door.`
*   **ルーク** (Luke Triton):  
    `<T><A2/2>Sounds like a puzzle! Let me handle it, Professor. I'll have the door open before you know it!`
*   **ルーク** (Luke Triton):  
    `<T>I think I need another minute to think about this...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Would you like me to have a go at it, Luke?`
*   **ルーク** (Luke Triton):  
    `<T><A1/5>That won't be necessary, Professor. I'm sure I can solve this one!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm confident the door will open just as soon as we solve this puzzle.`
*   **ルーク** (Luke Triton):  
    `<T>All set!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/2>Smashing work, Luke.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>There's no time to celebrate. Let's head inside.`

### `09_027020.lbin.txt` — Goggles - personal projection device / memory recorder foreshadow

*   **ルーク** (Luke Triton):  
    `<T>What's this contraption, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It appears to be a peculiar set of goggles.`
*   **ルーク** (Luke Triton):  
    `<T>I think they're too big for me...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let's see...<W> Ah, this is some sort of personal projection device.`
*   **ルーク** (Luke Triton):  
    `<T>Personal what?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>Think of it as a television for one, Luke. Only the wearer can see the image displayed inside.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'd wager that there's a puzzle in these goggles that only the wearer can see.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Solving it is probably the only way to get through this door.`
*   **ルーク** (Luke Triton):  
    `<T><A4/1>Now that's high-tech!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>They should fit me comfortably. Let's have a look.`
*   **ルーク** (Luke Triton):  
    `<T>What do you see, Professor?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Tee hee! Those glasses make you look like a bug! A robot bug!`
*   **レイトン（ゴーグル）** (Layton (Goggles)):  
    `<T>I think something's coming into focus here.`
*   **レイトン（ゴーグル）** (Layton (Goggles)):  
    `<T>I need to rest for a moment. These glasses have a very tiring effect on the eyes.`
*   **レイトン（ゴーグル）** (Layton (Goggles)):  
    `<T>All right. Time to give this one another try.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Phew! What a relief to take those off. I was feeling all light-headed and was having trouble focusing.`
*   **ルーク** (Luke Triton):  
    `<T><A3/2>But it was all worth it! Thanks to you, the door's unlocked and we're free to move on!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I don't believe I have any desire to wear those strange goggles again.`

### `09_027030.lbin.txt` — Corredor sombrio - gloomy dragons

*   **ルーク** (Luke Triton):  
    `<T>It's so gloomy...`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>And there are dragons all over the place...`

### `09_027040.lbin.txt` — Walmy (ワルミー) vs Future Luke - bullying Barmey, puzzle

*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T><A2/5>So, you're the one who's been bullyin' my bruvver Barmey! You're gonna pay for that!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/1>Well well. Look who went crying to the older boys.<W> What an impressive act of bravery.`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>Quiet, you! What was I supposed to do back there? I was outnumbered!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A4/2>There, there, I understand. You're only small and you knew you had no chance of stopping us.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>So, you're getting this big lump here to do the dirty work for you.`
*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T><A3/5>Hmph! Sticks and stones, sunshine!`
*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T>Believe you me, if the boss allowed violence in the pagoda, I'd have pounded you already!`
*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T>Since I can't do that, I'll have to sock it to you with this vicious puzzle!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Would you like me to deal with this one, Big Luke?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/2>Don't trouble yourself with this piece of riff-raff, Professor. I can handle anything he dishes out.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>This puzzle's no joke.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Would you like me to step in for you, Luke?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>I appreciate the offer, but I've got this, Professor. I just need a break to regain my focus.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>All right, let's try this again!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/5>So much for that puzzle. What are you going to do now?`
*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T>Hmph! You're lucky the boss doesn't let me rough people up in here.`
*   **ワルミー** (Walmy (Family Thug - Barmey's older brother)):  
    `<T>But you've gotta go outside at some point, and when you do, watch your back!`
*   **ワルートン** (Barmey / Walton (Family Thug - small)):  
    `<T>Yeah! Too right!`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/2>All bark and no bite. Come on, everyone. We've got places to be!`

### `09_027050.lbin.txt` — Sala de espelhos - porta oculta no escuro

*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T>Strange... This whole room is covered in mirrors.`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>It's very confusing. I've got no idea which way we need to go.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>It seems we've hit a dead end. How do you think we should proceed, Big Luke?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A3/5>Maybe we have to press a hidden panel on one of the walls to open the door out of here.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/2>Close, but not quite. If my guess is correct, the door is hidden in the dark over there.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>But we can't just rush headlong into the shadows. There's no telling what traps await us there.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A2/2>Ah, now I see what you're getting at!`
*   **ルーク** (Luke Triton):  
    `<T>Are you saying that this room is a puzzle, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That's right, Luke. And I'm about to solve our way out of here.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hmm. I may need to ponder this one a little bit more.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>All right. I'm quite sure I've got the answer this time.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>It seems my theory was right. This way, everyone.`

### `09_027055.lbin.txt` — Top floor - Estamos perto

*   **ルーク** (Luke Triton):  
    `<T>Professor, I think this is the top floor! We must be close now!`

### `09_027060.lbin.txt` — Sliding block gigante - piso puzzle antes do falso Layton

*   **レイトン** (Professor Hershel Layton):  
    `<T>The future professor's quarters are probably on the other side of that door.`
*   **ルーク** (Luke Triton):  
    `<T>But how are we supposed to make it across this huge gap?`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A2/5>Does anyone else think this floor looks like a giant sliding block puzzle?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>An astute observation, Flora. It seems the floor of this room is yet another puzzle for us to solve.`
*   **ルーク** (Luke Triton):  
    `<T>The future Layton loves to keep things dramatic, doesn't he?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That does seem to be the case.<W> Now let's get started on this puzzle...`
*   **レイトン** (Professor Hershel Layton):  
    `<T>My goodness. This is proving much more difficult than I anticipated.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This puzzle is the only thing that stands between us and the future Professor Layton.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>There! It's safe to cross now, everyone.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This puzzle is the only thing that stands between us and the future Professor Layton.`

### `09_027070.lbin.txt` — Abertura da porta - encontro iminente

*   **レイトン** (Professor Hershel Layton):  
    `<T>All right, stand back. We're opening the door.`
*   **ルーク** (Luke Triton):  
    `<T>At last we get to meet the future Professor Layton! Let's be careful, everyone.`

### `09_029000.lbin.txt` — Falso Layton dublado - I demand an explanation, charlatan

*   **レイトン** (Professor Hershel Layton) <V0010>:  
    `<V0010><T>I demand an explanation!</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T>Are you really Professor Layton?</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0030>:  
    `<V0030><T>Ha ha ha! Yes, of course!</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0040>:  
    `<V0040><T><A1/2>Don't you recognise your old friend?</V>`
*   **ルーク** (Luke Triton) <V0050>:  
    `<V0050><T><A2/1>I don't know... Something about you seems...off.</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0060>:  
    `<V0060><T>Surely you recognise yourself, Hershel?</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0061>:  
    `<T><V0061>This fortune - our fortune - is a result of your ambition and genius.</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><K><A4/5>Hmm...</V>`
*   **ルーク** (Luke Triton) <V0080>:  
    `<V0080><T><A1/1>What is it, Professor?</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T><A4/1>You've put on quite a show, but it's clear to me that you're nothing but a charlatan.</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0100>:  
    `<V0100><T><A1/1>Oh, is that so?</V>`
*   **ルーク** (Luke Triton) <V0110>:  
    `<V0110><T><A1/6>What tipped you off, Professor?</V>`
*   **にせレイトン** (False Layton (Fake Future Layton)) <V0120>:  
    `<V0120><T><A1/2>Heh heh heh... Yes, what indeed? I'm all ears.</V>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You, sir, are a fraud, and exposing you for the impostor that you are will prove simple.`

### `09_029010.lbin.txt` — Teste do impostor - blocos, memória e caneta vazia

*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>Fascinating! Do continue.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Luke, would you be so kind as to solve a quick puzzle for me?`
*   **ルーク** (Luke Triton):  
    `<T>Uh...right now, Professor?<W> Aren't we in the middle of something here?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Give it some more thought, Luke.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let's try this once more.`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>Yes, yes, the boy is quite bright. We all know that. But what does that have to do with anything?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm getting there.<W> But first, a question. I have a pen in my pocket that's either red or blue.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Could you tell me which colour it is?`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>What a terribly uncharacteristic query for you to make. There's no logic for me to work through.`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>I'm not a mind-reader, and I refuse to guess blindly. How can I solve your puzzle without a single hint?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>So in other words, you have no idea what colour pen I have in my pocket?`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>Of course not.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That's funny.`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>Oh?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A2/1>Luke, what would happen if you removed the bottom row of blocks from that pile I just showed you?`
*   **ルーク** (Luke Triton):  
    `<T>The rest of the blocks would fall down, I suppose.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>That's right. Those blocks in the middle of the structure don't float in mid-air.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Only by resting on the blocks beneath can those blocks stay elevated.`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T><K>...`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>If you were really my future self, you would have experienced this very moment before.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There is simply no way you could forget it.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Given your answer, I can only assume that your memory of this crucial event is missing.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>But remember those blocks. All blocks are supported by other blocks.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>When you remove one, everything on top of it comes tumbling down. <W>The same goes for memory.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You can't simply be missing a whole block of memory. It would destroy your very persona.`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>It all makes sense now!`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T>I see... So, what colour is the pen in your pocket, then?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>My pockets are empty. There was never a pen there to begin with.`
*   **にせレイトン** (False Layton (Fake Future Layton)):  
    `<T><K>...`

### `09_030010.lbin.txt` — Dimitri dublado - Hats off, time machine, Claire, memory recorder (42 blocos)

*   **ディミトリー** (Dimitri Allen) <V0010>:  
    `<V0010><T>Hats off to you, Hershel.</V>`
*   **レイトン** (Professor Hershel Layton) <V0020>:  
    `<V0020><T>So you're the one who's been kidnapping scientists under my name. But why?</V>`
*   **ディミトリー** (Dimitri Allen) <V0030>:  
    `<V0030><T><A3/2>Have you ever tried to build a time machine by yourself? It's a Herculean task!</V>`
*   **ディミトリー** (Dimitri Allen) <V0040>:  
    `<V0040><T>And by pinning the blame on you, I could disguise myself as one of the poor scientists who vanished.</V>`
*   **ディミトリー** (Dimitri Allen) <V0050>:  
    `<V0050><T><A4/5>Conveniently, that also provided an excellent way to lure you here.</V>`
*   **ディミトリー** (Dimitri Allen) <V0060>:  
    `<V0060><T>After all, the virtuous Hershel Layton would never stand by as someone sullied his good name.</V>`
*   **ディミトリー** (Dimitri Allen) <V0070>:  
    `<V0070><T>Sure enough, you came running. And faster than expected, at that!</V>`
*   **ルーク** (Luke Triton) <V0080>:  
    `<V0080><T><A1/3>You're a real piece of work!</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T>So why me? You could have chosen anyone to be the scapegoat.</V>`
*   **ディミトリー** (Dimitri Allen) <V0100>:  
    `<V0100><T><A2/5>Oh no, it had to be you. You see, you play a critical part in the completion of my time machine.</V>`
*   **ディミトリー** (Dimitri Allen) <V0110>:  
    `<V0110><T><A2/5>Or rather, your memories do.</V>`
*   **レイトン** (Professor Hershel Layton) <V0120>:  
    `<V0120><T>What are you saying?</V>`
*   **ディミトリー** (Dimitri Allen) <V0130>:  
    `<V0130><T>The best part is that I've already got what I need from you.</V>`
*   **レイトン** (Professor Hershel Layton) <V0140>:  
    `<V0140><T><A3/1>Of course! So that strange device...</V>`
*   **ディミトリー** (Dimitri Allen) <V0150>:  
    `<V0150><T><A3/2>Finally catching on, eh? Those glasses you put on were a cognitive capture unit of my own design.</V>`
*   **ディミトリー** (Dimitri Allen) <V0151>:  
    `<T><V0151>In layman's terms, a memory recorder.</V>`
*   **レイトン** (Professor Hershel Layton) <V0160>:  
    `<V0160><T><A1/1>But what use could you possibly have for my memories?</V>`
*   **ディミトリー** (Dimitri Allen) <V0170>:  
    `<V0170><T>Why, they provide me with data, of course.</V>`
*   **ディミトリー** (Dimitri Allen) <V0171>:  
    `<T><V0171>Your memories contain all the information I need...to recreate that fateful day's experiment.</V>`
*   **レイトン** (Professor Hershel Layton) <V0180>:  
    `<V0180><T><A4/1>Which day?</V>`
*   **ディミトリー** (Dimitri Allen) <V0190>:  
    `<V0190><T><A1/4>The day I lost everything that mattered to me.</V>`
*   **ルーク** (Luke Triton) <V0200>:  
    `<V0200><T>I still don't understand...</V>`
*   **ディミトリー** (Dimitri Allen) <V0210>:  
    `<V0210><T>I'd imagine you know quite a bit about loss yourself, Hershel. Think, man!</V>`
*   **ディミトリー** (Dimitri Allen) <V0220>:  
    `<V0220><T>I'm talking about Claire.</V>`
*   **レイトン** (Professor Hershel Layton) <V0230>:  
    `<V0230><T>Claire...</V>`
*   **ディミトリー** (Dimitri Allen) <V0240>:  
    `<V0240><T><A3/5>As you know, time travel is based on movement through wormholes.</V>`
*   **ディミトリー** (Dimitri Allen) <V0250>:  
    `<V0250><T>One end of the wormhole is anchored in the present.</V>`
*   **ディミトリー** (Dimitri Allen) <V0251>:  
    `<T><V0251>But every wormhole also needs a point of origin. And to find this point of origin, one needs data.</V>`
*   **ディミトリー** (Dimitri Allen) <V0260>:  
    `<V0260><T><A3/2>Both you and Bill had substantial interactions with Claire on the day of the accident.</V>`
*   **ディミトリー** (Dimitri Allen) <V0270>:  
    `<V0270><T>Using your memories of those interactions, I will triangulate the point right before her death.</V>`
*   **ディミトリー** (Dimitri Allen) <V0280>:  
    `<V0280><T>Of course, finding a wormhole's point of origin is no easy task.</V>`
*   **ディミトリー** (Dimitri Allen) <V0281>:  
    `<T><V0281>If my calculations were even the slightest bit off, I could be trapped...forever.</V>`
*   **レイトン** (Professor Hershel Layton) <V0290>:  
    `<V0290><T>Then why take the risk? What do you stand to gain?</V>`
*   **ディミトリー** (Dimitri Allen) <V0300>:  
    `<V0300><T><A1/4>Everything. You see, like you, Hershel...I loved Claire.</V>`
*   **レイトン** (Professor Hershel Layton) <V0310>:  
    `<V0310><T>So you intend to travel back through time and save her?</V>`
*   **ディミトリー** (Dimitri Allen) <V0320>:  
    `<V0320><T>Surely you wouldn't stop me. After all, haven't you wished for this yourself?</V>`
*   **レイトン** (Professor Hershel Layton) <V00330>:  
    `<V00330><T><K>...</V>`
*   **レイトン** (Professor Hershel Layton) <V0340>:  
    `<V0340><T><A1/1>Nothing can excuse the kidnapping of all those scientists. Not even this, Dimitri.</V>`
*   **ディミトリー** (Dimitri Allen) <V0350>:  
    `<V0350><T>You disappoint me.</V>`
*   **ディミトリー** (Dimitri Allen) <V0351>:  
    `<T><V0351><A4/5>I had hoped a rational man like yourself would understand that the ends justify the means.</V>`
*   **レイトン** (Professor Hershel Layton) <V0360>:  
    `<V0360><T>I don't see it that way.</V>`
*   **ディミトリー** (Dimitri Allen) <V0370>:  
    `<V0370><T>Then, what's your next move?<W> <A2/5>Turn me in to the police? Ha! I'd like to see you try.</V>`

### `09_030020.lbin.txt` — Relevo de tropas - 5 vs 5 estrelas, empate estratégico

*   **レイトン** (Professor Hershel Layton):  
    `<T>You're mistaken in thinking I came here to report you to the authorities.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I'm here to stop the man who's been dragging my good name through the dirt.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A2/6>Hah. That's a noble sentiment, Hershel, but you seem to have forgotten one key detail.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>The Towering Pagoda is my stronghold, and that means you're on my turf.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/2>I have more than enough men here to overpower you. Look here.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A1/1>This 18th-century relief illustrates our situation perfectly.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>It displays two warring factions of five troops. The stars indicate the strength of each soldier.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>The red troops represent you in your current situation. The white troops are mine.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>It should be fairly clear who the victor will be.`
*   **ルーク** (Luke Triton):  
    `<T><A4/4>The white side has more powerful troops! There's no way red could win!`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/2>Exactly. Your apprentice has a good head on his shoulders, Hershel.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A4/1>I think it's a touch premature to praise him in this case, Dimitri.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I don't see why our troops need lose, provided the battles are fought one-on-one.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A1/1>It sounds to me as if you simply don't wish to admit defeat.<W> If you think victory is possible, prove it!`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>There. Each side wins two fights, loses two fights and ties one. It's a perfect draw.`
*   **ルーク** (Luke Triton):  
    `<T><A4/2>Of course! What the red side lacks in troop strength it can make up for with strategy!`
*   **ディミトリー** (Dimitri Allen):  
    `<T><S671><A3/2>I find myself once again impressed by your logic.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/2>Hah! Arrange your troops like that and my victory is assured!`
*   **ナゾバトル** (Puzzle Battle (System)):  
    `<T>Each soldier will engage one soldier from the other side in combat. Pair each of your red troops against one of the opposing white troops. Your troops are marked with an icon depicting Professor Layton. The strength of each soldier is represented by the number of stars on his banner. Arrange your forces so that the red side avoids defeat. Touch <CR>OK!</C> to submit your answer.`

### `09_031010.lbin.txt` — Armadilha dupla dublado - two Laytons, genuine article

*   **ルーク** (Luke Triton):  
    `<T>Oh no! We're trapped!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hmm...`
*   **ナレーション** (Narration) <V0010>:  
    `<V0010><T>I hate to disappoint you, but it seems you've failed to ensnare the genuine article.</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T>Uh...Professor? How did you get there?</V>`
*   **ディミトリー** (Dimitri Allen) <V0030>:  
    `<V0030><T>Just what is going on here? Why are there two of you?</V>`
*   **未来ルーク** (Future Luke (Big Luke)) <V0040>:  
    `<V0040><T>Which one is the real professor?</V>`

### `09_032010.lbin.txt` — Don Paolo como decoy - ace in the hole e fechadura

*   **未来ルーク** (Future Luke (Big Luke)) <V0010>:  
    `<V0010><T><A3/5>This is getting far too complicated.</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T><A1/6>Yeah, what's going on?</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T><A2/2>Take note, Luke. A true gentleman never plays his ace in the hole until absolutely necessary.</V>`
*   **ドン・ポール** (Don Paolo) <V0040>:  
    `<V0040><T><A2/3>Hey, Layton, here's an idea for you. Why don't you quit it with the lectures and get me out of here?</V>`
*   **ルーク** (Luke Triton) <V0050>:  
    `<V0050><T><A1/3>Help us, Professor!</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T><A3/1>Be patient, Luke. I just need to find a way past this lock.</V>`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Odd. I was certain that I had the answer.`
*   **ルーク** (Luke Triton):  
    `<T>Professor, you've got to get us out of here!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>This time I've got it for sure.`

### `09_032030.lbin.txt` — Tables have turned - diversions, Bostro, fuga com PM, alarme

*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/1>It would seem the tables have turned, Dimitri.`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A3/2>That's a rather delusional statement for someone with your penchant for logical thought.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>Look around you. In case you hadn't noticed, you're deep within the Family's headquarters.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>I need only say the word and my men will come rushing to my aid.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>You underestimate me, Dimitri.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>Do you think I'd be so na{:i}ve as to set foot in your base without a plan of my own?`
*   **ディミトリー** (Dimitri Allen):  
    `<T><A1/1>Meaning?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/2>This building is fascinating in its complexity.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I saw plenty of spots where one might conceal a trap or the like.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>On my way up here, I set up a few diversions of my own. Call for your henchmen, if you like.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>I imagine most of them will have their hands full for a few more minutes at least.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>Hmph. Clever, Hershel. Very clever.`
*   **ボストロ** (Bostro (Family Lieutenant)):  
    `<T>C'mon, Boss! We've got to scarper!`
*   **ディミトリー** (Dimitri Allen):  
    `<T>It seems I must concede defeat for now, but this is far from over.`
*   **ディミトリー** (Dimitri Allen):  
    `<T>I look forward to seeing you when our paths cross next.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>Drat. They're much faster than I thought. There's no chance of us catching them.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Oh no!`
*   **ルーク** (Luke Triton):  
    `<T>What's wrong?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>All this commotion allowed Dimitri and his men to grab the prime minister and take him with them.`
*   **ルーク** (Luke Triton):  
    `<T>Uh-oh. That doesn't sound good.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/5>Dimitri's activated an alarm. This place will be flooded with Family thugs before long.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There's the distinct possibility that we may have to fight our way out of the Towering Pagoda...`
*   **ルーク** (Luke Triton):  
    `<T><A1/6>But didn't you take care of Dimitri's henchmen on the way in, Professor?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>Not quite, I'm afraid. The few diversions I managed to set up will only last a few more minutes.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>The path we took on the way in is almost certainly swarming with Family now.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Our only hope is to find some sort of emergency escape route.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Dimitri is a prudent man. He may have one hidden somewhere in this room.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We must search this place thoroughly.`

### `09_032035.lbin.txt` — Caminho bloqueado - Family waiting below

*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>We can't head out that way. The Family's bound to have men waiting for us below.`

### `09_032040.lbin.txt` — Trapdoor e mapa de túneis - split em dois grupos

*   **ルーク** (Luke Triton):  
    `<T>Aha! There's a trapdoor here!`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Then my hunch was right. It looks as if we've found a way out of here.`
*   **ドン・ポール** (Don Paolo):  
    `<T><A2/3>Oof! They must have built this stairwell for men less, er, buff and muscular than me!`
*   **ドン・ポール** (Don Paolo):  
    `<T><A3/5>And there's more than one path! Which way do we go, Layton?`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>Look, there's a map here that charts out the network of tunnels below us.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let me see. <W>My, this is a bit of a tangled mess, isn't it?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Strange. I was sure I'd found a way through. I'll just have to try again.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We need to plot our escape route before heading down.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A1/4>The passages below are too narrow for all of us to move through at the same time.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>If we want to get out of here quickly, we'll need to split into two groups.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Hmm. I don't like it, but it seems we've no choice. Now, who should I take with me...?`
*   **ドン・ポール** (Don Paolo):  
    `<T><A1/1>You always get to be the gentleman. This time, I want to escort the young lady.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Sorry, but I'd prefer you to come with me, Don Paolo.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T><A2/2>Very well then. Flora and I will go together.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>Luke, you go with the professor and help him keep an eye on Don Paolo.`
*   **アロマ** (Flora Reinhold (Aroma)):  
    `<T><A1/5>Trade with me, Little Luke! I want to be in the professor's group.`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A3/2>We'll see each other soon enough, Flora.<W> Go with Big Luke, and we'll meet back at the hotel.`
*   **未来ルーク** (Future Luke (Big Luke)):  
    `<T>All right, the groups are set.<W> Let's get moving.`

### `09_032050.lbin.txt` — Stairwell - parede que é porta

*   **ルーク** (Luke Triton):  
    `<T>Ouch! <A1/4>What did I just run into?`
*   **ドン・ポール** (Don Paolo):  
    `<T>Let me guess... A wall?`
*   **レイトン** (Professor Hershel Layton):  
    `<T>Let's see.<W> Hmm. This might actually be a door.`
*   **ルーク** (Luke Triton):  
    `<T><A1/1>Yes, it is! There's a handle here!`
*   **ルーク** (Luke Triton):  
    `<T>Phew...`
*   **ドン・ポール** (Don Paolo):  
    `<T>Great. NOW where are we?`
*   **レイトン** (Professor Hershel Layton):  
    `<T><A1/1>We're at the bottom of an emergency stairwell.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>There should be a way out of the building here somewhere.`

### `09_032060.lbin.txt` — Saída do pagoda - put some distance

*   **レイトン** (Professor Hershel Layton):  
    `<T>This door should take us outside.`
*   **ドン・ポール** (Don Paolo):  
    `<T>Well, look at that. We made it out.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>The Family is bound to have some thugs in the vicinity.`
*   **レイトン** (Professor Hershel Layton):  
    `<T>We need to put some distance between us and the pagoda.`

### `09_032080.lbin.txt` — Aviso - foolish to return under heavy guard

*   **レイトン** (Professor Hershel Layton):  
    `<T>It would be foolish and dangerous to return to the pagoda when it's under such heavy guard.`

### `09_032090.lbin.txt` — Exposição longa dublada - Don Paolo como Schrader/Delmona, Claire (61 blocos)

*   **ルーク** (Luke Triton) <V0010>:  
    `<V0010><T><A1/3>I still don't understand why Don Paolo's here. Can someone please explain that to me?</V>`
*   **ドン・ポール** (Don Paolo) <V0020>:  
    `<V0020><T>Always with the questions. Won't you put a lid on it for a few minutes, you brat?</V>`
*   **ルーク** (Luke Triton) <V0030>:  
    `<V0030><T><A1/3>I most certainly will not!</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>Honestly, you two! Would you please stop bickering? You're on the same side!</V>`
*   **ドン・ポール** (Don Paolo) <V0050>:  
    `<V0050><T><A2/3>And while I'm getting things off my chest, why the heck did I have to play the decoy who gets caught?</V>`
*   **レイトン** (Professor Hershel Layton) <V0060>:  
    `<V0060><T><A1/2>Come now, Paul, it wasn't that bad. Your role was certainly the more exciting one. </V>`
*   **ルーク** (Luke Triton) <V0070>:  
    `<V0070><T>Professor, you still haven't explained what's going on!</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T><A4/2>I knew we'd be monitored from the moment we stepped foot inside the pagoda.</V>`
*   **レイトン** (Professor Hershel Layton) <V0081>:  
    `<T><V0081>So I wanted to make sure we had at least one trick up our collective sleeve.</V>`
*   **レイトン** (Professor Hershel Layton) <V0090>:  
    `<V0090><T>Don Paolo, master of deception and disguise, seemed like the perfect man to employ for the task.</V>`
*   **ルーク** (Luke Triton) <V0100>:  
    `<V0100><T><A1/5>You two are friends? That's the first I've heard of this!</V>`
*   **ドン・ポール** (Don Paolo) <V0110>:  
    `<V0110><T><A1/1>Hah! Don't get it confused, kid. I'm no friend of his.</V>`
*   **ドン・ポール** (Don Paolo) <V0120>:  
    `<V0120><T><A4/1>We both want answers to the same questions, so we decided to work together. That's all.</V>`
*   **ルーク** (Luke Triton) <V0130>:  
    `<V0130><T><A1/1>When did this start?</V>`
*   **レイトン** (Professor Hershel Layton) <V0140>:  
    `<V0140><T><A1/1>Tell me, Luke. When we visited Dr Schrader, did anything he said strike you as strange?</V>`
*   **ルーク** (Luke Triton) <V0150>:  
    `<V0150><T>Um, no, not really.</V>`
*   **レイトン** (Professor Hershel Layton) <V0160>:  
    `<V0160><T>It was his greeting that made me suspicious.</V>`
*   **ルーク** (Luke Triton) <V0170>:  
    `<V0170><T>Huh?</V>`
*   **未来シュレーダー** (Future Dr Schrader (Don Paolo in disguise)) <V0180>:  
    `<V0180><T>Who's that?<W> Oh, it's you, Hershel! And little Luke!</V>`
*   **ルーク** (Luke Triton) <V0190>:  
    `<V0190><T>Yeah, I remember. But what of it?</V>`
*   **レイトン** (Professor Hershel Layton) <V0200>:  
    `<V0200><T><A2/2>He didn't seem terribly surprised to see {''}little Luke{''}, did he?</V>`
*   **ルーク** (Luke Triton) <V0210>:  
    `<V0210><T><A1/6>Of course!<W> <A1/1>In the future, I'm not a kid any more. But the doctor didn't even notice!</V>`
*   **レイトン** (Professor Hershel Layton) <V0220>:  
    `<V0220><T>Precisely.</V>`
*   **ルーク** (Luke Triton) <V0230>:  
    `<V0230><T>That means Dr Schrader was...</V>`
*   **レイトン** (Professor Hershel Layton) <V0240>:  
    `<V0240><T>Don Paolo in disguise, yes.</V>`
*   **ルーク** (Luke Triton) <V0250>:  
    `<V0250><T><A2/1>So you knew he was a fake before he even said four sentences!<W> Wow. You're good, Professor!</V>`
*   **レイトン** (Professor Hershel Layton) <V0260>:  
    `<V0260><T><A1/1>That planted the seed of doubt, though I didn't confirm my suspicion until much later.</V>`
*   **ルーク** (Luke Triton) <V0270>:  
    `<V0270><T><A1/1>Did Don Paolo pose as anyone else?</V>`
*   **レイトン** (Professor Hershel Layton) <V0280>:  
    `<V0280><T>Yes. He did a bit of spying on us as Dean Delmona when we met him last.</V>`
*   **レイトン** (Professor Hershel Layton) <V0290>:  
    `<V0290><T>From the moment I laid eyes on him, it was obvious we were dealing with an impostor.</V>`
*   **ルーク** (Luke Triton) <V0300>:  
    `<V0300><T>Amazing! How did you know?</V>`
*   **レイトン** (Professor Hershel Layton) <V0310>:  
    `<V0310><T><A1/2>His white hair gave it away.</V>`
*   **ルーク** (Luke Triton) <V0320>:  
    `<V0320><T><A4/1>But white hair seems perfectly natural on a man his age.</V>`
*   **レイトン** (Professor Hershel Layton) <V0330>:  
    `<V0330><T><A2/2>Not if he wears a wig. He let me in on his secret some time ago. He's been bald for ages.</V>`
*   **レイトン** (Professor Hershel Layton) <V0340>:  
    `<V0340><T>Don Paolo mistakenly selected a white wig to show how much Dean Delmona had aged.</V>`
*   **ルーク** (Luke Triton) <V0350>:  
    `<V0350><T><A1/1>Wow. Nice work there, Professor.</V>`
*   **レイトン** (Professor Hershel Layton) <V0360>:  
    `<V0360><T><A4/1>Shortly after that, I confronted Don Paolo and had him tell me everything.</V>`
*   **レイトン** (Professor Hershel Layton) <V0361>:  
    `<T><V0361>It seems Dimitri had been paying him quite handsomely to make sure we headed toward the pagoda.</V>`
*   **レイトン** (Professor Hershel Layton) <V0370>:  
    `<V0370><T>I filled Don Paolo in on all the strange happenings we've witnessed here.</V>`
*   **レイトン** (Professor Hershel Layton) <V0371>:  
    `<T><V0371>And then I requested his assistance in solving this mystery.</V>`
*   **ルーク** (Luke Triton) <V0380>:  
    `<V0380><T>Well, that all makes sense, I suppose...</V>`
*   **ルーク** (Luke Triton) <V0390>:  
    `<V0390><T>But the part I still don't get is why Don Paolo decided he wanted to help us.</V>`
*   **ルーク** (Luke Triton) <V0391>:  
    `<T><V0391>After all, this is the man who tried to run us over with a Ferris wheel.</V>`
*   **ドン・ポール** (Don Paolo) <V0400>:  
    `<V0400><T><A2/3>That's none of your business, brat!</V>`
*   **ルーク** (Luke Triton) <V0410>:  
    `<V0410><T><A1/3>Hey! Call me a brat again and just see what happens!</V>`
*   **レイトン** (Professor Hershel Layton) <V0420>:  
    `<V0420><T>It was Claire, Luke. It all had to do with Claire.</V>`
*   **ルーク** (Luke Triton) <V0430>:  
    `<V0430><T><A1/1>The woman Dimitri was talking about...</V>`
*   **レイトン** (Professor Hershel Layton) <V0440>:  
    `<V0440><T><A1/1>Claire was my...girlfriend, back when I was just starting my academic career.</V>`
*   **レイトン** (Professor Hershel Layton) <V0450>:  
    `<V0450><T>She was a researcher who worked in the same laboratory as Dimitri.</V>`
*   **ルーク** (Luke Triton) <V0460>:  
    `<V0460><T>Oh no! So she...</V>`
*   **レイトン** (Professor Hershel Layton) <V0470>:  
    `<V0470><T><A4/1>Yes... The last time I saw her, she was on her way to the lab the day of that massive explosion.</V>`
*   **レイトン** (Professor Hershel Layton) <V0480>:  
    `<V0480><T>The oddest thing is that the accident received very little media coverage.</V>`
*   **レイトン** (Professor Hershel Layton) <V0481>:  
    `<T><V0481>It's clear someone with a lot of influence was suppressing information about the incident.</V>`
*   **レイトン** (Professor Hershel Layton) <V0490>:  
    `<V0490><T>I did everything I could to research the matter on my own.<W> My efforts were largely fruitless.</V>`
*   **ルーク** (Luke Triton) <V0500>:  
    `<V0500><T>I had no idea...</V>`
*   **レイトン** (Professor Hershel Layton) <V0510>:  
    `<V0510><T>It's likely that Dimitri feels he is to blame for Claire's death.</V>`
*   **レイトン** (Professor Hershel Layton) <V0520>:  
    `<V0520><T>His obsession with going back in time seems like a twisted version of atonement.</V>`
*   **ルーク** (Luke Triton) <V0530>:  
    `<V0530><T><A4/4>What a terribly sad story...<W> <A4/1>But what does it have to do with Don Paolo?</V>`
*   **レイトン** (Professor Hershel Layton) <V0540>:  
    `<V0540><T><A3/2>Well Luke, as it turns out, Dimitri and I weren't the only ones with strong feelings for Claire.</V>`
*   **ルーク** (Luke Triton) <V0550>:  
    `<V0550><T><A1/6>What? You mean...</V>`
*   **ドン・ポール** (Don Paolo) <V0560>:  
    `<V0560><T>What?! Don't act so surprised!<W> I have...feelings too, you know!</V>`

### `09_033010.lbin.txt` — Don Paolo arqui-inimigo - Paul da universidade, sleuthing, retorno ao hotel

*   **ドン・ポール** (Don Paolo) <V0010>:  
    `<V0010><T><A4/1>Layton has been my arch-nemesis ever since that fateful day!</V>`
*   **ルーク** (Luke Triton) <V0020>:  
    `<V0020><T>I see...</V>`
*   **レイトン** (Professor Hershel Layton) <V0030>:  
    `<V0030><T><A4/2>Yes, though it's worth mentioning that I had no inkling of Paul's crush until he told me himself.</V>`
*   **レイトン** (Professor Hershel Layton) <V0040>:  
    `<V0040><T>He was in the year above me at university.</V>`
*   **レイトン** (Professor Hershel Layton) <V0041>:  
    `<T><V0041>Imagine my surprise when I learned that Don Paolo was none other than my old classmate Paul.</V>`
*   **ルーク** (Luke Triton) <V0050>:  
    `<V0050><T><A4/4>I had no idea you'd been through so much. Sorry for being so mean to you, um, Paul.</V>`
*   **ドン・ポール** (Don Paolo) <V0060>:  
    `<V0060><T><A2/3>Ugh. Spare me your sappy sympathy. <A5/2>And my name is Don Paolo. Address me as such, boy!</V>`
*   **レイトン** (Professor Hershel Layton) <V0070>:  
    `<V0070><T><A1/2>Anyway, you put on quite the performance, er, Don Paolo.</V>`
*   **レイトン** (Professor Hershel Layton) <V0080>:  
    `<V0080><T>With you distracting Dimitri, I had just enough time to do some sleuthing in the area.</V>`
*   **ルーク** (Luke Triton) <V0090>:  
    `<V0090><T><A3/2>So, that's what you were doing while we were climbing the pagoda! Did you find anything?</V>`
*   **レイトン** (Professor Hershel Layton) <V0100>:  
    `<V0100><T>Yes, but I need to confirm a few facts before I can connect all the dots.</V>`
*   **ルーク** (Luke Triton) <V0110>:  
    `<V0110><T>Then it sounds like that should be our next move. Where to, Professor?</V>`
*   **レイトン** (Professor Hershel Layton) <V0120>:  
    `<V0120><T><A1/2>Oh ho ho! I'll let you ponder that for yourself.</V>`
*   **レイトン** (Professor Hershel Layton) <V0130>:  
    `<V0130><T><A2/1>But first, we should head back to the hotel. Flora and the other Luke are waiting for us there.</V>`

---

## 5. Enigmas & Eventos Notáveis

| Arquivo | Enigma / Evento | Descrição |
|---|---|---|
| `09_026490` | **Segal's Preparation Enigma** | Trocadilho prepare/prepared; portão opcional antes do Pagoda. |
| `09_026500` | **Rudolph Pepper Gag** | Evento sem enigma: rendezvous clandestino com Pepper, Myrtle. |
| `09_026520` | **Pepper's Noodle Enigma** | Noodle enigmas no Noodle Palace; flavor + enigma opcional. |
| `09_026530` | **Deloy Portão Enigma** | Boss enigma portão: só passa quem o boss espera. |
| `09_026540` | **Professor Vanishing / Note Event** | Bilhete Go on without me nas costas de Flora. |
| `09_026550` | **Barmey Casino Enigma** | Barmey cobra enigma após rampage no casino. |
| `09_026560` | **Reappearance (dublado)** | Layton retorna com Sorry to keep everyone waiting. |
| `09_027010` | **Dragon Eyes Door Enigma** | Olhos do dragão como chave; Luke resolve. |
| `09_027020` | **Goggles Projection Enigma** | Personal projection device; Layton sente light-headed. |
| `09_027040` | **Walmy Vicious Enigma** | Irmão de Barmey, sock it to you with this vicious enigma. |
| `09_027050` | **Mirror Room Enigma** | Porta oculta no escuro; enigma de reflexão. |
| `09_027060` | **Sliding Block Floor Enigma** | Piso inteiro é sliding enigma antes da sala do falso Layton. |
| `09_029000` | **False Layton Confrontation (dublado)** | Charlatan reveal; sem enigma, só drama. |
| `09_029010` | **Block Memory / Pen Enigma** | Teste da caneta vazia + metáfora dos blocos; prova de memória. |
| `09_030010` | **Dimitri Exposition (dublado)** | Lore central: time machine, memory recorder, Claire. |
| `09_030020` | **Troop Relief Enigma (5 vs 5 stars)** | Red vs White; empate estratégico 2-2-1; enigma 671. |
| `09_031010` | **Double Layton Trap (dublado)** | Narração failed to ensnare the genuine article. |
| `09_032010` | **Lock Enigma + Ace in the Hole (dublado)** | Layton liberta grupo com Don Paolo decoy. |
| `09_032030` | **Tables Have Turned / Alarm + PM Kidnap** | Diversions, Bostro scarper, PM capturado, alarme. |
| `09_032040` | **Tunnel Map Enigma + Split** | Mapa emaranhado; divisão em dois grupos. |
| `09_032050`–`09_032080` | **Emergency Stairwell Escape** | Porta-parede, saída externa, aviso de heavy guard. |
| `09_032090` | **Don Paolo Retrospective (dublado 61 blocos)** | Schrader/Delmona wigs, backstory Claire/explosão. |
| `09_033010` | **Hotel Return Setup (dublado)** | Sleuthing de Layton no Pagoda, retorno ao hotel. |

**Eventos narrativos sem enigmas diretos:** Vivian gentleman line (`09_026510`), gloomy dragons (`09_027030`), top floor (`09_027055`), abertura de porta (`09_027070`), caminho bloqueado (`09_032035`).

---

## 6. Notas de Localização & Observações Técnicas

*   **Arquitetura de capítulo-ponte para clímax:** `09` tem 32 arquivos (vs 17 no Cap. 08) e mistura 7 arquivos dublados (`09_026560`, `09_029000`, `09_030010`, `09_031010`, `09_032010`, `09_032090`, `09_033010`) com longos corredores não-dublados de enigmas ambientais — estrutura típica de dungeon final de Level-5 antes do desfecho.
*   **Goggles = Chekhov's gun:** `09_027020` introduz personal projection device como enigma isolado; `09_030010` o ressignifica como cognitive capture unit / memory recorder que já extraiu memórias de Layton e futuro Bill. O mal-estar light-headed e tiring effect on the eyes é pista diegética do roubo.
*   **Falso Layton e teoria da memória em blocos:** `09_029010` é único enigma lógico-diegético sem interface de enigma tradicional; a metáfora All blocks are supported by other blocks. When you remove one, everything on top of it comes tumbling down. The same goes for memory. formaliza que amnésia em bloco destruiria persona — argumento que desmonta viagem no tempo falsa e antecipa discussão de wormholes em `09_030010`.
*   **Dimitri/Claire como espelho de Layton:** Texto repete like you, Hershel...I loved Claire e His obsession with going back in time seems like a twisted version of atonement. Layton limita com Nothing can excuse the kidnapping of all those scientists. Not even this, Dimitri. — tese moral do jogo sobre luto vs meios. Claire é explicitada como girlfriend...researcher who worked in the same laboratory as Dimitri morta na explosão com cobertura suprimida.
*   **Don Paolo como par romântico trágico:** `09_032090` revela que Paolo/Paul era calouro acima de Layton na universidade, concursado por Claire, e que trabalha com Layton por interesse convergente, não amizade — We both want answers to the same questions, so we decided to work together. A peruca branca de Delmona (careca bald for ages) entrega o disfarce, ecoando tema de disfarces falhos do Cap. 08 (cartola).
*   **Ace in the hole e diversions:** Layton some em `09_026540` para plantar diversions (I saw plenty of spots where one might conceal a trap) que só são pagos em `09_032030` com I imagine most of them will have their hands full for a few more minutes at least. e o decoy Don Paolo preso — construção de setup/payoff em dois atos.
*   **Wormhole lore:** Dimitri explica time travel is based on movement through wormholes. One end... anchored in the present. But every wormhole also needs a point of origin...Using your memories of those interactions, I will triangulate the point right before her death. e risco If my calculations were even the slightest bit off, I could be trapped...forever. — base científica para ato final no laboratório.
*   **Tropas e pedagogia de enigma:** `09_030020` usa relevo do século 18 com estrelas para ensinar estratégia vs força bruta; Layton prova empate 2-2-1 e sistema pede ao jogador Arrange your forces so that the red side avoids defeat. com marca <S671> visível no dump.
*   **Split party e controle de fluxo:** `09_032040` impõe divisão forçada too narrow for all of us to move through at the same time com Layton escolhendo ficar com Paolo para vigiá-lo (help him keep an eye on Don Paolo) e Flora/Big Luke como segundo grupo — portão narrativo que separa elenco para capítulos seguintes e justifica meet back at the hotel.
*   **Voz e texto:** 7 arquivos dublados concentram exposição (Dimitri, Don Paolo, Falso Layton); 24 arquivos não-dublados são enigmas de exploração com <A> e <W> mas sem <V>. Placeholder {''} para aspas internas preservado nos dumps; `09_000000` mantém cabeçalho vazio como em todos os capítulos.

---

*Gerado a partir de dumps LSCR brutos — 32/32 arquivos lidos. Nenhum diálogo inventado; todos os trechos são literais dos textos `uk/09`. Próximo capítulo: `10` — Verdade sobre o Futuro / Laboratório.*