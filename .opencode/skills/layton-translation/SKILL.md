---
name: layton-translation
description: Use ao traduzir jogos Professor Layton (playton-2/3) para PT-BR — aplica voz dos personagens, bordões, glossário e limites da caixa de diálogo. Aciona com translate, tradução, enigma, puzzle, hint coin, moeda de dica, Layton, Luke ou edição de Textos Traduzidos.
---

# Skill de Tradução — Layton

Skill para tradução **não-mecânica** de Professor Layton PT-BR. Use ao traduzir, revisar ou validar qualquer texto de `Textos Traduzidos`, `Textos Originais`, `Spec/` ou `Spec/Personagens/`.

## Quando usar

- `translate`, `tradução`, `enigma`, `puzzle`, `hint coin`, `moeda de dica`, `Layton`, `Luke`, `Flora`, `Don Paolo`, `Chelmey`, `Barton`
- Edição de `*.plz.txt`, `Spec/REGRAS_TRADUCAO.md`, `Spec/Personagens/*.md`
- Validação de caixa de diálogo (3 linhas, largura variável)

## Fontes de verdade (ler antes de traduzir)

1. **Regras obrigatórias:** `Spec/REGRAS_TRADUCAO.md` — glossário (`enigma`, `Livro de Enigmas`, `moeda de dica`, `cavalheiro`, `Inspetor/Agente`, `Vovó Riddleton`, `Don Paolo`), placeholders, caixa 3 linhas, tags na mesma posição e sem contar na largura, encoding `utf-8` sem BOM
2. **Voz por personagem:** `Spec/Personagens/_INDICE.md` → dossiê do falante (`Hershel_Layton.md`, `Luke_Triton.md`, `Flora_Reinhold.md`, `Clive_FutureLuke.md`, `Dimitri_Allen.md`, `Don_Paolo.md`, `Claire_Celeste.md`, `Chelmey_Barton.md`, `Coggs.md`, `Bostro_Family.md`, `Secundarios_*.md`, `Criaturas_Mascotes.md`) — **única fonte de registro, bordões e proibições; não fixar voz na skill**
3. **Continuidade J2→J3:** `Spec/Personagens/Mapeamento_Continuidae_Jogo2_Jogo3.md` + `Spec/Analise_Traducao_Jogo2.md` (nota 8.4/10) — o que manter (`Bem pensado!`, `Bom trabalho!`, `Pode deixar, Professor!`) e o que corrigir (`quebra-cabeça` → `enigma` exceto `jigsaw`, `Índice` → `Livro`, `Granny` → `Vovó`)
4. **Resumos narrativos:** `Spec/Capitulo_00_Prologo.md` → `Spec/Capitulo_14.md` + `Spec/Extras_18.md`/`19.md`/`20.md`/`30.md` — contexto narrativo e informações relevantes das falas e arquivos de cada capítulo. **Leia o resumo do capítulo antes de iniciar sua tradução e consulte o resumo específico do arquivo sempre que disponível.** Use esses documentos para manter continuidade de eventos, relações entre personagens, referências, objetos, locais, informações já reveladas e contexto de cada fala. Quando uma fala depender de acontecimentos de outro capítulo, consulte também o resumo correspondente. Não invente contexto ausente nos documentos.
5. **Original vs traduzido J2:** `../playton-2/Textos Originais/plz` ↔ `../playton-2/Textos Traduzidos/plz` — para checar `gentleman` → `cavalheiro` (`ev_t15.plz.txt:t15_020_500.gds:1`), `my boy` → `meu garoto` (`ht_tlk.plz.txt:ht_011_3:1`), `puzzle` → `enigma` (`txt2.plz.txt:tx_204:1`)
6. Nomes em japonês **não devem ser traduzidos**

> **Princípio de continuidade:** nunca trate uma fala como texto isolado. Antes de escolher uma tradução ambígua, verifique o contexto narrativo, o falante, a relação entre os personagens e o que já foi estabelecido no jogo. Uma tradução deve ser coerente não apenas com a frase original, mas com o universo narrativo e com as traduções já estabelecidas.

## Fluxo de trabalho

