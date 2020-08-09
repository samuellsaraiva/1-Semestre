''' Sintaxe da estrutura de repetição for (para):
. . .
comando antes do for                                        # Executa uma vez
for variavel in range (inicial , final + 1 , passo):
    comando dentro do for                                   # Executa várias vezes.
    . . .                                                                   # . . .
    comando dentro do for                                   # Executa várias vezes.
comando depois do for, quando sai do for       # Executa uma vez
. . .
O range retorna uma lista.
Para cada valor da variavel no intervalo de inicial e final.
7. Elabore o programa que gere a sequência dos números naturais na ordem
decrescente de 7 até 0.                        -------------------------------------    '''
print ('Ordem decrescente:')                   # Cabeçalho.
for decrescente in range(7, 0 - 1, -1):      # for decrescente in range(7, - 1, -1):
    print (decrescente)             # para cada item no intervalo entre 7 e -1, em saltos de -1
''' ALTERAÇÕES:
a. Mostre também a soma da sequência gerada. Saída:      Soma = 28
b. Quebre o comando "for" em dois comandos de forma equivalente.   
     Use lista.                             -----------   DICAS ABAIXO:
soma = 0                                          # a.
     soma = soma + decrescente
print (soma)                                     # a.
lista = [ 7, 6, 5, 4, 3, 2, 1, 0]            # b.   (solução 1, cria a lista na mão)
lista = range(7, -1, -1)                     # b.   (solução 2, cria a lista com o range) 
for i in lista:
    print(i)                                          # b.  



---
for decrescente in reversed (range(0, 7 +1, 1)):     
'''
