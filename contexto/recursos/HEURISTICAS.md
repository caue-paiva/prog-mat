# Método alternativo — FFD como caminho mínimo

Consultado em 17/10/2026. Escolher FFD atende à categoria de heurística sugerida no enunciado para o BPP base; não é obrigatório implementar uma meta-heurística adicional.

## Referência teórica verificada

György Dósa, **The Tight Bound of First Fit Decreasing Bin-Packing Algorithm Is FFD(I) ≤ 11/9 OPT(I) + 6/9**, ESCAPE 2007, LNCS 4614, pp. 1–11, DOI [10.1007/978-3-540-74450-4_1](https://link.springer.com/chapter/10.1007/978-3-540-74450-4_1).

O resumo público define FFD e enuncia o limite `FFD(I)≤(11/9)OPT(I)+6/9`, além de afirmar que é justo. A prova integral não foi consultada. A garantia se refere ao BPP unidimensional clássico de caixas idênticas; não atribuí-la automaticamente a CPU/RAM, incompatibilidades, capacidades heterogêneas ou geometria 2D/3D.

**Interpretação derivada:** 11/9 é um fator assintótico, não promessa de erro máximo de 22,22% em toda instância finita, pois existe termo aditivo. A heurística também não fornece por si só um limite inferior.

O capítulo aberto [Bin packing and cutting stock problems](https://scipbook.readthedocs.io/en/latest/bpp.html) apresenta FFD em Python e seu uso para obter um limite superior de caixas. Há ainda a tese original de David S. Johnson, **Near-optimal bin packing algorithms** (MIT, 1973), disponível pelo [repositório institucional](https://dspace.mit.edu/entities/publication/b6bde6a7-fedf-4f2a-9184-24318ff54c85). A ficha foi verificada; a tese não foi lida integralmente nesta pesquisa.

## Especificação operacional proposta

Entrada: itens identificáveis, tamanhos positivos ≤ C e capacidade C positiva. Preservar IDs, mesmo se tamanhos forem iguais.

```text
caixas := lista vazia
ordenar itens por tamanho decrescente; desempatar por posição original
para cada item:
    percorrer caixas na ordem de abertura
    se encontrar a primeira caixa com espaço suficiente:
        alocar nela e atualizar a carga
    senão:
        abrir uma caixa e alocar o item
retornar caixas e alocações
```

Esta especificação adapta a definição de FFD ao contrato de dados do projeto. Definir lista vazia como zero caixas. Cronometrar ordenação e construção conjuntamente. Na implementação direta, cada item pode percorrer todas as caixas: custo `O(n log n+nU)`, até `O(n²)`. Não anunciar `O(n log n)` para uma busca linear por caixa.

## BFD e extensões opcionais

Para **Best-Fit Decreasing**, manter ordenação decrescente e escolher, entre as caixas factíveis, a que deixa a menor sobra; desempatar pela ordem de abertura. É a especificação operacional de uma opção mencionada no enunciado; esta pesquisa não atribui a ela uma garantia teórica de aproximação específica. FFD sozinho já permite o caminho mínimo com fonte teórica identificada.

Para uma meta-heurística, a publicação primária de Emanuel Falkenauer, [A hybrid grouping genetic algorithm for bin packing](https://link.springer.com/article/10.1007/BF00226291), apresenta algoritmo genético de agrupamento com melhoria local. O resumo e os dados bibliográficos foram consultados, não os operadores completos. Usar como leitura adicional, não como especificação suficiente para reproduzir o algoritmo nem como obrigação do projeto.

## Validação analítica proposta

| C; tamanhos | O que verificar |
|---|---|
| 10; `[6,4,5,5]` | FFD usa 2 caixas e atinge limite de volume 2 |
| 10; `[6,6,6]` | Usa 3 caixas; volume sozinho só limita por 2 |
| 10; `[6,5,3,2,2,2]` | FFD usa 3; ótimo é 2 pelas caixas `[6,2,2]` e `[5,3,2]` |
| 10; `[]` | Retorna zero caixas |
| 10; `[11]` | Identificar item impossível, sem abrir caixa inválida |

São exemplos calculados, não resultados de uma execução. Aplicar o mesmo validador de alocação e capacidade usado nas soluções dos solvers.

## Adaptação proposta ao tema definido

Para baús heterogêneos de inventário finito e conflitos, consultar primeiro [TEMA_DO_GRUPO.md](../../projeto/TEMA_DO_GRUPO.md). O procedimento abaixo é uma política inicial proposta pelo agente, não um algoritmo da publicação de Dósa:

```text
ordenar itens por tamanho decrescente, desempatar pelo índice original
para cada item i:
    procurar a primeira caixa aberta j que satisfaça:
        carga_j + w_i ≤ C_j
        nenhum item h já em j forma par incompatível com i
    se encontrada, alocar i nela
    senão, procurar nos baús ainda disponíveis algum que comporte i
        política inicial: menor capacidade suficiente, desempate por ID
    se encontrado, abrir esse baú e alocar i
    senão, encerrar sem solução completa e registrar o motivo
```

A incompatibilidade pode ser consultada por pares de itens ou por matriz de categorias. Se houver conflito de uma categoria com ela própria, dois itens dessa categoria não podem compartilhar baú. Validar toda a alocação; verificar apenas o último item inserido não basta para auditar uma solução arbitrária.

Uma busca direta que varre todos os itens de cada baú para cada tentativa pode custar mais que o FFD escalar original. Se as regras forem exclusivamente por categoria, conjuntos de categorias e contagens podem acelerar consultas, preservando a regra de conflito interno. Não declarar a complexidade clássica sem analisar a implementação adaptada.

Com inventário limitado, uma decisão gulosa pode consumir um recurso necessário adiante. Registrar solução parcial separadamente; ela não dá UB para o objetivo de armazenar todos os itens. Se for implementado reparo, explicitar movimentos, limite de esforço e tempo incluído. Não comparar uma heurística com inventário ilimitado contra solvers com inventário finito.

Referência conceitual para essa extensão: [Algorithms for the Bin Packing Problem with Conflicts](https://pubsonline.informs.org/doi/10.1287/ijoc.1090.0355). A proposta acima continua sendo uma adaptação do grupo a validar experimentalmente.
