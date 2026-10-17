# Aula 02 — Modelagem e programação linear contínua

## Construção e classificação — pp. 3–9

Começar ouvindo quem conhece o problema real. Identificar o que decidir (variáveis), o que está disponível (dados) e as relações que limitam decisões (restrições). Definir o objetivo separadamente.

Programação linear (PL): objetivo e restrições lineares, variáveis contínuas. Programação linear inteira (PLI): variáveis inteiras. Programação linear inteira mista (PLIM): variáveis contínuas e inteiras. Formas matriciais exemplificadas incluem `min cᵀx`, `Ax≥b`, com o domínio apropriado; o sentido das desigualdades depende do problema.

Hipóteses da PL: **aditividade**, **proporcionalidade** e **divisibilidade**. A contribuição total resulta da soma das contribuições individuais; consumo/custo por unidade é proporcional à quantidade; valores fracionários são aceitos quando fazem sentido físico.

## Dieta e mistura — pp. 10–42

No exemplo de dieta, `x_L` representa porções de 100 ml de leite achocolatado e `x_P` porções de 100 g de pão com manteiga. Modelo:

```text
min 0,9 x_L + 0,1 x_P
70 x_L + 2,5 x_P ≥ 130       # cálcio mínimo
83 x_L + 343 x_P ≤ 480       # energia máxima
x_L, x_P ≥ 0
```

Mistura/ração: escolher quantidades de ingredientes com custo mínimo e nutrientes mínimos. Exemplo: `min 65x_M+30x_F`, com `2x_M+3x_F≥7`, `3x_M+2x_F≥9`, `x_M≥1`, `x_F≥0`. Os slides apresentam `(1,3)`, custo 155.

No modelo geral, `a_ij` é a fração do componente i no ingrediente j; `x_j` é a quantidade usada e `c_j` seu custo. Para uma unidade de mistura, `Σ_j x_j=1`; a composição pode ser exata, `Σ_j a_ij x_j=b_i`, ou ter limites `r_i≤Σ_j a_ij x_j≤p_i`. Para Q unidades, a soma passa a Q e limites de composição tornam-se `r_i Q` e `p_i Q`.

A história do problema da dieta ilustra diferenças entre heurística e ótimo provado e a importância de limites que evitem soluções matematicamente válidas, mas inadequadas na prática.

## Planejamento da produção — pp. 43–69

Escolher quantidades de produtos para maximizar receita/margem, respeitando recursos e limites de venda/produção. Forma típica: `max Σ_j c_j x_j`, `Σ_j a_ij x_j≤b_i`, com limites inferiores/superiores de produção.

Exemplo de geladeiras: `max 100x_1+50x_2`, `10x_1+8x_2≤25000`, `x_1+x_2≤4500`, `0≤x_1≤1500`, `0≤x_2≤6000`. A escolha de domínio precisa refletir se se contam unidades indivisíveis ou se se trabalha com uma aproximação contínua.

A resolução gráfica dos exemplos apresenta interseção de semiplanos, região factível e deslocamento das retas de nível do objetivo. Ela é instrumento didático para poucas variáveis.

## Atenção e conexão com o projeto

No exemplo da padaria, o texto da p. 45 informa 38 unidades de fermento, mas tabela/modelo das pp. 46 e 48 usam 30. Não transportar esses números sem resolver a inconsistência. Para Bin Packing, itens são indivisíveis e a alocação deve ser binária: a divisibilidade da PL não representa a solução final. Manter unidades compatíveis e não inventar restrições apenas para ajustar resultados.

Fonte: [Aula02PM (1).pdf](../pdfs/Aula02PM%20%281%29.pdf), 70 páginas.
