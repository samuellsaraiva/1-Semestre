'''
6. Baseado na fórmula do exercício anterior, desenvolva a
fórmula que faça a conversão de graus Cel-sius (ºC) para
graus Fahrenheit (ºF). Usando a fórmula que você encontrou,
construa o programa que faça a conversão de graus Celsius (ºC)
para graus Fahrenheit (ºF).
     Onde:     C = 5 . ( F - 32 )
                           9


'''
















#Formulas
#°F = °C × 1, 8 + 32
#°C = (°F − 32) ÷ 1,8

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 1.8 + 32

print("Fahrenheit:", fahrenheit)
