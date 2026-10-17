# Recursos externos para completar o contexto

Pesquisa e consulta realizadas em **17/10/2026**. Foram priorizadas documentação dos próprios projetos, publicações dos autores/editoras e repositórios dos responsáveis pelos dados. Os textos abaixo são sínteses e orientações, não cópias de artigos ou manuais.

## Ordem de leitura

| Documento | Lacuna atendida |
|---|---|
| [Gurobi em Python](GUROBI.md) | Instalação, licença, construção e execução do modelo |
| [SCIP com PySCIPOpt](SCIP.md) | Instalação, modelagem e consulta de resultados |
| [FFD e método alternativo](HEURISTICAS.md) | Referência teórica, algoritmo, limitações e validação |
| [Status, limites e gaps](METRICAS_E_STATUS.md) | Extração comparável das métricas exigidas |
| [Dados e experimentos](DADOS_E_EXPERIMENTOS.md) | Instâncias públicas e protocolo reproduzível |
| [Aplicação real e literatura](APLICACAO_E_LITERATURA.md) | Literatura para o tema definido e delimitação do cenário |
| [Referências](REFERENCIAS.md) | Bibliografia inicial e links verificáveis |

## Como usar

Ler também os [requisitos oficiais](../../enunciado/REQUISITOS.md) e o [modelo base](../../projeto/MODELO_MATEMATICO.md). O [tema do grupo](../../projeto/TEMA_DO_GRUPO.md) é armazenamento de recursos em um jogo de sobrevivência fictício, com conflitos e capacidades heterogêneas. O caminho técnico proposto é Python 3, formulação compacta idêntica nos dois solvers e FFD adaptado. Os exemplos uniformes dos guias são degraus didáticos; a implementação final deve representar C_j e os conflitos.

As fontes fornecem base para os gaps de documentação e literatura. Continuam pendentes detalhes da aplicação (inventário, unidades e matriz de conflitos), alinhamento do cenário fictício à exigência de aplicação real, disponibilidade efetiva dos solvers, implementação e resultados dos experimentos. Nenhum solver foi instalado ou executado nesta pesquisa; os exemplos Markdown são esboços próprios e precisam de validação na implementação.

Links `current`, `stable` e `latest` podem mudar. Fixar versões de bibliotecas e registrar versões dos solvers na primeira execução reproduzível. Artigos com acesso restrito foram usados apenas nos limites dos resumos e metadados públicos; a leitura integral não é presumida. Não é necessário adquirir material pago para implementar o caminho mínimo descrito.
