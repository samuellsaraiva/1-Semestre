''''   5. Construa o programa que calcule a média aritmética dos números pares.
O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou
ímpar. A condição de saída será o número -1.
   6. Complemente o programa anterior, acrescente o cálculo da média aritmética
dos números ímpares.
Teste 1:   numero: 1, 2 e -1.    Resposta: Média pares: 2
                                                                Média ímpares: 1
Teste 2:   numero: 1, 5 e 1-.    Resposta: Não tem número par
                                                                Média ímpares: 3
Teste 3:   numero: 2, 4 e -1.    Resposta:  Média pares: 3
                                                                 Não tem número ímpar
Teste 4: numero: -1                Resposta: Não tem número par
                                                               Não tem número ímpar
'''
soma_par = 0                # Declaração das variáveis
soma_impar = 0
ct_par = 0
ct_impar = 0
print ('Digite ( -1 ) para sair')
while(True):          # while(numero != -1):    # Laço de repetição while com o uso do break
    numero = int(input("Digite um número: "))
    if(numero == -1):
        break                                # Interrompe a repetição while
    if(numero%2==0):                # Se o resto da divisão de numero por 2 for 0
        soma_par = soma_par + numero
        ct_par = ct_par + 1
    else:
        soma_impar = soma_impar + numero
        ct_impar = ct_impar + 1
    # Fim da estrutura de repetição (while)
if (ct_par != 0):                             #imprime se algum par for digitado
    media_par = soma_par/ct_par
    print("Média dos pares: %.2f" %(media_par))
else:
    print ("Não tem números pares")
if(ct_impar != 0):                          # imprime se algum impar for digitado
    media_impar = soma_impar/ct_impar
    print("Média dos ímpares: %.2f" %(media_impar))
else:
    print ("Não tem números ímpares")
'''   ALTERAÇÕES:
a. Mostre também a quantidade de números pares.
b. Mostre também  a quantidade de números ímpares.
c. Mostre também a quantidade de números digitados.
d. Calcule e mostre a porcentagem dos números pares.
'''
