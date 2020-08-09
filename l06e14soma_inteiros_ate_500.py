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
14. Elabore o programa para somar todos os números inteiros que se encontram no
intervalo de um a quinhentos. Saída: soma = 125250        -----------------     '''
soma = 0
# sintaxe do range: lista1 = range( inicial , final + 1) , range retorna uma lista
for i in range(1, 500 + 1):
    soma += i                                            # Adiciona o valor de i a soma
print("Soma:", soma)
'''     ALTERAÇÕES:
a - Deixe o usuário escolher o valor final.
b - Some apenas os números pares. Saída: soma = 62750  -----   DICAS ABAIXO:
fim = int(input("Número final: "))               # a.
for i in range(1, fim + 1):                                # a.
if(i % 2 == 0):                                                   # b.
      soma+= i                                                      # b.

'''

