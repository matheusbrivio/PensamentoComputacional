qntnumeros = int(input("Quantos numeros você deseja ver?"))

contador = 0
primeiro = 0
segundo = 1

while contador <qntnumeros:
    
    print (primeiro)
    proximo = primeiro + segundo
    
    primeiro = segundo
    segundo = proximo
    contador += 1
