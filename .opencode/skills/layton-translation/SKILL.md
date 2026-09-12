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
5. **Respeite a caixa:** 3 linhas por página (`!------------------------------!` = nova página). A largura de cada linha deve ser calculada usando as **métricas reais dos glifos da NFTR**, documentadas em `Spec/Fontes_NFTR.md`, e não por quantidade de caracteres ou estimativas de largura média. Para cada caractere, use o valor `adv` correspondente na tabela CWDH e some os avanços da linha. Tags (`<01:...>`, `<W>`, `<A>`) não contam. Nunca hifenizar — palavra inteira por linha. A tela do Nintendo DS tem 256 px de largura; nunca permita que uma linha ultrapasse fisicamente esse limite. Para a área útil específica de cada tela, use a configuração correspondente do Previewer.
6. **Valide:** `Previewer/Configs/Screen01.ini` (`Texts.png`, `fontevent.nftr`, `ScreenNewLine 16`) + cálculo da largura real por `adv` da NFTR. Não use contagem de caracteres, "caractere médio" ou largura estimada como substituto da validação.
7. **Checklist:** `REGRAS_TRADUCAO.md:6` (enigma 100%, Livro, moeda, Inspetor/Agente, placeholders, 3 linhas, largura real da NFTR, `windows-1252`).

## Exemplos

- **CORRETO — Layton:** `Comporte-se, Luke. Um cavalheiro jamais força uma dama a falar mais do que ela quer.` (`ev_t15:t15_020_500.gds:1`)
- **INCORRETO — Layton:** `Se comporta, Luke. Um cavalheiro nunca força uma mina a falar.` — gíria, perde época
- **CORRETO — caixa:** `Caro Hershel. Sendo o exímio` / `arqueólogo que sei que é, estou` — `ev_t10:t10_030_500.gds:1` — 3 linhas, com largura validada pelas métricas reais da NFTR e palavra inteira por linha

## Saída esperada

Ao traduzir, cite o dossiê e a regra usados: `Hershel_Layton.md:4` + `REGRAS_TRADUCAO.md:8`. Nunca invente bordão novo se já existe em J2.
