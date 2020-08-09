''' - Estrutura de repetição (laço)   while (enquanto):
A estrutura de repetição (laço) while executa o bloco de instrução enquanto a expressão
definida para condição for  igual a verdadeira (True).
- Sintaxe:
while (condição):
    executa bloco       # Indentação obrigatória.
    . . .
- 1. Relembre o exercício que calcula a média aritmética de um aluno que realizou duas
avaliações e gera o boletim com a média e uma das mensagens “Aluno aprovado” ou
“Aluno reprovado”. O aluno está aprovado se tiver média maior ou igual a cinco.
Agora refaça-o para uma turma com cinquenta alunos.
Para facilitar os testes, vamos fazer como quatro alunos.
'''
ct = 0      # O contador (ct) controla a quantidade de vezes que o while repete
while ct < 4:         # while ct < 50:         # enquanto o ct for menor que 4
    print("Aluno número ", ct)
    nota1 = float (input("Digite a primeira nota: ")) # Recebe as notas
    nota2 = float (input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2                              # calcula a média
    print ("Média = ", media)
    if media >= 5:                                                   # se a média for maior ou igual a cinco
        print("Aluno aprovado\n")
    else:
        print("Aluno reprovado\n")
    ct = ct + 1                                                          # ct += 1 (aumenta o ct (contador) em 1)
    # Fim da estrutura de repetição "while"
'''     ALTERAÇÕES:
a. Altere a primeira mensagem de "Aluno número 0" para "Aluno número 1"
b. No final do processamento, mostre a mensagem "Encerrando o programa".
    Essa mensagem deve aparecer somente uma vez.
    DICAS: 
a.     print("Aluno número ", ct + 1)
b. print ('Encerrando programa')
'''
