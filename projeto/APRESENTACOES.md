# Roteiros das apresentações

## Apresentação 1 - 11/11/2026, Aula 21

Duração não informada: adaptar os blocos ao tempo concedido. Não presumir que este roteiro substitui apresentações efetivamente realizadas.

1. Problema e motivação: todos os recursos devem entrar; minimizar baús; cenário fictício, UA, inventário finito e matriz de conflitos.
2. Exemplo de 20 itens: abrir `instances/game_n20_s22.json`. Mostrar diferença entre seleção de mochila e empacotamento obrigatório.
3. Modelo: apresentar I, J, E, w_i, C_j, x_ij e y_j; explicar cada restrição de `MODELO_IMPLEMENTADO.md`.
4. Solvers: explicar mesmo modelo, parâmetros, redução segura e ausência de warm start. Executar o comando abaixo.
5. Resultado verificado: ótimo 5 nos dois solvers, FFD 6; solver economiza um baú (16,67% de redução em relação aos 6 da heurística; excesso da heurística sobre ótimo é 20%). Não misturar os denominadores.
6. Validação e próximos passos: testes com enumeração, experimentos maiores, limitação da licença e confirmação do tema com o professor.

```bash
survival-packing solve instances/game_n20_s22.json --method scip --time-limit 10 --out results/apresentacao_scip.json
survival-packing validate instances/game_n20_s22.json results/apresentacao_scip.json
```

Backup: JSON já executado em `results/pilot/game_n20_s22_scip.json`, com alocação completa, cargas e tempos. Se a demonstração ao vivo falhar, identificar o backup como execução anterior.

## Apresentação 2 - data a confirmar

1. Recapitular problema, hipóteses e alterações desde a primeira apresentação.
2. Demonstrar FFD adaptado, política de abertura e verificação de compatibilidade.
3. Apresentar protocolo experimental e tabelas do relatório, com bloqueios de licença claramente identificados.
4. Mostrar caso FFD subótimo e caso de falha gulosa factível: pesos [4,3,3], capacidades [6,4]. FFD abre 6 para 4, depois 4 para 3 e falha; ótimo põe [3,3] no baú 6 e [4] no baú 4.
5. Comparar tempo, qualidade e limites, sem generalizar o bound clássico de FFD para esta variante.
6. Conclusões, limitações e trabalhos futuros: warm start comum aos dois solvers, formulação por categorias, inventários mais apertados e dados de uma aplicação validada.

Dividir blocos entre os 4 ou 5 integrantes após identificar o grupo. Cada pessoa deve compreender o modelo e a interpretação dos resultados; realizar ensaio com os comandos e arquivos entregues.
