''''    7. Construa o programa que leia dois valores quaisquer e
mostre o maior deles ou mostre a mensagem “Os valores são iguais.”
Teste: Entrada: 5 e 10                       Saída: Maior valor = 10
'''
# recebe os dois valores digitados
valor1 = float (input("Digite um valor:\n"))       # \n - Pula uma linha
valor2 = float (input("Digite ouro valor:\n"))
if valor1 > valor2:
    print("O maior valor é", valor1)
elif valor2 > valor1:                 # caso contrário
    print("O maior valor é", valor2)
else:
    print("Os valores são iguais")
''' ALTERAÇÕES:
a. Se eles forem diferentes, mostre os valores digitados na ordem decrescente.
b. Se eles forem iguais, mostre a mensagem e o valor digitado.
                 // DICAS ABAIXO:



if valor1 > valor2:                                                     # a
    print("Ordem decrescente: ", valor1, valor2)
elif valor2 > valor1:                 # caso contrário
    print("Ordem decrescente: ", valor2, valor2)   # a
else:                                                                            # b
    print("Os valores são iguais ", valor1)               # b
                                            
                                            
                                            
                                            
                                            
                                            
---
else:                 # caso contrário
    # max(a, b) retorna o maior valor entre a e b
    print("O maior valor é", max(a, b))

'''

