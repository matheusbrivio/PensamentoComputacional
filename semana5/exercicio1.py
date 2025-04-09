nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))
media = (nota1 + nota2) / 2
if media >= 7 and media <= 10:
    print ("Aprovado!")
elif media >= 0 and media < 7:
    print("Reprovado!")
else:
    print("Numero invalido")
