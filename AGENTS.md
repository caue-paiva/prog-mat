# Contexto para o agente implementador

## Objetivo e fontes

Implementar o projeto acadêmico de Bin Packing da SME 0110, conforme `enunciado/Projeto_PM_BCC_2026.pdf`. Leia nesta ordem: `enunciado/REQUISITOS.md`, `contexto/SINTESE_PARA_PROJETO.md`, `projeto/MODELO_MATEMATICO.md`, `projeto/IMPLEMENTACAO.md` e `projeto/RELATORIO_E_ENTREGA.md`. Consulte os resumos individuais e PDFs para detalhes.

## Requisitos essenciais

- Escolher e contextualizar uma aplicação real de empacotamento/alocação, distinta das de outros grupos.
- Formular conjuntos, parâmetros, variáveis, objetivo e restrições.
- Resolver o mesmo problema com **Gurobi e SCIP**.
- Implementar também uma heurística ou meta-heurística e comparar qualidade e tempo.
- Usar Python 3 ou C/C++; entregar códigos, instâncias e relatório PDF em um único arquivo compactado, além das duas apresentações.

## Estado e decisões pendentes

O repositório contém documentação; nenhuma aplicação específica, linguagem, biblioteca, conjunto de dados ou prazo foi escolhido/informado. Os slides contêm anos diferentes, que não definem os prazos deste projeto. Não confundir `Atividade.pdf` com o enunciado do projeto.

Antes de especializar o modelo, alinhar a aplicação com o grupo. Pode-se desenvolver o núcleo genérico 1D como base técnica, deixando explícito que isso não substitui a escolha da aplicação real. Python 3, FFD/BFD e a estrutura sugerida em `projeto/IMPLEMENTACAO.md` são recomendações, não exigências do professor.

## Critérios de trabalho

Preservar os PDFs. Manter rastreabilidade entre requisitos e entregas. Não inventar referências, resultados, tempos, ótima solução ou execuções de solvers. Registrar ausência de licença/dependência como indisponibilidade, sem substituir silenciosamente os solvers obrigatórios. Verificar a documentação oficial das APIs quando começar a implementação.

Validar alocação, capacidade, uso de caixas e valor objetivo independentemente do solver. Não chamar uma solução de ótima apenas porque foi produzida por um método exato: exigir prova/status apropriado ou igualdade entre limites válidos. Não comparar apenas os rótulos das caixas, pois soluções equivalentes podem permutá-los. Separar requisitos oficiais, decisões do grupo e melhorias opcionais. Usar as mesmas instâncias e condições experimentais documentadas nos métodos comparados.
