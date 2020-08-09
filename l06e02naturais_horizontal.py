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
2. Elabore o programa que gere a sequência dos números naturais até 10 na horizontal.
'''
print ("Números naturais na horizontal")
for i in range (0, 10+1, 1):             # para cada item i no intervalo entre 0 e 10
    print(i, end=" ")  # O end=" " evitar a quebra de linha, o padrão é end="\n"
'''    Alterações:
a. Coloque cinco espaços entre cada número.
b. Coloque uma vírgula entre os números da sequência.
c. Retire a vírgula do último número da sequência.   ---   DICAS ABAIXO:
print (i, end="     ")       # a.
print (i, end=" "*5)       # a.
print (i, end = ", ")        # b.
for i in range (0, 10+1, 1):    # c.     (solução 1)
    if (i < 10):
        print (i, end=", ")
    else:
        print (i, end=" ")            # c.
for i in range (0, 10+1, 1):    # c.     (solução 2)
    if (i == 10):
        print (i, end=" ")            # c.
    else:
        print (i, end=", ")
'''
