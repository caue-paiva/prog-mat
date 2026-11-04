# Plano de implementação e validação

Plano definido em 04/11/2026, antes da implementação. Base: commit a2943f1ea499052a24b09e428c8ccc51956a7124 de caue-paiva/prog-mat; PDF oficial; Archive.zip.

## 1. Decisões operacionais desta implementação

Python 3; tamanho escalar inteiro em unidades abstratas de armazenamento (UA); itens indivisíveis e obrigatórios. Inventário finito explícito de baús. Dados sintéticos, sem atribuir estas escolhas ao grupo ou a um jogo comercial. Categorias: madeira, pedra, metal, alimento, pocao, explosivo, combustivel. Alimento e pocao conflitam com explosivo e combustivel; as demais combinações são permitidas. Conflitos adicionais por IDs são aceitos. Uma regra entre uma categoria e ela mesma proíbe dois itens dessa categoria no mesmo baú.

Gerador: tamanhos inteiros uniformes de 1 a 9 UA; n baús, sendo max(1,n//10) de 20 UA, max(1,n//5) de 15 UA e os restantes de 10 UA (para n>=20). Sementes 11, 22, 33; n=20,50,100,200. Assim existe solução trivial com um item por baú, mas o estoque dos maiores é limitado. Experimentos não representam coleta empírica.

## 2. Implementação em sequência

1. Contrato JSON, validação de entrada e verificador independente da saída.
2. FFD adaptado: itens por tamanho decrescente, empate pela posição; primeiro baú aberto compatível; abrir o maior disponível que caiba, empate pela posição. Falha retorna ausência de solução completa, não infactibilidade.
3. Formulação idêntica em Gurobi/PySCIPOpt: x_ij e y_j binárias, alocação exata, capacidade C_j, vínculo e conflitos por pares. Proibir baú vazio ativo. Simetria apenas entre capacidades iguais.
4. Redução opcional e demonstrada: se FFD encontrar U baús, manter os U maiores candidatos. Qualquer solução de até U baús pode ser remapeada para esses U maiores sem diminuir capacidades. Válida porque compatibilidade depende só dos itens e não existe restrição por tipo de baú. Não manter simplesmente os baús escolhidos pela heurística. Oferecer opção sem redução.
5. CLI para gerar, resolver, experimentar e validar; JSON por execução e CSV consolidado, metadados e hashes das entradas; logs dos solvers.
6. Testes manuais conhecidos, enumeração independente de casos pequenos, integração com os dois solvers, testes de dados inválidos e de soluções adulteradas.
7. Experimentos nas 12 instâncias, relatório nas cinco seções exigidas, roteiro das apresentações e ZIP reproduzível.

## 3. Protocolo de validação

Conferir todos os itens exatamente uma vez, baús existentes, capacidades, pares incompatíveis, cargas declaradas e objetivo. Objetivo desconhecido é null. Testar vazio, capacidade exata, item grande, inventário insuficiente, conflitos totais, capacidades heterogêneas, categoria auto-incompatível, duplicatas, números não inteiros e conflito desconhecido. Incluir FFD subótimo [6,5,3,2,2,2] em baús de 10, e falha gulosa com solução existente. Comparar solvers a enumeração exaustiva, não somente entre si.

Critérios: todos os testes sem falhas; toda solução publicada validada; resultados com licença indisponível sinalizados; nenhuma afirmação de ótimo sem certificado. Executar também instalação/CLI após extração limpa.

## 4. Experimentos e métricas

Mesmas entradas, uma thread, seed solver 0, gap alvo zero, sem warm start. Piloto: 10 s de otimização por instância/solver; construção e validação fora desse limite e medidas separadamente. Reexecução final sugerida: 300 s em máquina com licença Gurobi adequada, em diretório separado. Registrar objetivo UB, bound global LB, gap nativo e gap comum 100*(UB-LB)/max(abs(UB),1), status original/normalizado, tempo de construção, otimização e total, versões e hardware. O bound global não é a relaxação linear inicial. Para heurística, registrar distância ao bound de volume e, na análise, excesso relativo ao ótimo quando provado. Não misturar essas métricas.

## 5. Entrega e pendências externas

Plano, código, testes, instâncias, resultados brutos/CSV, relatório PDF e fonte editável, instruções e roteiros de apresentação. Preparar material para 11/11/2026 (Aula 21); segunda apresentação sem data informada. O PDF solicita aplicação real: confirmar com o professor a aceitação do cenário fictício. Identificar integrantes e confirmar originalidade em relação aos demais grupos. Se Gurobi bloquear tamanhos maiores, entregar evidência e comando de reexecução, sem declarar comparação completa.
