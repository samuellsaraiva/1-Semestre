''' 29. Implemente o programa que mostre a sequência dos números octais de 00 até 77.
Use paras encadeados. A representação de números octais , na base oito, utiliza apenas
estes oito dígitos: 0, 1, 2, 3, 4, 5, 6 e 7. Veja a sequência:
0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, . . . , 77.
'''
for i in range (0, 7+1):
    for j in range (0, 7+1):
        print(i, j)
''' ALTERAÇÕES:
a. Acrescente um cabeçalho.
b. Mostre a quantidade de repetiçoes realizadas.
c. Melhore o leiaute
    ----- DICAS ABAIXO:
print ("Números octais:")           # a.
ct = 0                                             # b.
    ct += 1
print(ct)                                       # b.
        print(f"{i}{j}")                    # c.











---
# para cada número i no intervalo desejado
for i in range(0, 78):
    # valor recebe i, para realizar os cálculos mantendo i com seu valor original
    valor = i
    # string com o valor correspondente em octal que será montada
    string_octal = ""

    # 0 decimal = 0 octal
    if valor == 0:
        string_octal = "0"
    # para qualquer valor diferente de 0, um cálculo deve ser feito
    else:
        # enquanto valor for maior que 0
        while valor > 0:
            # adiciona o resto da divisão de valor por 8 à esquerda na string
            string_octal = str(valor % 8) + string_octal
            # atualiza valor pela divisão inteira dele mesmo por 8
            valor //= 8
    # mostra o resultado
    print(i, " decimal = ", string_octal, " octal")
'''

'''
Alterações

a. Altere o programa para aceitar qualquer base numérica que o usuário digitar

base = int(input("Digite a base desejada: "))

# para cada número i no intervalo desejado
for i in range(0, 78):
    # valor recebe i, para realizar os cálculos mantendo i com seu valor original    
    valor = i
    # string com o valor correspondente em octal que será montada
    string = ""

    # 0 decimal = 0 em qualquer base
    if valor == 0:
        string = "0"
    # para qualquer valor diferente de 0, um cálculo deve ser feito
    else:
        # enquanto valor for maior que 0
        while valor > 0:
            # adiciona o resto da divisão de valor por base à esquerda na string
            string = str(valor % base) + string
            # atualiza valor pela divisão inteira dele mesmo por base
            valor //= base
    # mostra o resultado
    print(i, " decimal = ", string, " em base ", base)
'''