1. **Identifique o falante** pela tag `<01:0000000X>` / `レイトン`, `ルーク` etc. Abra o dossiê correspondente em `Spec/Personagens/` — ele define formalidade, gírias permitidas/proibidas e bordões.
2. **Carregue o contexto:** leia o resumo do capítulo que está sendo traduzido e, quando disponível, o resumo específico do arquivo. Consulte outros resumos de capítulos quando a fala fizer referência a acontecimentos anteriores, personagens, objetos, locais ou informações já estabelecidas. O contexto narrativo deve orientar a tradução, mas não substituir o texto original.
3. **Aplique o glossário** de `REGRAS_TRADUCAO.md:2` sem alterar.
4. **Escreva na voz do dossiê** — busque a personalidade, registro, bordões e proibições do personagem em questão em `Spec/Personagens/*.md`; não use lista fixa da skill, o dossiê é a fonte da verdade.
5. **Respeite a caixa:** 3 linhas por página (`!------------------------------!` = nova página). A largura de cada linha deve ser calculada usando as **métricas reais dos glifos da NFTR**, documentadas em `Spec/Fontes_NFTR.md`, e não por quantidade de caracteres ou estimativas de largura média. Antes de medir, decodifique placeholders `{...}` para caractere único (`{''}`→`"` 4px etc. `Spec/Fontes_NFTR.md:4`) — não some `{`/`}` como glifos. Para cada caractere já decodificado, use o valor `adv` correspondente na tabela CWDH e some os avanços da linha. Tags (`<01:...>`, `<W>`, `<A>`, `{#0}`) não contam. Nunca hifenizar — palavra inteira por linha. A tela do Nintendo DS tem 256 px de largura; nunca permita que uma linha ultrapasse fisicamente esse limite. Para a área útil específica de cada tela, use a configuração correspondente do Previewer.
6. **Nunca use `replace` literal com bloco que contém quebra de linha como chave.** O motor LSCR quebra diálogo em linhas físicas (`\n`) — uma chave sem `\n` não casa (causa raiz de `00_004000.lbin.txt:41` `Ummm - gulp...probable!\nHighly` ter ficado em EN). Em vez disso, **parseie por blocos** `re.findall(r'!\*{30}!(.*?)!\*{30}!', txt, DOTALL)` e traduza só o texto fora das tags dentro de cada bloco, preservando toda sequência `<V>`, `<T>`, `<W>`, `<A>` na mesma ordem.
7. **Valide:**
   - `Previewer/Configs/Screen01.ini` (`Texts.png`, `fontevent.nftr`, `ScreenNewLine 16`) + cálculo da largura real por `adv` da NFTR (decodificando placeholders antes). Não use contagem de caracteres, "caractere médio" ou largura estimada.
   - **Completude:** após traduzir, extraia todo `re.findall(r'<T>(.*?)</V>', original, DOTALL)` com `clean = re.sub(r'<[^>]+>','', snippet)` e verifique `clean not in traduzido` (exceção: nomes próprios `Stahngun|Baldwin|Midland Road`). Qualquer `clean` com `len>15` ainda presente = bloco não traduzido — falhar.
   - **Tags:** `len(re.findall(r'<[^>]+>', original)) == len(re.findall(r'<[^>]+>', traduzido))` e ordem idêntica por página.
   - **Oralidade:** leia **todo texto de personagem** (dublado `<V>` ou não — `レイトン`/`ルーク`/`バートン` etc.; não é narração) em voz alta como o falante do dossiê (idade/classe/estado). Se soar escrito, literal ou não falável, reescreva pelo sentimento antes de revalidar caixa.
8. **Checklist:** `REGRAS_TRADUCAO.md:6` (enigma 100%, Livro, moeda, Inspetor/Agente, placeholders, 3 linhas, largura real da NFTR com placeholders decodificados, `windows-1252`/`utf-8` sem BOM) + completude e oralidade acima.

## Passe gramatical (obrigatório, automático — sem discussão)

Gramática é **no-brainer**: corrige-se, não se discute. Rode `Spec/REGRAS_TRADUCAO.md` → *“Gramática PT-BR — correção automática”* sobre **todo** bloco do arquivo e aplique os fixes in-place. Não envie desvio gramatical como "proposta" ao usuário — só registre "já corrigido". Vale para: regência/crase (`chegar a/ao/à`, `páreo para`, `De que cor`, `olhar as`, `deslizar até`), subjuntivo após `supondo que`/`talvez`/`embora`, concordância verbal/nominal, gênero não inventado, ordem de advérbios, `embaixo`, dupla negativa, **continuidade de falas repetidas** (mesmo trecho `{''}` EN → PT idêntico) e voz do narrador (não coloquializar bloco sem falante).

