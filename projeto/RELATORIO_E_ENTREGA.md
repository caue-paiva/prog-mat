# Roteiro do relatório e conferência de entrega

**Contexto atualizado:** o [tema do grupo](TEMA_DO_GRUPO.md) define baús heterogêneos e incompatibilidades, com Apresentação 1 em 11/11 — Aula 21. Os exemplos uniformes deste arquivo são a base; a implementação e o relatório devem seguir a variante escolhida. [Recursos externos](../contexto/recursos/README.md) complementam APIs, heurística e experimentos.

As cinco seções abaixo seguem a ordem do enunciado, pp. 3–4. Os artefatos sugeridos servem para orientar o desenvolvimento, sem substituir o relatório final.

## 1. Introdução

Descrever a aplicação realmente escolhida, quem se beneficia, quais são os itens e recipientes e por que reduzir recipientes/custo é relevante. Apresentar revisão breve com referências reais em ABNT ou IEEE. Referências citadas nos slides são pontos de partida; conferir os dados bibliográficos antes de usá-las. Não inventar coleta de dados nem afirmar distinção do tema entre grupos sem confirmação.

## 2. Modelagem Matemática

Definir conjuntos, parâmetros com unidades, variáveis com domínios, objetivo, cada restrição e hipóteses. Explicar as diferenças em relação ao BPP base. Documentar reforços, redução de caixas candidatas e quebra de simetria se utilizados.

## 3. Solução via Solvers de Otimização

Descrever implementação em Gurobi e SCIP, ambiente e configurações. Apresentar status, objetivo, tempo e gap, discutindo desempenho e qualidade. Explicar limites de tempo, execução sem incumbente e indisponibilidades; não apresentar execução faltante como resultado.

Tabela sugerida: instância, n, capacidade/recursos, solver, status, objetivo, melhor limite, gap (%), tempo de otimização e tempo total. Cada linha deve ser rastreável à saída bruta.

## 4. Método de Solução Alternativo

Apresentar método escolhido, justificativa com referencial teórico, passos, complexidade pertinente e adaptações à aplicação. Comparar com solvers em qualidade e tempo. Identificar quando a referência é ótimo provado ou apenas limite inferior. Discutir instâncias em que a heurística perde qualidade e quando sua rapidez é útil.

## 5. Conclusão

Sintetizar achados sustentados pelos experimentos, benefícios à aplicação, limitações, aprendizados/desafios e trabalhos futuros pertinentes (por exemplo capacidades distintas, 2D/3D ou métodos híbridos). Não escrever conclusões experimentais antes de obter resultados.

## Checklist da entrega oficial

- [ ] Aplicação real escolhida e modelo completo explicado.
- [ ] Código em Python 3 ou C/C++.
- [ ] Modelo executado em Gurobi e SCIP, com métricas e comparação.
- [ ] Heurística ou meta-heurística implementada, executada e comparada.
- [ ] Relatório PDF com as cinco seções na ordem exigida e referências ABNT ou IEEE.
- [ ] Códigos e dados das instâncias incluídos com o relatório num único `.zip`, `.rar` ou `.tar.gz`.
- [ ] Duas apresentações realizadas/preparadas conforme calendário comunicado pelo professor.
- [ ] Grupo de 4 ou 5 pessoas e procedimentos individuais de apresentação/avaliação acompanhados.

## Recomendações de reprodutibilidade

Incluir instruções de instalação/execução, dependências/versões, configurações, sementes e resultados brutos. Conferir a execução a partir de uma extração limpa do pacote. Não incluir chaves de licença, ambientes virtuais ou arquivos locais desnecessários. Confirmar datas e formato das apresentações no canal da disciplina, pois não constam no PDF.
