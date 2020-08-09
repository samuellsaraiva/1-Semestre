'''            Comentários de várias linhas.
3. Faça o programa que calcule a média aritmética de duas notas
bimestrais fornecidas pelo usuário.
   Onde:     média = nota1 + nota2
		           2
Teste o seu programa com os valores 5 e 6.             Resposta certa 5.5
Abaixo segue uma lista com os operadores aritméticos utilizados em Python:
    + → soma
    – → subtração
    * → multiplicação
    / → divisão
    // → divisão de inteiros
    ** → potenciação
    % → módulo (resto da divisão)
'''
# recebe os valores convertidos para float
nota1 = float(input("Digite a primeira nota ")) 
nota2 = float(input("Digite a segunda nota "))

# atribui o cálculo à variável media
media = (nota1 + nota2) / 2                       # Parênteses obrigatórios.
# mostra o resultado
print("A média é ", media)
'''   ALTERAÇÕES:
a. Refaça-o considerando que o aluno realizou três avaliações. Teste com 2, 3 e 4. Resposta 3
b. Na execução, pule três linhas antes de mostrar o valor da média. 
c. Depois da média, mostre também o valor das três notas.
d. Acrescente o calculo da média ponderada, considerando que a prova1 
tem peso 1, a prova2 tem peso 2 e a prova3 tem peso 3.  
Teste com os valores 5, 6, 7.       A resposta certa é 6,3333335
e. Agora, refaça-o sem usar a variável media.
a. nota3 = float (input ("Digite terceira nota: ")         ----- VEJA AS DICAS ABAIXO:
   . . .
   media = ( nota1 + nota2 + nota3) / 3;
b. print ()
   print ()
   print ()
   print ('\n\n\n')   // Outra solução.
c. print ( "Nota 1:", nota1 )
    . . .
d. media2 = ( nota1 * 1 + nota2 * 2 + nota3 * 3 ) / ( 1 + 2 + 3 ); 
e. faça o cálculo dentro do print:
   print ("Média:", ( nota1 * 1 + nota2 * 2 + nota3 * 3 ) / ( 1 + 2 + 3 ) );
---
print("A média é", str(media) )
print("A média é "+ str(media) )
#saida de dados com o . format
print('Média {:.2f}'.format(media))   # Mostra com 2 casas decimais.

    '''
