# Referências verificadas e trilha de consulta

Consulta em 17/10/2026. Bibliografia inicial, não revisão exaustiva. Os registros acadêmicos abaixo seguem um formato próximo de IEEE; uniformizar a versão final conforme o padrão adotado pelo grupo. URLs técnicas `current`/`stable` podem mudar; registrar também versões realmente usadas.

## Publicações para o relatório

1. G. Dósa, “The Tight Bound of First Fit Decreasing Bin-Packing Algorithm Is FFD(I) ≤ 11/9 OPT(I) + 6/9,” in *Combinatorics, Algorithms, Probabilistic and Experimental Methodologies*, LNCS 4614, pp. 1–11, 2007. [Editora e DOI](https://link.springer.com/chapter/10.1007/978-3-540-74450-4_1). Consultados resumo e metadados; prova completa não consultada.
2. D. S. Johnson, *Near-optimal bin packing algorithms*, tese de doutorado, Department of Mathematics, Massachusetts Institute of Technology, 1973. [Registro institucional](https://dspace.mit.edu/entities/publication/b6bde6a7-fedf-4f2a-9184-24318ff54c85). Consultada a ficha bibliográfica, não a tese integral.
3. A. E. Fernandes Muritiba, M. Iori, E. Malaguti e P. Toth, “Algorithms for the Bin Packing Problem with Conflicts,” *INFORMS Journal on Computing*, vol. 22, no. 3, pp. 401–415, 2010. [DOI](https://pubsonline.informs.org/doi/10.1287/ijoc.1090.0355). Consultados resumo e metadados; publicação online em 2009, edição em 2010.
4. M. Gendreau, G. Laporte e F. Semet, “Heuristics and lower bounds for the bin packing problem with conflicts,” *Computers & Operations Research*, vol. 31, no. 3, pp. 347–358, 2004. [DOI](https://www.sciencedirect.com/science/article/pii/S0305054802001958). Resumo/metadados da editora recuperados pela busca; abertura direta bloqueada.
5. T. Bacci e S. Nicoloso, “On the benchmark instances for the Bin Packing with Conflicts,” arXiv:1706.03526v3, 2017. [Preprint](https://arxiv.org/abs/1706.03526v3). Consultados resumo e metadados; citar como preprint, sem atribuir a ele os dados de outra versão publicada.
6. D. K. Friesen e M. A. Langston, “Variable Sized Bin Packing,” *SIAM Journal on Computing*, vol. 15, no. 1, pp. 222–230, 1986. [DOI](https://epubs.siam.org/doi/abs/10.1137/0215016). Ficha/resumo indexados; abertura direta bloqueada. Checar correspondência de objetivo e disponibilidade de caixas antes de usar resultados.
7. E. Falkenauer, “A hybrid grouping genetic algorithm for bin packing,” *Journal of Heuristics*, vol. 2, pp. 5–30, 1996. [Editora e DOI](https://link.springer.com/article/10.1007/BF00226291). Consultados resumo e metadados; opção de meta-heurística, sem reprodução dos operadores.
8. E. D. Dolan e J. J. Moré, “Benchmarking optimization software with performance profiles,” *Mathematical Programming*, vol. 91, pp. 201–213, 2002. [Publicação](https://doi.org/10.1007/s101070100263); [versão dos autores](https://arxiv.org/html/cs/0102001). Consultadas definições e discussão de avaliação; usar como fundamento de análise, não como requisito imposto pelo professor.

## Recursos técnicos oficiais

| Responsável | Recurso | Uso no projeto |
|---|---|---|
| Gurobi | [Instalação Python](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python) | Instalar a interface |
| Gurobi | [Guia acadêmico](https://support.gurobi.com/hc/en-us/articles/4534601245713-How-do-I-get-started-with-Gurobi-for-academic-users) e [licenças](https://www.gurobi.com/product/pricing-and-licensing) | Confirmar acesso e tamanho de modelos |
| Gurobi | [Model Python](https://docs.gurobi.com/projects/optimizer/en/current/reference/python/model.html) | Variáveis, restrições e execução |
| Gurobi | [Atributos](https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html) | Objetivo, bound, gap e tempo |
| Gurobi | [Status](https://docs.gurobi.com/projects/optimizer/en/current/reference/numericcodes/statuscodes.html) | Interpretar encerramento |
| Gurobi | [Parâmetros](https://docs.gurobi.com/projects/optimizer/en/current/reference/parameters.html) | Tempo, threads, tolerância e semente |
| PySCIPOpt | [Instalação](https://pyscipopt.readthedocs.io/en/stable/install.html) | Ambiente Python/SCIP |
| PySCIPOpt | [Introdução](https://pyscipopt.readthedocs.io/en/stable/tutorials/model.html) e [API Model](https://pyscipopt.readthedocs.io/en/stable/api/model.html) | Modelagem e extração |
| SCIP | [Parâmetros](https://www.scipopt.org/doc/html/PARAMETERS.php) e [status](https://www.scipopt.org/doc/html/type__stat_8h_source.php) | Limites e interpretação |
| SCIP | [Exemplo de BPP](https://www.scipopt.org/scip/doc/html/BINPACKING_PROBLEM.php) | Leitura opcional de padrões/colunas |
| Python | [time.perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter) | Medição de intervalos |
| J. E. Beasley / OR-Library | [BPP 1D](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html) | Formato e referências de instâncias |

Leitura didática complementar: [Bin packing and cutting stock problems](https://scipbook.readthedocs.io/en/latest/bpp.html). Não copiar exemplos antigos sem ajustar validação e consultar a API instalada.

## Aplicação das fontes

As fontes dos solvers cobrem as APIs; Dósa fundamenta FFD clássico; as referências de conflitos e capacidades variadas posicionam a variante do jogo; OR-Library fornece benchmark clássico; Dolan e Moré ajudam na avaliação. Nenhuma dessas fontes prova regras do jogo fictício ou a qualidade da heurística adaptada. Essas partes dependem da definição explícita do grupo e dos experimentos.