O passe é **sempre duplo**: no fim da tradução/revisão autônoma **e de novo** no fim do passe interativo, após as correções aprovadas — edits e reflows introduzem erros novos.

## Revisão — contexto (quando já existe `Textos Traduzidos`)

Revisão não é retradução: é comparar `Textos Originais` vs `Textos Traduzidos` e julgar se a tradução soa estranha **no registro da cena e do falante**. Não use lista fixa de exemplos — infira pelo contexto narrativo e pelo dossiê. Eixos para avaliar:

1. **Registro cerimonial vs. coloquial:** discursos oficiais, apresentações e falas de autoridade exigem formalidade elevada e vocativo cerimonial; diálogos cotidianos exigem naturalidade falada. Se a tradução rebaixa ou eleva o registro em relação ao original e ao dossiê do falante, marque para revisão.
2. **Tradução literal que soa estranha em PT-BR:** idioms e construções inglesas que, traduzidas palavra a palavra, geram pleonasmo, calque sintático ou sentido mecânico em PT-BR. Julgue pela naturalidade do PT-BR no contexto — não por dicionário — e reescreva com idiom equivalente quando o literal quebrar a fluidez.
3. **Humor, trocadilho e jogo de palavras:** quando o original usa aliteração, trocadilho ou metáfora humorística, a tradução deve recriar o efeito em PT-BR em vez de neutralizar. Avalie se a graça/ironia se mantém falada em voz alta pelo personagem.
4. **Gênero gramatical:** em inglês objetos podem ser personificados como `she/her` (`old girl` para relógio, `her` para máquina). Em PT-BR o gênero é gramatical (`relógio` masc., `máquina` fem.). Não preserve o gênero inglês literalmente se gerar ambiguidade com pessoa; escolha o substantivo que mantém a personificação sem confundir referente (ex.: `a velha` só se `máquina` estiver explícita).
5. **Pleonasmo:** redundância que o original não tem (`convidado não convidado`, `subir para cima`, `ver com os olhos`). Se o PT-BR repete o mesmo traço semântico duas vezes, marque como pleonasmo e reduza ao termo idiomático (`intruso`, `subir`, `ver`).
6. **Número (singular/plural):** verifique concordância com o original e o glossário. Coletivo/plural inglês (`hint coins`, `scientists`) deve manter número em PT-BR (`moedas de dica`, `cientistas`), salvo genérico singular idiomático. Singular onde o original é plural quebra glossário e sentido.

Em todos os eixos, a fonte de verdade continua sendo o dossiê (`Spec/Personagens/*.md`) + resumo do capítulo. Marque apenas o que destoa do original **e** do registro esperado; não invente correção estilística fora desses critérios.

## Naturalidade coloquial — jovens e cômicos (sem quebrar época)

Coloquialidade só para quem o dossiê permite. Aplique o **princípio de personalidade** (`sentir → quer provocar → tom`) e consulte o dossiê (`Spec/Personagens/*.md:7`) para registro, bordões e proibições — **não fixe frase na skill; dossiê é a única fonte**. Se o dossiê não autoriza coloquialidade, use forma culta.

## Exemplos (ilustrativos, não copiar fora do contexto do dossiê)

- **CORRETO — Layton:** `Comporte-se, Luke. Um cavalheiro jamais força uma dama a falar mais do que ela quer.` (`ev_t15:t15_020_500.gds:1`)
- **INCORRETO — Layton:** `Se comporta, Luke. Um cavalheiro nunca força uma mina a falar.` — gíria, perde época
- **CORRETO — Barton coloquial controlado (ilustrativo):** hesitação + onomatopeia preservam humor faminto (`00_004000.lbin.txt:43` `Chelmey_Barton.md:3` `Ahn... glup... ahn... provável!` — `ahn` + `glup` + `Nhac` cabe em 3 linhas, `adv` <240px) — não é frase fixa, infira do dossiê a cada cena
- **INCORRETO — jovem coloquial excessivo:** `Véi, que festão, mano!` — quebra classe/época e bordão J2 `Pode deixar, Professor!`
- **CORRETO — caixa:** `Caro Hershel. Sendo o exímio` / `arqueólogo que sei que é, estou` — `ev_t10:t10_030_500.gds:1` — 3 linhas, com largura validada pelas métricas reais da NFTR e palavra inteira por linha

## Saída esperada

Ao traduzir, cite o dossiê e a regra usados: `Hershel_Layton.md:4` + `REGRAS_TRADUCAO.md:8`. Nunca invente bordão novo se já existe em J2.
