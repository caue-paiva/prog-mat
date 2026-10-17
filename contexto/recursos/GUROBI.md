# Gurobi — roteiro prático para o agente

Consultado em 17/10/2026. Proposta em Python; o enunciado também permite C/C++.

## Instalação e licença

O procedimento oficial inclui `python -m pip install gurobipy`. Instalar o pacote não equivale a ativar uma licença acadêmica; as ferramentas de licenciamento não são incluídas pelo método pip. Consultar o [guia de instalação Python](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python).

A oferta oficial distingue a licença restrita incluída no pacote — até 2.000 variáveis e 2.000 restrições lineares — e a licença acadêmica sem esse limite de tamanho, sujeita à elegibilidade/ativação. Verificar o acesso do grupo no [guia acadêmico](https://support.gurobi.com/hc/en-us/articles/4534601245713-How-do-I-get-started-with-Gurobi-for-academic-users) e na [página de licenças](https://www.gurobi.com/product/pricing-and-licensing).

**Consequência calculada para este projeto:** com m=n, o modelo tem n²+n binárias. Para n=45 são 2.070, acima do limite restrito citado; n=44 dá 1.980. Reforços `x_ij≤y_j` também aumentam as restrições. Não planejar os experimentos grandes presumindo que a licença restrita basta. Registrar indisponibilidade sem substituir Gurobi por outro solver.

Exemplo proposto de preparação, a executar na implementação:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install gurobipy
```

## Construir a formulação compacta

O [manual da classe Model](https://docs.gurobi.com/projects/optimizer/en/current/reference/python/model.html) documenta `addVars`, `addConstrs`, `setObjective` e `optimize`. Esboço próprio da tradução do modelo local, assumindo entrada validada, não vazia e w com índices 0,...,n−1:

```python
import gurobipy as gp
from gurobipy import GRB

n = len(w)
I = range(n)
J = range(n)
model = gp.Model("bpp")
x = model.addVars(I, J, vtype=GRB.BINARY, name="x")
y = model.addVars(J, vtype=GRB.BINARY, name="y")
model.addConstrs((gp.quicksum(x[i, j] for j in J) == 1 for i in I))
model.addConstrs((gp.quicksum(w[i] * x[i, j] for i in I) <= C * y[j] for j in J))
model.setObjective(gp.quicksum(y[j] for j in J), GRB.MINIMIZE)
model.Params.TimeLimit = 60.0
model.Params.Threads = 1
model.Params.MIPGap = 0.0
model.Params.Seed = 0
model.optimize()
```

Os valores de configuração são exemplos de estudo. O [manual de parâmetros](https://docs.gurobi.com/projects/optimizer/en/current/reference/parameters.html) descreve `TimeLimit`, `Threads`, `MIPGap` e `Seed`. `MIPGap=0` não elimina tolerâncias numéricas de factibilidade/integralidade. `TimeLimit` não é um limite para todo o programa Python.

## Resultados e aceitação

Consultar os [atributos do modelo](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html) e o [guia comum de métricas](METRICAS_E_STATUS.md). Ler valores de solução somente se `model.SolCount>0`. O agente deverá extrair os IDs de itens, reconstruir as caixas, validar cargas e comparar o objetivo extraído com as caixas efetivamente usadas.

Casos mínimos propostos: C=10 e pesos `[6,4,5,5]` têm ótimo 2; `[6,6,6]` têm ótimo 3; `[11]` é infactível. A lista vazia deve ser tratada explicitamente pela aplicação. Capturar erros de importação/licença e preservar sua mensagem sem registrar segredos de credenciais. Não há resultados medidos neste documento.

## Ajustes obrigatórios para o tema do grupo

O esboço acima usa caixas uniformes apenas como introdução. Na implementação final, definir `J=range(len(chests))`, manter `I=range(len(w))`, usar `capacity[j] * y[j]` no lado direito e acrescentar, para cada par de índices `{i,h}` incompatível e j, `model.addConstr(x[i,j] + x[h,j] <= 1)`. Reforços `x[i,j]<=y[j]` são opcionais, mas devem ser iguais nos dois solvers. Definir o inventário em dados; não gerar automaticamente apenas baús grandes em lugar da política escolhida. Ver a formulação completa no [tema](../../projeto/TEMA_DO_GRUPO.md).
