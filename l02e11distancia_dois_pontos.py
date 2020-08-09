'''
11.  Construa o programa que, tendo como dados de entrada dois pontos quaisquer do
        plano, P(x1,y1) e Q(x2,y2), calcule a distância entre eles. Use a seguinte fórmula:
       		distância =   (x2 - x1)2 + (y2 - y1)2       (raiz quadrada)
Testes: P (1, 2) e Q (1, 2)                         Resposta: distância = 0
              P (1, 2) e Q (5, 7)                         Resposta: distância = 6.4031242374328485
'''
# bliblioteca de funcões matemáticas
import math

# recebe as coordenadas de p
x1 = float(input("Digite a coordenada x do ponto p "))
y1 = float(input("Digite a coordenada y do ponto p "))

# recebe as coordenadas de q
x2 = float(input("Digite a coordenada x do ponto q "))
y2 = float(input("Digite a coordenada y do ponto q "))

# calcula a distância e atribui à variàvel d
d = (pow(x1 - x2, 2) + pow(y1 - y2, 2)) ** 0.5  #d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# mostra o resultado
print("A distância é", d)
