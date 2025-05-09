idades = []
soma = 0
idade = None
while idade != 0:
    idade = int(input("Digite a idade:"))
    idades.append(idade)
quantidadeidades = len(idades)
for i in range(quantidadeidades):
    soma += idades[i]

media = soma / (quantidadeidades)
print("A media é:", media)
