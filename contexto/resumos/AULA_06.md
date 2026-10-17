# Aula 06 — Localização, disjunções e coloração

## Localização de instalações — pp. 3–10

Decidir quais instalações abrir e a qual delas atribuir cada cliente. Parâmetros: custo fixo `c_j`, custo de atendimento `f_ij`, demanda `d_i` e capacidade `e_j` quando existente. Binárias `y_j` (abertura) e `x_ij` (atendimento).

```text
min Σ_j c_j y_j + Σ_i Σ_j f_ij x_ij
Σ_j x_ij = 1                para cada cliente i
x_ij ≤ y_j                  para cada par i,j
Σ_i d_i x_ij ≤ e_j y_j      para cada instalação j, se capacitada
x_ij, y_j binárias
```

A capacidade pode ser retirada na versão não capacitada. Atribuir cliente exige instalação aberta. A p. 10 mantém título de versão “sem limitações de capacidade”, mas a fórmula exibida inclui capacidade; interpretar a fórmula e o contexto das pp. 9–10.

## p-medianas e p-centros — pp. 11–17

Fixar `Σ_i y_i=p`. p-medianas minimiza soma de distâncias/custos de atribuição; p-centros minimiza a maior distância por variável auxiliar r com restrições que a limitam inferiormente pela distância de cada cliente atribuído. O material inclui versões capacitadas. A demanda aparece na capacidade; o objetivo de distância mostrado não a pondera automaticamente.

## Ativação e disjunções com Big-M — pp. 18–29

Para ativar `f(x)≤0` quando `y=1`, usar `f(x)≤M(1−y)`. M deve ser um limite válido da violação possível no domínio restante. Um valor apenas “muito grande” pode prejudicar relaxação e desempenho numérico.

Para `f(x)≤0 OU g(x)≤0`, usar `f(x)≤M_f(1−y)` e `g(x)≤M_g y`. Uma das restrições é imposta; as duas podem ser satisfeitas simultaneamente. Isso representa OU inclusivo, não proíbe a interseção. O exemplo `x≤1 OU x≥6` usa a mesma ideia com sinais adaptados.

No exemplo de restaurantes, apenas um estabelecimento pode ser contratado: impor simultaneamente as capacidades dos dois é incorreto. Uma binária escolhe qual capacidade vale. Ao implementar, declarar também produção não negativa, além de inteira.

Selecionar k entre n restrições pode usar binárias de ativação com `Σ_i w_i=k`; isso não obriga as outras n−k desigualdades a serem violadas.

## Coloração de grafos — pp. 30–33

Minimizar cores usadas. `x_uc` atribui cor c ao vértice u e `y_c` ativa a cor. Cada vértice recebe uma cor; para aresta `(u,v)`, `x_uc+x_vc≤1`; `x_uc≤y_c` vincula atribuição e uso. Domínio binário para ambas (a última linha do slide tem lapso de notação).

## Aplicação ao projeto

Abrir uma instalação e atribuir clientes é estruturalmente parecido com ativar caixas e alocar itens. Custos de atendimento e exatamente p instalações pertencem a variantes de localização; não são requisitos do BPP. As restrições de coloração inspiram incompatibilidades entre itens, caso a aplicação escolhida as exija.

Fonte: [Aula 06.pdf](../pdfs/Aula%2006.pdf), 34 páginas.
