''' 1. Leia trinta valores inteiros digitados pelo usuário e armazene-os numa lista.
Gere a tela de saída com os valores armazenados na lista.
- Observação: para simplificar os testes, substitua trinta por três.
Prova P2 (turma A: 06/05, turma B: 07/05) e Prova P3 (AMC, 21/05) ------------- '''
l_valores = []                              # Lista inicialmente vazia
for i in range(0, 2+1):                 #for i in range(0, 3):  # Repete 3 vezes
    num = int(input("Digite um número: "))  # Recebe um número do usuário
    l_valores.append(num)                              # e adiciona o número à lista
print('Valores da lista:')  # mostra todos os valores da lista
print(l_valores)                # print (l_valores[ : : ])
''' ALTERAÇÕES:
a. Mostre os valores armazenados na lista na vertical usando o for com a lista.
b. Mostre os valores armazenados na lista na vertical usando o for com a lista.
    E mostre também suas respectivas posições (índices).
c. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
d. Mostre os valores armazenados na lista usando notação de vetor, use o for com range.
    E suas respectivas posições usando notação        ----- DICAS ABAIXO:   
for conteudo in l_valores:              # a.
    print(conteudo)   
ct = 0                                               # b.
print ('Posição - Valor')
for conteudo in l_valores:
    print(ct , "        -  ", conteudo)
    ct = ct + 1    
for i in range(0, 2+1):                          # c.    #for i in range(0, 3):                          
    print (l_valores [ i ])
print ('Posição - Valor')                  # d.
for i in range(0, 2+1):                                       #for i in range(0, 3):                         
    print (i, " - ", l_valores[i] )
    #print("[", i, "] : ", l_valores[i])
---
Veja os vídeos abaixo:
video1 - Introdução a Listas
https://www.youtube.com/watch?v=YeaB5IgS2rY&index=25&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
video2 - Listas dentro de listas, Adicionar novos elemetos a listas(append) 
https://www.youtube.com/watch?v=zzRiX_nIIMc&index=26&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
'''
