''' - Estrutura de repetição (laço)   while (enquanto):
A estrutura de repetição (laço) while executa o bloco de instrução enquanto a expressão
definida para condição for  igual a verdadeira (True).
- Sintaxe:
while (condição):
    executa bloco       # Indentação obrigatória.
    . . .
    4. Desenvolva o programa que calcule a média aritmética de uma turma,
onde cada aluno realizou uma avaliação. Não sabemos a quantidade de alunos,
por isso usaremos o valor “ -1” como condição de saída. Na tela de saída,
mostre também a quantidade de alunos da turma. Sempre que tivermos uma divisão,
temos que verificar se o divisor é diferente de zero.
Teste 1:    notas: 1, 2 e -1.      Resposta: Média 1.5        Quantidade de alunos: 2
Teste 2:    notas: -1.               Resposta: Não existe divisão por zero (0)
'''
soma = 0       # Inicialização de variáveis
ct = 0
nota = 0
print('Digite [ -1 ] para sair')
while (nota != -1):  # while (True): # Laço de repetição while, repete enquanto condição verdadeira
    nota = float(input("Digite a nota do aluno: "))
    if (nota == -1):
        break            # Sai de uma estrutura de repetição (while)
    ct = ct + 1          # Incrementa variáveis se a nota for diferente de -1
    soma = soma + nota
    # Fim da estrutura de repetição "while"
if (ct != 0):
    media = soma / ct
    print("Média da turma: ", media)
    print('Quantidade de alunos: ', ct)
else:
    print("Não existe divisão por zero (0)")
'''     ALTERAÇÕES:
a. Troque a mensagem estática da entrada de dados por uma mensagem dinâmica.
b. Mostre também a soma das notas dos alunos da turma.
c. Mostre a média da turma com duas casas decimais.
d. Mostre a média e a quantidade de alunos na mesma linha, nesta frase:
    A média da turma de X alunos é X.XX.
        DICAS:
    nota = float (input("Digite a nota do aluno " + str (ct+1) + ": ") )            # a.
    nota = float (input("Digite a nota do aluno {} : " . format (ct+1) ) )          # a.
    nota = float (input(f"Digite a nota do aluno {ct+1} : " ) )                          # a.
    print("A média da turma de %d alunos é %.2f" %(ct, media) )                # d.
    print("A média da turma de {} alunos é {:.2f}" .format(ct, media) )         # d.
'''



