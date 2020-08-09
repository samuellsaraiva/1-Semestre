''' 5. Elabore o programa que faça a conversão de
graus Fahrenheit (ºF) para graus Celsius (ºC).
     Onde:     C = 5 . ( F - 32 )
                           9
Teste: fahrenheit = 32          Resposta: celsius = 0
           fahrenheit = 55          Resposta: celsius = 12.77777777777779
'''
# recebe a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em F "))
# efetua o cálculo 
celsius = 5 / 9 * (fahrenheit - 32)              # celsius = 5 * (fahrenheit - 32) / 9
# mostra o resultado
print ("A temperatura em Celsius é", celsius)
'''   Alterações:
a. Mostre o valor celsius com três casas decimais.
b. Altere o leiaute da mensagem de saída:
   Valor em Fahrenheit: x.xx  (Mostrar com duas casas decimais).
   Valor em Celsius: x.xxxx   (Mostrar com quatro casas decimais).  ----- DICAS ABAIXO:  
print ( "Graus correspondente em Celsius: {:.3f} °C" .format (c))  # a.
   O valor 3 é a quantidade de casas decimais.
print ("Valor em Fahrenheit: {:.2f}" .format(f))                                   # b.
print ("Valor em Celsius: {:.4f}" .format(c))

'''






