'''   6. Elabore o programa que leia um número qualquer e verifique
se ele é positivo, negativo ou nulo.
- Sintaxe do if ... elif ... else:
if condicao1:                             # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executa, se a condição1 for verdadeira
elif condicao2:
    print(“Mensagem 2”)            # Executa, se a condição2 for verdadeira
else
    print("Mensagem 3")            # Executa, se todos os testes anteriores forem falsos.
Teste 1: numero = 4         Saída: positivo
Teste 2: numero = 0         Saída: nulo
Teste 3: numero = -4         Saída: negativo
'''
numero = float(input("Digite um número: ")) # Lê, converte e atribui à variável
if numero > 0:
    print("Número positivo")                   # Imprime, se numero for maior que 0
elif numero < 0:
    print("Número negativo")                  # Imprime, se numero for menor que 0
else:
    print("Número nulo")                        # Imprime, se numero for igual a 0
'''         ALTERAÇÕES:
a. Além da mensagem, mostre também o número digitado pelo usuário.
b. Se o número for positivo, mostre a mensagem, a variável numero e o dobro;
    se negativo, mostre a mensagem, a variável numero e o triplo;
    se nulo, mostre a mensagem, a variável numero.
   --- DICAS ABAIXO:
print ("Valor digitado: ", numero)      # a
if numero > 0:
    print("Número positivo, ", numero, "Dobro do número ", numero *2)  
elif     . . .
'''





