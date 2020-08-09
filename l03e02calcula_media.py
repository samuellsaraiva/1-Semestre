''' 2. Refaça o programa que calcule a média aritmética de um aluno que realizou duas
avaliações. Além do valor da média, inclua na tela de saída uma das mensagens:
“Aluno aprovado.” ou “Aluno reprovado.”.
Considere que o aluno será aprovado se conseguir média maior ou igual a cinco.
- Sintaxe do if ... else:
if condição:                               # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executado se a condição for verdadeira
else:
    print(“Mensagem 2”)            # Executado se a condição for false
'''
# Leia um valor, converta para float e atribua à variável nota1
nota1 = float(input("Digite a primeira nota: "))
# Leia um valor, converta para float e atribua à variável nota2
nota2 = float(input("Digite a segunda nota: "))
#atribui o resultado do cálculo à variável media
media = (nota1+nota2) / 2                # Parênteses obrigatórios.
print ('Média = ', media)
if media >= 5:
    print("Aluno aprovado")        #imprime se a média for maior ou igual a 5
else:
    print("Aluno reprovado")       #imprime se a condição do if não for verdadeira
'''   Alterações:
Teste 1: nota1 = 5, nota2=6                                   Saída: média = 5,5
Teste 2: nota1 = 5, nota2=6, peso1=3, peso2=5    Saída: média = 5,625
a. Mostre o valor da média aritmética com duas casas decimais.
b. Altere a saída. Mostre a média e a mensagem na mesma linha:
    Média do aluno: x.xxx           Aluno aprovado ou Aluno reprovado
c. Refaça-o considerando que a primeira prova tem peso três e
   a segunda, peso cinco. Ou seja, calcula a média ponderada do aluno.
d. Deixe o programa mais interessante, permita que o usuário digite
   o valor dos pesos para usar no cálculo da média ponderada. ----- DICAS ABAIXO:
print ('Média = {:.2f}' .format (media) )           # a.
print ('Média = %.2f' % (media) )                     a.
if media >=5:                                                   # b.
    print("Média = {:.2f}   Aluno aprovado" .format(media))     # b.
else:                                                                 # b.
    print("Média = {:.2f}   Aluno reprovado" .format(media))  # b.
media = (nota1 * 3 + nota2 * 5) / (3 + 5) // Parênteses obrigatórios. # c.
media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2) // Parênteses obrigatórios.  # d.

'''


