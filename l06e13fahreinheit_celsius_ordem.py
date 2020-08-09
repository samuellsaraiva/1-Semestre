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
digitado. Considere que o valor inicial será menor que o valor final.
13. Complete o problema de conversão de graus, gere o relatório
na ordem crescente, se o valor inicial for menor ou igual ao valor final.
E na ordem decrescente, se valor inicial for maior que o valor final.
'''
# recebe os números inicial e final
inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
print("Fahreinheit | Celsius")        # mostra o cabeçalho da tabela
if inicial < final:                   # inicial < final, indica ordem crescente
    passo = +1
    final = final  + 1
elif inicial > final:              # inicial > final, indica ordem decrescente
    passo = -1
    final = final - 1
else:                                 # inicial = final
    print("Os valores são iguais!")
    passo = +1
    final = final  + 1
# executa o for dentro dos limites recebidos, variando de forma crescente ou decrescente
for fahrenheit in range(inicial, final, passo):
    celsius = 5 / 9 * (fahrenheit - 32)                 # celsius = 5 * (fahrenheit - 32) / 9
    print ("{:2.1f}{:10s}| {:2.3f}{:3s}".format(fahrenheit, " ºF", celsius, " ºC"))
    # Mostra os valores formatados em uma tabela
    # {:2.1f} o primeiro argumento da função format será formatado para preencher o
    # espaço de número de 2 algarismos inteiros e uma casa decimal.
    # {:10s} O segundo argumento preencherá um espaço de 10 caracteres alinhado a esquerda
    # | a barra vertical será impressa normalmente
    # {:2.3f} o terceiro argumento preencherá o espaço de número de 2 algarismos
    # inteiros e 3 casas decimais.
    # {:3s} o quarto argumento preencherá um espaço de 3 caracteres.
    # Os valores são para alinhar a tabela com o cabeçalho.
    # print("Fahrenheit: %.1f | Celsius: %.4f" %( fahrenheit, (((fahrenheit - 32)*5)/9))) # Outra solução.
'''   Alterrações:
a. Refaça usando lista.
b. Refaça o escreva (print) usando uma máscara mais simples.
        DICAS:
if inicial < final:                   # inicial < final, indica ordem crescente                 # a.
    lista = range (inicial, final + 1, 1)
elif inicial > final:              # inicial > final, indica ordem decrescente
    lista = range (inicial, final - 1, -1)
else:                                 # inicial = final
    print("Os valores são iguais!")
    lista = range (inicial, final + 1, 1)
...
for fahrenheit in lista:            #                                                                              # a.

print(  " %.1f             |    %.4f" % (fahrenheit  , celsius)  )                                    # b.

----------------------------------------------
    quit()
'''
