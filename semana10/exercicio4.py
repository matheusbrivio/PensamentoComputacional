numeros = []
maiornumero = 0
menornumero = 0
for i in range (10):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
    if numeros[i] > maiornumero:
        maiornumero = numeros[i]
    if i == 0:
        menornumero = numeros[i]
    elif menornumero > numeros[i]:
        menornumero = numeros[i]
    
print(maiornumero,menornumero)
