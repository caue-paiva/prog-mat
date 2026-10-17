# Aula 03 — Transporte, designação e transbordo

## Região factível — pp. 2–4

Exercício sobre reconhecer uma região factível de PL contínua. A interseção de restrições lineares é convexa: para dois pontos factíveis, todo o segmento entre eles também é factível. Uma região desenhada que viole essa propriedade não corresponde a uma PL contínua simples.

## Transporte — pp. 5–17

Distribuir um produto de origens para destinos minimizando custo. Parâmetros: oferta `a_i`, demanda `d_j`, custo unitário `c_ij`; variável contínua não negativa `x_ij`, quantidade enviada.

```text
min Σ_i Σ_j c_ij x_ij
Σ_j x_ij ≤ a_i            para cada origem i
Σ_i x_ij = d_j            para cada destino j
x_ij ≥ 0
```

O material ilustra bebidas (duas fábricas, três mercados) e rochas (quatro pedreiras, três depósitos). No exemplo das bebidas, ofertas 800 e 1000 e demandas 500, 400 e 900 totalizam 1800 de cada lado. Oferta limita saída; demanda exige atendimento. Não confundir capacidade da origem com consumo por destino.

## Designação — pp. 18–20 e 27–29

Atribuir n tarefas a n pessoas: `x_ij=1` se a pessoa i recebe a tarefa j. Cada pessoa recebe exatamente uma tarefa e cada tarefa tem exatamente uma pessoa: `Σ_j x_ij=1`, `Σ_i x_ij=1`, domínio binário. Maximizar `Σ_ij p_ij x_ij` quando p mede interesse, ou minimizar custos quando representam propostas financeiras, como no exercício de empreiteiras.

## Transbordo — pp. 21–26

Adicionar depósitos intermediários entre fábricas e mercados. Definir variáveis apenas para ligações permitidas e minimizar custos dos dois trechos. A formulação requer conservação em cada depósito: total recebido igual ao total enviado, caso não haja estoque/perdas. Essa é a leitura normalizada do exercício; os slides pedem formular o modelo.

## Conexão com Bin Packing

A igualdade que atribui cada tarefa exatamente uma vez inspira `Σ_j x_ij=1` no BPP. A diferença é que uma caixa pode receber vários itens, sob capacidade ponderada; não impor “uma caixa recebe exatamente um item”. Transporte permite dividir quantidades; BPP base não permite fracionar um item. O custo de ativar caixas também precisa ser modelado.

Fonte: [Aula03PM (1).pdf](../pdfs/Aula03PM%20%281%29.pdf), 30 páginas.
