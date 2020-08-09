'''   1. Projete o programa que leia um valor numérico e
verifique se ele é maior ou igual a cem.Mostre uma
das mensagens: “Valor maior ou igual a cem.” ou
“Valor menor que cem.”
- Sintaxe
if condição:
    print (“Mensagem 1”)           # Executado se a condição for verdadeira
else:
    print(“Mensagem 2”)            # Executado se a condição for false
'''
# recebe um número digitado
valor = int(input("Digite um número:\n"))
# verifica se valor >= 100 para mostrar a mensagem
if valor >= 100:
    print("Valor maior ou igual a cem\n")
else:         # caso não seja
    print("Valor menor que cem")
'''
Alterações:
a. Mostrar também na tela de saída o valor numérico lido.
--- DICAS ABAIXO:
print ("Valor lido: ", valor)        # a.
'''


