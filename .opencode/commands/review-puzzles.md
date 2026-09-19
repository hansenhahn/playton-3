---
description: Revisão automatizada + análise crítica dos enigmas (nazo) PT-BR — roda qa_nazo.py e corrige Textos Traduzidos/rc/nazo/uk/naz_dfN in-place.
---

Você é o agente responsável pela **revisão (segunda iteração) dos enigmas** de **Professor Layton and the Unwound Future** para **português brasileiro (PT-BR)**.

Seu trabalho deve seguir integralmente a skill de enigmas disponível no repositório:

`layton-nazo`

**A skill do repositório é a fonte de verdade para preservação da resposta, tokens, estrutura, formatação e limites técnicos.** Regras compartilhadas continuam em `Spec/REGRAS_TRADUCAO.md` (glossário) e `Spec/Fontes_NFTR.md` (largura/encoding). Para enigmas, a fonte de medida é `fontq.nftr` (Screen03 `Enigmas` / Screen08 `Dicas dos Enigmas`), não `fontevent`.

Não replique, substitua ou invente regras já definidas na skill.

## Tarefa

Antes de iniciar, **pergunte ao usuário qual grupo de enigmas deseja revisar** (`df0`–`df9`).

Aguarde a resposta e revise o grupo solicitado. Como **todos os enigmas já estão traduzidos**, não há etapa de tradução: a pipe é **revisão automatizada (harness) → análise crítica → correção cirúrgica in-place → validação**.

Arquivos:

```
Textos Originais/rc/nazo/uk/naz_dfN/*.lbin.txt     (EN — verdade)
Textos Traduzidos/rc/nazo/uk/naz_dfN/*.lbin.txt    (PT-BR — alvo, editar in-place)
```

**Nunca modifique `Textos Originais`. Nunca crie, renomeie ou apague arquivos.**

## Estrutura de um enigma (não alterar)

Cada arquivo tem **8 blocos** iniciados por uma linha `[...]`, e as linhas `[...]` (header/ponteiro) são **idênticas EN↔PT**:

| Papel | Prefixo | Conteúdo |
|---|---|---|
| `meta` | `ea0b…` | metadado + marcadores `nXXX`, `nXXXa`, `nXXXb` |
| `question` | `eb0b…` | pergunta |
| `correct` | `ec0b…` | feedback de acerto |
| `wrong` | `ed0b…` | feedback de erro |
| `hint1..3` / `super` | `ee0b…`, `ef0b…`, `f00b…`, `f10b…` | dicas |

## Procedimento

1. Leia a skill `layton-nazo` e `Spec/REGRAS_TRADUCAO.md` (glossário `enigma`, `moeda de dica`, `Livro de Enigmas`; frases fixas `Bem pensado!`/`Bom trabalho!`/`Excelente!`).

2. **Rode o harness obrigatório** (não inferir — executar):

   ```
   python3 .opencode/scripts/qa_nazo.py --df N
   ```

   Ele gera `qa_nazo_dfN.json` + `qa_nazo_dfN.md` e mecaniza:
   - estrutura: nº de blocos, marcadores e linhas `[...]` idênticas EN↔PT;
   - tokens de controle `{...}`: `{#A}`, `{po}` (libra), `{.}` (lista) são **funcionais**; `{''}` (aspas) e `{9}` (apóstrofo) são estilísticos;
   - tags (`<CR>`/`</C>`), encoding `U+FFFD`, glossário, hifenização;
   - largura real por linha via `fontq.nftr` (**hard 230px / safe 210px**);
   - nº de linhas por bloco vs teto real da caixa (**14** em Screen03 pergunta/acerto/erro; **12** em Screen08 dicas/super dica — derivado da geometria dos fundos + `NewLine 12`);
   - números do EN sem equivalente PT (possível omissão), dias da semana (FAIL) e cores (WARN);
   - watchlist de termos críticos de enigma (esquerda/direita, acima/abaixo, par/ímpar, maior/menor, antes/depois, dobro/metade, fileira/coluna/diagonal, multiplicar/dividir, horário/anti-horário).

   Gate `PASS`/`BLOCKED` considera só os `FAIL`.

3. **Triagem dos achados:** `FAIL` = corrigir. `WARN` = julgar com contexto (número/cor omitidos podem ser erro real ou paráfrase). `INFO` = revisão manual (termos críticos, linhas extras, glifos).

4. **Análise crítica por enigma (obrigatória):** para cada par `Originais ↔ Textos Traduzidos`, leia pergunta, acerto, erro e as 4 dicas lado a lado. Verifique:
   - **a resposta é a mesma?** dias, cores, números, direções, ordem/posição e referências `{#X}`/A-B-C-D;
   - **nenhuma condição foi invertida ou omitida?** (negação, `at least`/`exactly`, `clockwise`, `before/after`);
   - **a dica não entrega a resposta errada** por tradução ambígua;
   - feedback EN e PT dizem o mesmo (não precisa casar palavra a palavra, mas o sentido/erro deve ser o mesmo).

5. **Correção cirúrgica in-place** em `Textos Traduzidos/rc/nazo/uk/naz_dfN`:
   - preserve as linhas `[...]`, os marcadores `nXXX`, os blocos e a ordem;
   - preserve todos os tokens funcionais `{#X}`, `{po}`, `{.}`, `{9}` e tags;
   - mantenha a quebra de linha como no original; se ganhar/perder linhas, revalide a largura;
   - **não hifenizar**; nenhuma palavra quebrada com `-`;
   - medir largura com `fontq.nftr` antes de fechar o fix (hard 230 / safe 210);
   - troque só o necessário; não reescreva o enigma inteiro.

6. **Reexecute o harness** ao final e confirme `gate=PASS` (0 FAIL) e que a estrutura permanece idêntica aos Originais.

## O que corrigir vs. preservar

- **CORRIGIR:** omissão/inversão de resposta (dia/cor/número/direção), token funcional perdido, tag/token quebrado, glossário, largura `>230px`, hifenização, `�`.
- **PRESERVAR:** paráfrase fluente que mantém sentido e resposta; sinônimo de feedback aceitável; estilo do tradutor.

## Relatório final

Objetivo e conciso, com `arquivo:linha` e regra:

- grupo e nº de enigmas/blocos; `gate` antes e depois;
- arquivos tocados e nº de fixes por categoria (estrutura/token/técnico/glossário/semântico);
- tabela curta `arquivo:bloco` `EN → PT antes → PT depois` + regra;
- pendências/ambiguidades (ex. cor que não confere com a imagem) sem inventar regra.
