# Contexto para o agente implementador

## Objetivo e fontes

Implementar o projeto acadêmico de Bin Packing da SME 0110, conforme `enunciado/Projeto_PM_BCC_2026.pdf`. Leia primeiro `projeto/TEMA_DO_GRUPO.md`, que registra o tema definido pelo usuário e a Apresentação 1 em 11/11 (Aula 21), com modelagem e solução utilizando solver. Depois leia nesta ordem: `enunciado/REQUISITOS.md`, `contexto/SINTESE_PARA_PROJETO.md`, `projeto/MODELO_MATEMATICO.md`, `projeto/IMPLEMENTACAO.md` e `projeto/RELATORIO_E_ENTREGA.md`. Consulte os resumos individuais e PDFs para detalhes. Veja também `contexto/COBERTURA_DO_ENUNCIADO.md` para as lacunas restantes; os materiais adicionais de Simplex e sequenciamento são complementares e não substituem a heurística/meta-heurística de Bin Packing.

## Requisitos essenciais

- Escolher e contextualizar uma aplicação real de empacotamento/alocação, distinta das de outros grupos.
- Formular conjuntos, parâmetros, variáveis, objetivo e restrições.
- Resolver o mesmo problema com **Gurobi e SCIP**.
- Implementar também uma heurística ou meta-heurística e comparar qualidade e tempo.
- Usar Python 3 ou C/C++; entregar códigos, instâncias e relatório PDF em um único arquivo compactado, além das duas apresentações.

## Tema definido, prazo e decisões pendentes

Tema: **Otimização de Armazenamento de Recursos em Jogos de Sobrevivência com Restrições de Compatibilidade e Capacidade**. O jogo é fictício; todos os itens devem ser armazenados; pares incompatíveis não compartilham baú; capacidades podem diferir; minimizar a quantidade de baús. Usar x_ij e y_j, capacidade C_j e restrições de conflitos. Não trocar por seleção de itens, minimização de custo ou outro tema sugerido anteriormente.

Apresentação 1: **11/11 — Aula 21 — modelagem e solução utilizando solver**. O ano de trabalho é interpretado como 2026 pelo contexto; horário e duração não foram informados. Gurobi, SCIP e FFD adaptado foram sugeridos pelo grupo, com comparação em 20, 50, 100 e 200 itens. A garantia clássica de FFD não se transfere à variante.

Ler `contexto/recursos/README.md` para documentação oficial, literatura e protocolo experimental. Python 3 é proposta técnica, não linguagem já escolhida. O repositório segue sem implementação nem resultados.

Pendências: inventário finito/disponibilidade por capacidade de baú, unidades, categorias e matriz de incompatibilidades, política de abertura de baús da heurística, geração dos dados e acesso aos solvers. Não inventar esses dados como decisões tomadas. O cenário é fictício, enquanto o enunciado solicita aplicação real; o documento do tema registra a necessidade de alinhar sua aceitação com o professor. Não confundir `Atividade.pdf` com o projeto nem datas dos slides com seu calendário.

## Critérios de trabalho

Preservar os PDFs. Manter rastreabilidade entre requisitos e entregas. Não inventar referências, resultados, tempos, ótima solução ou execuções de solvers. Registrar ausência de licença/dependência como indisponibilidade, sem substituir silenciosamente os solvers obrigatórios. Verificar a documentação oficial das APIs quando começar a implementação.

Validar alocação, capacidade, uso de caixas e valor objetivo independentemente do solver. Não chamar uma solução de ótima apenas porque foi produzida por um método exato: exigir prova/status apropriado ou igualdade entre limites válidos. Não comparar apenas os rótulos das caixas, pois soluções equivalentes podem permutá-los. Separar requisitos oficiais, decisões do grupo e melhorias opcionais. Usar as mesmas instâncias e condições experimentais documentadas nos métodos comparados.
