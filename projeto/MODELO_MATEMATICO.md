# Modelo matemático base e adaptações

**Contexto atualizado:** o [tema do grupo](TEMA_DO_GRUPO.md) define baús heterogêneos e incompatibilidades, com Apresentação 1 em 11/11 — Aula 21. Os exemplos uniformes deste arquivo são a base; a implementação e o relatório devem seguir a variante escolhida. [Recursos externos](../contexto/recursos/README.md) complementam APIs, heurística e experimentos.

Fonte: enunciado, pp. 2–3, e Aula 05, pp. 37–39. As extensões abaixo são recomendações, não requisitos adicionais.

## Bin Packing unidimensional

Itens indivisíveis `I={1,...,n}`, caixas candidatas `J={1,...,m}`; `w_i` é o tamanho do item e `C` a capacidade uniforme. Hipóteses propostas para o núcleo: `C>0`, `0<w_i≤C`, recursos aditivos, caixas intercambiáveis e sem restrições geométricas ou de incompatibilidade.

O enunciado adota `m≥n`. Escolher **m=n** satisfaz essa condição e permite uma caixa por item. Para lista vazia, definir por convenção resultado de zero caixas; essa borda é recomendação de software.

Variáveis:

- `x_ij ∈ {0,1}`: item i alocado à caixa j.
- `y_j ∈ {0,1}`: caixa j utilizada.

```math
\min \sum_{j\in J} y_j
```

```math
\sum_{j\in J} x_{ij}=1 \quad \forall i\in I
```

```math
\sum_{i\in I} w_i x_{ij}\le C y_j \quad \forall j\in J
```

Cada item vai para exatamente uma caixa. A capacidade impede excesso e, com pesos positivos, impede alocar em caixa desativada. O objetivo reduz o número de caixas abertas.

## Reforços opcionais e limites — recomendações

- `x_ij ≤ y_j` explicita a ligação, fortalece a relaxação e também protege a semântica caso a variante aceite itens de tamanho zero.
- `y_j ≥ y_(j+1)` elimina parte da simetria; só é válida quando as caixas são intercambiáveis.
- `LB_volume=ceil(Σ_i w_i/C)` é limite inferior para o BPP uniforme 1D. Não é garantia de que o empacotamento com essa quantidade exista.
- Uma solução heurística factível com `U` caixas dá `OPT≤U`. Reduzir `m` a `U<n` preserva o ótimo sob as hipóteses do BPP base, mas diverge da escolha literal `m≥n` do enunciado: documentar a redução como otimização opcional, mantendo `m=n` como referência.
- O modelo com `m=n` tem `n²+n` variáveis binárias; considerar isso ao gerar instâncias grandes.

Não usar um Big-M arbitrário: `C` já é o limite físico da restrição de capacidade. Não misturar integralidade com não linearidade: este é um modelo linear inteiro binário.

## Variantes possíveis — dependem da aplicação escolhida

**Múltiplos recursos:** `w_ik` e `C_k`, com `Σ_i w_ik x_ij ≤ C_k y_j` para cada caixa j e recurso k. CPU e RAM são duas restrições. Com capacidades positivas e todos os itens individualmente compatíveis, um limite inferior é `max_k ceil(Σ_i w_ik/C_k)`.

**Caixas heterogêneas/custos:** substituir capacidade por `C_j` (ou `C_jk`) e objetivo por `Σ_j c_j y_j`, se o problema real exigir. Reavaliar limites, simetria e heurísticas.

**Incompatibilidades:** `x_ij+x_hj≤1` para pares que não podem compartilhar uma caixa. Requer validação adicional na heurística.

**Questões de prova:** fixar altura útil após margens/cabeçalhos; tratar cada questão como indivisível apenas se essa for a regra acordada. Minimizar páginas com soma de alturas não assegura legibilidade, ordem original ou penalidade por fragmentação: explicitar tais condições quando exigidas.

O usuário escolheu capacidades heterogêneas e incompatibilidades, conforme o documento do tema. As demais extensões continuam opcionais e não devem ser acrescentadas por padrão.
