idade = int(input("Insira sua idade"))
cartao = input("Voce possui cartao de entrada?").upper()
if idade >= 18 and cartao == "SIM":
    print("Entrada aprovada!")
else:
    print("Entrada nao aprovada!")
