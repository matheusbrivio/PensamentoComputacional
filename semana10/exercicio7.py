listapar = []
listaimpar = []

for i in range (10):
    numero = int(input("digite um numero:"))
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
print(listapar,listaimpar)
