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
6. Elabore o programa que gere a sequência dos números naturais múltiplos de 3 até 21.
'''
print ('Números múltiplo de 3:')                   # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 3):
    print (multiplo3)
''' ALTERAÇÕES:
a. Mostre também a soma da sequência gerada. Saída:     soma = 84
b. Obtenha o mesmo resultado usando passo igual a 1       ---   DICAS ABAIXO:
soma = 0                                                            # a.
    soma = soma + multiplo3                                         Dentro do for
print (soma)                                                       # a.
for multiplo3 in range(0, 21 + 1, 1):                                                       # b.
    # Verifica se o resto da divisão por 3 é igual a zero
    if (multiplo3 % 3 == 0):
        # O end=" " evitar a quebra de linha, o padrão é end="\n"
        print(multiplo3, end=" ")                                                                # b.





'''
