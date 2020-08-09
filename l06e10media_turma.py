''' Sintaxe da estrutura de repetição for (para):
. . .
comando antes do for                                           # Executa uma vez
for variavel in range (inicial , final + 1 , passo):
    comando dentro do for                                    # Executa várias vezes.
    . . .                                                                      # . . .
    comando dentro do for                                    # Executa várias vezes
comando depois do for, quando sai do for       # Executa uma vez
. . .
O range retorna uma lista.
Para cada valor da variavel no intervalo de inicial até final.
10. Refaça o programa que calcule a média aritmética de uma turma com
cinquenta alunos. Onde cada aluno realilzou uma avaliação.
Observação: para facilitar, troque o valor cinquenta por cinco.
Teste 1: Entrada: nota: 2, 4, 6, 8, 10           Saída: Média = 6         ----- '''
soma = ct = 0
for i in range(1, 5 + 1, 1):                     # Alterado para cinco alunos
    nota = float(input("Digite a nota do aluno: "))
    soma = soma + nota                        # soma += nota    (somador)
    ct = ct + 1
    # Fim da repetição for
media = soma / ct                                   # media = soma / 5
print("Média da turma %.2f" %(media)  )          # Formatação 1
print("Média da turma {:.2f}" .format(media)  )  # Formatação 2
'''    ALTERAÇÕES:
a. Deixe o usuário escolher a quantidade de alunos
b. Refaça sem usar a variável média.
c. Resolva usando lista.
d. Resolva sem usar a variável nota        -----   DICAS ABAIXO:
qtd = int(input("Digite a quantidade de alunos: "))    # a.
for i in range(1, qtd + 1, 1):                                             # a.
print("Média da turma %.2f" %(soma/5)  )                # b. 
lista_numeros = [ 1, 2, 3, 4, 5]                                         # c. Solução 1
lista_numeros = range (1, 5+1, 1)                                   # c. Solução 2
for i in lista_numeros:
for i in lista_numeros:
    soma = soma + float (input("Digite a nota do aluno: "))   # d. 
---




#media = soma / i                                   # media = soma / 5
'''
