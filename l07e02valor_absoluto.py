'''     - Sintaxe do uso de função
def nome_funcao (par1, par2, ... , parn):    # par (parâmetro) - o que a função recebe
    script                                                          # indentação obrigatória.
    .  .  .
    return val1, val2, ... , valn
def --> declara que estamos construindo uma funçao
nome_funcao --> nome da função definido pelo desenvolvedor
script --> código da função
return --> indica o fim da função e o que estará sendo retornado
val1, val2, ... , valn --> Valores retornados
- Chamada da função:
nome_funcao (arg1, arg2, ... , argn)            # arg (argumento) - o que envio para a função
- Exemplo:
print() é uma função, ou seja, a ideia de criar uma função é a sua reutilização
em vários momentos do programa
- 2. Elabore a função valor_absoluto que recebe um número qualquer e retorna o valor absoluto
(módulo) correspondente. A função principal (função main) lê o número, chama a função 
valor_absoluto passando o número lido e depois gera a tela de saída com o valor retornado 
pela função valor_absoluto. Lembrando que valor absoluto de um número positivo é ele mesmo 
e o valor absoluto de um número negativo é ele multiplicado por -1.
Use variável local e não use a função abs da linguagem.
Teste 1: valor = 3.2       Resultado: 3.2
Teste 2: valor = -3         Resultado: 3.0                                                                ----- '''
# Cria uma função que recebe um valor e retorna um valor.
def valor_absoluto(v):
    if v < 0:
        v = -v      # v = -1 * v
    else:
        v = v
    return v
# Fim da função valor_absoluto
if __name__ == '__main__':      # main <tab>
    valor = float (input("Digite um numero: "))  # Lê um valor do usuário
    # O valor do usuário está sendo passado para a função
    recebe = valor_absoluto(valor) # imprime o valor retornado pela função,
    print("Valor absoluto: ", recebe)
'''   Alterações:
a. Refaça a funçao valor_absoluto sem usar o else:
b. No main, imprima o valor retornado sem usar a variável 'recebe'
c. Resolva usando a função do Python que tem a mesma funcionalidade.
def valor_absoluto(v):                                                 # a.  ----- DICAS ABAIXO:
    if v < 0:
        v = -v      # v = -1 * v 
    return v                                                                        # a.   
    print("Valor absoluto: ", valor_absoluto(valor))   # b. 
    recebe2 = abs (valor)                                            # c. (No final da função principal)
    print("Valor absoluto: ", recebe)                      # c.

'''




