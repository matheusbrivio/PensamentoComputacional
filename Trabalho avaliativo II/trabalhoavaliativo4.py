def cadastrarparticipante(lista):
    nome = input("Digite o nome do participante:")
    idade = int(input("Digite a idade do participante:"))
    if idade < 18:
        participante = [nome, idade]
        lista.append(participante)
    elif idade >= 18:
        participante = [nome, idade, "18+"]
        lista.append(participante)
    print("O participante:", nome,"foi adicionado com sucesso!")
    
def mostrarparticipante(lista):
    if len(lista) > 0:
        for i in range (len(lista)):
            print ("Participante -", i + 1,":", lista[i])
        return
    print("Voce nao tem participantes adicionados!")

def removerparticipante(lista):
    print(lista)
    nome = input("Digite o nome que deseja remover:")
    for i in range (len(lista)):
        if nome == lista[i][0]:
            lista.pop(i)
            return
    print("O nome nao está na lista!")

def mostrarestatisticas(lista):
    if len(lista) > 0:
        totalparticipantes = len(lista)
        somamediaidade = 0
        for i in range (len(lista)):
            somamediaidade += lista[i][1]
            mediaidade = somamediaidade / len(lista)
        print("A media de idade é:", mediaidade)
        for i in range (len(lista)):
            if i == 0:
                maioridade = lista[i][1]
            elif lista[i][1] > maioridade:
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
