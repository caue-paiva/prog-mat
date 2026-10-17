# Cobertura dos materiais em relação ao projeto

Avaliação dos 15 PDFs de contexto disponíveis e do [enunciado oficial](../enunciado/Projeto_PM_BCC_2026.pdf). Foram acrescentados seis materiais: cinco sobre fundamentos de PL/Simplex e um sobre sequenciamento. A avaliação original abaixo se refere aos PDFs locais. A pesquisa externa posterior está em [recursos](recursos/README.md), e o [tema definido pelo grupo](../projeto/TEMA_DO_GRUPO.md) atualiza a escolha da aplicação. A tabela distingue cobertura dos slides e complementação, sem tratar leitura de documentação como execução concluída.

**Conclusão:** os novos arquivos fazem sentido como contexto da disciplina e aprofundam a base teórica. Eles não fecham as principais lacunas práticas identificadas para executar o projeto.

## O que os novos materiais acrescentam

| Arquivo | O que acrescenta | Relevância direta para BPP |
|---|---|---|
| [DefinicaoVerticeSolucaobasica.pdf](pdfs/DefinicaoVerticeSolucaobasica.pdf) | Forma padrão, convexidade, vértices, bases e factibilidade | Apoio à compreensão da relaxação linear |
| [Aula13PM.pdf](pdfs/Aula13PM.pdf) | Multiplicadores e custos reduzidos para testar otimalidade | Apoio à distinção entre solução e certificado de PL |
| [Aula14SimplexDeterminandoSolucaoMelhor.pdf](pdfs/Aula14SimplexDeterminandoSolucaoMelhor.pdf) | Direção Simplex, passo, pivô e ilimitabilidade | Fundamento de resolução de PL |
| [BaseInicialSimplex.pdf](pdfs/BaseInicialSimplex.pdf) | Fases I/II, artificiais, degenerescência e múltiplos ótimos | Apoio conceitual a diagnósticos de otimização |
| [Simplex-revisado.pdf](pdfs/Simplex-revisado.pdf) | Atualização da base/inversa e custo por iteração | Complementar; não é tutorial de solver MIP |
| [PI_Scheduling.pdf](pdfs/PI_Scheduling.pdf) | Sequenciamento com precedências e atrasos | Modelagem adicional; problema distinto do BPP |

Os resumos individuais estão no [índice geral](../README.md). Há sobreposição entre os cinco materiais de PL, e entre as disjunções de Scheduling e as aulas anteriores; isso é útil para estudo, sem criar novos requisitos de implementação.

## Matriz de cobertura atual

| Exigência ou necessidade | Situação com todos os materiais | O que falta |
|---|---|---|
| Modelagem: conjuntos, parâmetros, domínios, objetivo e restrições | Bem coberta | Adaptar ao cenário escolhido |
| Formulação base de Bin Packing | Coberta diretamente na Aula 05 e no enunciado | Justificar adaptações da variante |
| Geometria e solução da relaxação linear | Aprofundada pelos novos PDFs | Conectar os resultados contínuos aos limites do BPP |
| Prova de ótimo inteiro e limites de MIP | Parcial: há relaxação, exemplos inteiros e menção a branch-and-bound | Entender incumbente e limite global; não confundir certificado de PL com certificado do BPP inteiro |
| Uso de Gurobi e SCIP | Não coberto operacionalmente | Instalação, interfaces, disponibilidade/licença, parâmetros, execução e extração de resultados |
| Heurística/meta-heurística para BPP | O enunciado sugere FFD/BFD e outras alternativas; não há desenvolvimento suficiente nas aulas | Referência teórica, descrição e implementação do método escolhido |
| Status, objetivo, tempo e gap | Requisitos estão no enunciado; novas aulas explicam casos de PL | Mapeamento de status MIP, convenção de gap, extração de métricas e tratamento de limite de tempo |
| Comparação experimental reproduzível | Não há protocolo pronto nos PDFs | Instâncias, sementes, condições de comparação, saídas e análise |
| Aplicação real distinta por grupo | Há exemplos de aplicações | Escolha do grupo, regras reais e dados coerentes |
| Revisão da literatura do relatório | Há bibliografias didáticas, inclusive referência a Bertsimas e Tsitsiklis nos novos materiais | Referências específicas de BPP, da heurística e da aplicação; verificar dados bibliográficos |
| Estrutura do relatório e entrega | Coberta pelo enunciado | Produzir conteúdo e evidências do projeto |

