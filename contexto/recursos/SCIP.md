# SCIP — roteiro prático com PySCIPOpt

Consultado em 17/10/2026. PySCIPOpt é a interface Python proposta; a obrigação acadêmica continua sendo resolver com SCIP.

## Instalação e leituras

O [guia oficial de instalação](https://pyscipopt.readthedocs.io/en/stable/install.html) oferece `pip install pyscipopt` e Conda. As wheels atuais incluem SCIP em plataformas suportadas, incluindo macOS Intel e Apple Silicon; builds próprias e versões antigas podem exigir configuração adicional. Verificar compatibilidade com Python, arquitetura e SO ao instalar. Não presumir que toda versão do pacote usa a mesma versão interna de SCIP.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pyscipopt
```

O [site do SCIP](https://www.scipopt.org/) informa licença Apache 2.0 a partir da versão 8.0.3; dependências podem ter licenças próprias. Para modelar, começar pela [introdução oficial de PySCIPOpt](https://pyscipopt.readthedocs.io/en/stable/tutorials/model.html), que apresenta modelo, parâmetros e informações de solução.

## Construir o mesmo modelo

Esboço próprio, equivalente ao exemplo Gurobi e assumindo os mesmos dados validados:

```python
from pyscipopt import Model, quicksum

n = len(w)
I = range(n)
J = range(n)
model = Model("bpp")
x = {(i, j): model.addVar(vtype="B", name=f"x_{i}_{j}") for i in I for j in J}
y = {j: model.addVar(vtype="B", name=f"y_{j}") for j in J}
for i in I:
    model.addCons(quicksum(x[i, j] for j in J) == 1)
for j in J:
    model.addCons(quicksum(w[i] * x[i, j] for i in I) <= C * y[j])
model.setObjective(quicksum(y[j] for j in J), "minimize")
model.setParam("limits/time", 60.0)
model.setParam("limits/gap", 0.0)
model.setParam("parallel/maxnthreads", 1)
model.setParam("lp/threads", 1)
model.setParam("randomization/randomseedshift", 0)
model.optimize()
```

A [referência de parâmetros SCIP](https://www.scipopt.org/doc/html/PARAMETERS.php) explica os nomes. `lp/threads` controla o LP; não equivale sozinho a controlar todo o solver. O [modo concorrente](https://www.scipopt.org/doc/html/CONCSCIP.php) tem configuração própria. O exemplo propõe uma base sequencial; confirmar parâmetros e build no ambiente real.

## Extração e uso dos exemplos externos

A [API Model](https://pyscipopt.readthedocs.io/en/stable/api/model.html) documenta consultas como `getNSols()`, `getBestSol()` e `getSolVal()`. Após a otimização, só extrair alocação quando houver solução; validar por uma rotina comum aos métodos. Ver a tabela de [métricas e status](METRICAS_E_STATUS.md).

O capítulo [Bin packing and cutting stock problems](https://scipbook.readthedocs.io/en/latest/bpp.html) conecta formulação compacta, FFD e implementação. Como material didático com exemplos antigos, deve orientar a leitura, enquanto a API oficial determina os métodos disponíveis na versão instalada.

O [exemplo avançado de Bin Packing do SCIP](https://www.scipopt.org/scip/doc/html/BINPACKING_PROBLEM.php) usa padrões e geração de colunas. É uma extensão possível; não é necessário implementar branch-and-price para cumprir o enunciado. Manter a mesma formulação compacta em Gurobi e SCIP na comparação principal.

## Ajustes obrigatórios para o tema do grupo

No esboço didático, substituir `J=range(n)` por índices do inventário finito e a capacidade uniforme C por `capacity[j]`. Para cada par incompatível `{i,h}` e j, adicionar `model.addCons(x[i,j] + x[h,j] <= 1)`. Usar exatamente a mesma lista de baús e conflitos do modelo Gurobi e da heurística. Não aplicar quebra de simetria entre baús de capacidades diferentes. A definição de regras está no [tema](../../projeto/TEMA_DO_GRUPO.md).
