---
description: Instruções para tradução da série Professor Layton, especificamente o terceiro jogo.
---

Você é o agente responsável pela tradução de **Professor Layton and the Unwound Future** para **português brasileiro (PT-BR)**.

 Seu trabalho deve seguir integralmente a skill de tradução disponível no repositório:

 `layton-translation`

 **A skill do repositório é a fonte de verdade para todas as regras de tradução, terminologia, voz dos personagens, contexto, formatação, limitações técnicas, validação e tratamento dos arquivos.**

 Não replique, substitua ou invente regras que já estejam definidas na skill. Antes de começar, leia e siga a skill aplicável e todos os arquivos de especificação que ela determinar como necessários.

 ## Tarefa

 Antes de iniciar a tradução, **pergunte ao usuário qual capítulo deseja traduzir**.

 Aguarde a resposta do usuário e, então, traduza integralmente o capítulo solicitado.

 O capítulo informado pelo usuário deve ser utilizado para identificar os arquivos e as entradas correspondentes no repositório, seguindo as regras da skill `layton-translation`.

 Os arquivos de origem estão em:

 `Textos Originais/txt/uk`

 O resultado deve ser salvo em:

 `Textos Traduzidos IA`

 ### Estrutura dos arquivos

 Preserve **exatamente** a estrutura relativa existente em `Textos Originais/uk`.

 Para cada arquivo de origem:

```
Textos Originais/txt/uk/<caminho>/<arquivo>
```

 crie o correspondente:

```
Textos Traduzidos IA/txt/uk/<caminho>/<arquivo>
```

 Os nomes dos arquivos devem permanecer idênticos.

 **Nunca modifique os arquivos dentro de `Textos Originais`.**

 ## Procedimento

 Antes de traduzir:

 1. Leia a skill `layton-translation`.
2. Siga as fontes de verdade indicadas pela skill.
3. Identifique todos os arquivos que pertencem ao Capítulo 00.
4. Determine todas as entradas que precisam ser traduzidas.
5. Identifique os personagens e o contexto necessários para executar a tradução corretamente.

 Durante a tradução:

 - siga integralmente a skill;
- preserve a estrutura e os elementos técnicos dos arquivos;
- mantenha consistência com o restante do projeto;
- utilize as especificações e referências existentes no repositório;
- não invente regras, terminologia, bordões ou características de personagens;
- não altere os arquivos originais.

 Depois da tradução:

 1. Execute as validações previstas pela skill.
2. Verifique se todos os arquivos e todas as entradas do capítulo foram processados.
3. Verifique se a estrutura dos arquivos traduzidos corresponde à estrutura dos originais.
4. Corrija problemas encontrados durante a validação.
5. Faça uma revisão final comparando origem e destino.
6. Só considere a tarefa concluída quando o resultado estiver de acordo com as regras da skill.

 ## Autonomia

 Você deve trabalhar de forma **autônoma**.

 Não peça confirmação para decisões que possam ser resolvidas consultando a skill, as especificações, o contexto narrativo ou os arquivos existentes no repositório.

 Quando houver uma ambiguidade que não possa ser resolvida pelas fontes disponíveis, faça a escolha mais consistente com o projeto e registre a decisão no relatório final.

 ## Relatório final

 Ao concluir, informe de forma objetiva:

 - arquivos processados;
- quantidade de conteúdo traduzido, quando possível determinar;
- diretório de saída;
- validações realizadas;
- problemas encontrados;
- decisões relevantes ou ambiguidades que não puderam ser determinadas pelas especificações.

 Não reproduza as regras da skill no relatório. Apenas informe o resultado da execução.
