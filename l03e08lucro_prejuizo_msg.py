'''   8. Analise o resultado de uma transação comercial. Verifique a situação final
do comerciante trabalhando com os valores lidos, ou seja, o preço de compra
e o preço de venda. Gere a tela de saída com uma das seguintes mensagens:
“Teve lucro.”, “Teve prejuízo.” ou “Os valores são iguais.”.
- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
'''
# Lê um valor, converte para float e atribui à variável
compra = float(input("Digite preço de compra: "))
venda = float(input("Digite preço de venda: "))
if venda > compra:
    print("Teve lucro.")
elif compra > venda:
    print("Teve prejuízo.")
else:
    print("Os valores são iguais.")
'''
Alterações:
a. Na tela de saída, mostre também o valor do preço de compra e do preço de venda.
'''
