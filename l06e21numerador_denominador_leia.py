''' 20. Sendo H = 1 + 1 + 1 + 1 + . . . + 1 .
                          --     --    --    --              --
                          1     2    3    4                30
21. Deixe o problema anterior flexível, permita que o usuário forneça a quantidade de
termos da série. Sendo H = 1/1 + 1/2 + 1/3 + ... + 1/n
Teste 1:    Entrada = 9           Saída: H = 2.82897
Teste 2:    Entrada = 30        Saída:   H = 3.99499
Use as variáveis numerador e denominador       ----- '''
h = 0                                   # a variável h (somador) começa com zero
numerador = 1
# recebe o tamanho da série a ser avaliado
n = int(input("Digite o tamanho da série: "))
for denominador in range(1, n + 1):      # n + 1 para incluir o último termo
    h += numerador / denominador          # Acrescenta numerador/denominador à soma
print("O somatório da série é: ", h)     # Mostra o somatório da série
''' ALTERAÇÕES:
a. Mostre a soma com cinco casas decimais.
b. Modifique o programa para o usuário entre com o valoe do numerador da série
    ----- DICAS ABAIXO:
print("Valor de H= %.5f" %h)                  # a.
print("Valor de H= {:.5f}" .format(h))      # a.
# Adicionar essa linha no início, antes do for                           # b.
numerador = int(input("Digite o numerador da série: "))     # b.
'''


