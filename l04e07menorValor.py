'''    7. Construa o programa que encontre o menor valor de um conjunto de valores
inteiros digitados pelo usuário. Use o valor 0 (zero) na condição de saída que não será
considerado na pesquisa.
Teste 1: valor: 2, 1, 3, 0         Resposta: Menor = 1
Teste 2: valor: 1, 3, 2, 0         Resposta: Menor = 1
'''
menor_valor = 999999
print('Digite 0 (zero) para sair')
while True:     # while valor != 0:
    valor = int(input("Digite um valor: "))  # recebe um valor
    if valor == 0:  # se o valor for igual a zero, o laço encerrar, saí do while.
        break
    if valor < menor_valor:
        menor_valor = valor           # Atualiza a variável menor_valor.
    # Fim da estrutura de repetição (while).
print("O menor valor é: ", menor_valor)
'''     ALTERAÇÕES:
a. Mostre também a quantidade de valores foram digitados.
b. Se a condição de saída (zero) na primeira leitura, mostre a mensagem:
    "Não foi digitado nenhum valor."
c. Mostre a soma dos valoes digitados.         ---DICAS ABAIXO:
ct = 0                                                                                                  # a.
ct = ct + 1                     # Dentro do while
print ('Quantidade de valores digitados: ', ct)                                # a.
if ct != 0:                     # Mostra o resultado apropriado                  # b.
    print("Nenhum valor válido recebido")
else:
    print("O menor valor é: ", menor_valor)                                     
    print ('Quantidade de valores digitados: ', ct)                           # b.
soma = 0                                                                                            # c.
soma = soma + valor      # Dentro do while
    print ('Soma dos valores digitados: ', soma)                               # c.
'''
