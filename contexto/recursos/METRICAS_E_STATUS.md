# Status, limites e gaps comparáveis

Consultado em 17/10/2026. Aplicável à minimização de baús no [tema do grupo](../../projeto/TEMA_DO_GRUPO.md).

## Consultas após otimização

| Informação | Gurobi | PySCIPOpt / SCIP |
|---|---|---|
| Status original | `model.Status` | `model.getStatus()` |
| Há solução armazenada? | `model.SolCount > 0` | `model.getNSols() > 0` |
| Valor da melhor solução | `model.ObjVal`, se houver incumbente | `model.getSolObjVal(model.getBestSol())`, se existir |
| Melhor limite global | `model.ObjBound` | `model.getDualbound()` |
| Gap nativo (fração) | `model.MIPGap` | `model.getGap()` |
| Tempo de otimização | `model.Runtime` | `model.getSolvingTime()` |

Fontes: [atributos Gurobi](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html) e [API PySCIPOpt](https://pyscipopt.readthedocs.io/en/stable/api/model.html). Extrair atributos apenas em estados suportados; tratar valores indefinidos/infinidade e falhas de execução explicitamente.

## Não comparar diretamente os gaps nativos

Para os valores positivos do BPP, Gurobi usa `|UB−LB|/|UB|`; SCIP usa `|UB−LB|/min(|UB|,|LB|)`. As convenções de zero, infinitude e sinais exigem consulta às fontes. Ver [MIPGap](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html#mipgap) e [parâmetro limits/gap](https://www.scipopt.org/doc/html/PARAMETERS.php).

Exemplo calculado: UB=10 e LB=8 geram 20% no denominador UB e 25% no denominador LB. Multiplicar por 100 uma única vez para exibir porcentagem. Preservar `gap_native_fraction` e informar `gap_common_pct` separadamente.

**Convenção proposta do projeto:** para solução inteira completa e limites finitos com UB>0, usar `gap_common_pct=100·(UB−LB)/UB`. Se UB=LB=0, usar zero por convenção explícita; se faltar solução ou limite válido, usar `null`. Uma violação significativa de `LB≤UB` é erro a investigar, não um valor para corrigir silenciosamente.

## Parada e factibilidade são campos diferentes

Os [códigos de Gurobi](https://docs.gurobi.com/projects/optimizer/en/current/reference/numericcodes/statuscodes.html) distinguem ótimo, infactível, limite de tempo, interrupção e dificuldades numéricas. `INF_OR_UNBD` não é prova específica de infactibilidade. O [enum de status SCIP](https://www.scipopt.org/doc/html/type__stat_8h_source.php) também separa `OPTIMAL`, `INFEASIBLE`, `TIMELIMIT` e `GAPLIMIT`; valores numéricos podem variar entre versões.

Proposta de esquema próprio:

```text
termination_reason: optimal | infeasible | time_limit | gap_limit | other_limit | error | unknown
solution_state: complete_valid | none | invalid
proof_state: solver_optimal_with_tolerances | bound_match | not_proven
```

Preservar sempre status original. Limite de tempo pode coexistir com uma solução válida, mas não prova ótimo nem infactibilidade. Parada por gap positivo deve carregar essa tolerância; não a descrever como prova de igualdade exata dos limites. Uma heurística que não conclui a alocação também não prova infactibilidade.

## Que limite está sendo registrado?

Síntese matemática para o agente: em minimização, um empacotamento completo validado dá UB; relaxação ou prova válida dá LB; `LB≤OPT≤UB`. O limite global ao final da busca pode ser mais forte que a relaxação linear inicial. Se o relatório usar ambos, guardar `lp_relaxation_bound` e `solver_dual_bound` separadamente. Não chamar qualquer um deles simplesmente de “ótimo”.

Para comparar a heurística H: com ótimo conhecido O>0, usar `100·(H−O)/O`; sem O, uma distância a LB positivo não é erro ótimo medido. Só comparar valores da mesma instância, inventário e regras de incompatibilidade.

Para o tema heterogêneo, `ceil(Σ_i w_i/max_j C_j)` é um limite inferior simples, geralmente fraco. `Σ_j C_j≥Σ_i w_i` não garante factibilidade, pois os itens são indivisíveis e podem ser incompatíveis. A escolha de limites mais fortes pode ser uma extensão futura, não pré-requisito da primeira implementação.
