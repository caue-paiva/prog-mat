# Aula 05 — Variáveis inteiras, mochila e Bin Packing

## Contínuo, inteiro e relaxação — pp. 2–23

PL usa variáveis contínuas; PLI impõe integralidade; PLIM combina ambos os domínios. A região de PL é convexa, enquanto pontos inteiros geralmente não formam um conjunto convexo. O conjunto inteiro é finito nos exemplos limitados apresentados, mas integralidade sozinha não garante finitude.

Mesmo com variáveis binárias, existem `2^n` atribuições antes de filtrar restrições: o espaço cresce rapidamente. Arredondar uma solução contínua pode gerar inviabilidade ou perder o ótimo. O domínio deve refletir o significado da decisão: ingredientes em kg podem ser contínuos; número de ônibus é inteiro. Variáveis binárias também servem como ferramenta para custos fixos e lógica.

## Mochila — pp. 24–31

Mochila binária: selecionar itens de pesos `w_i` e benefícios `p_i`, maximizando `Σ_i p_i x_i` sob `Σ_i w_i x_i≤C`, `x_i∈{0,1}`. Alguns itens podem ficar de fora. O material cita branch-and-bound como método de solução.

Mochila inteira com repetições: `x_i` conta cópias e pertence aos inteiros não negativos. Relaxar o domínio para contínuo amplia a região factível; em maximização, o valor relaxado é um limite superior para o ótimo inteiro.

## Múltiplas mochilas — pp. 32–36

Há um número fixo de recipientes com capacidades `b_j`. `x_ij` indica que o item i foi colocado na mochila j. Maximizar `Σ_i Σ_j p_i x_ij`, impondo `Σ_i w_i x_ij≤b_j` e `Σ_j x_ij≤1`. A segunda restrição permite não selecionar um item. Extensões incluem vários recursos e tempos dependentes da máquina.

## Bin Packing — pp. 37–39

Aqui **todos os itens devem ser colocados**, e o número de mochilas usadas é minimizado. `y_j` indica uso da caixa; `x_ij` indica alocação. Formulação com n caixas candidatas:

```text
min Σ_j y_j
Σ_j x_ij = 1                  para todo item i
Σ_i w_i x_ij ≤ C y_j          para toda caixa j
x_ij, y_j binárias
```

Esta é a conexão mais direta dos slides com o projeto. A capacidade multiplicada por `y_j` impede carga positiva numa caixa desativada. Mochila, múltiplas mochilas e BPP não têm o mesmo objetivo nem a mesma obrigação de atendimento.

## Custos fixos e lotes — pp. 40–47

A alocação de banda é apresentada como aplicação da mochila. Custos de preparação podem ser representados por `s_i y_i+c_i x_i`, com `x_i≤M_i y_i`. Isso força produção positiva a ativar a preparação; não força sozinho `x_i=0 ⇒ y_i=0`. Um custo fixo positivo minimizado elimina ativações desnecessárias no modelo simples.

Dimensionamento de lotes usa produção `X_it`, estoque `I_it` e preparação `Y_it`. Balanço: `I_i,t−1+X_it=d_it+I_it`. A capacidade agrega tempo produtivo e de preparação; `X_it≤M_it Y_it` vincula produção à ativação. O objetivo ilustrado soma preparação e estoque.

## Inconsistências e uso no projeto

Na mochila didática, a tabela da p. 25 dá peso 75 ao primeiro objeto, mas a fórmula da p. 27 usa 70. O texto anuncia vetor com dez objetos, porém a solução ilustrada tem oito componentes e peso indicado não coerente com as tabelas. Não usar esse exemplo como teste numérico sem corrigir a instância.

Para BPP (minimização), a direção do limite relaxado se inverte em relação à mochila de maximização: relaxação dá limite inferior. O modelo completo e adaptações propostas estão em `../../projeto/MODELO_MATEMATICO.md`.

Fonte: [Aula 05.pdf](../pdfs/Aula%2005.pdf), 48 páginas.
