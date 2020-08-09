''' 22.
Prepare o programa que calcule o valor de H, sendo que ele é determinado pela série:
H = 1 + 3 + 5 + 7 + . . . + 99
       --    --    --    --             ----
       1     2     3    4              50
Saída: soma = 95.50079
Use as variáveis numerador e denominador       ----- '''
soma = 0
denominador = 1
for numerador in range(1, 99 + 1, 2):
    soma += numerador / denominador
    denominador += 1
print("Valor de H: %.2f" % soma)
''' ALTERAÇÕES:
a. Refaça o programa, use a variável denominador como a variável do for.
    ----- DICAS ABAIXO:
numerador = 1                                                   # a.
for denominador in range(1, 50 + 1, 1):
    soma += numerador / denominador
    numerador += 2
print("Valor de H: %.2f" % soma)                # a.
    
'''


