'''
17. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar
a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.
'''



# recebe o valor
numero = int(input("Digite o número para obter a tabuada: "))

# range(1, 10) não inclui o valor 10, por isso 11 foi utilizado
for i in range(1, 11):
    # mostra o resultado
    print(i, " x ", numero, " = ", i * numero)

'''
Alterações

a.
'''
