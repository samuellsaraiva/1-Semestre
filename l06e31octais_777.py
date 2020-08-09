'''     31. Implemente o programa que mostre a sequência dos números octais
de 000 até 777. Use paras encadeados.
'''
for i in range (0, 7+1):
    for j in range (0, 7+1):
        for k in range (0, 7+1):
            print(i, j, k)
''' ALTERAÇÕES:
a- Melhore o leiaute
    ----- DICAS:
for i in range(0,8):
    for j in range(0,8):
        for k in range(0,8):
            print(f"{i}{j}{k}")

'''