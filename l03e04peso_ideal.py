'''    4. Construa o programa que calcule o peso ideal de uma pessoa.
Utilize as seguintes fórmulas:
- Se homem, o peso ideal é calculado assim: ( 72,7 * altura ) - 58;
- Se mulher, o peso ideal é calculado assim: ( 62,1 * altura ) - 44,7.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
- Sintaxe do if ... else:
if condição:                               # A indentação é obrigatória.
    print (“Mensagem 1”)           # Executado se a condição for verdadeira
else:
    print(“Mensagem 2”)            # Executado se a condição for false
- Operadores de Comparação:
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
4. Construa o programa que calcule o peso ideal de uma pessoa.
Utilize as seguintes fórmulas:
- Se homem, o peso ideal é calculado assim: ( 72,7 * altura ) - 58;
- Se mulher, o peso ideal é calculado assim: ( 62,1 * altura ) - 44,7.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
Teste1: altura = 1.70 e genero = 1           Saída: peso ideal = 65.59 Kg
Teste2: altura = 1.70 e genero = 2           Saída: peso ideal = 60.8699999 Kg
'''
altura = float(input("Digite a altura: ")) # lê um valor, converte para float e atribui à variável
genero = int(input("Digite 1 para Masculino ou 2 para Feminino: "))
if genero == 1:
    peso_ideal = (72.7*altura)-58          #imprime se sexo for igual a 1
    print("Peso ideal do homem: %.2f  Kg" %( peso_ideal) )
else:
    print("Peso ideal da mulher: %.2f  Kg" %((62.1*altura)-44.7) ) #imprime se sexo for igual a 2
''' Testes: altura = 1.8     genero = M           Saída: peso ideal = 72.86 Kg
Teste1: altura = 1.70 e genero = 1           Saída: peso ideal = 65.59 Kg
Teste2: altura = 1.70 e genero = 2           Saída: peso ideal = 60.8699999 Kg
Alterações:
a. Troque a entrada para M ou F.
b. Mostre uma mensagem de erro se ele digitar valor de gênero diferente de M e F.
    ----- DICAS ABAIXO:
 # ler a letra M ou F e atribui à variálvel genero                                          # a.
genero = input("Digite M para Masculino ou F para Feminino: ")
if genero =='M':                      # if genero =="M":
    print("Peso ideal para o Homem: %.2f Kg" %((72.7*altura)-58) )
else:
    print("Peso ideal para a Mulher: %.2f Kg" %((62.1*altura)-44.7) )    # a.


'''
