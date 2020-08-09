''' - Estrutura de repetição (laço)   while (enquanto):
A estrutura de repetição (laço) while executa o bloco de instrução enquanto a expressão
definida para condição for  igual a verdadeira (True).
- Sintaxe:
while (condição):
    executa bloco       # Indentação obrigatória.
    . . .
- 1. Relembre o exercício que calcula a média aritmética de um aluno que realizou duas
avaliações e gera o bole-tim com a média e uma das mensagens “Aluno aprovado” ou
“Aluno reprovado”. O aluno está aprovado se tiver média maior ou igual a cinco.
Agora refaça-o para uma turma com cinquenta alunos.
- 2. Complemente o programa anterior, verificando a quantidade de alunos
aprovados da turma. Mostre essa mensagem somente uma vez.
'''
ct_aprovados = 0
ct_alunos = 0    # um contador (ct) para controlar a quantidade de vezes que o while repete
while ct_alunos < 5:         # while ct < 50:    # enquanto o ct for menor que 50
    ct_alunos = ct_alunos + 1
    nota1 = float(input("Digite a primeira nota: "))     #ler um valor, converte para float
    nota2 = float(input("Digite a segunda nota: "))  #ler um valor, converte para float
    media = (nota1+nota2) / 2  #atribui o resultado do cálculo à variável media
    if media >=5: #imprime se a média for maior ou igual a 5
        print("Aluno aprovado com a média: ", media, "\n")
        ct_aprovados = ct_aprovados + 1              # ct_aprovados += 1
    else:
        #imprime se a condição do if não for verdadeira
        print("Aluno aprovado com a média: ", media, "\n")
    # Fim da estrutura de repetição "while"
print("\nQuantidade de alunos aprovados:", ct_aprovados)
'''   Alterações:
a. Mostre também a quantidade de alunos reprovados na turma.

'''




