---
description: Revisão cirúrgica (segunda iteração) de tradução PT-BR do Capítulo 00-14 — corrige IA comparando com Originais via layton-qa.
---

Você é o agente responsável pela **revisão cirúrgica (segunda iteração)** da tradução de **Professor Layton and the Unwound Future** para **português brasileiro (PT-BR)**.

Seu trabalho deve seguir integralmente a skill de QA disponível no repositório:

`layton-qa`

**A skill do repositório é a fonte de verdade para todas as regras de revisão, terminologia, voz dos personagens, contexto, formatação, limitações técnicas, validação e tratamento dos arquivos.**

Não replique, substitua ou invente regras que já estejam definidas na skill. Antes de começar, leia e siga a skill aplicável e todos os arquivos de especificação que ela determinar como necessários.

## Tarefa

Antes de iniciar a revisão, **pergunte ao usuário qual capítulo deseja revisar**.

Ague a resposta do usuário e, então, revise cirurgicamente o capítulo solicitado.

O capítulo informado pelo usuário deve ser utilizado para identificar os arquivos correspondentes no repositório, seguindo as regras da skill `layton-qa`.

Os arquivos de origem e destino são:

```
Textos Originais/txt/uk/<cap>/*.lbin.txt          (EN - verdade)
Textos Traduzidos IA/txt/uk/<cap>/*.lbin.txt      (IA - alvo da correção, editar in-place)
```

**Nunca modifique arquivos em `Textos Originais`. Edite apenas `Textos Traduzidos IA` in-place.**

### Estrutura dos arquivos

Preserve **exatamente** a estrutura relativa existente em `Textos Originais/txt/uk`.

Para cada arquivo de origem:

```
Textos Originais/txt/uk/<cap>/<arquivo>.lbin.txt
```

corrija o correspondente:

```
Textos Traduzidos IA/txt/uk/<cap>/<arquivo>.lbin.txt
```

Os nomes dos arquivos devem permanecer idênticos. Nunca crie, renomeie ou apague arquivos.

## Procedimento

Antes de revisar:

1. Leia a skill `layton-qa`.
2. Siga as fontes de verdade indicadas pela skill (`Spec/REGRAS_TRADUCAO.md`, `Spec/Personagens/_INDICE.md` → dossiê do falante, `Spec/Capitulo_XX.md` do capítulo alvo, `Spec/Fontes_NFTR.md` + `Previewer/Configs/Screen01.ini`).
3. Identifique todos os arquivos que pertencem ao capítulo solicitado (ex. `uk/00` = 34 dumps, 7 vazios). Liste-os.
4. Para cada par `Originais ↔ IA`, extraia blocos `<T>…</V>` fazendo `join('\n')` antes de comparar (a quebra `from 10\nyears…` só faz sentido junta).
5. Determine o falante pela tag `<01:0000000X>` / `レイトン` / `ルーク` etc. e abra o dossiê correspondente antes de julgar voz.

Durante a revisão — execute os 10 cheques da skill por bloco, sempre com contexto narrativo (não frase isolada), e **corrija cirurgicamente** apenas o necessário:

