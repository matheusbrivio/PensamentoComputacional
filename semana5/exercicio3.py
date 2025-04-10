temperatura = float(input("Qual a temperatura?"))
umidade = int(input("Qual a umidade do local?"))
if temperatura > 30 and umidade < 30:
    print("Alerta: risco de desidratação!")
else:
    print ("Condiçoes normais")
