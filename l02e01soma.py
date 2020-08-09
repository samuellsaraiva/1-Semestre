'''
1. Elabore o programa que calcule a soma de dois valores inteiros que serão fornecidos pelo usuário.
Teste: valor: 1 e 2.   Resposta: 3
'''
# recebe os valores convertidos para inteiro
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
# efetua a soma atribuindo o resultado à variável soma
soma = valor1 + valor2
# mostra o resultado
print("A soma é igual a  ", soma)

'''
ALTERAÇÕES:
a. No final do método, acrescente a subtração dos valores lidos e mostre o resultado.
b. No final do método, acrescente a multiplicação dos dois valores lidos e mostre o resultado.
c. No final do método, leia mais um valor inteiro, ou seja, o terceiro valor inteiro.
d. No final do método, acrescente a soma dos três valores lidos e mostre o resultado.
      DICAS:
# Alteração a:
subtracao = valor1 - valor2  
print("A subtração e igual a  ", subtracao)
# Alteração b:
multiplicacao = valor1 * valor2
print("A multiplicação e igual a  ", multiplicacao)
# Alteração c:
valor3 = int(input("Insira o terceiro valor: "))
# Alteração d:
soma = valor1 + valor2 + valor3
print("A soma é igual a  ", soma)
'''
