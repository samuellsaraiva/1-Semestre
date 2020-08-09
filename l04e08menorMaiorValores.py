'''    8. Construa o programa que e ncontre o menor valor e o maior valor de
um conjunto de valores inteiros digitados pelo usuário. A condição de saída
será o valor -1 que não será considerado na pesquisa.
Teste 1: valor: 1, 3, 2, -1         Saída: Menor: 1      Maior: 3
Teste 2: valor: 1, 2, 3, -1         Saída: Menor: 1      Maior: 3
        PROVA P1, sequência, seleção (if) e repetição (wihile)   ---   '''
menor = 999999
maior =  -999999
print ('Digite [ -1 ] para sair')
while True:                     # while (valor != -1):
    valor = float (input("Digite um valor: "))
    if valor == -1:              # if (valor == -1):
        break
    if valor > maior:          # Se for maior, atualize o valor da variável maior.
        maior = valor
    if valor<menor:          # Se for menor, atualize o valor da variável menor.
        menor = valor
    # Fim da repetição (while)
print("Menor: ", menor)
print("Maior:" , maior)
''' ALTERAÇÕES:
a. Mostre também a quantidade de valores digitados.
b. Mostre também a soma de valores digitados.    
c. Digite o valor -1 de primeira e mostre somente esta mensagem: 
    "Não foi digitado nenhum valor"          
d. Calcule e mostre a média dos valores digitados -----  DICAS ABAIXO:
ct = 0                                         # a.
    ct = ct + 1
print ('Quantidade: ', ct)            # a.
soma = 0                                   # b.
    soma = soma + valor
print ('Soma: ', soma)                # b.
if ct != 0:                                                       # c.
    print("Menor: ", menor)
    print("Maior:" , maior)
else:
    print ("Não foi digitado nenhum valor")  # c.
'''
