# Requisitos do projeto — Bin Packing

Fonte oficial: [Projeto_PM_BCC_2026.pdf](Projeto_PM_BCC_2026.pdf), 4 páginas. Esta é uma síntese fiel; propostas de engenharia ficam em `../projeto/`.

## Objetivo, grupo e entregáveis — página 1

Aprofundar otimização inteira por meio da modelagem e solução do Problema do Empacotamento (BPP) e variantes práticas/industriais. Grupos de **4 ou 5 pessoas**, escolhidos no e-disciplinas; o professor aloca quem não escolher no prazo.

O trabalho compreende **duas implementações**: abordagem por solvers e método alternativo, em **Python 3 ou C/C++**; relatório técnico; **duas apresentações durante o semestre**. A abordagem por solvers deve executar com **Gurobi (comercial) e SCIP (livre)**.

Enviar códigos, dados das instâncias de teste e relatório PDF pelo e-disciplinas em **um único `.zip`, `.rar` ou `.tar.gz`**. Só o último envio será considerado. O documento não informa datas, duração das apresentações, tamanho do relatório nem quantidade mínima de instâncias.

## Aplicação e modelagem — páginas 1–3

Cada grupo deve escolher um cenário distinto de empacotamento ou alocação de recursos. Exemplos fornecidos, sem obrigação de escolher um deles:

- Cargas em caminhões/contêineres com limites de peso ou volume.
- Máquinas virtuais com CPU e RAM em servidores físicos.
- Arquivos/bases de pesquisa em mídias ou volumes com capacidade em GB/TB.
- Equipamentos e insumos em armários/espaços de laboratórios.
- Questões de prova em páginas com limite de linhas/altura, minimizando páginas e fragmentação.

Apresentar conjuntos de itens e recipientes, parâmetros, variáveis binárias de alocação e ativação (ou outras variáveis pertinentes), função objetivo e restrições de alocação, capacidade e domínio.

No modelo base do enunciado: `I={1,...,n}`, `J={1,...,m}`, com **m ≥ n**; tamanho `w_i`, capacidade uniforme `C`; `x_ij` indica alocação e `y_j` uso. Minimizar `Σ_j y_j`, impondo `Σ_j x_ij = 1` para todo item e `Σ_i w_i x_ij ≤ C y_j` para toda caixa; ambas as variáveis são binárias.

## Método alternativo — página 3

Implementar heurística (exemplos: First-Fit Decreasing, Best-Fit Decreasing) **ou** meta-heurística (exemplos: algoritmo genético, Simulated Annealing, Busca Tabu), visando eficiência em instâncias grandes. Executar e analisar qualidade e tempo; comparar com ótimo conhecido ou limite inferior. Não é necessário implementar todos os exemplos.

## Relatório obrigatório — páginas 3–4

Respeitar esta ordem:

1. **Introdução:** contexto, relevância e breve revisão da literatura com referências ABNT ou IEEE.
2. **Modelagem Matemática:** formulação da variante escolhida, conjuntos, parâmetros, variáveis e explicação do objetivo e de cada restrição.
3. **Solução via Solvers de Otimização:** implementação e comparação entre solver comercial e gratuito. Informar status (ótima, factível, infactível), valor objetivo, tempo e gap de otimalidade, descrito no enunciado como diferença percentual entre melhor solução inteira e bound do problema relaxado.
4. **Método de Solução Alternativo:** fundamentação teórica da escolha, implementação, resultados e comparação crítica com os solvers.
5. **Conclusão:** resultados, benefícios práticos, trabalhos futuros, aprendizados e desafios.

O enunciado não fixa uma fórmula/denominador para o gap; documentar a convenção utilizada. Separar limite da relaxação inicial e melhor limite global do solver quando ambos forem registrados.

## Avaliação — página 4

| Componente | Pontos |
|---|---:|
| Modelagem Matemática (NM) | 3 |
| Implementação (NI) | 4: 2 para solver, 2 para método alternativo |
| Relatório (NR) | 3 |
| Apresentação (NA), individual | 1 |
| Autoavaliação e avaliação de pares (NAAP), individual | 1 |

Fórmula literal normalizada: `NT = (NM + NI + NR) · min{NA, NAAP}`. NA e NAAP funcionam como fatores individuais conforme a fórmula; não somar os componentes como se o total fosse 12. O documento afirma que o trabalho vale 10 pontos. Trabalhos iguais ou muito semelhantes entre grupos diferentes recebem zero.

## Pendências que o documento não resolve

Aplicação específica do grupo; composição do grupo; calendário; fonte das instâncias; dimensões e restrições da variante; limites de tempo e ambiente computacional; disponibilidade de licença Gurobi. Registrar as decisões reais antes de apresentá-las como definidas.
