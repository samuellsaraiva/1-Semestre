''' - Sintaxe do uso de função
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
2. Crie a função mostra_valor pra mostrar o valor recebido.
A função principal chama a função passando um valor inteiro.               ----- '''
def mostra_valor (p_valor):
    print("Parâmetro recebido: ", p_valor)
    return
if __name__ == '__main__':               # Função principal
    mostra_valor(5)
''' ALTERAÇÕES:
a. Na função principal, mostre uma mensagem antes de chamar a função 
b. Na função principal, mostre uma mensagem depois de chamar a função
c. Na função principal, leia um valor inteiro e chame a função passando o valor lido.
d. crie a função mostra_dois_valores, ela recebe dois valores e mostra esses valores.
    ----- DICAS:
print ("Mensagem antes da chamada da função")          # a.
print ("Mensagem depois da chamada da função")        # b.
valor_lido = int(input("Digite um valor: ")                      # c.
mostra_valor(valor_lido)
def mostra_dois_valores(valor1, valor2):                           # d.
    print("Valor 1: ", valor1)
    print("Valor 2: ", valor2)
    return 
mostra_dois_valores(10, 22)        # Dentro da função principal.


'''






