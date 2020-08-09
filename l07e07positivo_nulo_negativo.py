''' 7. Desenvolva a função positivo_nulo_negativo que recebe um número qualquer real
e retorna um valor inteiro. Ela retorna o valor +1, se o número recebido for positivo;
ela retorna o valor zero, se o número recebido for nulo e ela retorna o valor -1,
se o número recebido for negativo. A função principal (main) lê o número, chama a
função positivo_nulo_negativo passando o valor lido (argumento) e com o valor
retornado pela função mostra uma mensagem apropriada. Use variável local. ------ '''
def positivo_nulo_negativo(numero):           # Definição da função.
    if numero > 0:
        resposta = 1
    elif numero == 0:
        resposta = 0
    else:
        resposta = -1
    return resposta                         # Use somente um return dentro da função def
if __name__ == '__main__':                                 # main <tab>
    valor = float(input("Digite um número: "))    # Início do programa.
    # A variável resposta recebe o retorno da função def
    resposta = positivo_nulo_negativo(valor)
    print("Resposta: ", resposta)
'''    Alterações:
a. Refaça o exercício sem usar a variável resposta, na função principal.
b. Refaça o exercício sem usar a variável valor, na função principal.
c. Acrescente a função positivo_nulo_negativo_mostra que recebe um número 
e não retornar nada. Ela mostrar uma das mensagens: 
"Número positivo", "Número negativo" ou "Número nulo".    ----- DICAS:
#resposta = positivo_nulo_negativo(valor)               # a.
#print("Resposta:", resposta)
print("Resposta:", positivo_nulo_negativo(valor))
#valor = float(input("Digite um número: "))              # b.
#resposta = positivo_nulo_negativo(valor)
#print("Resposta:", resposta)
#print("Resposta:", positivo_nulo_negativo(valor))
print("Resposta:", positivo_nulo_negativo(float(input("Digite um número: "))))
def positivo_nulo_negattivo_mostra (number):         # c.
    if number > 0:
        print("Número positivo")
    elif number == 0:
        print("Número nulo")
    else:
        print("Número negaativo")                     
    return                                                       
valor = float(input("Digite um número: "))                             # Na função principal
positivo_nulo_negativo_msotra(valor)                        # c.
---
"Número positivo.", "Número nulo." ou "Número negativo"
'''
