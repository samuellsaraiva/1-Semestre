'''   20. Construa o programa que calcule o valor de H.
Sendo H = 1 + 1 + 1 + 1 + . . . + 1
                  --    --    --    --     . . .     --
                  1     2     3    4     . . .     30
Saída:   H = 3.99499
Use as variáveis numerador e denominador       ----- '''
h = 0                      # Somador
numerador = 1
for denominador in range(1, 30 + 1):   # for denominador in range(1, 30 + 1, 1):
    h += numerador / denominador         # h = h + numerador / denominador (somador)
print("Valor de H = ",h)
'''   ALTERAÇÕES:
a. Mostre o valor da soma como cinco casas decimais.
   ----- DICAS ABAIXO:
print("Valor de H = %.5f" %h)
print("Valor de H = {:.5f}" .format (h))     
'''