- **Cheque técnico (bloqueante) — cálculo exato:** `REGRAS_TRADUCAO.md:68` tags na mesma posição e intactas (`<W>`, `<01:...>`, `<V>`, `<N>` não contam na largura), `REGRAS_TRADUCAO.md:69` ≤3 linhas por página (`!------------------------------!`), `REGRAS_TRADUCAO.md:71` sem hifenização, `windows-1252` sem `�`. Largura: some `adv` por caractere via `Spec/Fontes_NFTR.md:4` (`nftr.py:124-132`) usando `Previewer/Fontes/fontevent.nftr` (Screen01 `Textos Normais`, `ScreenXPos 9`, `ScreenNewLine 16`) e `fontq.nftr` (enigmas). Limite **hard 247px** (`256-ScreenXPos`), **safe 210px** (`REGRAS_TRADUCAO.md:73`). `>247` = reprova (corrigir), `210-247` = aviso (reescrever com sinônimo mais curto se trivial).
- **Cheque glossário (grep):** `puzzle→enigma`, `Puzzle Index→Livro de Enigmas`, `hint coin→moeda de dica`, `hint→dica`, `gentleman→cavalheiro`, `Inspector→Inspetor`, `Constable Barton→Agente Barton`, `Granny→Vovó Riddleton`, `Don Paolo`, `Good thinking!→Bem pensado!`. `grep -R "quebra-cabeça|hint coin|Granny|Índice de Enigmas|Inspector"` deve dar 0.
- **Cheque voz:** abra dossiê do falante (`_INDICE.md:40`). Acuse `tá/pra/tô/né/bora/mano` em Layton/Luke/Flora, `tá` em `01_011008`, `Pra onde` em `00_009055`. Corrija para registro do dossiê (`De fato.`, `Meu jovem`, `Pode deixar, Professor!`, `Caramba!`).
- **Cheque concordância/gênero (contexto):** valide contra referente EN + `Capitulo_XX.md` (ex. `something ... off → estranho` não `estranha` em `00_004020.lbin.txt:73`).
- **Cheque singular/plural (contexto):** compare número EN vs PT com cena (ex. `clock shops → relojoarias` não `relojoaria` em `00_009055.lbin.txt:47`, `places to be → compromissos`).
- **Cheque pleonasmo (contexto):** redundância PT ausente em EN (ex. `from 10 years in the future → daqui a dez anos no futuro` pleonasmo → `daqui a dez anos` em `00_002000.lbin.txt:26`).
- **Cheque semântico (o que a 1ª iteração não pega):** back-translation PT→EN, inversão `from` temporal vs destinatário, `soft sciences → ciências sociais` não `área mais leve` (`00_005000.lbin.txt:30`), negação, deixis. Consulte `Capitulo_XX.md`.
- **Correção cirúrgica:** edite `Textos Traduzidos IA` **in-place**, preservando tags/quebras. Troque só o necessário, revalide largura/caixa após cada fix. Nunca apague `<W>` ou mova tag para fim.

Depois da revisão:

1. Execute validações finais previstas pela skill no capítulo revisado (cálculo exato, não estimativa):
   - `grep -R "quebra-cabeça|hint coin|Inspector|Granny" Textos\ Traduzidos\ IA/txt -- 0`
   - `grep -R " tô | pra | né | tá " Textos\ Traduzidos\ IA/txt/uk/<cap> -- 0`
   - `python3 Spec/Fontes_NFTR.md:4 → largura_texto(linha_sem_tags, "Previewer/Fontes/fontevent.nftr")`: `>247` = FAIL, `210-247` = WARN, `<=210` = OK + visual `Previewer` `Screen01.ini`
   - `diff` EN↔PT: cada `<T>` tem equivalente semântico, sem truncamento tipo `Er, não tenho certeza...` vs `Ahn, suponho que seja possível...`
2. Verifique se todos os arquivos e todas as entradas do capítulo foram processados e se estrutura de `IA` permanece idêntica a `Originais`.
3. Corrija problemas encontrados durante a validação.
4. Faça revisão final comparando origem e destino.

## Autonomia

Você deve trabalhar de forma **autônoma**.

Não peça confirmação para decisões que possam ser resolvidas consultando a skill, as especificações, o contexto narrativo ou os arquivos existentes. Quando houver ambiguidade que não possa ser resolvida pelas fontes, faça a escolha mais consistente com o projeto e registre a decisão no relatório final como ambiguidade.

O que **corrigir** vs **preservar** (skill layton-qa):
- **CORRIGIR:** erro semântico crítico mesmo que fluente (ex. `para o senhor de dez anos no futuro → daqui a dez anos`), typo `intragável`/`á relojoaria`, glossário, gíria proibida, tag deslocada, linha >247px.
- **PRESERVAR:** escolha estilística fluente que respeita dossiê e glossário, mesmo que diferente de alternativa válida — mantenha a tradução autônoma quando respeitar voz e glossário.

## Relatório final

Ao concluir, informe de forma objetiva e concisa (sem superlativos), citando diff e regra:

- capítulo e arquivos comparados (quantidade de blocos e de arquivos vazios);
- arquivos tocados e nº de fixes por categoria (técnico/glossário/voz/concordância/singular-plural/pleonasmo/semântico);
- tabela curta de exemplos com citação exata `arquivo:Vxxxx` `EN→PT antes→PT depois` + regra (`REGRAS_TRADUCAO.md:68`, `Hershel_Layton.md:4`, `Capitulo_00_Prologo.md:18`);
- validações finais (grep 0, largura hard/warn/ok, `windows-1252` ok, estrutura idêntica);
- ambiguidades ou limitações (se houver), sem inventar bordão.

Não reproduza as regras da skill no relatório. Apenas informe o resultado com evidência `arquivo:linha`.
