# Atividade — modelagem inteira e auditoria entre grupos

Fonte datada de **24/08/2026**. É uma atividade de avaliação contínua distinta do projeto de Bin Packing.

## Organização — página 1

A turma é dividida em uma quantidade par de grupos; pares discutem um dos cinco problemas. A atividade prevê 15 minutos de organização, 35 de modelagem e 50 de banca. Depois, cada aluno envia no e-disciplinas a resolução de uma questão sorteada.

Cada modelo deve definir índices/conjuntos, parâmetros, variáveis, função objetivo e restrições. A banca compara formulações e verifica o funcionamento delas. As formulações abaixo são sínteses normalizadas das tarefas propostas, não gabaritos fornecidos no PDF.

## Problema 1 — Seleção de features, página 2

Oito funcionalidades, capacidade de sprint 50 pontos. Valores `(15,12,18,9,25,10,13,20)` e custos `(20,15,25,12,30,10,18,22)`. Binária `x_j` por feature: maximizar `Σ_j v_j x_j`, com `Σ_j p_j x_j≤50`. É mochila binária: não é obrigatório escolher todas.

## Problema 2 — Alocação de servidores, página 3

Data centers SP, Fortaleza e BH, custos fixos `(10000,7000,8500)` e capacidades `(8000,5000,6500)` RPS. Clientes A–D demandam `(3000,5000,4000,2500)` RPS. A demanda pode ser dividida entre locais.

Usar binária `y_j` de ativação e fração contínua `f_ij≥0` de atendimento. `Σ_j f_ij=1` para cada cliente; `Σ_i d_i f_ij≤C_j y_j`; minimizar custos fixos mais custos de atendimento em unidades coerentes. Se os custos tabulados forem por requisição e o objetivo mensal, explicitar conversão de RPS para quantidade mensal; o enunciado da atividade não detalha essa conversão. Isso evita somar fluxos por segundo com valores mensais sem hipótese declarada.

## Problema 3 — Escalonamento, página 4

Cinco tarefas com tempos `(10,7,15,8,12)` minutos em três processadores idênticos. Binária `x_ij` de atribuição e variável auxiliar T: minimizar T, impor `Σ_i x_ij=1` por tarefa e `Σ_j p_j x_ij≤T` por processador. Minimiza makespan, não quantidade de processadores.

## Problema 4 — Designação generalizada, página 5

Seis tarefas, três equipes com capacidades `(100,120,90)` horas; tempo e custo dependem do par equipe–tarefa. Minimizar `Σ_i Σ_j c_ij x_ij`, com `Σ_i x_ij=1` por tarefa, `Σ_j t_ij x_ij≤H_i` por equipe e variáveis binárias. As tabelas completas permanecem no PDF; não são instâncias definidas para o projeto.

## Problema 5 — Cobertura de testes, página 6

Sete requisitos e cinco suítes. Coberturas: S1 `{R1,R3,R7}`, S2 `{R2,R4,R6}`, S3 `{R1,R2,R5}`, S4 `{R3,R5,R6}`, S5 `{R4,R7}`. Custos em horas `(3,4,5,4,2)`. Minimizar custo das suítes selecionadas com `Σ_(j que cobre r) x_j≥1` para cada requisito r, domínio binário. Sobreposição é aceita.

## Conexão com o projeto

Reaproveitar a disciplina de explicitar variáveis, unidades e domínios e auditar se todas as condições do texto são satisfeitas. Seleção, alocação fracionável, makespan e cobertura são objetivos/regras diferentes do BPP; não incorporar seus requisitos à entrega do projeto.

Fonte: [Atividade.pdf](../pdfs/Atividade.pdf), 6 páginas.
