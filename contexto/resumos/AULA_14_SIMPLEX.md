# Aula 14 — Direção Simplex e troca de base

## Da otimalidade à melhoria — pp. 2–20

Revisa custos reduzidos e procura uma variável não básica k com `c̄_k<0` para minimização. Aumentar `x_k` em ε altera o objetivo em `c̄_k ε`, mas a nova solução precisa continuar factível.

O critério “base factível e todos os custos reduzidos ≥0 implica ótimo” é suficiente mesmo com degenerescência. A interpretação recíproca — custo reduzido negativo necessariamente permite melhora imediata a partir dessa base — exige cuidado com degenerescência; o PDF destaca essa ressalva na p. 4.

## Direção, passo e pivô — pp. 21–32

Resolver `By=a_k`. Ao aumentar a variável que entra:

```text
x_k = ε
x_B(novo) = x_B(atual) − ε y
```

Preservar não negatividade exige `ε≤x_Bi/y_i` para componentes `y_i>0`. Portanto `ε*=min_(i:y_i>0) x_Bi/y_i`. Uma variável que atinge zero sai e sua coluna é substituída por `a_k`.

Se não houver componente positiva em y e `c̄_k<0`, há direção factível de melhoria ilimitada. O caso é `y≤0`, incluindo componentes zero, não apenas todas estritamente negativas. Empates e passos zero precisam de tratamento ao implementar um algoritmo geral.

## Algoritmo e exemplos — pp. 33–41

Apresenta Fase II, inicialização simples por colunas de folga quando possível e exercícios para continuar as iterações. A Fase II pressupõe base inicial factível; obtê-la de modo geral é assunto do material de base inicial.

## Relação com o projeto

Aprofunda a resolução de PLs e o significado de melhoria e ilimitabilidade. Não é método alternativo de empacotamento: aplicar Simplex ao relaxamento do BPP pode gerar atribuições fracionárias. Não há especificação de FFD/BFD, protocolo comparativo ou uso das interfaces de Gurobi/SCIP.

Fonte: [Aula14SimplexDeterminandoSolucaoMelhor.pdf](../pdfs/Aula14SimplexDeterminandoSolucaoMelhor.pdf), 41 páginas.
