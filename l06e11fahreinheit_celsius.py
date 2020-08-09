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
Fahreinheit  | Celsius                       (Layout de saída)
50.0 ºF          | 10.000 ºC
51.0 ºF          | 10.556 ºC
. . .
80.0 ºF          | 26.667 ºC                                                                             -------------------------     '''
print("Fahreinheit | Celsius")                        # Mostra o cabeçalho da tabela
for fahrenheit in range (50, 80 + 1, 1):           # for fahrenheit in range (50, 80+1):
    celsius = 5 / 9 * (fahrenheit - 32)                 # celsius = 5 * (fahrenheit - 32) / 9
    print (fahrenheit, '      |        ', celsius)           # Solução com print simples.
    print("{:2.1f}{:10s}| {:2.3f}{:3s}".format(fahrenheit, " ºF", celsius, " ºC"))
    # Mostra os valores formatados em uma tabela
    # {:2.1f} o primeiro argumento da função format será formatado para preencher o
    # espaço de número de 2 algarismos inteiros e uma casa decimal.
    # {:10s} O segundo argumento coloca um espaço de 10 caracteres alinhado à esquerda
    # | a barra vertical será impressa normalmente
    # {:2.3f} o terceiro argumento preencherá o espaço de número de 2 algarismos
    # inteiros e 3 casas decimais.
    # {:3s} o quarto argumento preencherá um espaço de 3 caracteres.
    # Os valores são para alinhar a tabela com o cabeçalho.
    # print("Fahrenheit: %.1f | Celsius: %.4f" %( fahrenheit, (((fahrenheit - 32)*5)/9))) # Outra solução.
'''
Fahreinheit  | Celsius                       (Layout de saída)
50.0 ºF          | 10.000 ºC
51.0 ºF          | 10.556 ºC
. . .
80.0 ºF          | 26.667 ºC   
    Alterações:
a. Mostre a soma dos valores Fahrenheit.
b. Use o for com uma lista gerada antes.
c. Substitua o for por um while equivalente
        DICAS:
soma = 0                                                   # a.
    soma = soma + fahrenheit
print ("Soma = ", soma)                           # a.
lista_fahrenheit = range (50, 80+1, 1)    # b.
for fahrenheit in lista_fahrenheit              # b.
ct = 50                                           # c.
while ct < 80:
    print(ct , " ºF = ", 5 * (ct - 32) / 9, " ºC")
    ct += 1                                       # c.

-----

    print("{}{:6s}| {:2.3f}{:3s}".format(i, " ºF", 5 * (i - 32) / 9, " ºC")) # Mostra Fahrenheit com inteiros
'''

