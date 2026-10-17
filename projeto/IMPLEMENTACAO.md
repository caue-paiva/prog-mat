# Proposta de implementação e experimentos

**Contexto atualizado:** o [tema do grupo](TEMA_DO_GRUPO.md) define baús heterogêneos e incompatibilidades, com Apresentação 1 em 11/11 — Aula 21. Os exemplos uniformes deste arquivo são a base; a implementação e o relatório devem seguir a variante escolhida. [Recursos externos](../contexto/recursos/README.md) complementam APIs, heurística e experimentos.

Tudo neste arquivo é orientação técnica proposta, subordinada aos [requisitos oficiais](../enunciado/REQUISITOS.md). Não há código implementado neste estágio.

## Sequência sugerida

1. Partir do tema definido e registrar unidades, inventário de baús, matriz de conflitos, fonte de dados e hipóteses com o grupo.
2. Implementar leitura de instâncias e um validador independente.
3. Implementar FFD como referência para BPP 1D (BFD é opção adicional).
4. Implementar a mesma formulação em Gurobi e SCIP, com resultados normalizados.
5. Verificar casos pequenos e bordas, executar experimentos reproduzíveis e produzir tabelas.
6. Escrever o relatório com referências verificadas e preparar a entrega/apresentações.

Python 3 é uma escolha sugerida. Avaliar as interfaces oficiais/compatíveis de Gurobi e SCIP ao implementar; versões, instalação e licenciamento não foram verificados nesta documentação. Ter uma interface única não elimina a obrigação de executar os dois solvers.

Estrutura possível, a criar somente na implementação:

```text
src/             # dados, validação, heurísticas, solvers, execução
instances/       # entradas e metadados de origem/geração
experiments/     # configurações e sementes
results/         # saídas brutas e tabelas reproduzíveis
report/          # fontes do relatório e PDF
```

## Contrato de dados proposto para BPP 1D

```json
{
  "instance_id": "exemplo-01",
  "capacity": 10,
  "items": [
    {"id": "a", "size": 6},
    {"id": "b", "size": 4},
    {"id": "c", "size": 5},
    {"id": "d", "size": 5}
  ]
}
```

Validar identificadores únicos, números finitos, capacidade positiva e tamanhos positivos. Um item maior que a capacidade torna o BPP base infactível; distinguir isso de JSON inválido. Se suportar decimais, definir escala inteira ou tolerâncias documentadas. A entrada vazia pode retornar zero caixas. Esquema multirrecurso depende de decisão explícita da variante.

Saída proposta: identificação da instância/método, status original e normalizado, objetivo ou `null`, alocações por caixa, cargas, tempo de otimização e tempo total, melhor limite inferior disponível, gap nativo do solver e parâmetros/versões. Não ler objetivo/alocação quando não há incumbente. `time_limit` e `no_solution` não equivalem a infactibilidade demonstrada. Solvers indisponíveis devem gerar registro explícito da indisponibilidade.

## FFD e BFD — especificação operacional proposta

**First-Fit Decreasing:** ordenar itens por tamanho decrescente, desempatar por posição original; para cada item, percorrer caixas abertas na ordem de abertura e colocá-lo na primeira com capacidade suficiente; se nenhuma servir, abrir outra. Preservar IDs originais.

**Best-Fit Decreasing:** mesma ordenação; escolher a caixa factível que deixará a menor sobra; desempatar por ordem de abertura. Abrir caixa quando necessário.

Incluir ordenação no tempo total da heurística. Implementações diretas custam `O(n log n+nU)`, com U caixas abertas, e podem chegar a `O(n²)`. Não aplicar essas regras 1D sem adaptação a CPU/RAM, incompatibilidades ou caixas heterogêneas. O método alternativo deve resolver a mesma variante dos solvers.

## Validação necessária

O validador deve conferir que cada ID aparece exatamente uma vez, não há itens desconhecidos, cada carga respeita a capacidade, toda alocação usa caixa ativada e o objetivo coincide com o número de caixas usadas. Aplicar o mesmo validador às saídas dos três métodos. Comparar objetivos e factibilidade, sem exigir rótulos de caixas iguais.

Casos recomendados para a implementação futura:

| Capacidade; tamanhos | Resultado esperado |
|---|---|
| 10; [] | 0 caixas por convenção |
| 10; [10] | ótimo 1 |
| 10; [6,4,5,5] | ótimo 2 |
| 10; [6,6,6] | ótimo 3; limite de volume é apenas 2 |
| 10; [11] | infactível no BPP base |
| 10; itens repetidos com IDs diferentes | preservar todas as ocorrências |
| 0; qualquer lista | entrada inválida |

Para instâncias muito pequenas, enumeração independente pode conferir o ótimo. Incluir um caso que exponha a limitação da heurística: `C=10`, tamanhos `[6,5,3,2,2,2]`; FFD usa 3 caixas, mas `[6,2,2]` e `[5,3,2]` provam ótimo 2. Esse é um exemplo analítico proposto, não uma execução registrada.

## Protocolo experimental proposto

Usar as mesmas instâncias para todos os métodos. Incluir tamanhos pequenos para prova de ótimo e tamanhos maiores para observar qualidade/tempo; variar distribuição dos tamanhos e ocupação. Registrar origem de dados reais ou sementes e regras de geração de dados sintéticos. Dados sintéticos devem ser identificados como tais; contextualizá-los não os transforma em coleta real.

Registrar hardware, SO, linguagem, versões, número de threads, limite de tempo, tolerância de gap, sementes, parâmetros e política de warm start. Se a heurística fornecer solução inicial a um solver, documentar e aplicar política comparável. Medir separadamente construção do modelo, otimização e tempo total; informar claramente qual tempo aparece na comparação. Repetir medições quando necessário para avaliar variação, sem inventar quantidades mínimas exigidas.

Para minimização: `LB ≤ OPT ≤ UB`, com UB de solução factível. Limite global do solver pode melhorar ao longo da busca e não é necessariamente a relaxação linear inicial. Preservar o gap nativo de cada solver e definir uma métrica comum para comparação, por exemplo `100·(UB−LB)/max(|UB|,epsilon)` com epsilon positivo documentado. Esta fórmula é proposta, não determinação do enunciado.

Para heurística com H caixas e ótimo conhecido O positivo: excesso relativo `100·(H−O)/O`. Se houver apenas LB positivo: `100·(H−LB)/LB` é distância ao limite, não erro ótimo conhecido. Se não houver limite válido/solução, usar `null` e explicar. Tratar instância vazia sem divisão por zero.

Uma heurística alcançar um limite inferior válido prova a otimalidade do valor nessa instância, mesmo sem um solver encerrar. Isso não constitui prova geral de que a heurística é exata.
