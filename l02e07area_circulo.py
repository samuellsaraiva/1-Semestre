''' 7. Construa o programa que calcule a área de um círculo.
O usuário fornecerá o dado necessário.
Onde:	área = pi . raio2       (raio2 = raio ao quadrado)
Teste:       raio = 2            Resposta: area = 12.56636
'''
# recebe o raio que o usuário digitar
raio = float(input("Digite o raio do círculo: "))
# efetua o cálculo da área do círculo atribuindo à variável area.
area = 3.14 * raio * raio
# Outras maneiras de fazer potenciação:
#area = 3.14 * raio ** 2
#area = 3.14 * pow (raio, 2)
print("A área igual a ", area)        # mostra o resultado
''' Alterações:
# bliblioteca de funcões matemáticas
import math                # Importando os métodos de math, colocar no início do programa
area = math.pi * pow (raio, 2)
area = math.pi * raio** 2
a. mostre o valor da constante pi
b. Calcule e mostre o valor do diâmetro. diametro = 2*r    ----- DICAS ABAIXO:
pi = 3.14                                                            # Alteração a:
print("Valor de pi igual a ", pi)          ou
print("Valor de pi igual a ", math.pi)
diametro = raio * 2                                            # Alteração b:
print("Valor do diametro e ", diametro)
'''
