''' - Operadores de Comparação:
Operador 	Descrição 	        Exemplo
<               	Menor que  	        a < 10
<= 	            Menor ou igual 	b  <= 5
> 	                Maior que  	        c  > 2
>= 	            Maior ou igual 	d  >= 8
== 	            Igual 	                 e == 5
!= 	            Diferente 	          f  != 12
- Operadores aritméticos em Python:
    +    →     soma
    –    →     subtração
    *    →     multiplicação
    /     →     divisão
    //    →    divisão de inteiros (quociente da divisão)
    **  →    potenciação
    %   →     módulo (resto da divisão)
- Sintaxe do if ... else:
if condição:                               # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executado se a condição (teste) for verdadeira
else:
    print(“Mensagem 2”)            # Executado se a condição (teste) for falsa
3. Elabore o programa que verifique se o valor inteiro fornecido pelo usuário é
par ou ímpar.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
Teste com os valores 7 e 8.
'''
valor = int(input("Digite um número:\n"))  # recebe um número digitado
resto = valor % 2  # pega o resto da divisão dos dois números.
if resto == 0:         # verifica se n % 2 tem resto = 0, ou seja, o número é par
    print("Número é par")
else:  # caso contrário
    print("Número é ímpar")
''' Alterações:
a. Acrescente na tela de saída o número digitado e o valor do resto da divisão por 2.    
b. Verifique também se o valor fornecido é divisivel por cinco.
   --- DICAS ABAIXO:
print ("Valor digitado: ", valor)                # a.
print ("Resto da divisão: ", resto)           # a.
if valor % 5 == 0:                                      # b.
    print ("O número é divisível por 5.")
else:
    print ("O número não é divisível por 5.")


'''

