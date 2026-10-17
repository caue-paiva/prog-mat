# Forma padrão, convexidade, vértices e soluções básicas

## Conteúdo — pp. 2–24

Transformações para PL na forma padrão `min cᵀx`, `Ax=b`, `x≥0`: acrescentar folga em restrições `≤`, subtrair excesso em `≥`, representar variável livre como diferença de duas não negativas e inverter o sinal do objetivo ao converter maximização em minimização.

Um poliedro é a interseção de um número finito de semiespaços; se limitado, é um politopo. Um conjunto é convexo quando contém todo segmento entre dois de seus pontos. Combinação convexa usa pesos não negativos cuja soma é 1; o casco convexo reúne todas essas combinações. A interseção de conjuntos convexos é convexa e todo poliedro é convexo.

## Vértices e bases — pp. 25–48

Um ponto extremo não é combinação convexa não trivial de dois pontos distintos do conjunto. Um vértice pode ser caracterizado como único minimizador de algum objetivo linear. Uma restrição é ativa em x quando vale com igualdade.

A caracterização algébrica usa n restrições ativas linearmente independentes no espaço de n variáveis. Para `Ax=b`, com posto de linhas m, uma base B é formada por m colunas independentes; fixar as outras variáveis em zero e resolver `Bx_B=b` produz uma solução básica. Ela é **factível** se `x_B≥0`. Vértice, ponto extremo e solução básica factível são equivalentes para poliedros.

Há no máximo `C(n,m)` escolhas de colunas; algumas podem não ser bases invertíveis ou não gerar soluções factíveis. O exemplo `C(20,10)=184756` motiva evitar enumerá-las todas. As pp. 49–51 propõem exercícios de reconhecimento geométrico e folgas.

## Ressalvas para leitura correta

A afirmação da p. 27 de que a região factível é o casco convexo dos vértices precisa de hipótese de limitação: vale para politopos não vazios; um poliedro ilimitado pode também exigir direções de recessão. Tampouco todo ótimo de PL precisa ser um vértice: podem existir pontos ótimos em uma face inteira. No contexto padrão, quando há ótimo finito, pode-se procurar uma solução básica factível ótima.

## Relação com o projeto

Reforça a geometria da relaxação linear do BPP e a diferença entre factibilidade e otimalidade. Uma solução básica pode ser fracionária; “estar num vértice” não prova integralidade. Não ensina APIs de solvers, FFD/BFD, instâncias experimentais ou aplicação real. Material complementar, não necessário para reimplementar álgebra de um solver no projeto.

Fonte: [DefinicaoVerticeSolucaobasica.pdf](../pdfs/DefinicaoVerticeSolucaobasica.pdf), 51 páginas.
