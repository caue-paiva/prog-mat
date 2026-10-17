# Simplex — casos especiais e base inicial

## Ilimitabilidade, degenerescência e múltiplos ótimos — pp. 1–14

Exemplos de PL com direção factível que reduz o objetivo sem limite. No Simplex de minimização, uma variável com custo reduzido negativo e direção `y=B⁻¹a_k≤0` não encontra bloqueio na não negatividade das variáveis básicas.

Degenerescência: alguma variável básica vale zero. Uma troca de base pode ter passo zero; uma mesma solução pode corresponder a bases diferentes. Custos reduzidos nulos em base ótima podem permitir percorrer soluções ótimas alternativas, mas não bastam sozinhos para garantir uma solução distinta em situação degenerada: é preciso haver movimento factível não nulo.

## Base de folgas e duas fases — pp. 15–38

Para `Ax≤b`, `b≥0`, `x≥0`, acrescentar folgas cria matriz `[A I]`, com base inicial I, variáveis originais zero e folgas b. Isso não funciona automaticamente para qualquer igualdade ou restrição com excesso.

A **Fase I** introduz variáveis artificiais não negativas e minimiza sua soma num problema auxiliar com base conhecida. Ajustar os sinais dos lados direitos conforme necessário para começar factível. Se o ótimo auxiliar for positivo, o problema original é infactível. Se for zero, há factibilidade e pode-se preparar a base para a Fase II, descartando artificiais e restaurando o objetivo original.

Ressalva à p. 27: ótimo zero garante que as artificiais têm **valor zero**, não que todas saíram da base. Artificiais básicas nulas podem permanecer por degenerescência; é preciso pivotear para removê-las ou tratar linhas redundantes antes da Fase II. A simples presença de uma artificial na base não prova infactibilidade.

O exemplo das pp. 32–38 aplica duas fases a uma igualdade e uma desigualdade. A p. 39 apresenta a alternativa de penalizar artificiais com Big-M no objetivo. Esse Big-M de penalização não é a mesma construção das restrições lógicas de ativação, embora ambas usem uma constante grande.

## Relação com o projeto

Reforça a distinção entre ótimo, infactível e ilimitado no contexto de PL. Não fornece o mapeamento dos status das APIs para MIP. O BPP base com número finito de caixas e variáveis binárias é limitado quando factível; um diagnóstico de objetivo ilimitado nesse modelo merece investigação da implementação.

Não substitui a heurística obrigatória nem justifica incluir artificiais manualmente no modelo enviado aos solvers: deixar o processamento interno a Gurobi/SCIP.

Fonte: [BaseInicialSimplex.pdf](../pdfs/BaseInicialSimplex.pdf), 39 páginas.
