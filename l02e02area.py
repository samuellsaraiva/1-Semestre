'''
2. Projete o programa para calcular a área de um triângulo. O usuário informará os dados
    necessários para o cálculo, ou seja, a base e a altura do triângulo.
   Onde:     área = base . altura
                                     2
'''

#calcular área de um triângulo.

#recebe um valor do usuário e converte para real.
base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = base * altura / 2

print ("Área: ",area)

'''
Alterações:
a. Na tela de saída de dados, mostre também o valor da base e da altura.
'''
