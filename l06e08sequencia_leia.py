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
8. Elabore o programa que gere a sequência dos números inteiros, onde o usuário
fornecerá os valores inicial e final da sequência.   ------------------------------   '''
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
print ("Sequência de números inteiros:")   # Cabeçalho.
for numero in range(inicio, fim + 1, 1):
    print (numero)
''' ALTERAÇÕES:
a. No final, mostre a quantidade de números gerados na sequência. Use contador.
b. No final, mostre a média dos gerados na sequência.
    Teste: Entrada: Inicial 1, final 3           Saída: média: 2
c. Mostre os números da sequência na horizontal.        ---   DICAS ABAIXO:
ct = 0                                      # a.
    ct = ct + 1                                     # Dentro do for
print ("Quantidade: ", ct)    # a.
soma = 0                                    # b.
    soma = soma + numero                   # Dentro do for
media = soma / ct                                # Depois do for
print ('Média: ', media)            # b.
print (i, end=" ")                   # c.

'''
