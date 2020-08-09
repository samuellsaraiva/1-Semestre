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
4. Elabore o programa que gere a sequência dos números naturais pares até 12.
'''
print ('Números naturais pares')                  # Cabeçalho.
for par in range(0, 12 + 1, 2):
    # o end=" " evitar a quebra de linha, o padrão é end="\n"
    print(par, end=" ")
''' ALTERAÇÕES: 
a. Obtenha o mesmo resultado, trocando o passo 2 pelo passo 1 no range.
     ---   DICAS ABAIXO:
for par in range(0, 12 + 1, 1)           # for par in range(0, 12 + 1)     # a.
    if (par % 2 == 0):
        print(par, end=" ")


'''
