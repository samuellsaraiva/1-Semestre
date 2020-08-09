''' Sintaxe da estrutura de repetição for (para):
. . .
comando antes do for                                           # Executa uma vez
for variavel in range (inicial , final + 1 , passo):
    comando dentro do for                                    # Executa várias vezes.
    . . .                                                                      # . . .
    comando dentro do for                                    # Executa várias vezes
comando depois do for, quando sai do for       # Executa uma vez
. . .
O range retorna uma lista.
Para cada valor da variavel no intervalo de inicial até final.
15. Elabore o programa para somar todos os números inteiros que são ao mesmo
tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.
Use ifs.                 Resposta: soma = 20667                       ---- '''
soma = 0                                            # valor inicial da soma é zero
for i in range(1, 500 + 1, 1):             # para cada valor i entre 1 e 500 com passo 1
    if i % 2 != 0 and i % 3 == 0:       # se i é ímpar e múltiplo de 3
        soma = soma + i                       # soma += i     (Resposta: soma = 20667)
print("O valor da soma é: ", soma)
'''     ALTERAÇÕES:
a. Mostre a quantidade de repetições executadas.
b. Refaça, troque o if com and por dois ifs (testando uma condição de cada vez)
c. Use passo 2 no for para fazer somente o teste (if) de número múltiplo de 3.
d. Use passo 3 no for para fazer somente o teste (if) de número ímpar.
e. Faça um for que não precise de fazer nenhum teste com o if. -----DICAS ABAIXO:
ct = 0                                                      # a.
    ct = ct + 1                                                  Logo depois do for, antes do if
print ('Quantidade de repetições: ', ct ) # a. 
if i % 2 != 0:                              # b. Realiza 500 repetições e faz 1.000 testes.
    if i % 3 == 0:
        soma += i                           # b.
for i in range(1, 500 + 1, 2):          # para cada valor i entre 1 e 500     # c.
    ct = ct + 1
    if i % 3 == 0 :                             # se i é múltiplo de 3
            soma += i                            # Realiza 250 repetições e faz 250 testes.         # c.
for i in range(0, 500 + 1, 3):               # para cada valor i entre 1 e 500     # d.
    ct = ct + 1
    if i % 2 != 0 == 0:       # se i é ímpar 
            soma += i               # Realiza 167 repetições e faz 167 testes.         # d.
for i in range (3, 500+1, 6):                                                                   # e.
    ct = ct + 1
    soma += i                       # Realiza 83 repetições e nenhum teste.      # e.










c. Use passo 3 no for para fazer somente o teste (if) de número par.
    
d. Faça um for que não precise de fazer nenhum teste com o if.

  
'''
