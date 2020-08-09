''' 19. Construa o programa que gere cinco números inteiros aleatórios sorteados
pelo computador. Eles devem estar no intervalo fechado de zero a noventa e cinco.
import random                           # Biblioteca para gerar números aleatórios.
    Sintaxe:    nr_sorteado = random.randint (inicio, final)
    A função randint gera um número aleatório no intervalo de inicio até final e
armazena o número sorteado na variável nr_sorteado.                          ---------- '''
import random                           # Biblioteca para gerar números aleatórios
print('Números aleatórios:')
for i in range(1, 5+1):                                 # for i in range(1, 5+1, 1):
    nr_sorteado = random.randint (0, 95)     # Intervalo de 0 a 95
    print(nr_sorteado)         # Mostra os cinco números aleatórios gerados individualmente
''' ALTERAÇÕES:
a. Altere o programa para gerar vinte valores aleatórios no intervalo de -2 até +2.
b. Altera o programa para gerar dez números aleatórios no intervalo de 1 e 6.
c. Some todos os números aleatórios gerados e mostre a soma no final da execução.
d. Mostre a quantidade de vezes de cada um dos valores do intervalo foi sorteado.
e. Calcule a porcentagem de cada um dos valores sorteados no item anterior. 
      ---------- DICAS ABAIXO:
    nr_sorteado = random.randint (-2, 2)   # a.
for i in range(1, 10+1):                                # b.
    print(random.randint(1, 6))                    # b.
soma = 0                                                    # c.
for i in range(1, 10+1):
    nr_sorteado = random.randint(1, 6)
    soma += nr_sorteado
    print(nr_sorteado)
print("A soma é: ", soma)                       # c.
ct1 = ct2 = ct3 = ct4 = ct5 = ct6 = 0       # d.
if nr_sorteado == 1:                                        # Dentro do for
    ct1 += 1
elif nr_sorteado == 2
    ct2 += 1
...
print('Valor 1: ', ct1)                                     # Depois do for
print('Valor 2: ', ct2)
...                                                                    # d.
ct_total = ct1 + ct2 + ct3 + ct4 + ct5 + ct6                            # e.
porcentagem1 = ct1 / ct_total * 100               
. . .                                                                     
print ("Porcentagem do valor 1 = ", procentagem1)    
. . .                                                                                               # e.

---
from random import randint     # Erro
from random import *               # Ok
'''
