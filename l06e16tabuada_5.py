''' 16. Elabore o programa que imprima a tabuada de multiplicação do número cinco
de um até dez. Gere o seguinte leiaute:
1 x 5 = 5
. . .
10 x 5 = 50
'''
for i in range(1, 10 + 1):                      # for i in range(1, 10 + 1, 1):
    calculo = i * 5
    print(i, " x 5 = ", calculo)
''' ALTERAÇÕES:
a. Refaça sem usar a variável cálculo.
b. Altere para a tabuada de soma.
c. Use o format para configurar o leiaute        -----   DICAS ABAIXO:
    print(i, "x 5 =", (i * 5))                              # a.
    print(i , "+ 5 =", (i+5))                               # b.
    print("{} + {} = {}".format(i, 5, (i+5)))     # c.
'''



