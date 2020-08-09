'''    9. Elabore o programa que leia a altura e o gênero (‘m’ pra masculino e
‘f’ pra feminino) de um grupo de pessoas. Gere a tela de saída com as seguintes
informações: maior altura do grupo, menor altura do grupo, quantidade de homens
e quantidade de mulheres.
Teste 1: 1.80, m, 1.60,  f, 0      Saída: Maior=1.80   Menor=1.60   Masc.= 1   Fem.= 1
---   ALTERAÇÕES:
a. Calcule e mostre também a média das alturas do grupo.
b. Calcule e mostre também a porcentagem de homens.
c. Digite a condição de saída de primeira e mostre somente esta mensagem:
    "Não foi digitado nenhum dado."
d. Permita o usuário digitar letra maiúscula ou minúscula   ---   DICAS ABAIXO:'''
maior = 0                                      # Valores iniciais.
menor = 3
ct_masc = 0             #   PROVA P1, 28/03 (sequência, seleção (if) e repetição (wihile)
ct_fem = 0
print ('Digite  [ 0 ] para sair')
while True:                                     # Início da estrutura de repetição while.
    altura = float (input("Digite a altura: ") )              # Recebe a altura
    if altura == 0:
        break
    genero = input("Digite\n[m] para Masculino\n[f] para Feminino")  # Recebe o gênero
    if (genero == "m"):                 # Se gênero é masculino
        ct_masc += 1                        # ct_masc = ct_masc + 1
    else:
        ct_fem += 1                         # ct_fem = ct_fem + 1
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura                       # Fim da estrutura de repetição while.
print ("Maior altura no grupo: ", maior)
print ("Menor altura no grupo: ", menor)
print ("Quantidade de homens: ", ct_masc)
print ("Quantidade de mulheres: ", ct_fem)
'''   ALTERAÇÕES:
a. Mostre também a média das alturas do grupo.
b. Mostre também a porcentagem de homens.
c. Digite o valor 0 de primeira e mostre somente esta mensagem: 
    "Não foi digitado nenhum dado."              -----    DICAS ABAIXO:
porc_masc = ct_masc / (ct_masc + ct_fem) * 100         # b.
    if (genero == "m" or genero == "M"):                    # d. 
'''
