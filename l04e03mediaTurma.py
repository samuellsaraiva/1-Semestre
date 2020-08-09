''' - Estrutura de repetição (laço)   while (enquanto):
A estrutura de repetição (laço) while executa o bloco de instrução enquanto a expressão
definida para condição for  igual a verdadeira (True).
- Sintaxe:
while (condição):
    executa bloco       # Indentação obrigatória.
    . . .
    3. Projete o programa que calcula a média aritmética de uma turma com
cinquenta alunos, sabendo-se que cada aluno realizou uma avaliação.
Para facilitar os testes, faça com quatro alunos.
Testes: notas: 2, 3, 4 e 5                 Saída: Média da turma = 3.5
'''
ct = 0                  # Contador (ct) de controle de repetições
soma = 0             # Somador armazena a soma de todas as notas recebidas
while ct < 4:       # enquanto contador (ct) é menor que 4
    nota = float (input("Digite a nota do aluno:\n"))
    soma = soma + nota        # soma += nota      # incrementa soma com a nota recebida
    ct = ct + 1                      # ct+= 1                 # incrementa o ct em 1
# ao sair do laço, calcula a média
media = soma / ct                 # media = soma / 4
print("A media da turma é: ", media)     # mostra o resultado
''' Alterações:
a. Troque a mensagem de entrada estática por uma mensagem dinâmica:
     Digite a nota do aluno número X:
b. Mostre  média da turma com duas casas decimais.
      DICAS:
nota = float (input("Digite a nota do aluno { }:\n" .format (ct)))                    # a.
print("A media da turma é: %.2f " %(media))     # Mostra o resultado        # b.
print("A média da turma e´: {:.2f}" .format(ct, media) )            # b.


------

    soma += int(input("Digite a nota do aluno:\n"))
'''
