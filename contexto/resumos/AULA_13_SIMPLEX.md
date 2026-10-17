# Aula 13 — Bases, custos reduzidos e teste de otimalidade

## Bases e geometria — pp. 2–33

Revisa forma padrão, folgas, restrições ativas, soluções básicas factíveis/infactíveis e partição `A=[B N]`. B tem m colunas independentes; as n−m restantes compõem N. Resolver `Bx_B=b` com `x_N=0` produz a solução básica. Não negatividade, e não positividade estrita, determina factibilidade: componentes básicas nulas são possíveis.

A expressão geral é `x_B=B⁻¹b−B⁻¹N x_N`. Testar todas as bases é combinatorialmente caro. O Simplex parte de uma base factível e faz trocas de base, buscando melhorar o objetivo. A descrição geométrica de ir a um vértice melhor é uma intuição; degenerescência pode ocasionar trocas sem melhora estrita.

## Teste de otimalidade — pp. 34–50

Para minimização em forma padrão, resolver `Bᵀλ=c_B` para obter os multiplicadores. Para variável não básica j, o custo reduzido é `c̄_j=c_j−λᵀa_j`.

```text
f(x) = c_BᵀB⁻¹b + Σ_(j não básico) c̄_j x_j
```

Se a base é factível e todos os custos reduzidos não básicos são **não negativos**, essa expressão fornece certificado de otimalidade para a PL. Custo reduzido zero é permitido. O material apresenta exercícios de cálculo a partir de uma base identidade e prepara a busca por uma base melhor na aula seguinte.

As condições de sinal dependem de minimização, forma padrão e convenção de custos reduzidos adotadas; não transplantá-las sem ajuste a outra representação.

## Relação com o projeto

Ajuda a entender como se certifica a solução de uma relaxação linear e por que valor factível e prova de ótimo são coisas diferentes. Não fornece solução inteira do BPP, branch-and-bound completo, cálculo de gap MIP nem código Gurobi/SCIP. Para cumprir o projeto, usar os solvers exigidos e manter a heurística de empacotamento como implementação distinta.

Fonte: [Aula13PM.pdf](../pdfs/Aula13PM.pdf), 50 páginas.
