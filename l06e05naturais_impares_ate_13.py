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
5. Elabore o programa que gere a sequência dos números naturais ímpares até 13.
'''
print ('Números ímpares:')                   # Cabeçalho.
for impar in range(1, 13 + 1, 2):
    print (impar)
''' ALTERAÇÕES:
a. Mostre também a soma dos valores da sequência.       Saída: soma = 49.
b. Refaça o exercício usando o passo 1.
c. Utilize a mesma ideia (de saltos de 2 elementos) para substituir o for por  um
while equivalente:              ---   DICAS ABAIXO:
soma = 0                                            # a.
    soma = soma + impar                             # Dentro do for       
print (soma)                                       # a.  
for i in range(0, 13 + 1, 1):                # b.
    # se i é impar, mostra i
    if i % 2 != 0:
        print(i)                                         # b.
contador = 1                                      # c.
while(contador <= 13)
    print(i)
    contador += 2                                # c.
'''
