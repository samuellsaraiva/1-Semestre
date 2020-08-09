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
- 1. Crie a função para somar dois valores inteiros. Ela recebe dois valores e retorna
o resultado do cálculo. A função principal lê os valores, chama a função soma_ retorna 
passando os valores lidos e depois mostra o valor retornado pela função soma, ou seja, 
0 resultado obtido. Use variável local.
- Teste: Entrada: 3 e 2. resultado: 5                                                        ----- '''
# Define a função soma_retorna, que recebe os parâmetros a e b.
# A definição da função não é executada. Ela só será executada quando for
# chamada nesta linha de código: retorno = soma_retorna (valor1, valor2)
def soma_retorna(a, b):
    calculo = a + b                   # variável recebe a soma dos parâmetros
    return calculo                   # retorna para função principal o valor calculado
    # Fim da funçao soma_retrona.
if __name__ == '__main__':              # main+ <tab>   (função principal)
    valor1 = int (input  ('Primeiro valor: ') )
    valor2 = int (input  ('Segundo valor: ' ) )
    vl_retorno = soma_retorna (valor1, valor2) # A chamada da função é realizada após a criação da função.
    print("A soma é: ", vl_retorno)
'''    ALTERAÇÕES:
a. Substitua os dois valores inteiros digitados pelo usuário e passados para função por
    estes dois valores reais (digite 2.1 e 3.3).
b. Refaça a função sem utilizar a variável calculo dentro da função.
c. Refaça a função principal sem usar a variável vl_retorno.
d. Acrescente a função soma_mostra, ela recebe dois valores, efetua a soma e
     mostra o resultado do cálculo. Ela não retorna nada. 
valor1 = float (input  ('Primeiro valor: ') )                  # a                 ----- DICAS ABAIXO:
valor2 = float (input  ('Segundo valor: ') )
retorno = soma_retorna (valor1, valor2)                       # a.
def soma_retorna (a, b):                                                    # b.
    return a + b                                                                       # b.
print ("A soma é:", soma_retorna(valor1, valor2))   # c.
def soma_mostra (v1, v2):                                                   # d.
    soma = v1 + v2
    print ("Resultado do cálculo: ", soma)
    retrun
if __name__ == '__main__':              # Função principal
    . . 
    soma_mostra (valor1, valor2)                                        # d.
---    
def soma(a, b=2):                        # 
'''
