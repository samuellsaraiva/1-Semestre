''' 28. Implemente o programa que mostra a sequência dos números binários
de 000 até 111. Use paras encadeados.
0  0  0
0  0  1
0  1  0
0  1  1
1  0  0
1  0  1
1  1  0
1  1  1                                                                                          ---------- '''
for b1 in range(0, 1+1):                          # for b1 in range(0, 2):
    for b2 in range(0, 1+1):                      # for b2 in range(0, 2):
        for b3 in range(0, 1+1):                  # for b3 in range(0, 2):
            print(f"{b1}{b2}{b3}")
''' ALTERAÇÕES:
a. Acrescente um cabeçalho antes dos valores.
b. Mostre uma tabela com os valores em decimal e os valores em binário.
0       000
1       001
2       010
. . . 
7       111    
c. Refaça usando uma função do Python.               ----- DICAS ABAIXO:
print("Números binários")               # a.
valor = b1 * 4 + b2 * 2 + b3 * 1                    # b.        (dentro dos fors, solução 1)
valor = b1 * 2**2 + b2 * 2**1 + b3 * 2**0  # b.        (dentro dos fors, solução 2)
print (valor, ' - ', end='    ' )                         # b.
for i in range (0, 7+1):                      # c.
    print(bin (i))                                   # c.        (usando a função bin)
---
# potencia = int(base) ** int(expoente) (Colocado como comentário para visualização)
import math
potencia = math.pow(int(base),int(expoente))
'''
