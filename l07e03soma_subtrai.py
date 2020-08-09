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
- 3. Construa o programa contendo as duas funções soma e subtrai. A função principal(main)
lê dois valores inteiros, chama a função soma passando os dois valores lidos e depois
chama a função subtrai passando os dois valores lidos. A função soma recebe dois
valores inteiros, realiza a soma deles e retorna o resultado do cálculo. A função
subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado
do cálculo. O programa recebe o valor retornado pelas funções soma e subtrai e
gera a tela de saída com essas informações. Use variável local.
Teste:   entrada: 3 e 2.   result: 5 e 1                                      ---------- '''
def soma(a, b):                      # Definição de funções
    somar = a + b
    return somar
def subtrai(a, b):
    subtrair = a - b
    return subtrair
if __name__ == '__main__':  # Início da execução do programa pela função principal (main).
    num1 = int(input("Digite o primeiro valor inteiro: "))         # Recebe os valores
    num2 = int(input("Digite o segundo valor inteiro: "))
    retorno_soma = soma (num1, num2)
    print("A soma é:", retorno_soma) # A chamada da função é usada após a criação da função
    retorno_subtrai = subtrai(num1, num2)
    print("A subtração é:", subtrai(num1, num2))
'''   ALTERAÇÕES:
a. Refaça sem usar a variável somar dentro da funçao soma.
b. Refaça sem usar a variável retorno_soma da função principal.
c. Crie mais uma função (recebe_inteiro) para realizar o trabalho de recepção de dados
    do usuário (que é feito com int(input("..."))).
    Ela não recebe nada, lê um valor inteiro e retorna o valor lido.
    Chame essa função duas vezes na função principal(main) para substituir os dois inputs.
d. Na função principal, coloque comentário ( # ) nos dois inputs e chame a função
    recebe_inteiro duas vezes.
e. Altere a declaração da função recebe_inteiro. Agora ela recebe uma mensagem que 
  será usada no input. A mensagem estática ("Digite um número inteiro") será substituida
  por uma  mensagem dinâmica. Na função prindipal (main), chame a função recebe_inteiro 
  passando uma das  mensagens dinâmicas: "Digite o primeiro valor" ou 
  "Digite o segundo valor".
    return a + b                                                                  # a.        ----- DICAS ABAIXO:
    print("A soma é:", soma (num1, num2) )                        # b. (na função principal)
def recebe_inteiro ():                                                             # c.
    vl_inteiro = int(input("Digite um numero inteiro: "))
    return vl_inteiro                                                                 # c.
    # num1 = int(input("Digite o primeiro valor inteiro: "))       # d. (na funçao principal)
    # num2 = int(input("Digite o segundo valor inteiro: "))
    num1 = recebe_inteiro ()
    num2 = recebe_inteiro ()                                                            # d.
def recebe_inteiro (msg):                                                       # e.
    vl_inteiro = int(input(msg))
    return vl_inteiro                                                           
    num1 = recebe_inteiro ("Digite o primeiro valor")                 (na função principal)                                     
    num2 = recebe_inteiro ("Digite o segundo valor")           # e.
---
    # O retorno das funções pode substituir argumentos em outras funções
    # O próprio print() é uma função já implementada no Python que apenas utilizamos

'''
