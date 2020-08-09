''' 8. Simule uma calculadora com as quatro operações aritméticas. Implemente uma
função para cada operação aritmética. Ela recebe dois valores e não retorna nada.
O usuário fornecerá a operação desejada(operação: +, -, x, / )
e os dois valores dentro do programa que chamará uma das quatro funções.
O resultado do cálculo será mostrado dentro de cada função. Use variável local.
Teste 1: Teste com os valores a = 45 , b = 89 e op = +. Resultado Esperado:134
Teste 2: Teste com os valores a = 67, b = 45 e op = -.   Resultado Esperado:22
Teste 3: Teste com os valores a = 23, b = 8 e op = *.     Resultado Esperado:184
Teste 4: Teste com os valores a = 230, b = 4 e op = /.   Resultado Esperado:57.5 --- '''
def soma(x, y):               # Definição das funções.
    print('Soma: ', x+y)
    return
def subtracao(x, y):
    print('Subtração: ', x-y)
    return
def multiplicacao(x, y):
    print('Multiplicação:', x*y)
    return
def divisao(x, y):
    print('Divisão: ', x/y)
    return
if __name__ == '__main__':
    a = float(input("Digite primeiro valor: "))             # Início da função principal.
    b = float(input("Digite segundo valor: "))
    op = input("Digite a operação [+] [-] [*] [/]: ")
    if(op=="+"):
        soma(a, b)
    elif(op=="-"):
        subtracao(a, b)
    elif(op=="x"):
        multiplicacao(a, b)
    else:
        divisao(a, b)
'''    Alterações:
a. Na função principal, inclua a mensagem opção inválida.
b. invés de mostrar o resultado dentro da função, faça a função 'soma' retornar o valor.
c. Por que o programa deixou de mostrar a soma? corrija o problema.
        DICAS:
. . .                                     # a.
elif(op=="x"):
    multiplicacao(a, b)
elif (op=="/"):
    divisao(a, b)
else
    print ('Opção inválida')
def soma(x, y):                # b.
    return x+y

print(soma(a, b))            # c.


'''
