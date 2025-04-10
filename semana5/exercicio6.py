morador = input("Voce é morador?:").upper()
cartaovisitante = input("voce tem cartão de visitante?:").upper()
if morador == "SIM" or cartaovisitante == "SIM":
    print("Acesso ao estacionamento permitido!.")
else:
    print("Acesso negado!.")
