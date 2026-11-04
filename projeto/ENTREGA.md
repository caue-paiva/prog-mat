# Entrega e rastreabilidade

| Exigência | Artefato | Situação |
|---|---|---|
| Plano de implementação e validação | PLANO_EXECUCAO.md | Concluído antes do código |
| Modelo completo | MODELO_IMPLEMENTADO.md; relatório seção 2 | Implementado |
| Solver comercial e livre | exact.py; results/pilot | Ambos executados em 20 itens; Gurobi bloqueado por licença em 50/100/200 |
| Método alternativo | heuristic.py | Executado nas 12 instâncias |
| Validação independente | validation.py; tests; results/tests.txt | Testes e alocações verificados |
| Dados e reprodutibilidade | instances; experiments; README | Incluídos |
| Relatório PDF em cinco seções | report/relatorio.pdf | Incluído, com limitações explícitas |
| Código + dados + relatório em ZIP | projeto_sobrevivencia.zip | Gerado por scripts/package.py |
| Duas apresentações | APRESENTACOES.md | Roteiros; realização depende do grupo |
| Aplicação real/distinta | Tema fictício escolhido | Aceitação e distinção entre grupos a confirmar |
| Integrantes e avaliações individuais | Sem dados pessoais fornecidos | Preencher pelo grupo |

## Antes de enviar ao e-disciplinas

1. Ler o relatório e conferir nomes/instituição exigidos pelo professor; esta versão não inventa autoria nem composição do grupo.
2. Confirmar a aceitação do jogo fictício como aplicação e a originalidade em relação aos outros grupos.
3. Habilitar licença Gurobi suficiente e executar a comparação ampliada com o comando do README. Atualizar resultados, análise e PDF; preservar o piloto para rastreabilidade. A comparação completa nos quatro tamanhos permanece pendente.
4. Conferir as duas apresentações e a autoavaliação/avaliação de pares.
5. Extrair o ZIP, instalar dependências, rodar testes e uma instância antes do envio. Enviar um único arquivo pelo canal oficial; nenhum envio é realizado automaticamente.

Os documentos antigos de contexto descrevem o estado anterior à implementação e foram mantidos como fonte. Para o estado atual, consultar README, PLANO_EXECUCAO, MODELO_IMPLEMENTADO e este checklist.
