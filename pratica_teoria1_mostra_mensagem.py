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
1. Crie a função mostra_mensagem pra mostrar a mensgem "Bem-vindo ao def 
do Python" --- '''
def mostra_mensagem ():
    print("Bem-vindo ao def do Python")
    return
if __name__ == '__main__':      # main + tecla<tab>
    mostra_mensagem()           # Chama a função
'''
A convenção acima ( __ ) é utilizada frequentemente em Python e, muitas vezes, a chamamos de 
"dunder" (vem da expressão em inglês "double-underscore" - sublinhado duplo em português).
     ALTERAÇÕES:
a. Na função principal, mostre uma mensagem antes de chamar a função 
b. Na função principal, mostre uma mensagem depois de chamar a função
c. Crie a função mostra_mensagem2, ela recebe uma frase e mostra a frase
recebida. Na função principal, chame a funnção passando uma mensagem
    ----- DICAS:
print ("Mensagem antes da chamada da função")          # a.
print ("Mensagem depois da chamada da função")        # b.
def mostra_mensagem2 (msg):                                            # c.
    print(msg)
    return 
if __name__ == '__main__':      # main + tecla<tab>
   . . .
   var = "Mensagem passada"
   mostra_mensagem2(var)                                                     # c.

'''






