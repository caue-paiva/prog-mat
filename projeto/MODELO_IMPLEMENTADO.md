# Modelo implementado

## Hipóteses e dados

I: itens individuais; J: inventário finito de baús; E: pares não ordenados incompatíveis. Tamanho w_i e capacidade C_j inteiros positivos em UA. Cada item é indivisível; não há geometria, peso adicional, custo diferenciado, aquisição de baús nem restrição de tipo. Regras de categoria geram E e são unidas aos conflitos por ID.

x_ij = 1 se i ocupa j; y_j = 1 se j é utilizado. Ambas binárias.

```math
\min \sum_{j\in J} y_j
```

```math
\sum_{j\in J} x_{ij} = 1 \quad (i\in I)
```

```math
\sum_{i\in I} w_i x_{ij} \le C_j y_j \quad (j\in J)
```

```math
x_{ij} \le y_j \quad (i\in I,j\in J)
```

```math
x_{ij}+x_{hj}\le 1 \quad (\{i,h\}\in E,j\in J)
```

```math
y_j\le \sum_i x_{ij} \quad (j\in J), \qquad x_{ij},y_j\in\{0,1\}
```

Alocação exata impede descarte e duplicação. Capacidade vincula consumo e abertura. Vínculo individual reforça a relaxação. Conflitos proíbem coexistência, sem impedir categorias diferentes compatíveis. A desigualdade de não vazio torna a ativação semanticamente exata também em soluções intermediárias. Fixar x_ij=0 se w_i>C_j. Para cada grupo de baús com a mesma capacidade, ordenar seus y em ordem não crescente; nunca impor essa simetria entre capacidades distintas. Modelo tem n*m+m variáveis e n+2*m+n*m+|E|*m restrições antes de simetria, sem contar limites de variáveis.

## Redução segura de candidatos

Se a heurística fornece solução factível com U baús, OPT<=U. Ordene todo o inventário por capacidade não crescente e mantenha os primeiros U. Considere uma solução ótima com k<=U baús; ordene suas capacidades d_1>=...>=d_k. A r-ésima maior capacidade global C_(r) satisfaz C_(r)>=d_r. Transfira integralmente cada grupo de itens do baú r dessa solução para o r-ésimo maior baú global. A carga continua permitida e todos os pares de itens permanecem juntos/separados como antes. Logo existe solução com k baús no inventário reduzido. A inclusão do conjunto reduzido no original dá a desigualdade oposta e ambos os ótimos são iguais. A redução falha em generalizações com restrições por tipo ou custos diferenciados; não usar nesse caso.

Se FFD falhar, manter J inteiro. Nos dados gerados, m=n originalmente; a redução é uma transformação computacional explicitada, não mudança silenciosa do inventário. Ambos os solvers usam a mesma redução e não recebem warm start.

## Limites e status

LB de volume é o menor k com soma das k maiores capacidades >= soma dos tamanhos. Se tal k não existir, o inventário não comporta o volume. Este bound ignora incompatibilidades e indivisibilidade. Não é automaticamente o ótimo. Os solvers registram seu melhor bound global, diferente da relaxação linear inicial. Gap comum (%) = 100*(UB-LB)/max(abs(UB),1); nativo é preservado em fração. Para objetivo 0 e bound 0, gap 0.

Resultados ótimos requerem status ótimo do solver; a rotina FFD conserva rótulo factível mesmo quando iguala um limite. Igualdade H=LB pode certificar o valor durante a análise, sem transformar o método em algoritmo exato geral.

## Ligação com as aulas

Aula 05, seção de Bin Packing: objetivo, x/y e alocação de todos os itens. Aula 06 e notebook Aula06.ipynb: vínculo lógico entre atividade e ativação; aqui C_j fornece limite físico, sem M arbitrário. Aula 08: partição, cada item exatamente uma vez. Modelagem com variáveis inteiras: incompatibilidades lineares. Simplex e bases: relaxação e limites; arredondar solução contínua não substitui a solução inteira.
