# Simplex revisado — implementação e atualização da base

O arquivo tem **25 páginas físicas**, mas a numeração dos slides salta da capa para 59/82 e termina em 82/82. As referências abaixo usam posições físicas no PDF.

## Implementação direta — pp. 2–8

As implementações diferem em como calculam e reutilizam `B⁻¹a_j`. Uma iteração direta resolve `Bᵀp=c_B`, calcula custos reduzidos `c̄_j=c_j−pᵀa_j`, escolhe coluna de entrada e resolve `Bu=a_j` para direção e passo.

Na contagem didática de álgebra densa apresentada, resolver sistemas/fatorar uma matriz de ordem m custa `O(m³)`, e calcular custos reduzidos para n colunas custa `O(mn)`, resultando em `O(m³+mn)` por iteração sem reaproveitamento adequado.

## Atualização da inversa — pp. 9–21

A nova base difere da anterior em uma coluna. O material deriva operações elementares que transformam a coluna `u=B⁻¹a_j` no vetor da identidade correspondente à posição de saída. Aplicar as mesmas operações a `B⁻¹` produz a nova inversa. O aproveitamento dessa estrutura reduz a contagem didática para `O(m²+mn)` por iteração.

Essas ordens são por iteração, para as operações descritas; não constituem garantia de tempo total polinomial do Simplex nem previsão do desempenho de Gurobi/SCIP. O tratamento prático de estabilidade, esparsidade e fatorações não é desenvolvido como tutorial de solver.

## Iteração completa — pp. 22–25

1. Partir de base factível e inversa da base.
2. Calcular multiplicadores e custos reduzidos; parar ótimo se todos forem ≥0 na minimização padrão.
3. Escolher custo reduzido negativo e calcular `u=B⁻¹a_j`.
4. Se `u≤0`, identificar melhoria ilimitada; senão usar razão mínima sobre `u_i>0`.
5. Trocar coluna, atualizar solução básica e atualizar a inversa.

## Relação com o projeto

É material de implementação de um algoritmo de **programação linear contínua**, não de utilização de um solver MIP. Ajuda a entender por que representações matematicamente equivalentes podem ter custos computacionais diferentes, mas não cobre comparação experimental entre Gurobi e SCIP, APIs, licenças, FFD/BFD ou gap de integralidade.

O projeto não exige escrever um Simplex próprio. Essa tarefa acrescentaria escopo sem resolver as principais lacunas da entrega.

Fonte: [Simplex-revisado.pdf](../pdfs/Simplex-revisado.pdf), 25 páginas.
