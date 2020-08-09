''' 10. Construa o programa que calcule a raiz ( x ) de uma equação do primeiro grau.
Expressão de uma equação do 1º grau: a x + b = 0.
x = - b
        a
Teste 1: a = 2 e b = 3.         Resposta: Raiz = -1.5
Teste 2: a = 0 e b = 1.         Resposta: Não posso dividir por zero.
- Operadores de Comparação (relacionais):
Operador 	Descrição 	        Exemplo
<               	Menor que  	        a < 10
<= 	            Menor ou igual 	b  <= 5
> 	                Maior que  	        c  > 2
>= 	            Maior ou igual 	d  >= 8
== 	            Igual 	                 e == 5
!= 	            Diferente 	          f  != 12
Teste 1: a = 2 e b = 3.         Resposta: -1.5
Teste 2: a = 0 e b = 1.         Resposta: "Não posso dividir por zero."
'''
# ler um valor, converte para int e atribui à variável
a = int(input("Valor de A: "))
if a == 0:
    print ("Não posso dividir por zero")
else:
    b = int(input("Valor de B: "))
    x = - b / a
    print('Raiz = ', x)                             #imprime a raiz x




'''




'''
