# Programação inteira — sequenciamento de tarefas

## Problema e motivação — pp. 2–12

Ordenar n tarefas em um único servidor, sem interrupção, todas disponíveis no instante zero. Dados: duração `p_i` e prazo `d_i`. Objetivo: minimizar atraso total, isto é, `Σ_i A_i`, com `A_i=max(0,C_i−d_i)` e `C_i` tempo de conclusão.

O exemplo usa durações `(8,12,5,11,3)` e prazos `(12,18,20,30,25)`; a ordem `(1,2,3,4,5)` termina em `(8,20,25,36,39)` e soma atrasos 27. Os slides mostram construção de permutações e n! sequências possíveis, sem desenvolver uma heurística de empacotamento.

## Modelo 1 — precedência imediata, pp. 13–32

Binárias `x_ij=1` indicam que i precede **imediatamente** j. Usam-se nós fictícios de início 0 e fim n+1 para definir primeiro e último processos. Restrições de predecessor e sucessor são combinadas com vínculos de tempo ativados por Big-M; `A_i≥C_i−d_i` e `A_i≥0` representam o atraso no objetivo de minimização.

A relação exibida no PDF é `C_j≥C_i−M+(p_j+M)x_ij`: quando `x_ij=1`, impõe `C_j≥C_i+p_j`; quando zero, resta `C_j≥C_i−M`, que só deixa de restringir se M tiver limite válido para o domínio.

Cuidado para implementação: o domínio de x precisa incluir os arcos aos nós fictícios que aparecem nas somas; a apresentação final da p. 32 os omite na linha de domínio. Também é preciso assegurar a duração da primeira tarefa, por exemplo `C_j≥p_j`, e controlar os vínculos de início/fim. Não copiar a formulação resumida sem completar e auditar essas condições.

## Modelo 2 — precedência entre pares, pp. 33–37

Aqui `x_ij=1` significa que i precede j, sem exigir adjacência. Impor `x_ij+x_ji=1` por par distinto, vínculos condicionais de conclusão e `C_j≥p_j`. Os tempos de processamento positivos e as relações temporais impedem ciclos. O objetivo e a linearização de atraso permanecem iguais.

As pp. 19–29 revisam disjunções e Big-M. Essa parte se sobrepõe ao material de variáveis inteiras já existente.

## Relação com o projeto

É útil como exemplo adicional de binárias, implicações e comparação entre formulações. Mas minimizar atraso de uma sequência não é minimizar o número de caixas. Escolher uma aplicação de alocação de tarefas só será Bin Packing se houver recipientes/recursos com capacidade e objetivo correspondente; a mera existência de tarefas não basta.

Não apresenta FFD/BFD, meta-heurística implementável para BPP, APIs Gurobi/SCIP ou protocolo experimental. Deve ficar como leitura complementar, principalmente se a variante escolhida realmente tiver restrições temporais.

Fonte: [PI_Scheduling.pdf](../pdfs/PI_Scheduling.pdf), 37 páginas.
