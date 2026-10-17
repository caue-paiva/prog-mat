# Tema definido pelo grupo

Informações fornecidas pelo usuário em 17/10/2026. Este documento registra a escolha do grupo; prevalece sobre sugestões anteriores de aplicação ainda não definida.

## Título

**Otimização de Armazenamento de Recursos em Jogos de Sobrevivência com Restrições de Compatibilidade e Capacidade**

## Contexto e objetivo

O cenário é um jogo de sobrevivência fictício em que jogadores precisam guardar recursos coletados em diferentes baús. O problema é uma variante de Bin Packing com incompatibilidades e capacidades heterogêneas.

Características definidas:

- **Todos os itens precisam ser armazenados.** Não é um problema de escolher apenas os recursos mais valiosos.
- **Certos itens não podem compartilhar um baú**, como materiais perigosos e alimentos.
- **Baús podem ter capacidades diferentes.**
- **Objetivo:** minimizar a quantidade de baús utilizados; não minimizar custo, desperdício ou valor de itens descartados.

Capacidades, consumos e categorias são hipotéticos. Não apresentar o cenário como dados coletados de um jogo comercial nem como restrições reais de um produto existente. O enunciado pede aplicação real: registrar essa diferença e validar com o professor a aceitação do cenário fictício como aplicação prática antes da entrega. Isso não impede desenvolver e estudar o modelo proposto.

## Apresentação 1

**11/11 — Aula 21 — Apresentação 1 do trabalho: modelagem e solução utilizando solver.**

O usuário informou dia e mês; no contexto do projeto de 2026, a interpretação de trabalho é **11/11/2026**. Não foram informados horário, duração, formato ou data da segunda apresentação. Para essa etapa, preparar cenário, conjuntos/dados, formulação, implementação via solver e resultados efetivamente obtidos. O projeto completo continua exigindo Gurobi, SCIP e método alternativo conforme o enunciado.

## Exemplo ilustrativo fornecido

| Baú | Conteúdo | Ocupação / capacidade |
|---|---|---|
| 1 | Madeira, pedra e metal | 15 / 20 |
| 2 | Alimentos e poções | 12 / 15 |
| 3 | Explosivos e combustíveis | 18 / 20 |

Este quadro ilustra a apresentação de uma alocação. Não define tamanhos individuais, instância completa, matriz de incompatibilidades ou uma solução ótima. Não inferir que explosivos e combustíveis sempre são compatíveis, nem que poções sempre são compatíveis com alimentos: o grupo precisa declarar as regras do jogo fictício.

## Métodos e experimentos sugeridos pelo grupo

- Gurobi e SCIP para o modelo inteiro.
- **First-Fit Decreasing adaptado**, verificando capacidade e compatibilidade antes de alocar cada item.
- Comparar instâncias com **20, 50, 100 e 200 itens**.

Esses tamanhos são a proposta experimental informada pelo usuário, não quantidade de instâncias fixada pelo professor. A licença restrita de Gurobi não suporta todos esses tamanhos no modelo compacto com m=n; confirmar licença acadêmica para executar a comparação completa. Não reduzir silenciosamente o experimento para caber na licença.

## Tradução matemática proposta

Esta seção deriva uma formulação da descrição e deve ser validada pelo grupo:

- `I`: itens individuais, com ID único, tamanho positivo `w_i` e categoria `k_i`.
- `J`: baús candidatos, cada um com capacidade positiva `C_j`.
- `E`: pares não ordenados de itens incompatíveis, derivados das categorias ou declarados individualmente.
- `x_ij∈{0,1}`: item i é colocado no baú j.
- `y_j∈{0,1}`: baú j é utilizado.

```text
min Σ_j y_j
Σ_j x_ij = 1                           para cada item i
Σ_i w_i x_ij ≤ C_j y_j                 para cada baú j
x_ij ≤ y_j                             para cada i,j
x_ij + x_hj ≤ 1                        para cada par {i,h}∈E e baú j
x_ij, y_j binárias
```

O vínculo explícito `x_ij≤y_j` é reforço proposto. Se `w_i>C_j`, pode-se fixar `x_ij=0`. Não agregar categorias incompatíveis como se o impedimento fosse apenas consumo de capacidade. Não impor que só uma categoria possa ocupar cada baú, pois categorias diferentes podem ser compatíveis.

## Decisões ainda necessárias

1. **Inventário de baús:** quantos baús de cada capacidade estão disponíveis? A formulação acima supõe lista finita J fornecida na instância. Essa é uma proposta de representação, não um dado já definido pelo usuário. Com baús grandes ilimitados, sem custo adicional ou restrições por tipo, sempre se pode trocar um baú pequeno por um grande; a diversidade de capacidades perde parte do efeito na minimização da contagem.
2. **Categorias e incompatibilidades:** definir lista e matriz simétrica, incluindo a possibilidade de incompatibilidade entre itens da mesma categoria. Ausência de regra não deve virar proibição implícita.
3. **Unidade de tamanho:** definir slots, unidades abstratas ou peso; não misturar essas medidas. Nesta proposta a capacidade é escalar, sem geometria 2D/3D.
4. **Geração das instâncias:** escolher distribuições, sementes, quantidade de casos por tamanho e inventários. Dados serão sintéticos e precisam ser identificados assim.
5. **Política de FFD com baús heterogêneos:** definir a ordem dos baús abertos e a escolha entre os disponíveis quando é necessário abrir outro.

## Atenção à heurística adaptada

Uma política inicial proposta é ordenar itens por tamanho decrescente, tentar baús abertos em ordem de abertura e, na falta de posição compatível, abrir um baú disponível de menor capacidade que comporte o item, desempate por ID. Essa política é apenas referência inicial para discussão; pode desperdiçar inventário e ficar sem alocação mesmo quando a instância é factível.

Se isso ocorrer, registrar **heurística sem solução completa**, não “instância infactível”. Uma solução parcial não vale como UB do problema. Pode-se propor reparo ou política alternativa, com descrição e comparação claras. O limite teórico clássico de FFD 1D não se transfere automaticamente a esta variante.

## Leitura do agente

Consultar [modelo base e variantes](MODELO_MATEMATICO.md), [implementação](IMPLEMENTACAO.md), [recursos externos](../contexto/recursos/README.md) e [requisitos oficiais](../enunciado/REQUISITOS.md). O modelo uniforme e os exemplos de API desses documentos são base didática; a implementação final deve representar `C_j` e E e validar as mesmas regras em todos os métodos.
