# Caixeiro Viajante — redes e eliminação de sub-rotas

Muitas fórmulas estão em imagens; as páginas sobre caminho mínimo e formulações foram conferidas visualmente. O objetivo deste resumo é registrar os modelos e sua relação com a disciplina, sem transformar BPP em roteamento.

## Caminho mínimo — pp. 2–6

Ir da origem ao destino com custo mínimo; não é necessário visitar todas as cidades. Binária por arco e objetivo de soma dos custos dos arcos selecionados. Balanços indicam uma unidade saindo da origem, entrando no destino e conservação nos nós intermediários. Os slides assumem arcos sem laços e custos positivos; essas hipóteses ajudam a evitar ciclos extras com custo favorável.

## Problema do Caixeiro Viajante — pp. 7–26

Encontrar um circuito hamiltoniano de custo mínimo: visitar cada cidade exatamente uma vez e retornar ao início. No caso simétrico, `c_ij=c_ji`; no assimétrico, isso não é garantido. A enumeração de rotas cresce fatorialmente; o material apresenta história e exemplos de soluções computacionais como motivação.

Na formulação dirigida, `x_ij=1` se a cidade j é visitada imediatamente após i, com `i≠j`:

```text
min Σ_i Σ_(j≠i) c_ij x_ij
Σ_(j≠i) x_ij = 1        uma saída de cada cidade i
Σ_(i≠j) x_ij = 1        uma entrada em cada cidade j
x_ij binária
```

Essas restrições de designação sozinhas permitem vários ciclos desconectados. Visitar cada nó não assegura um único circuito.

## Eliminação de sub-rotas e cortes — pp. 27–31

Para cada subconjunto próprio S com pelo menos dois vértices, impor `Σ_(i∈S) Σ_(j∈S,j≠i) x_ij≤|S|−1`. Impede formar um ciclo todo dentro de S. A quantidade de subconjuntos cresce exponencialmente.

Os slides apresentam a ideia de resolver uma relaxação/modelo parcial, identificar sub-rotas, adicionar restrições violadas e resolver novamente. Uma solução inteira sem sub-rotas atende a conectividade desejada. A implementação de separação/cortes não é detalhada em código.

## Formulação MTZ — pp. 32–42

Variáveis auxiliares de ordem `u_i` aumentam a cada arco selecionado entre cidades que não são o depósito. Uma versão normalizada pode usar `1≤u_i≤n−1` e `u_i−u_j+n x_ij≤n−1` para `i≠j`, ambos diferentes do depósito. Se o arco é escolhido, `u_j≥u_i+1`; somar esses aumentos ao redor de um ciclo sem depósito gera contradição.

O depósito fica fora dessas restrições de ordem para permitir o circuito principal. O material mostra uma versão equivalente de implicação com Big-M; limites e índices precisam ser coerentes com a convenção adotada.

## Exercício final e aplicação — pp. 43–46

O exercício de postos de saúde exige servir seis povoados a distância de até 15 km com o menor número de postos. É **cobertura de conjuntos**: para cada povoado, pelo menos um posto acessível deve ser instalado. Não é PCV.

Recordes e números históricos do PDF não foram atualizados nem devem ser apresentados como recordes atuais. Para o projeto de BPP, aproveitar a lição de que restrições locais podem ser insuficientes para propriedades globais e de que uma formulação correta precisa ser auditada com contraexemplos. Não adicionar MTZ ao BPP sem uma decisão explícita de modelar também rotas.

Fonte: [Caixeiro Viajante.pdf](../pdfs/Caixeiro%20Viajante.pdf), 46 páginas.
