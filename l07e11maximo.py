''' 11. Desenvolva a função maximo que recebe dois números inteiros e retorna o maior
deles. A função principal lê dois números, chama a função maximo passando os dois
argumentos (os valores lidos) e gera a tela de saída com o valor retornado pela função
maximo. Use variável local.                                          ---------- '''
def maximo(num1, num2):  # Definição de função
    if num2 > num1: # Se numero2 seja maior que numero1
        maior = num2
    else:
        maior = num1
    return maior
if __name__ == '__main__':
    numero1 = int(input("Digite o primeiro número: "))  # Início do programa.
    numero2 = int(input("Digite o segundo número: "))
    maior = maximo(numero1, numero2) # A variável maior recebe o retorno da função
    print("O maior é", maior)
''' ALTERAÇÕES:
a. Na função principal, coloque um comentário na chamada da função maximo e 
    use uma função do Python que tem  mesma funcionalidade. 
    Use a função max que é nativa do Python.
b. Crie a função calculo para subtrair o maior pelo um novo numero digitado e mostre
    o resultado.                                                                    ---------- DICAS:
#maior = maximo(numero1, numero2)                  # a.
maior = max (numero1, numero2)                         # a.
def calculo (numero):                                       # b.
    numero2 = int(input("digite um numero: "))
    print(numero - numero2)
calculo (maior)                                                  # b.   (na função principal)

'''
