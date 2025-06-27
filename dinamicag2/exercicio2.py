numeros = []
for i in range (5):
    numero = int(input("Digite o numero:"))
    numeros.append(numero)
maior = numeros[0]
for item in numeros:
    if item > maior:
        maior = item

print(numeros, maior)
