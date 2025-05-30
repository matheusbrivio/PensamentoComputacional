def cadastrarparticipante(lista1, lista2):
    nome = input("Digite o nome do participante:")
    idade = int(input("Digite a idade do participante:"))
    if idade < 18:
        lista1.append(nome)
        lista2.append(idade)
    elif idade >= 18:
        lista1.append(nome)
        lista2.append(idade, "18+")
    print("O participante:", nome,"foi adicionado com sucesso!")
    
def mostrarparticipante(lista, lista2):
    if len(lista) > 0:
        for i in range (len(lista)):
            print ("Participante -", i + 1,":", lista, lista2)
        return
    print("Voce nao tem participantes adicionados!")

def removerparticipante(lista, lista2):
    print(lista)
    nome = input("Digite o nome que deseja remover:")
    for i in range (len(lista)):
        if nome == lista[i]:
            lista.pop(i)
            lista2.pop(i)
            return
    print("O nome nao está na lista!")

def mostrarestatisticas(lista,lista2):
    if len(lista) > 0:
        totalparticipantes = len(lista, lista2)
        somamediaidade = 0
        for i in range (len(lista2)):
            somamediaidade += lista2[i]
            mediaidade = somamediaidade / len(lista2)
        print("A media de idade é:", mediaidade)
        for i in range (len(lista)):
            if i == 0:
                maioridade = lista2[i]
            elif lista2[i] > maioridade:
                maioridade = lista[i][1]
                pessoamaisvelha = lista[i]
        print("A pessoa mais velha é:", pessoamaisvelha)



def main ():
    print("1 - Cadastrar participante")
    print("2 - mostrar participante")
    print("3 - remover participante")
    print("4 - mostrar estatisticas")
    print("5 - sair")
    opcao = 0
    participante = []
    while opcao != 5:
        opcao = int(input("Digite a opçao:"))
        if opcao == 1:
            cadastrarparticipante(participante)
        elif opcao == 2:
            mostrarparticipante(participante)
        elif opcao == 3:
            removerparticipante(participante)
        elif opcao == 4:
            mostrarestatisticas(participante)
        elif opcao == 5:
            print("Voce saiu...")
        else:
            print("Opcao invalida!, tente novamente.")


main()
