''' Sintaxe da estrutura de repetição for (para):
. . .
comando antes do for                                        # Executa uma vez
for variavel in range (inicial , final + 1 , passo):
    comando dentro do for                                   # Executa várias vezes.
    . . .                                                                   # . . .
    comando dentro do for                                   # Executa várias vezes.
comando depois do for, quando sai do for       # Executa uma vez
. . .
O range retorna uma lista.
Para cada valor da variavel no intervalo de inicial até final.
9. Melhore o programa anterior, se o usuário fornecer o valor inicial menor que o
valor final, gere a sequência na ordem crescente. E se o valor inicial for maior que
o valor final, gere a sequência na ordem decrescente.
Teste 1: Entrada: 1, 5         Saída: 1 2 3 4 5
Teste 2: Entrada: 5, 1         Saída: 5 4 3 2 1     ----------------------------     '''
# Executa o for dentro dos limites recebidos, variando de forma crescente ou decrescente
inicio = int(input("Digite o valor inicial: "))    # Recebe os valores inicial e final
fim = int(input("Digite o valor final: "))
if inicio < fim:                                      # inicio < fim - indica ordem crescente
    for i in range(inicio, fim + 1, 1):
        print(i)
else:                                                      # inicio > fim - indica ordem decrescente
    for i in range(inicio, fim - 1, -1):
        print(i)
'''    ALTERAÇÕES:
a. Acrescente a  mensagem "Os valores são iguais."
b. Mostre também a quantidade de números gerados na sequência.
c. Mostre também a soma de números gerados na sequência.
d. Deixe o programa mais flexível, permita que o usuário forneça o valor do passo.
        DICAS ABAIXO:
if inicio < fim:                                               # a.   (inicio < fim, indica ordem crescente)
    for i in range(inicio, fim + 1, 1):
        print(i)
elif inicio > fim:                                                  # (inicio > fim ,indica ordem decrescente)
    for i in range(inicio, fim - 1, -1):
        print(i)
else:                                                                    # inicio = fim
    print("Os números são iguais!", inicio)  # a.
ct = 0                                                 # b.
    ct = ct + 1                                            # Dentro dos dois for.       
print ("Quantidade: ", ct)                   # b.
soma = 0                                           # c.
    soma = soma + i                                 # Dentro dos dois for.
print ('Soma ', soma)                        # c.

--------------------------------------

    quit()
'''
