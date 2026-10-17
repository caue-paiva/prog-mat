# Aula 08 — Cobertura, empacotamento de conjuntos e partição

Parte das tabelas e fórmulas está em imagens; a síntese inclui conferência visual das páginas correspondentes.

## Três modelos de incidência — pp. 2–7

Seja um universo de elementos e uma coleção de subconjuntos candidatos. `a_ij=1` quando o subconjunto j contém o elemento i; `x_j` indica seleção.

| Família | Restrição por elemento | Significado | Objetivo típico mostrado |
|---|---|---|---|
| Cobertura | `Σ_j a_ij x_j≥1` | Cobrir ao menos uma vez | Minimizar custo |
| Empacotamento de conjuntos | `Σ_j a_ij x_j≤1` | Evitar sobreposição | Maximizar valor |
| Partição | `Σ_j a_ij x_j=1` | Cobrir exatamente uma vez | Minimizar custo, ou maximizar receita conforme contexto |

Variáveis são binárias. Na cobertura de emergências, abrir instalações para que cada bairro tenha atendimento; o exemplo usa seis locais candidatos e cinco elementos a cobrir. Sobreposição é permitida.

## Exemplos de partição — pp. 8–15

**Venda de lotes:** três lotes A, B e C; nove propostas podem comprar lotes individuais ou conjuntos. Selecionar propostas maximizando receita, com cada lote vendido exatamente uma vez. Usar igualdade, porque todos devem ser vendidos e nenhum pode ser vendido duas vezes.

**Tripulações:** cada rotação candidata é uma sequência admissível de voos, já preparada respeitando regras de operação/trabalho. Escolher rotações com custo mínimo de modo que cada voo esteja em exatamente uma rotação selecionada. Variável binária por rotação e matriz de incidência voo–rotação. Gerar rotações é outra etapa; a aula assume a lista disponível.

## União de regiões e exercícios — pp. 16–21

As pp. 16–19 mostram a união de um triângulo e um retângulo. Uma PL contínua não descreve diretamente uma união não convexa apenas pela interseção de suas desigualdades; binária e Big-M selecionam qual conjunto de restrições deve valer. Normalizar os sinais e derivar limites válidos ao implementar.

A p. 20 propõe localização de armazéns com capacidades, custos fixos e de transporte e condições lógicas: locais A e C não podem coexistir; abrir A ou B implica abrir C; abrir D implica abrir C ou B. Em binárias, as leituras correspondentes são `y_A+y_C≤1`, `y_A≤y_C`, `y_B≤y_C` e `y_D≤y_C+y_B`. O conjunto das regras pode impedir A; isso deve ser investigado como consequência do modelo, sem apagar uma regra silenciosamente.

A p. 21 propõe escala hospitalar: uma pessoa trabalha cinco dias consecutivos e descansa dois. `x_j` conta enfermeiras que começam no dia j; minimizar `Σ_j x_j`, com cobertura da demanda por dia pela soma dos cinco inícios que trabalham naquele dia, usando índices cíclicos da semana. Demandas exibidas: `(10,12,14,12,18,19,12)`. Variáveis são inteiras não negativas; aqui se contam profissionais, não se escolhe uma única pessoa binária.

## Aplicação ao BPP

Atribuir cada item uma única vez é uma condição de partição; capacidade é outra família de restrições. “Empacotamento de conjuntos” não é automaticamente o modelo de Bin Packing. Uma abordagem por padrões poderia tratar subconjuntos de itens factíveis como candidatos, mas não é exigida no projeto.

Fonte: [Aula 08.pdf](../pdfs/Aula%2008.pdf), 22 páginas.
