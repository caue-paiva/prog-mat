# Aula 04 — Corte, padrões e empacotamento

## Motivação e padrões — pp. 2–23

Produzir peças pequenas cortando objetos grandes, atendendo demandas e reduzindo material ou custo. Aplicações: chapas, bobinas, barras, tecido e carregamento.

No exemplo de panelas, `x_j` conta chapas cortadas segundo a matriz j. O objetivo é `min x_1+2x_2+3x_3+2x_4`, com `8x_1+4x_2+2x_3≥500` para peças médias e `x_2+2x_3+3x_4≥350` para grandes. Os slides contrastam solução contínua e inteira.

Para barras de comprimento L e tipos de peças com comprimentos `l_i`, um **padrão** é um vetor de quantidades inteiras `α_i≥0` satisfazendo `Σ_i l_i α_i≤L`. É uma configuração factível de uma barra, relacionada a uma mochila inteira. Exemplo: `L=170`, comprimentos `(30,50,55)`, demandas `(80,120,110)`; o material enumera 27 padrões não vazios.

## Formulação por padrões — pp. 24–34

`a_ij`: número de peças do tipo i no padrão j. `x_j`: número de barras cortadas com esse padrão. Modelo normalizado:

```text
min Σ_j x_j
Σ_j a_ij x_j ≥ d_i       para todo tipo i
x_j inteiro não negativo
```

Objetivo alternativo apresentado: `min Σ_j r_j x_j`, em que `r_j=L−Σ_i l_i a_ij` é a perda física no padrão. Relaxar integralidade produz PL, que não assegura quantidades inteiras de barras. O número de padrões pode ser enorme; os slides mencionam geração de colunas e mochila como caminho para lidar com isso, sem desenvolver o algoritmo completo.

## Comparação de objetivos e padrões — pp. 35–43

Com seis padrões selecionados, os slides apresentam 115 barras para minimizar quantidade; com todos os 27, apresentam 90 barras sem sobra de itens. Minimizar só retalhos pode produzir excesso de itens: a solução ilustrada de perda zero usa 55 vezes `(2,0,2)` e 120 vezes `(4,1,0)`, sobrando 510 peças do primeiro tipo. Assim, perda de corte zero não equivale a menor uso de barras ou atendimento exato.

Esses valores são resultados didáticos informados pelos slides, não execuções deste repositório.

## Vários tipos de objetos e modelo direto — pp. 44–50

Com tipos k de barras, comprimentos `L_k` e disponibilidade `e_k`, usar padrões específicos e variáveis `x_jk`. Formulação normalizada: atender cada demanda com `Σ_k Σ_j a_ijk x_jk≥d_i`; limitar estoque por `Σ_j x_jk≤e_k`; minimizar barras ou custo. A soma extra sobre i que aparece na p. 47 não deve ser reproduzida na restrição já indexada por i.

Uma alternativa é modelar cada barra candidata diretamente, com binária de uso e quantidades inteiras de peças em cada barra; um limite superior para candidatas pode vir de padrões homogêneos.

## Ressalvas e aplicação ao BPP

Para o padrão `(1,2,0)`, a perda correta com os dados apresentados é `170−30−100=40`. A tabela da p. 22 mostra 50, enquanto o objetivo da p. 39 usa 40. Recalcular a partir das dimensões.

No BPP com itens individuais, cada item deve aparecer exatamente uma vez; no corte por tipos, `≥ demanda` permite sobreprodução. Não copiar a desigualdade de atendimento de corte para a atribuição individual do BPP. A formulação compacta por item/caixa é suficiente como base; geração de colunas é extensão opcional.

Fonte: [Aula04PM (1).pdf](../pdfs/Aula04PM%20%281%29.pdf), 51 páginas.
