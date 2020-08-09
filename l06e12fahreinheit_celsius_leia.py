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
11. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo.
Calcule a conversão e construa o relatório de saída tabular (em forma de tabela em
duas colunas) de graus Celsius em função de graus Fahrenheit que variam de 50 a
80 de 1 em 1. Fórmula: c = 5 ( f - 32 )
                                               9
12. Melhore o programa anterior para torná-lo mais abrangente. Agora, o usuário
fornecerá os valores inicial e final de graus Fahrenheit. Calcule a conversão e
gere o relatório de saída tabular (em forma de tabela) considerando o intervalo
digitado. Considere que o valor inicial será menor que o valor final.   -----   '''
inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
print("Fahreinheit | Celsius")                            # Mostra o cabeçalho da tabela
for fahrenheit in range(inicial, final + 1, 1):
    celsius = 5 * ( fahrenheit - 32) / 9
    print(  " %.1f             |    %.4f" % (fahrenheit  , celsius)  )
'''   Alterações:
a. Mostre o valor Fahrenheit como números inteiros.        -----   DICAS ABAIXO:      



    print(  " %d             |    %.4f" % (fahrenheit  , celsius)  )

'''

