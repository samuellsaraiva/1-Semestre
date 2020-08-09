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
3. Crie a função calcula_dobro. Não use o print dentro desta função.
Ele recebe um valor, calcula o dobro  e retorna o 
dobro do valor recebido. A função principal chama a função passando um valor 
inteiro e mostra o valor retornado pela função calcula_dobro              ----- '''
def calcula_dobro (p_valor):
    dobro = p_valor * 2
    return dobro
if __name__ == '__main__':                      # Função principal.
    valor = int(input("Valor: "))
    valor_retorno = calcula_dobro(valor)
    # O valor retornado pela função é armazenado na variável valor_retorno
    print(valor_retorno)
''' ALTERAÇÕES:
a. Acrescente a função calcula_triplo. Ela recebe um valor, calcula o triplo e 
retorna o valor calculado.
A função principal mostra o valor retornado pela função calcula_triplo.
    ----- DICAS:
def calcula_triplo(p_valor):                        # a.
    triplo = p_valor * 2
    return triplo
valor_retorno2 = calcula_triplo(valor)       # Dentro da função principal.
print(valor_retorno2)

'''






