# Modelagem com variáveis inteiras — Parte 2

## Custos fixos e implicações — pp. 5–13

Uma decisão de usar um serviço/produzir pode gerar custo fixo mais custo proporcional à quantidade. Com `x≥0`, `y` binária e limite superior válido U, usar `x≤Uy` e custo `F y+c x`. Se `x>0`, y precisa valer 1. Se `x=0`, y ainda pode valer 1; um custo F positivo minimizado tende a eliminar essa escolha desnecessária, mas a equivalência não vem apenas da desigualdade.

Produção combinada: para impor “se fabricar produto 1, fabricar pelo menos m do produto 2”, usar `x_1≤U_1 y` e `x_2≥m y`, com m positivo e limites coerentes. Não impor a recíproca sem necessidade.

Exemplo de equipe exclusiva: se uma equipe assume projeto 1, não pode assumir os projetos 2, 3 e 4. Uma formulação normalizada é `x_i1+x_is≤1` para cada `s∈{2,3,4}`. O mecanismo auxiliar do slide pode usar uma binária específica por equipe para ativar/desativar as atribuições; uma única binária global não deve acoplar equipes independentes.

## Restrições disjuntivas — pp. 14–24

Uma escolha pode exigir pelo menos uma entre duas condições. Para `f(x)≤0 OU g(x)≤0`, escrever `f(x)≤M_f(1−y)`, `g(x)≤M_g y`, `y∈{0,1}`. Exemplo mostrado: `4x_1+2x_2≤80 OU 2x_1+5x_2≤100`, com variáveis não negativas.

M precisa vir de limites válidos sobre o domínio; se não existe limite finito, não basta escolher um número arbitrário. O OU permite satisfazer ambas as condições. Usar duas desigualdades sem mecanismo de seleção impõe E, restringindo à interseção em vez da união.

## Relações lógicas — pp. 25–29

Com binárias de seleção:

- No máximo três de cinco investimentos: `Σ_j x_j≤3`.
- Selecionar 1 ou 2, possivelmente ambos: `x_1+x_2≥1`.
- Selecionar 3 implica selecionar 4: `x_3≤x_4`.
- Qualquer um de 2, 3 e 4 implica selecionar 1: `x_2+x_3+x_4≤3x_1`; também se pode impor cada implicação separadamente.

A direção das desigualdades expressa a direção da implicação. Não trocar “se” por “se e somente se”.

## Valores discretos — pp. 30–31

Para `x∈{4,6,9,12,20,25}`, introduzir binárias `y_k`, impor `Σ_k y_k=1` e `x=4y_1+6y_2+9y_3+12y_4+20y_5+25y_6`. Seleciona-se exatamente um valor permitido. Apenas tornar x inteiro não restringe aos seis valores.

## Uso no projeto

A variável de uso da caixa representa uma ativação. Regras de incompatibilidade, dependência ou escolha de capacidade só entram se existirem na aplicação. Preferir limites físicos derivados das capacidades ao Big-M sem justificativa. As formulações normalizadas e alertas são explicações para implementação, não cópias literais das imagens.

Fonte: [Aula-ModelagemVarInteiras-01-Parte2.pdf](../pdfs/Aula-ModelagemVarInteiras-01-Parte2.pdf), 31 páginas.
