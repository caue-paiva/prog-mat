# Literatura para o tema de armazenamento em jogos

Consultado em 17/10/2026. O [tema definido pelo grupo](../../projeto/TEMA_DO_GRUPO.md) é um jogo fictício com todos os recursos armazenados, conflitos entre itens e baús de capacidades diferentes. As fontes abaixo fundamentam as famílias matemáticas; não são evidência de regras existentes em um jogo real.

## Bin Packing com conflitos

**Fernandes Muritiba, Iori, Malaguti e Toth — Algorithms for the Bin Packing Problem with Conflicts.** [Publicação primária](https://pubsonline.informs.org/doi/10.1287/ijoc.1090.0355), volume 22(3), pp. 401–415, edição de 2010, publicada online em 2009. O resumo descreve pares que não podem compartilhar uma caixa, limites e abordagem exata por branch-and-price. Isso fundamenta representar incompatibilidade como grafo: item é vértice e incompatibilidade é aresta. O algoritmo completo não foi reproduzido nesta pesquisa.

**Gendreau, Laporte e Semet — Heuristics and lower bounds for the bin packing problem with conflicts**, Computers & Operations Research 31(3), pp. 347–358, 2004, DOI [10.1016/S0305-0548(02)00195-8](https://www.sciencedirect.com/science/article/pii/S0305054802001958). O resumo indexado da editora descreve heurísticas e limites para essa variante; a abertura direta retornou acesso negado. Usar a referência como leitura adicional, sem alegar consulta integral dos algoritmos.

**Bacci e Nicoloso — On the benchmark instances for the Bin Packing with Conflicts.** [Preprint dos autores, arXiv:1706.03526v3](https://arxiv.org/abs/1706.03526v3), 2017. O resumo aponta que um gerador usado na literatura produz grafos threshold em vez de grafos arbitrários e que essa estrutura influencia dificuldade. Para o grupo, isso motiva documentar como os conflitos são gerados; igual densidade não assegura igual estrutura ou dificuldade.

## Capacidades diferentes: cuidado com o objetivo

**Friesen e Langston — Variable Sized Bin Packing**, SIAM Journal on Computing 15(1), pp. 222–230, 1986, DOI [10.1137/0215016](https://epubs.siam.org/doi/abs/10.1137/0215016). A ficha e o resumo indexados da editora tratam capacidades variadas; a página direta retornou acesso negado nesta consulta.

A família “variable-sized” inclui formulações com objetivo de espaço total/custo. O projeto do grupo minimiza **quantidade de baús**, com inventário ainda a definir. Não transferir objetivos, hipóteses ou garantias de aproximação apenas pela semelhança do nome. O artigo ajuda a posicionar a extensão; não define sozinho a variante do grupo.

## Como construir a introdução do relatório — proposta

1. Apresentar o problema de organizar inventário de recursos no jogo fictício, com exemplos fornecidos pelo grupo.
2. Definir a ligação com BPP: itens indivisíveis, capacidade e minimização de recipientes.
3. Usar a literatura de conflitos para justificar os pares incompatíveis; relacionar essa restrição às aulas de coloração e variáveis binárias.
4. Explicar a extensão heterogênea e a política de disponibilidade de baús. Escrever o objetivo real, sem herdar minimização de custo dos artigos.
5. Justificar FFD como base simples e rápida, deixando a adaptação do grupo e suas limitações claramente descritas.

Não afirmar que as restrições representam toxicidade, segurança, empilhamento ou receitas de um jogo específico sem fonte e sem decisão do grupo. A matriz de compatibilidade e as capacidades serão parâmetros de um cenário hipotético. O alinhamento desse cenário à exigência de aplicação real consta como pendência no documento do tema.

## Delimitação proposta

Uma dimensão de consumo por item; pares incompatíveis simétricos; lista finita de baús candidatos; todos os itens armazenados; objetivo `min Σ_j y_j`. Não incluir geometria, descarte de recursos, valor de relíquias, roteamento, crafting ou evolução temporal sem nova decisão. Para leitura conceitual adicional do modelo compacto, consultar o [capítulo aberto de BPP](https://scipbook.readthedocs.io/en/latest/bpp.html).