## Cuidados para o agente implementador

1. **Simplex não substitui o método alternativo exigido.** Aplicado à relaxação do BPP, pode devolver atribuições fracionárias. O enunciado pede uma heurística ou meta-heurística para o problema escolhido, além de Gurobi e SCIP.
2. **Scheduling não é automaticamente Bin Packing.** O PDF minimiza atraso em um servidor. O BPP minimiza recipientes sob capacidade e obriga alocar todos os itens. Restrições de tempo só entram se pertencerem à aplicação real escolhida.
3. **Ótimo da relaxação não prova ótimo inteiro.** Para minimização, o valor da relaxação é limite inferior; é necessário combiná-lo com solução inteira factível e/ou certificado do solver.
4. **Não implementar o interior dos solvers como pré-requisito.** Base inicial, pivôs e inversa são conteúdo da disciplina, mas o projeto exige usar os solvers. Concentrar desenvolvimento no modelo, no método alternativo e na avaliação.
5. **Ler as ressalvas dos resumos.** Há simplificações sobre poliedros limitados, artificiais básicas nulas e condições de melhoria com degenerescência. Não transformar frases didáticas em regras de software sem as hipóteses corretas.

## Complementação mínima necessária — proposta

- Consultar documentação oficial das interfaces de Gurobi e SCIP ao implementar: criação de binárias/restrições, objetivo, limites de tempo, status, incumbente, melhor limite, gap e tempo; confirmar disponibilidade de execução dos dois.
- Escolher uma referência específica para FFD ou outro método do BPP e fundamentar sua escolha. O [plano de implementação](../projeto/IMPLEMENTACAO.md) já contém uma especificação operacional proposta de FFD/BFD e casos de validação; isso não substitui a fonte bibliográfica.
- Escolher aplicação e reunir suas regras/dados; se forem usados dados sintéticos, identificá-los e documentar a geração.
- Executar e documentar o protocolo experimental proposto no plano, adaptando-o ao problema e aos recursos disponíveis.
- Reunir referências para a introdução e para a comparação de métodos no relatório, em ABNT ou IEEE.

Não é necessário procurar mais slides de Simplex para fechar essas lacunas. A prioridade passa a ser documentação dos dois solvers, método alternativo de Bin Packing e definição da aplicação/experimentos.

## Complementação posterior com fontes externas

Foram acrescentados guias Markdown baseados em fontes primárias consultadas em 17/10/2026:

| Gap | Complementação disponível | Pendência prática |
|---|---|---|
| Gurobi | [Instalação, licença e modelo](recursos/GUROBI.md) | Ativar acesso e executar |
| SCIP | [PySCIPOpt e parâmetros](recursos/SCIP.md) | Instalar, validar versão/build e executar |
| Método alternativo | [FFD, referência teórica e adaptação](recursos/HEURISTICAS.md) | Definir política de baús e implementar conflitos |
| Métricas | [Status, limites e gaps](recursos/METRICAS_E_STATUS.md) | Extrair e validar saídas reais |
| Dados e comparação | [OR-Library e protocolo sintético](recursos/DADOS_E_EXPERIMENTOS.md) | Gerar instâncias do tema e medir |
| Literatura e aplicação | [Fontes sobre conflitos e capacidades](recursos/APLICACAO_E_LITERATURA.md) e [referências](recursos/REFERENCIAS.md) | Consolidar revisão e definir regras do jogo |

Tema escolhido: armazenamento de recursos de jogo de sobrevivência fictício com incompatibilidades e capacidades heterogêneas, minimizando a quantidade de baús. O grupo informou Apresentação 1 em **11/11 — Aula 21**, com modelagem e solução utilizando solver. Ainda faltam inventário, unidades e matriz de compatibilidade; a correspondência do cenário fictício à exigência de aplicação real deve ser alinhada com o professor.

A lacuna de recursos introdutórios tem agora um caminho documentado. Isso não equivale a bibliotecas instaladas, modelo validado, experimentos concluídos ou regras do cenário já aprovadas.
