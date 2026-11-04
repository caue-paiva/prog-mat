# Armazenamento de recursos em jogos de sobrevivência

Implementação Python de Bin Packing com capacidades heterogêneas e conflitos. Minimiza baús utilizados e armazena todos os itens. Base: [caue-paiva/prog-mat](https://github.com/caue-paiva/prog-mat), commit `a2943f1ea499052a24b09e428c8ccc51956a7124`. Materiais originais em `contexto/` e `enunciado/`; documentação histórica preservada, enquanto o estado implementado está nos arquivos abaixo.

## Comece aqui

- `projeto/PLANO_EXECUCAO.md`: plano anterior ao código, decisões e critérios de aceitação.
- `projeto/MODELO_IMPLEMENTADO.md`: formulação efetivamente executada e demonstração da redução.
- `report/relatorio.pdf` e `report/relatorio.md`: relatório e fonte, na ordem do enunciado.
- `projeto/ENTREGA.md`: checklist e limitações conhecidas.
- `projeto/APRESENTACOES.md`: roteiros das duas apresentações.
- `src/survival_packing/`: implementação; `tests/`: testes independentes.
- `instances/`: 12 entradas sintéticas (20, 50, 100, 200 itens; sementes 11, 22, 33).
- `results/pilot/`: saídas JSON, logs, ambiente e tabela CSV, sem estimativas inventadas.

## Instalação

Python 3.10 ou superior. Ambiente testado: Python 3.12. Solvers opcionais para permitir executar FFD sem licença ou dependência externa.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[solvers,test,report]'
python -m pytest -q
```

A instalação de gurobipy não garante licença suficiente para todos os modelos. Configurar uma licença acadêmica apropriada conforme a documentação oficial do Gurobi. Não colocar arquivos de licença no pacote ou no Git. Sem licença/dependência, a execução registra `unavailable`; erros de implementação ficam como `error`.

## Executar

```bash
survival-packing solve instances/game_n20_s11.json --method ffd --out results/local_ffd.json
survival-packing solve instances/game_n20_s11.json --method scip --time-limit 10 --out results/local_scip.json
survival-packing solve instances/game_n20_s11.json --method gurobi --time-limit 10 --out results/local_gurobi.json
survival-packing validate instances/game_n20_s11.json results/local_scip.json
# Reproduzir o piloto sem sobrescrever os resultados entregues:
survival-packing benchmark --instances instances --out results/reproduction --time-limit 10
# Após habilitar licença Gurobi suficiente, comparação mais longa:
survival-packing benchmark --instances instances --out results/final_300s --time-limit 300
```

Alternativa sem instalar o pacote: `PYTHONPATH=src python -m survival_packing.cli ...` (Linux/macOS). `--no-reduction` mantém todo o inventário nos modelos e permite aferir a redução; não comparar seu tempo diretamente com uma execução reduzida sem identificar a diferença.

`generate --out instances` recria os dados determinísticos. Faça isso em outra pasta se tiver editado as instâncias. `benchmark` recusa diretório de saída não vazio e grava cada resultado imediatamente. A ordem das instâncias é lexicográfica, fixa. Uma medição por instância/método; as três sementes representam instâncias diferentes, não repetições do mesmo tempo. O piloto não é um estudo estatístico de desempenho.

## Dados e resultados

Ver `instances/game_n20_s11.json` como exemplo completo. `items` tem `id`, `size` inteiro positivo em UA, `category`; `chests` tem `id`, `capacity`; regras simétricas em `incompatible_categories`, ou conflitos adicionais de IDs em `conflicts`. O estoque é finito. Ausência de regra significa compatibilidade. Capacidades e tamanhos inteiros até 10^9; dados fracionários devem ser escalados antes da leitura. Unidades geométricas não são modeladas.

JSON de saída: status, objetivo, alocações, cargas, bound global, gap nativo (fração), gap comum (porcentagem), tempos, parâmetros, versão e flag de validação. `objective: null` não equivale a zero. O campo `raw_status` preserva a causa de término. `feasible` pode vir de limite de tempo; `no_solution` não prova infactibilidade. `heuristic_failed` significa que a heurística não produziu alocação completa. Para resultados sem solução não execute `validate`.

O tempo total mede algoritmo, construção, otimização e extração/validação dos solvers, sem leitura do JSON, gravação de logs externos à API e serialização da saída. A medida FFD cobre ordenação e empacotamento; sua validação final é posterior à medida. Essa diferença é explicitada no relatório e não afeta a comparação por ordens de grandeza. O limite de 10 s refere-se somente à otimização, não ao tempo total.

## Relatório e pacote

```bash
python report/update_source.py
python report/build_report.py
python scripts/package.py
```

update_source.py recompõe o relatório com results/pilot e results/extended. Para outra rodada, adaptar os caminhos e revisar a análise narrativa antes de gerar o PDF. A fonte Markdown também pode ser editada diretamente; nesse caso não execute update_source.py, que a sobrescreve. Não apresentar o piloto como comparação completa quando Gurobi registrar restrição de licença. O pacote final inclui código, dados e relatório; nenhum envio ao e-disciplinas ou alteração remota do GitHub é realizado por esses comandos.
