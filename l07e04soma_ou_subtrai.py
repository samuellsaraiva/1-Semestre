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
- 3. Construa o programa contendo as funções soma e subtrai. O programa lê
dois valores inteiros, chama a função soma passando os dois valores lidos e depois
chama a função subtrai passando os dois valores lidos. A função soma recebe dois
valores inteiros, realiza a soma deles e retorna o resultado do cálculo. A função
subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado
do cálculo. O programa recebe o valor retornado pelas funções soma e subtrai e
gera a tela de saída com essas informações. Use variável local.
- 4. Altere o programa anterior, agora o usuário vai escolher apenas uma operação.
A opção desejada será lida na função principal que chama uma das funções
(soma ou subtrai) passando os dois valores lidos como argumentos.
Teste 1: valores v1 = 33, v2 = 54 e 2 para subtrair. Resultado: Subtração: -21
Teste 2: valores v1 = 33, v2 = 54 e 1 para somar.   Resultado: Soma: 87 ----------'''
def soma(x, y):                     # Definição de funções.
    calculo = x + y
    return calculo
def subtrai(x, y):                   # Recebe 2 valores e retorna  a subtração.
    return x - y
if __name__ == '__main__':
    v1 = int(input("Digite o primeiro valor: "))             # Início do programa principal.
    v2 = int(input("Digite o segundo valor: "))
    opcao = int(input("Digite:\n[1] Somar\n[2] Subtrair\n"))
    #se o usuário digitou 1, chama a função soma, senão, a função subtrai
    if(opcao==1):
        print('Soma: ', soma(v1, v2))
    else:
        print('Subtração: ', subtrai(v1, v2))
'''    Alterações:
a. Na função principal, mostre a mensagem de opção inválida.
b. Use a função 'soma' para somar 4 valores e mostre o resultado. Não mexa (altere)
    na função soma.
c. Chame a função subtrai e determine qual valor vai para cada parâmetro e mostre o
     resultado.                                                                        ---- DICAS ABAIXO:
elif (opcao == 2):                                     # a.
    print('Subtração: ', subtrai(v1, v2))
else:
    print ('Opção inválida')                        # a.
print (soma(8,6)+soma(9,3))                     # b.    Solução 1
print (soma ( soma(8,6), soma(9,3) ) )       # b.    Solução 2
def subtrai (x, y)                                         # c.
print (subtrai(y=2, x=5))                             # c.  (na função principal)

---
def subtrai(x, y):                   # Recebe 2 valores e retorna  a subtração.
    return x - y

'''





