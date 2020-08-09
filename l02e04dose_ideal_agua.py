''' 4. A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição. 
Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo. 
A dose ideal, ou seja, a necessidade diária em litros é calculada através desta fórmula:
massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.
- Os operadores aritméticos utilizados em Python:
    + → soma
    – → subtração
    * → multiplicação
    / → divisão
    // → divisão de inteiros
    ** → potenciação
    % → módulo (resto da divisão)
Teste: massa = 71              Resposta: qtd_ideal = 2.13
           massa = 60               Resposta: qtd_ideal = 1.7999999
'''
# Dose ideal de água
# Converte o valor para float
massa = float(input("Digite sua massa: "))
qtd_ideal = massa * 0.03                 # Notação americana, ponto decimal.
print ('Quantidade ideal:', qtd_ideal)
''' Alterações:
a. Na tela de saída, mostre também o valor da massa.
b. Mostre o resultado com uma casa decimal.             ----- DICAS ABAIXO:
print ('Valor da massa: ', massa)                                   # a.
print ("Quantidade ideal: {:.1f}" .format (qtd_ideal))       # b.
O valor 1 significa a quantidade de casas decimais.
print ("Quantidade ideal: %.1f  " % (qtd_ideal))                # b.

---







print("\n" * 30)   # Limpa a tela.

# str converte o valor para string
print('Quantidade ideal:' + str(qtd_ideal))
print(str(qtd_ideal)+" l","é a quantidade de água ideal")
print(str(qtd_ideal)+" l é a quantidade de água ideal")
'''
