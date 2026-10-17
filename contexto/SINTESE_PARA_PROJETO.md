# Síntese das aulas para implementar Bin Packing

Esta seção conecta os PDFs ao projeto. Os fundamentos vêm dos materiais locais; recomendações derivadas são marcadas como tal. Índice completo no [README](../README.md).

## O que aproveitar primeiro

| Prioridade | Fonte e páginas | Aplicação |
|---|---|---|
| Alta | Aula 05, pp. 24–39 | Mochila, múltiplas mochilas e formulação explícita de Bin Packing |
| Alta | Aula 04, pp. 10–34 e 44–50 | Capacidade, padrões de corte, limites e formulações alternativas |
| Alta | Aula 06, pp. 3–10 | Ativar recipientes e vincular alocação à ativação |
| Alta | Modelagem com inteiras, pp. 5–31 | Custo fixo, implicações, disjunções e relações lógicas |
| Média | Aula 02, pp. 3–16 | Processo de modelagem, unidades e classificação do problema |
| Média | Aula 08, pp. 2–19 | Diferença entre cobertura, empacotamento de conjuntos e partição |
| Complementar | Aula 03; Caixeiro Viajante; Atividade | Atribuição, conservação, conectividade e auditoria do modelo |

## Conceitos que não podem se perder

- **Mochila:** selecionar itens, podendo deixar alguns de fora, maximizando benefício sob capacidade.
- **Múltiplas mochilas:** número de recipientes dado; seleção/alocação maximiza benefício.
- **Bin Packing:** todos os itens precisam ser alocados; minimizar recipientes utilizados.
- **Set packing:** selecionar subconjuntos sem sobreposição, usualmente com incidência `Ax ≤ 1`. O nome “empacotamento” também aparece aqui, mas essa formulação não substitui automaticamente o BPP.
- **Partição:** cada elemento aparece exatamente uma vez, `Ax = 1`; no BPP, isso se traduz em uma caixa por item.
- **Capacidade com ativação:** `Σ_i w_i x_ij ≤ C y_j`; combina consumo de recurso e decisão de abrir a caixa.

Relaxa-se a integralidade para obter uma estimativa, não uma alocação final. Para minimização, relaxações válidas produzem limites inferiores e soluções factíveis produzem limites superiores. Arredondar variáveis pode quebrar alocação e capacidade.

## Recomendações derivadas para o projeto

Usar primeiro a formulação compacta da Aula 05, reproduzida em `../projeto/MODELO_MATEMATICO.md`. Escolher uma aplicação cujas regras possam ser descritas e verificadas. Se houver CPU e RAM, impor capacidade separadamente em cada dimensão: somar recursos incompatíveis numa única unidade não é justificável sem uma transformação validada.

Não acrescentar roteamento só porque há caminhões: distribuir cargas em veículos é BPP; decidir a sequência de visitas é outro problema. Não acrescentar geometria 2D/3D apenas porque itens têm volume: capacidade agregada não assegura encaixe físico.

FFD/BFD são sugestões do **enunciado**; os slides locais não fornecem uma especificação completa de suas implementações nem uma prova de garantia de aproximação. O plano de implementação descreve uma versão operacional proposta; fundamentação bibliográfica deve ser pesquisada e citada pelo grupo na etapa de desenvolvimento.

## Leitura crítica dos materiais

Há slides com datas de 2024/2025 e uma atividade de 2026. São materiais de contexto, sem determinar prazos do projeto. Os resumos preservam conceitos e exemplos úteis e apontam inconsistências numéricas identificadas nas Aulas 02, 04 e 05. As fórmulas normalizadas não devem ser tratadas como transcrição literal de imagens ou trechos com índices trocados.
