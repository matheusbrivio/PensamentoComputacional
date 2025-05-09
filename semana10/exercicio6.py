lista1 = []
lista2 = []
lista3 = []
for i in range (5):
    lista = int(input("digite um numero:"))
    lista1.append(lista)
    if lista in lista1:
        lista3.append(lista)
for i in range (5):
    lista = int(input("digite um numero:"))
    lista2.append(lista)
    if lista in lista1:
        lista3.append(lista)
print(lista1, lista2, lista3)
