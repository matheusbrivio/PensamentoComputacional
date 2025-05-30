def cadastrarparticipante(lista, lista2):
    nome = input("Digite o nome do participante:")
    while True:
        try:
            idade = int(input("Digite a idade do participante:"))
            if idade < 0:
                print("Tente uma idade maior que 0!")
            else:
                break
        except ValueError:
            print("Tente um numero!")
    lista.append(nome)
    lista2.append(idade)

        
    print("O participante:", nome,"foi adicionado com sucesso!")
    
def mostrarparticipante(lista, lista2):
    if len(lista) > 0:
        for i in range (len(lista)):
            if lista2[i] >= 18:
                print ("Participante maior de idade -", i + 1,":", lista[i], lista2[i])
            else:
                print ("Participante -", i + 1,":", lista[i], lista2[i])
        return
    print("Voce nao tem participantes adicionados!")

def removerparticipante(lista, lista2):
    print(lista)
    nome = input("Digite o nome que deseja remover:")
    for i in range (len(lista)):
        if nome == lista[i]:
            lista.pop(i)
            lista2.pop(i)
            print("O participante:", nome, "foi removido com sucesso!")
            return
    print("O nome nao está na lista!")

def mostrarestatisticas(lista,lista2):
    if len(lista) > 0:
        totalparticipantes = len(lista)
        print("O total de participantes é:", totalparticipantes)
        somamediaidade = 0
        for i in range (len(lista2)):
            somamediaidade += int(lista2[i])
        mediaidade = somamediaidade / len(lista2)
        print("A media de idade é:", mediaidade)
        maioridade = lista2[0]
        pessoamaisvelha = lista[0]
        for i in range (len(lista)):
            if lista2[i] > maioridade:
                maioridade = lista2[i]
                pessoamaisvelha = lista[i]
        print("A pessoa mais velha é:", pessoamaisvelha, "com", maioridade, "anos.")



def main ():
    opcao = 0
    nome = []
    idade = []
    while opcao != 5:
        print("1 - Cadastrar participante")
        print("2 - mostrar participante")
        print("3 - remover participante")
        print("4 - mostrar estatisticas")
        print("5 - sair")
        while True:
            try:
                opcao = int(input("Digite a opçao:"))
                break
            except ValueError:
                print("Insira uma opção valida!")
        if opcao == 1:
            cadastrarparticipante(nome, idade)
        elif opcao == 2:
            mostrarparticipante(nome, idade)
        elif opcao == 3:
            removerparticipante(nome, idade)
        elif opcao == 4:
            mostrarestatisticas(nome, idade)
        elif opcao == 5:
            print("Voce saiu...")
        else:
            print("Opcao invalida!, tente novamente.")


main()
