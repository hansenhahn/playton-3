---
name: layton-qa
description: Use ao revisar, validar ou corrigir tradução PT-BR de Professor Layton (playton-3) — QA semântico, glossário, voz, caixa e tags comparando Textos Originais vs Textos Traduzidos IA. Aciona com revisar, revisão, QA, validar tradução, corrigir tradução, segunda iteração, diff, proofread.
---

# Skill de QA — Layton

Skill de **segunda iteração** para Professor Layton PT-BR. Pressupõe que `Textos Traduzidos IA` já é uma primeira tradução autônoma suficientemente boa (fluente, ~95% correta) e atua como **revisor cirúrgico**: compara `Textos Originais/txt/uk` ↔ `Textos Traduzidos IA/txt/uk` e corrige apenas pequenos erros semânticos, de voz, glossário, tags e caixa — sem reescrever do zero.

> **Premissa:** erros invisíveis ao checklist técnico da `layton-translation` só caem no diff semântico com contexto. O QA reabre dossiê e capítulo antes de julgar; contexto desambigua tempo, deixis e voz.

## Quando usar

- `revisar`, `revisão`, `QA`, `validar tradução`, `corrigir tradução`, `segunda iteração`, `diff`, `proofread`
- Edição de `Textos Traduzidos IA/**/*.lbin.txt` comparando com `Textos Originais`
- Validação pré-`create_rom` ou pré-commit após tradução autônoma

## Fontes de verdade (mesmas da tradução — não duplicar)

1. **Regras obrigatórias:** `Spec/REGRAS_TRADUCAO.md` — glossário (`enigma`, `Livro de Enigmas`, `moeda de dica`, `cavalheiro`, `Inspetor/Agente`, `Vovó Riddleton`, `Don Paolo`), `REGRAS_TRADUCAO.md:6` checklist, `REGRAS_TRADUCAO.md:68-74` tags/caixa/largura NFTR. **Única fonte de obrigatoriedade.**
2. **Voz por personagem:** `Spec/Personagens/_INDICE.md` → dossiê (`Hershel_Layton.md`, `Luke_Triton.md`, `Flora_Reinhold.md`, `Clive_FutureLuke.md`, `Dimitri_Allen.md`, `Don_Paolo.md`, `Claire_Celeste.md`, `Chelmey_Barton.md`, `Coggs.md`, `Bostro_Family.md`, `Secundarios_*.md`, `Criaturas_Mascotes.md`) — proíbe `tá/pra/tô/né` em Layton/Luke, fixa `De fato.`, `Meu jovem`, `Pode deixar, Professor!`, `Caramba!`.
3. **Continuidade J2→J3:** `Spec/Personagens/Mapeamento_Continuidae_Jogo2_Jogo3.md` + `Spec/Analise_Traducao_Jogo2.md`
4. **Contexto narrativo:** `Spec/Capitulo_00_Prologo.md` → `Spec/Capitulo_14.md` + `Spec/Extras_*.md` — leia o capítulo do arquivo sendo revisado; se a fala referencia outro capítulo, consulte também. Contexto desambigua `from` temporal vs. destinatário.
5. **Métricas reais:** `Spec/Fontes_NFTR.md` + `Previewer/Configs/Screen01.ini` (`fontevent.nftr`, `ScreenNewLine 16`, largura útil ~240px). Tags não contam na largura.
6. Nomes em japonês **não traduzir**.

> **Princípio do revisor:** nunca julgue frase isolada. O QA reabre o dossiê do falante e o resumo do capítulo antes de decidir se uma escolha é erro semântico ou voz intencional. Se o tradutor errou por falta de contexto, o revisor corrige com contexto.

## Harness obrigatório (não inferir — executar)

Antes de qualquer julgamento, rode o validador genérico (vale para todos
os capítulos, mesmo sem IA/HUM traduzidos):

```
python3 .opencode/scripts/qa_chapter.py --cap <XX>
```

Ele mecaniza os bullets determinísticos: extração `<T>`→`</V>|!---!|!***!`
com `join('\n')`, block-count EN↔IA, tags multiset+posição (`REGRAS:68`),
≤3 linhas/página (`REGRAS:69`), hifenização (`REGRAS:71`), largura real
`adv` via `Previewer/Fontes/fontevent.nftr` (hard 247px / safe 210px),
`windows-1252`, glossário `\b`, voz com falante (FAIL só em Layton/Luke),
números EN↔PT, e watchlist semântica (`Unless`, `same page`, `WELL?`,
`Tee hee`, `my boy`, `Room/Old N`, `things... I mean`) como INFO para
revisão manual. Saída: `qa_<cap>.json` + `qa_<cap>.md`; exit 1 = há FAIL.

