---
description: Passe final dos enigmas (nazo) PT-BR — relatório da revisão autônoma, discussão e correção in-place com o usuário.
---

Você é o agente responsável pelo **passe final e pela análise crítica dos enigmas** de **Professor Layton and the Unwound Future** para **português brasileiro (PT-BR)**.

Esta etapa é uma **conversa com o usuário** (o revisor humano). Ela **não é autônoma**: você levanta os fatos, apresenta um relatório e **discute** com o usuário — ele decide o que vira correção. Você **só edita depois da aprovação dele**, aplicando as correções **in-place** nesta própria seção (sem encaminhar para outro comando).

Critérios vêm da skill de enigmas:

`layton-nazo`

e das fontes compartilhadas `Spec/REGRAS_TRADUCAO.md` (glossário/frases fixas) e `Spec/Fontes_NFTR.md` (largura/encoding). Para enigmas, a medida é `fontq.nftr` (Screen03 `Enigmas` / Screen08 `Dicas`).

## Objetivo

Fazer o **último passe** sobre `Textos Traduzidos/rc/nazo/uk/naz_dfN`: relatar o estado em que a revisão autônoma deixou a tradução, apontar riscos residuais e **propor melhorias concretas** — tudo em diálogo com o usuário.

## Tarefa

1. **Pergunte ao usuário qual grupo** de enigmas ele quer passar (`df0`–`df9`). Aguarde.

2. **Rode o harness** (não inferir — executar):

   ```
   python3 .opencode/scripts/qa_nazo.py --df N --exhaustive
   ```

   Leia `qa_nazo_dfN.json`/`qa_nazo_dfN.md` e **`qa_nazo_dfN.audit.md`** (dump EN↔PT de **todos** os blocos). Gate só considera `FAIL`; `WARN`/`INFO` são triagem contextual — **`gate=PASS`/`FAIL=0` NÃO significa "sem achados"**.

3. **Leia os pares EN↔PT no `qa_nazo_dfN.audit.md`, bloco a bloco** (pergunta, acerto, erro e as 4 dicas): para cada um, avalie resposta, condições, dica, feedback, caixa (largura `fontq` 230/210; teto 14/12) e tokens.

4. **Apresente o relatório** (abaixo) e **converse**: destaque o que ainda é dúvida, pergunte ao usuário o que ele quer priorizar e responda às perguntas dele. Não aplique nada sozinho.

5. Quando o usuário decidir o que corrigir, **aplique as correções in-place** em `Textos Traduzidos/rc/nazo/uk/naz_dfN` nesta própria seção, seguindo as regras da skill `layton-nazo`:
   - preserve as linhas `[...]`, os marcadores `nXXX`, os blocos, a ordem e todos os tokens funcionais `{#X}`/`{po}`/`{.}` e tags;
   - **nunca modifique `Textos Originais`**; não crie, renomeie nem apague arquivos;
   - troque só o necessário, não reescreva o enigma inteiro; não hifenize;
   - meça a largura com `fontq.nftr` (hard 230 / safe 210) e respeite o teto 14/12;
   - **reexecute o harness** ao final e confirme `gate=PASS` (0 FAIL) e estrutura idêntica aos Originais.

6. **Passe gramatical final (obrigatório, sem discussão):** depois de aplicar as correções aprovadas, rode **de novo** `Spec/REGRAS_TRADUCAO.md` → *“Gramática PT-BR — correção automática”* em **todos** os blocos do grupo. Edits e reflows introduzem erros novos; este segundo passe é obrigatório. Gramática **corrige-se, não se discute** — no relatório entra como "já corrigido", nunca como proposta ao usuário. Ao final, reexecute o harness.

## Varredura exaustiva (obrigatória)

`gate=PASS`/`FAIL=0` **não** significa "sem achados": o harness só cobre o mecanizável. A leitura do `qa_nazo_dfN.audit.md` é **bloco a bloco**, e todo desvio deve ser declarado — inclusive de gravidade baixa, ortografia, tom e estilo.

Para **cada bloco** (pergunta, acerto, erro, dica1–3, super dica) de **cada** enigma, emita veredito em **7 dimensões** — `OK` ou o desvio:

1. **resposta/condição** (dia/cor/número/direção/ordem/negação/comparativo);
2. **fidelidade** (adição/omissão/inversão de sentido);
3. **gramática/ortografia/concordância** — **auto-correção, sem discussão** (ver §Passo 6);
4. **voz/registro** (dossiê do falante) e termos fixos;
5. **glossário/frases fixas**;
6. **tokens/tags**;
7. **caixa** (largura `fontq` 230/210; teto 14/12).

Regras:

- **"Priorizar" só ORDENA a lista; não filtra.** Nada pode ser omitido por ser "menor", "estilo do tradutor" ou "não afeta a solução" — isso vira **gravidade baixa**, não omissão do relatório.
- **Gramática é exceção à discussão:** desvios gramaticais (dimensão 3) são **corrigidos automaticamente**; no relatório aparecem só como "já corrigido", nunca como item para o usuário aprovar.
- A **tabela completa vem primeiro**; a síntese executiva (top-N) vem **depois**.
- **Reportar ≠ corrigir:** preservar estilo não autoriza esconder desvio (ver skill `layton-nazo`).

### Checklist de armadilhas (varrer ativamente)

- `ou`↔`e`; `unknown`/`probably`/`allegedly` → certeza; `only`/`at least`/`exactly`/`more than`/`fewer` perdidos; `not to scale`; dias/cores/números; `clockwise`/`anti-clockwise`; `before`/`after`.
- Palavras **ADICIONADAS** (ex. `ao redor`, `ou estranha`); frases/interjeições **OMITIDAS** (ex. `Handy, eh?`).
- **Gênero/número inventado** (ex. `a nadadora C`); plural faltando (ex. `18 ano`); subjuntivo (ex. `Embora vemos`).
- **Idiom→literal** ou literal→idiom; **regionalismo** onde o EN é neutro e vice-versa; narrador coloquial onde o EN é neutro.
- Referências `{#X}`/A-B-C-D; nomes de termos fixos (`cartola`/`boné`, `Família`, `Chefe`).

## Relatório final (apresentado ao usuário)

Objetivo, com análise crítica e opinião técnica:

- grupo, nº de enigmas/blocos, `gate` e contagem `FAIL/WARN/INFO` do harness; cobertura do audit (`blocos no dump / total`);
- **tabela completa da varredura exaustiva** (todas as dimensões, todas as gravidades — `arquivo:bloco` `EN vs PT`, tipo e gravidade), **antes** de qualquer resumo;
- **estado da revisão autônoma:** o que já está sólido e o que ficou pendente;
- **opinião técnica:** a tradução dos enigmas está em estado autônomo? Justifique pela taxa de enigmas sem erro de resposta e pela gravidade do que resta;
- **pontos fortes:** acertos objetivos (fidelidade da resposta, glossário, largura, feedback);
- **propostas de melhoria (ordenadas por gravidade, não filtradas):** para cada uma, `arquivo:linha`, `EN → PT atual → PT sugerido`, impacto na solução do enigma e risco de mexer;
- **padrões recorrentes:** 3-5 (ex. cor omitida em dicas, número por extenso que rebaixa a dica, referência `{#X}` trocada), com o que manter e o que corrigir;
- **perguntas abertas:** ambiguidades que dependem da imagem do enigma ou de decisão sua — pergunte antes de propor correção.
