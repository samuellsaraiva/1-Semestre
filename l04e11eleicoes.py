''' 11. Em uma eleição presidencial, existem três candidatos. Os votos são
informados através de código. Os dados utilizados para escrutinagem obedecem
à seguinte codificação:
1, 2, 3 - voto dos respectivos candidatos;
5 - voto nulo; 6 - voto em branco;
Elabore o programa que calcule o total de votos de cada candidato, total de
votos nulos, total de votos em branco, percentual de votos nulos e percentual
de votos em branco.
Teste 1: Entrada: 1, 2, 3, 5, 6, 9
       Saída: Cand1=1 Cand2=1 Cand3=1 Nulo=1 Branco=1 pNulo=20 pBranco=20 '''
candidato1 = 0          # Inicializando variáveis
candidato2 = 0
candidato3 = 0
nulo = 0
branco = 0
while True:
    voto = int(input("""1 para candidato 1\n2 para candidato 2\n3 para candidato 3\
     \n5 para voto nulo\n6 para voto em branco\n9 para encerrar\nDigite seu voto: """))
    if voto == 9:                      #  \n  Pula para próxima linha
        break
    if voto == 1:                     # Computa o voto para o candidato correspondente
        candidato1 += 1           # candidato1 = candidato1 + 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        print("Voto não registrado")  # Fim da estrutura de repetição while
print("Candidato1 = ", candidato1, " votos.")       # Mostra os resultados
print("Candidato2 = ", candidato2, " votos.")
print("Candidato3 = ", candidato3, " votos.")
print("Votos nulos = ", nulo)
print("Votos em branco = ", branco)
ct_total = candidato1 + candidato2 + candidato3 + nulo + branco
porcNulo = nulo / ct_total * 100
porcBranco = branco / ct_total * 100
print('Porcentagem nulo: ', porcNulo)
print('Porcentagem branco: ', porcBranco)
'''   ---   ALTERAÇÕES:
a. Digite a condição de saída (voto = 9) de primeira e mostre somente esta mensagem
    "Ninguém votou."
b. Mostre uma mensagem de erro se eleitor digitar valor inválido.        


'''