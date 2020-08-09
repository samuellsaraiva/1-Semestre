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
1. Elabore o programa que gere a sequência dos números naturais até 10 na vertical.
'''
print('Números naturais na vertical')                        # print('Cabeçalho')
for i in range(0, 10 + 1, 1):  # for i in range (0, 11):    # for i in range(11):
    print(i)                     # mostra i na tela. O print() quebra a linha por padrão
print('Encerrou o programa')
''' ALTERAÇÕES:
a. No final, mostre a quantidade de números da sequência. Use contador. 
    Saída:  Quantidade=11
b. Substitua range(0, 10) por uma lista equivalente.
c. Refaça o programa utilizando while em vez de for   ---   DICAS ABAIXO:    
ct = 0                              # a.
    ct = ct + 1
print (ct)                         # a.
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]          # b. (solução 1, lista feita na mão)
for i in lista1:
    print(i)                                                      # b.
lista1 = range (0, 10+1, 1)                           # b. (solução 2, lista feita com range)
for i in lista1:
    print(i)                                                      # b.
    
    
    
contador = 0                                      # c.
while (contador < 11):
    print(contador)
    contador += 1                                # c.
'''
