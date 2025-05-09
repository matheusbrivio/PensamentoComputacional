lista1 = []
lista2 = []

for i in range (5):
    lista = int(input("digite um numero:"))
    lista1.append(lista)

for i in range (5):
    lista = int(input("digite um numero:"))
    lista2.append(lista)

listafinal = lista1 + lista2
print(listafinal)
