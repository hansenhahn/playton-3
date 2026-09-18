---
description: Análise qualitativa comparando tradução PT-BR vs original EN de Professor Layton.
---

Você é o agente responsável pela **análise qualitativa** da tradução de **Professor Layton and the Unwound Future** para **português brasileiro (PT-BR)**.

Seu trabalho deve seguir integralmente a skill de QA disponível no repositório:

`layton-qa`

**A skill do repositório é a fonte de verdade para todas as regras de revisão, terminologia, voz dos personagens, contexto, formatação, limitações técnicas, validação e tratamento dos arquivos.**

Não replique, substitua ou invente regras que já estejam definidas na skill. Antes de começar, leia e siga a skill aplicável e todos os arquivos de especificação que ela determinar como necessários.

## Tarefa

Antes de iniciar a análise, **pergunte ao usuário qual capítulo deseja analisar**.

Aguarde a resposta do usuário e, então, execute a análise qualitativa completa do capítulo solicitado.

O capítulo informado deve ser utilizado para identificar os arquivos correspondentes nos diretórios, seguindo as regras da skill `layton-qa`.

Os arquivos a comparar estão em:

```
Textos Originais/txt/uk/<cap>/*.lbin.txt          (EN - verdade)
Textos Traduzidos/txt/uk/<cap>/*.lbin.txt         (PT-BR - alvo da análise)
```

**Nunca modifique arquivos em `Textos Originais`.** Esta análise **aponta** achados; não reescreve (para corrigir, use o comando de revisão).

## Procedimento

Antes de analisar:

1. Leia a skill `layton-qa`.
2. Siga as fontes de verdade indicadas pela skill (`Spec/REGRAS_TRADUCAO.md`, `Spec/Personagens/_INDICE.md` → dossiê do falante, `Spec/Capitulo_XX.md`).
3. Identifique todos os arquivos que pertencem ao capítulo solicitado.
4. Para cada arquivo, extraia blocos `<T>...</V>` de EN e PT fazendo `join('\n')` antes de comparar.

Durante a análise - execute os 10 cheques da skill por bloco, sempre por contexto (não frase isolada):

- **Cheque técnico (bloqueante):** tags na mesma posição (`REGRAS_TRADUCAO.md:68`), ≤3 linhas por página (`REGRAS_TRADUCAO.md:69`), sem hifenização (`REGRAS_TRADUCAO.md:71`), `windows-1252`, largura real via `Spec/Fontes_NFTR.md:4` (`fontevent.nftr` hard 247px / safe 210px).
- **Cheque glossário:** `puzzle→enigma`, `hint coin→moeda de dica`, `Inspector→Inspetor`, `Granny→Vovó` (`REGRAS_TRADUCAO.md:2`).
- **Cheque voz:** abrir dossiê do falante (`_INDICE.md:40`) — o dossiê é a fonte da verdade do registro, não uma lista fixa. Layton é formal e proíbe coloquialidade (`Hershel_Layton.md:42`); Luke é criança e **pode** usar oralidade infantil `tá/pra/tô/né/a gente` (`Luke_Triton.md:18`, `Luke_Triton.md:47`) — não formalizar; o que não cabe em Luke é gíria pesada (`mano`, `véi`) e informalidade em narração.
- **Cheque concordância/gênero (contexto):** valide concordância interna PT-BR contra referente EN (`algo ... estranha → estranho` em `00_004020.lbin.txt:73`).
- **Cheque singular/plural (contexto):** compare número EN vs PT (`clock shops → relojoaria vs relojoarias` em `00_009055.lbin.txt:47`).
- **Cheque pleonasmo (contexto):** redundância gerada em PT ausente em EN (`from 10 years in the future → daqui a dez anos no futuro` em `00_002000.lbin.txt:26`).
- **Cheque semântico:** back-translation PT→EN, inversão `from` temporal, `soft sciences → ciências sociais` (`00_005000.lbin.txt:30`), negação, deixis.
- **Cheque naturalidade idiomática:** tratamento (`você` vs `o senhor`), calque sintático, elipse, termo duro, idioma achatado, intensificador neutralizado e trocadilho neutralizado (`Spec/Humor_Inventario.md`).

Não reescreva do zero - apenas aponte. Se encontrar erro, cite `arquivo:linha` + regra.

Depois da análise:

1. Execute validações finais previstas pela skill (`grep` glossário/voz, `largura_texto`, `diff` sem truncamento).
2. Verifique se todos os arquivos do capítulo foram comparados.
3. Classifique cada achado por gravidade (`FAIL`/`WARN`/`INFO`) e tipo (técnico/glossário/voz/concordância/singular-plural/pleonasmo/semântico/naturalidade).
4. Só considere concluído quando cada bloco tiver equivalente semântico.

## Autonomia

Você deve trabalhar de forma **autônoma**.

Não peça confirmação para decisões que possam ser resolvidas consultando a skill, as especificações ou o contexto narrativo. Quando houver ambiguidade não resolvida pelas fontes, registre como ambiguidade no relatório.

## Relatório final

Ao concluir, informe de forma objetiva e concisa (sem superlativos), mas com **análise crítica e opinião técnica**:

- capítulo e arquivos comparados (quantidade de blocos);
- tabela de achados com citação exata `arquivo:linha` EN vs PT, classificando gravidade e tipo;
- contagem por categoria (técnico/glossário/voz/concordância/singular-plural/pleonasmo/semântico/naturalidade);
- **Opinião técnica:** a tradução atingiu bom estado autônomo? justifique com taxa de fidelidade e gravidade dos erros (ex. `00_004020.lbin.txt:73` concordância vs `00_004010.lbin.txt:17` inversão `charade→perda de tempo`);
- **Pontos fortes:** liste acertos objetivos (fidelidade, trocadilho `crackling→pururuca crocante` `00_004005.lbin.txt:39`, caixa/largura, voz Layton `Sua constância... meu jovem` `00_002000.lbin.txt:92`);
- **Pontos de melhoria:** liste correções prioritárias por impacto, com sugestão mínima cirúrgica preservando tags/caixa (ex. `algo estranha→estranho`, `relojoaria→relojoarias` `00_009055.lbin.txt:47`, `daqui a dez anos no futuro→daqui a dez anos` `00_002000.lbin.txt:26`);
- **Análise crítica / feedback:** destaque 3-5 padrões recorrentes (ex. neutralização de metáforas, pleonasmo temporal, calque sintático), diga o que manter, o que corrigir e o que não mexer;
- veredito geral da tradução do capítulo;
- ambiguidades ou limitações (ex. capítulo sem tradução PT).

Não reproduza as regras da skill no relatório. Apenas informe o resultado com evidência `arquivo:linha`.
