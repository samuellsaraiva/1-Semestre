''' 16. Elabore o programa que imprima a tabuada de multiplicação do número cinco
de um até dez. Gere o seguinte leiaute:
1 x 5 = 5
. . .
10 x 5 = 50
17. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar
a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.
18. 	Modifique o programa para que ele imprima a tabuada de multiplicação de 1 até 10
de quaisquer números, sendo que esses números serão fornecidos pelo usuário.
Para cada número fornecido o programa deve gerar a respectiva tabuada.
Crie uma condição de saída.   ---------------------------------------------------   '''
while True:
    t = int(input("Digite o número para a tabuada ou [0] para sair: "))
    if (t == 0):     # se for 0, sai do while e não executa o for
        break
    for i in range(1, 10 + 1):
        print(i, "x", t, "=", (i * t))
    # fim da estrutura de repetição for
# fim da estrutura de repetição while
'''     ALTERAÇÕES:
a. Obtenha o mesmo resultado sem usar o break.        ----- DICAS ABAIXO:
t = int(input("Digite o número para a tabuada ou [0] para sair: "))      # a.
while t != 0:
   for i in range(1, 10 + 1):
      print(i , "x" , t , "=", (i*t))
   # fim da estrutura de repetição for
   t = int(input("Digite o número para a tabuada ou [0] para sair: "))
# fim da estrutura de repetição while                                                       # a.

'''
