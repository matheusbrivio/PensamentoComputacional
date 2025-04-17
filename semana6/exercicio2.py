valortotal = int(input("digite o valor total:"))
valorpago = int(input("digite o valor pago:"))

while valorpago < valortotal:
    print("valor insuficiente, tente novamente!")
    valorpago = int(input("digite o valor pago:"))

valortroco = valorpago - valortotal

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0

print("=== VALORES ===")
print("Valor total: R$", valortotal)
print("Valor pago R$:", valorpago)
print("Valor do troco R$:", valortroco)

while valortroco > 0:
    if valortroco >= 100:
        nota100 += 1
        valortroco -= 100
    elif valortroco >= 50:
        nota50 += 1
        valortroco -= 50
    elif valortroco >= 20:
        nota20 +1
        valortroco -= 20
    elif valortroco >= 10:
        nota10 += 1
        valortroco - 10
    elif valortroco >= 5:
        nota5 += 1
        valortroco -= 5
    else:
        nota2 += 1
        valortroco -= 2
print ("=== TROCO ===")
print ("Notas de 100R$:", nota100)
print ("Notas de 50R$:", nota50)
print ("Notas de 20R$:", nota20)
print ("Notas de 10R$:", nota10)
print ("Notas de 5R$:", nota5)
print ("Notas de 2R$:", nota2)
