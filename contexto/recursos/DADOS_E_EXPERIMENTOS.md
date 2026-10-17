# Instâncias e protocolo de comparação

Consultado em 17/10/2026. Os procedimentos abaixo são propostas do projeto, não requisitos adicionais do professor.

## Benchmark público: OR-Library

A página [Bin packing — one-dimensional, de J. E. Beasley](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html) descreve oito arquivos `binpack1` a `binpack8`, contribuídos por Falkenauer. O [diretório de dados](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/) está ligado pela própria página.

Formato: quantidade de problemas; para cada um, identificador, capacidade, quantidade de itens, referência de caixas e uma lista de tamanhos. As classes são uniformes e triplets. A referência nos uniformes não é automaticamente um ótimo provado: a documentação cita as exceções `u120_08`, `u120_19`, `u250_07`, `u250_12` e `u250_13`. Nos triplets, a construção fornece ótimo n/3. Tratar a referência com seu status e proveniência, sem presumir atualização posterior.

Esse benchmark é de BPP uniforme sem incompatibilidades. Serve para validar o núcleo clássico. Depois de acrescentar conflitos ou capacidades diferentes, os valores ótimos originais deixam de certificar a nova instância. Guardar a transformação e não comparar a solução modificada com o ótimo original como se fossem o mesmo problema.

## Dados do tema do grupo

O [tema definido](../../projeto/TEMA_DO_GRUPO.md) usa jogo fictício: instâncias sintéticas com 20, 50, 100 e 200 itens. Proposta de metadados:

```json
{
  "instance_id": "survival-n20-seed0",
  "source_type": "synthetic",
  "seed": 0,
  "size_unit": "abstract_slots",
  "items": [{"id": "i1", "category": "food", "size": 3}],
  "chests": [{"id": "b1", "capacity": 15}],
  "incompatible_categories": [["food", "explosive"]]
}
```

Este fragmento ilustra o esquema, não é uma instância de 20 itens completa. Cada baú representa uma unidade finita do inventário. Guardar uma versão da matriz de compatibilidade, distribuição dos tamanhos, capacidades disponíveis e regra de geração.

Proposta inicial: 5 sementes por tamanho (0–4), com dois cenários de conflitos — esparso e mais restritivo — totalizando 40 instâncias. Quantidades e densidades são configuráveis, não decisões do usuário. Sempre medir a densidade efetivamente gerada. Gerar parte das instâncias a partir de alocação testemunha para assegurar factibilidade; registrar esse viés. Casos infactíveis deliberados devem ser rotulados separadamente, nunca “descobertos” pela falha da heurística.

## Desenho experimental proposto

1. **Correção:** casos pequenos com ótimo calculável, baú insuficiente, item incompatível, inventário esgotado e vazio; validar todos os métodos com a mesma rotina.
2. **Piloto:** 20 itens para conferir tempo, licença e métricas. Depois 50, 100 e 200, preservando a lista completa de casos mesmo se algum método falhar.
3. **Comparação principal:** mesma formulação e reforços em Gurobi e SCIP, mesmo inventário e conflitos. Exemplo de orçamento inicial: 60 s por otimização, busca sequencial e gap alvo zero; ajustar após o piloto e registrar mudanças.
4. **Heurística:** medir ordenação, verificação de conflitos e escolha/abertura de baús. Uma execução basta para uma heurística determinística em termos de qualidade; repetir tempo quando a duração for curta/ruidosa. Métodos estocásticos exigem sementes e repetições documentadas.
5. **Ambiente:** registrar CPU, memória, SO, versões de Python/pacotes/solvers, parâmetros, política de warm start, sementes e hash dos dados. Rodar tarefas de medição sem concorrência entre solvers.

Para medir o programa Python, a documentação de [time.perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter) fornece um relógio de alta resolução para intervalos. Medir separadamente construção, chamada de otimização e tempo total. O tempo nativo do solver é outra coluna. Não contar somente o laço de alocação da heurística e comparar com o tempo total dos solvers.

Mesmo com semente fixa, parada por tempo pode produzir resultados diferentes; esse efeito é discutido no [guia de parâmetros Gurobi](https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/guidelines.html). Usar as repetições para relatar variação, sem prometer determinismo apenas pela semente.

## Registro e análise

Uma linha por instância, método e repetição: ID/hash, tamanho, inventário, conflitos, status original, estado de solução, objetivo, LB, gap nativo, gap comum, tempos, semente e parâmetros. Arquivar alocações e logs para auditoria. Em falhas, manter a linha com motivo e métricas ausentes como `null`.

Apresentar tabelas por tamanho e cenário: quantidade de soluções completas, ótimos certificados, medianas/variação do tempo e qualidade. Separar limites de tempo, erros de ambiente e falhas de heurística. Não excluir instâncias difíceis para melhorar médias.

Como análise opcional para muitos casos, Dolan e Moré apresentam **perfis de desempenho**: razão entre o tempo de um método e o melhor tempo por instância, agregada numa distribuição. Consultar o [artigo dos autores](https://arxiv.org/html/cs/0102001) e a [publicação de 2002](https://doi.org/10.1007/s101070100263). Só comparar tempos para a mesma tarefa/critério de sucesso: “achar qualquer solução” e “provar ótimo” são objetivos distintos. Os perfis não são obrigatórios; tabelas e gráficos de qualidade versus tempo podem bastar para este trabalho.