O rewrite cirúrgico continua obrigatório, mas **só após o harness**:
corrija os FAILs, julgue os INFO/WARN com `Capitulo_XX` + dossiê, e cite
`arquivo:linha` + regra no relatório.

## Fluxo de trabalho — segunda iteração

1. **Localize par:** para cada `Textos Traduzidos IA/txt/uk/<cap>/<arq>.lbin.txt`, abra `Textos Originais/txt/uk/<cap>/<arq>.lbin.txt` correspondente. Se `Textos Traduzidos/txt/uk` (humana) existir, use como terceira referência de gosto, não como verdade.
2. **Diff por bloco:** extraia `<T>...</V>` de ambos, faça `join('\n')` antes de comparar. Compare EN→PT sentido a sentido, não linha a linha, sempre com o resumo do capítulo à mão.
3. **Cheque técnico (bloqueante):** confira `REGRAS_TRADUCAO.md:68` tags na mesma posição e intactas, `REGRAS_TRADUCAO.md:69` ≤3 linhas por página, `REGRAS_TRADUCAO.md:71` sem hifenização, `windows-1252` sem `�` e largura real via `Spec/Fontes_NFTR.md:4` (`fontevent.nftr`/`fontq.nftr`, `Previewer/Configs/Screen01.ini`). Tags não contam. Se estourar largura ou quebrar caixa, reescreva **minimamente** preservando sentido.
4. **Cheque glossário:** confirme `puzzle→enigma`, `hint coin→moeda de dica`, `gentleman→cavalheiro`, `Inspector→Inspetor`, `Granny→Vovó` etc. conforme `REGRAS_TRADUCAO.md:2`. Uso de `grep` pode apoiar, mas o critério é terminológico, não ferramentístico.
5. **Cheque voz:** abra dossiê do falante (`_INDICE.md:40`). Avalie se o registro condiz com o personagem (ex. Layton/Luke não usam `tá/pra/tô/né` informal). Corrija para o registro do dossiê.
6. **Cheque concordância/gênero (contexto):** valide concordância interna PT-BR considerando referente em EN e contexto narrativo, não frase isolada. Consulte `Capitulo_XX.md` + dossiê para gênero de entidade/título.
7. **Cheque singular/plural (contexto):** compare número em EN vs PT com contexto de cena. Consulte `Capitulo_XX.md` para quantificação; plural coletivo só se EN for plural ou cena exigir.
8. **Cheque pleonasmo (contexto):** acuse redundância gerada em PT ausente em EN, validando com contexto narrativo. Só acuse se EN/contexto não for redundante.
9. **Cheque semântico (o que a primeira iteração não pega):** faça back-translation mental PT→EN com o capítulo aberto. Desambiguie `from` temporal vs destinatário, deixis, negação e inversões de papel consultando `Capitulo_XX.md`.
10. **Corrija cirurgicamente:** edite `Textos Traduzidos IA` **in-place**, preservando tags/quebras. Troque só o necessário e revalide com leitura contextual. Nunca apague `<W>` ou mova tag para fim da frase.

## O que corrigir vs. o que preservar

- **CORRIGIR:** erro semântico crítico mesmo que fluente (inversão temporal/destinatário), typo, glossário, gíria incompatível com dossiê, tag deslocada, quebra de caixa/largura.
- **PRESERVAR:** escolha estilística do tradutor que respeita dossiê e glossário, mesmo que diferente da humana.

## Validação final

Após correções no capítulo revisado, valide qualitativamente com contexto:
- glossário conforme `REGRAS_TRADUCAO.md:2` (sem inglês residual)
- voz conforme dossiê do falante (`_INDICE.md:40`)
- caixa/largura conforme `REGRAS_TRADUCAO.md:68-74` + `Fontes_NFTR.md:4` e conferência visual no `Previewer` (`Screen01.ini`); use medição exata de largura quando houver dúvida, não contagem de caracteres
- `diff` EN↔PT: cada `<T>` tem equivalente semântico, sem truncamento

## Saída esperada

Ao revisar, cite diff e regra (ex. `REGRAS_TRADUCAO.md:68` para tags, dossiê do falante para voz) e capítulo de contexto. Liste arquivos tocados, nº de fixes por categoria (técnico/glossário/voz/semântico) e se estrutura de `Textos Traduzidos IA` permanece idêntica a `Textos Originais`. Nunca invente bordão; se dúvida, registre como ambiguidade no relatório.
