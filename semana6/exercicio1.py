contador = 0
usuario = ""
senha = ""

while contador < 3 and usuario != "admin" or senha != "1234":
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario != "admin" or senha != "1234":
        print("Usuário ou senha incorretos.")
        contador += 1

if usuario == "admin" and senha == "1234":
    print("Acesso permitido!")
else:
    print("Conta bloqueada. Tente novamente mais tarde.")
