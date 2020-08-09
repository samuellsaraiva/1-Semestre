''' 26. Escreva o programa que mostre todas as combinações possíveis com os valores
de dois dados (objeto “dado” utilizado em jogos). Ou seja, mostre todas as
possibilidades.                                                                           ---------- '''
for dado1 in range(1, 6+1):                  # O for externo.
    for dado2 in range(1,6+1):                   # O for interno.
        print(dado1, ' - ', dado2)
''' ALTERAÇÕES:
a. Coloque um cabeçalho antes das combinações.
b. Mostre as combinações na horizontal.
c. Mostre a quantidade de combinações geradas nos fors aninhados.  Saída: ct = 36
d. Melhore o leiaute, mostre seis combinações por linha.
    1 - 1       1 - 2       1 - 3       1 - 4       1 - 5      1 - 6
    .  .  .
    6 - 1       6 - 2       6 - 3       6 - 4       6 - 5      6 - 6        
    ----- DICAS ABAIXO:
print('Combinações possíveis:')                          # a.  
        print(dado1, ' - ', dado2, end=" ")              # b.     (solução 1)    
        print(f"({dado1}, {dado2})", end=" ")       # b.     (solução 2) 
ct = 0                                                                      # c.
    ct = ct + 1         # ct += 1
print('Quantidade = ', ct)                                      # c.
    print()                                                                # d. Antes ou depois do segundo for.
    
    
    
    
    
    
    
    
    
    

---
        print(f"({d1}, {d2})")
'''