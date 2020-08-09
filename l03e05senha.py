'''   5. Elabore o programa que verifique se o usuário digitou a senha correta.
Mostre a mensagem “Senha incorreta.” ou “Acesso liberado.”.
Vamos supor que a senha correta seja 123.
Teste 1: senha = 123        Resposta: Acesso liberado.
Teste 2: senha = 111        Resposta: Senha incorreta.
'''
senha = 123                                     # armazena a senha correta
s = int (input("Digite a senha: ")) # O campo input mostra a senha enquanto o usuário digita
if s == senha:                                  # se a senha está correta
    print("Acesso liberado.")
else:                                                # caso contrário
    print("Senha incorreta.")
''' ALTERAÇÕES:
a. Considere que a senha correta é 1a3.
    ----- DICAS ABAIXO:
senha = '1a3'                                     # armazena a senha correta
s = input("Digite a senha: ") # O campo input mostra a senha enquanto o usuário digita
if s == senha:                                  # se a senha está correta






Não funcionou o exemplo abaixo: ----------
import getpass
# para esconder, basta usar getpass() do módulo getpass importado acima
s = getpass.getpass("Digite a senha: ")

'''
