''' 27. Reescreva o programa anterior para mostrar somente as combinações que
tenhamos o valor sete como resultado da soma dos valores dos dois dados (objeto “dado”
utilizado em jogos).                                                              ---------- '''
for dado1 in range(1, 6+1):                          # Para cada valor possível do dado 1
    for dado2 in range(1, 6+1):                      # Para cada valor possível do dado 2
        if dado1 + dado2 == 7:                         # Se a soma dos valores for igual a 7
            print (dado1, " - ", dado2)               # Mostra o resultado
''' ALTERAÇÕES:
a. Acrescente um cabeçalho.
b. Modifique o programa para mostrar todas as combinações cuja soma seja 
menor que cinco.
c. Mostra a quantidade de combinações geradas.      Saída: Quantidade = 6    
    ----- DICAS ABAIXO:
print ('Dado1 - Dado2')                                              # a. 
# Troque a linha if dado1 + dado2 == 7: pela            # b.
if dado1 + dado2 < 5;
ct = 0                                                                              # c.
    ct += 1
print ('Quantidade = ', ct)
'''
