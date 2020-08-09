''' 5. Construa o programa que calcule a média aritmética dos números pares. O usuário
fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar.
A condição de saída será o número 0 (zero).
Teste 1:    valor: 1, 2 e 0.    Resposta: Média 2
Teste 2:    valor: 1, 3 e 0.    Resposta: Não pode ser dividido por 0 (zero)
'''
soma = 0            # Soma dos números pares
ct = 0                  # Contador de números pares
valor = 1           # Valor inicial diferente de 0 (zero)
print ('Digite zero (0) para sair')
while valor != 0:                    # while True:
    valor = int(input("Digite um número:\n"))       # Recebe um número inteiro
    if valor == 0:                     # valor igual (==) 0 é a condição de saída
        break                            # O break força a saída da estrutura de repetição (while)
    resto = valor % 2
    if resto == 0:  # Se o valor recebido é par
        soma = soma + valor   # soma += valor  # incrementa a soma de valores recebidos
        ct = ct + 1                     # ct+= 1                # incrementa o registro de notas recebidas
    # Fim da estrutura de repetição "while"
media = soma / ct                # calcula a média
print("A media de todos os pares recebidos é: ", media) # mostra o resultado
'''   Alterações:
a. Digite a condição de saída (zero) na primeira leitura. Corrija este erro.
b. Mostre a média com quatro casas decimais.
c. Mostre também a quantidade de números pares e a soma dos pares.
d. Mostre a quantidade de números digitados.
        DICAS:
if ct != 0:                                                      # a.
    media = soma / ct                
    print ('Média = ', media)
else;
    print ('Não posso dividir por zero')        # a.
print("Média dos pares: %.4f" %(media) )          # b.            
print("Média dos pares: {:.4f}" .format(media) ) # b.
print("Quantidade de pares: ", ct)            # c.
print("Soma dos pares: ", soma)               # c.
'''


