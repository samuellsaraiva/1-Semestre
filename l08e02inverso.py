''' 1. Leia trinta valores inteiros digitados pelo usuário e armazene-os numa lista.
Gere a tela de saída com os valores armazenados na lista.
   2. Refaça o programa anterior, mostre os valores armazenados na lista na ordem
inversa da entrada de dados.
- Observação: para simplificar os testes, substitua trinta por três.
Prova P2 (turma A: 06/05, turma B: 07/05) e Prova P3 (AMC, 21/05) ------------- '''
l_valores = [ ]                                 # Lista inicialmente vazia
for i in range(0, 2+1):                     #for i in range(0, 3):  # Repete 3 vezes
    num = int(input("Digite um número: "))  # Recebe um número do usuário
    l_valores.append(num)                              # e adiciona o número à lista
print ('Valores da lista:')
print (l_valores [ : : -1])                   # Mostra todos os valores da lista em ordem inversa
''' ALTERAÇÕES:
a. Mostre os valores armazenados na lista na ordem inversa na vertical, use o for com range.
b. Mostre os valores armazenados na lista na ordem inversa na vertical, use o for com range.
    E suas respectivas posições.
c Também é possível acessar valores em uma lista do fim para o começo utilizando
    índices negativos. Refaça o loop que mostra os valores utilizando essa funcionalidade.
    ----- DICAS ABAIXO:
for i in range(2, 0-1, -1):                         # a.
    print(l_valores [i])
for i in range(2, 0-1, -1):                           # b.
    print(i, " - ", l_valores[i])
    #print("[", i, "] : ", l_valores[i])    
for i in range(-1, -3-1, -1):                          # c.                for i in range(-1, -4, -1):      
    print(i, " - ", l_valores[i])
    #print("[", i, "] : ", l_valores[i])
---
l_valores.reverse()             # Original
print(l_valores)
'''
