'''  8. Analise o resultado de uma transação comercial. Verifique a situação final do
comerciante trabalhando com os valores lidos, ou seja, o preço de compra e o
preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.
    9. Refaça o programa anterior. Se os valores forem diferentes, mostre também
o valor do lucro em reais ou o valor do prejuízo em reais.
Teste 1: compra = 1000 e venda = 1200. Resposta: Lucro = 200
Teste 2: compra = 1200 e venda = 1000. Resposta: Prejuízo = 200
- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
   print("A transação teve lucro de R$ {:.2f}" .format (lucro) )
Teste 1: compra = 1000 e venda = 1200. Resposta: Lucro = 200
Teste 2: compra = 1200 e venda = 1000. Resposta: Prejuízo = 200
'''
# recebe os valores de compra e venda
compra = float(input("Digite o preço de compra:\n"))
venda = float(input("Digite o preço de venda:\n"))
valor = venda - compra  # calcula o lucro da venda
if valor > 0: # valor > 0 significa que venda > compra, ou seja, houve lucro
    print("A transação teve lucro de R$ " + str(valor))
    print("A transação teve lucro de R$ ", valor)
    print("A transação teve lucro de R$ {:.2f}".format(valor))
elif valor < 0: # valor < 0 significa que venda < compra, ou seja, houve prejuízo
    print("A transação teve prejuízo de R$ " + str(-valor))
else: # valor = 0 significa que venda = compra, ou seja, não houve lucro ou prejuízo
    print("A transação não resultou em lucro ou prejuízo")
