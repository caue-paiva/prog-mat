# Programação Matemática | contexto para o projeto

Repositório de materiais da disciplina e documentação para um agente implementar o projeto de **Bin Packing**. Ainda não há implementação nem resultados experimentais.

**Tema do grupo:** armazenamento de recursos em jogo de sobrevivência fictício, com capacidades diferentes e incompatibilidades. [Definição e Apresentação 1 em 11/11 — Aula 21](projeto/TEMA_DO_GRUPO.md).

## Organização

- `enunciado/`: PDF oficial e requisitos em Markdown.
- `contexto/pdfs/`: slides e atividade de aula, com os nomes originais.
- `contexto/resumos/`: um resumo por PDF e uma síntese direcionada ao projeto.
- `contexto/recursos/`: documentação oficial, literatura e orientação para os gaps do projeto.
- `contexto/inventario.json`: páginas e SHA-256 dos 16 PDFs preservados.
- `projeto/`: modelo base, orientação de implementação e roteiro de relatório.
- `AGENTS.md`: instruções e ordem de leitura para o próximo agente.

## Ordem de leitura

1. [Tema e escopo definidos pelo grupo](projeto/TEMA_DO_GRUPO.md).
2. [Instruções para o agente](AGENTS.md).
3. [Requisitos oficiais](enunciado/REQUISITOS.md).
4. [Síntese das aulas](contexto/SINTESE_PARA_PROJETO.md).
5. [Modelo matemático](projeto/MODELO_MATEMATICO.md).
6. [Plano de implementação e validação](projeto/IMPLEMENTACAO.md).
7. [Relatório e entrega](projeto/RELATORIO_E_ENTREGA.md).

[Avaliação da cobertura do enunciado](contexto/COBERTURA_DO_ENUNCIADO.md) e [recursos externos para complementar os gaps](contexto/recursos/README.md).

## Resumos dos materiais

| Material | Resumo |
|---|---|
| Aula 02 - modelagem contínua | [Aula 02](contexto/resumos/AULA_02.md) |
| Aula 03 - transporte e designação | [Aula 03](contexto/resumos/AULA_03.md) |
| Aula 04 - corte e empacotamento | [Aula 04](contexto/resumos/AULA_04.md) |
| Aula 05 - programação inteira e Bin Packing | [Aula 05](contexto/resumos/AULA_05.md) |
| Aula 06 - localização, Big-M e coloração | [Aula 06](contexto/resumos/AULA_06.md) |
| Aula 08 - cobertura, empacotamento e partição | [Aula 08](contexto/resumos/AULA_08.md) |
| Modelagem com variáveis inteiras, parte 2 | [Variáveis inteiras](contexto/resumos/MODELAGEM_VARIAVEIS_INTEIRAS.md) |
| Caixeiro Viajante | [Caixeiro Viajante](contexto/resumos/CAIXEIRO_VIAJANTE.md) |
| Atividade de avaliação contínua | [Atividade](contexto/resumos/ATIVIDADE.md) |
| DefinicaoVerticeSolucaobasica | [Resumo](contexto/resumos/VERTICES_E_SOLUCOES_BASICAS.md) |
| Aula13PM | [Resumo](contexto/resumos/AULA_13_SIMPLEX.md) |
| Aula14SimplexDeterminandoSolucaoMelhor | [Resumo](contexto/resumos/AULA_14_SIMPLEX.md) |
| BaseInicialSimplex | [Resumo](contexto/resumos/BASE_INICIAL_SIMPLEX.md) |
| Simplex-revisado | [Resumo](contexto/resumos/SIMPLEX_REVISADO.md) |
| PI_Scheduling | [Resumo](contexto/resumos/PI_SCHEDULING.md) |

Os resumos consolidam slides repetidos e não são transcrições integrais. As páginas referenciadas são as posições no PDF, começando em 1. Fórmulas foram normalizadas e ressalvas sobre inconsistências aparecem nos resumos. Datas e recordes dos slides são contexto histórico, não informações atuais verificadas. O PDF oficial prevalece sobre os documentos auxiliares. Recomendações técnicas são identificadas como propostas; a aplicação escolhida está em `projeto/TEMA_DO_GRUPO.md`, e seus detalhes ainda pendentes não devem ser tratados como decisões tomadas.
