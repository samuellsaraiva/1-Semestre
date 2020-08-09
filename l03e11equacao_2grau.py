''' 11. Projete o programa que calcule as raízes de uma equação do 2° grau, levando em
consideração a análise da existência de raízes reais. Se o valor de delta for menor que
zero, não existem raízes nos reais; se delta for igual a zero, existem duas raízes iguais
e se delta for maior que zero, existem duas raízes diferentes.
Expressão: ax^2 + bx + c = 0
x = - b +-  raiz ( b^2 - 4 a c )                 delta = b^2 - 4 a c
                  2a
T este 1: a=0, b= 2 e c = 3.    Resposta: Não posso dividir por zero.
Teste 2: a=2, b= 2 e c = 3.    Resposta: Não existem raízes nos reais.
Teste 4: a = 3, b = 9 e c = 2. Resposta: x1 = - 0,241 ... e x2 = - 2,758 ...
 '''
import math      # bliblioteca de funcões matemáticas para usar a função sqrt (raiz quadrada)
print("Cálculo de raízes de equação do segundo grau ax^2 + bx + c = 0")
a = float(input("Insira a: "))
if a == 0:
    print ('Não posso dividir por zero')
else:
    b = float(input("Insira b: "))
    c = float(input("Insira c: "))
    delta = pow(b, 2) - 4 * a * c            # cálculo de delta
    if delta < 0:
        print("A equação não possui raízes no conjunto dos reais")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui duas raízes iguais a ", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui raízes diferentes x1 =", x1, "e x2 =", x2)

