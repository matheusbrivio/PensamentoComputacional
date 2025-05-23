pendentes = []
concluidas = []

def menu():
    opcao = 0
    while opcao != 6:   
        print("=== MENU ===")
        print("[1] Adicionar nova tarefa")
        print("[2] Listar tarefas")
        print("[3] Concluir tarefa")
        print("[4] Editar tarefa pendente")
        print("[5] Excluir tarefa pendente")
        print("[6] Sair")
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                break
            except ValueError: 
                print("Entrada inválida! Tente um número.")

        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            concluir_tarefa()
        elif opcao == 4:
            editar_tarefa()
        elif opcao == 5:
            excluir_tarefa()
        elif opcao == 6:
            print("Saindo do programa.")

def adicionar_tarefa():
    print("Você selecionou: [1] Adicionar nova tarefa")
    tarefanova = input("Digite uma nova tarefa: ")
    pendentes.append(tarefanova)
    print("Tarefa:", tarefanova, "adicionada com sucesso.")

def listar_tarefas():
    print("Lista de Tarefas: ")
    if len(pendentes) > 0:
        print("Pendentes:")
        i = 1
        for tarefa in pendentes:
            print(i, ". ", tarefa)
            i = i + 1
    else:
        print("Nenhuma tarefa pendente.")

    if len(concluidas) > 0:
        print("Concluídas:")
        i = 1
        for tarefa in concluidas:
            print(i, ". ", tarefa, "Concluída!")
            i = i + 1
    else:
        print("Nenhuma tarefa concluída.")

def concluir_tarefa():
    if len(pendentes) > 0:
        for i in range(len(pendentes)):
            print("Tarefa -", i + 1, pendentes[i])
        try:
            indice = int(input("Digite o número da atividade concluída: "))
            while indice <= 0 or indice > len(pendentes):
                print("Digite um número de um item que esteja na lista!")
                indice = int(input("Digite o número da atividade concluída: "))
            tarefaconcluida = pendentes[indice - 1]
            concluidas.append(pendentes[indice - 1])
            pendentes.pop(indice - 1)
            print("A tarefa:", tarefaconcluida, "foi concluída com sucesso!")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    else:
        print("Você ainda não tem atividades pendentes a ser concluídas!")

def editar_tarefa():
    if len(pendentes) == 0:
        print("Nenhuma tarefa pendente para editar.")
    else:
        i = 1
        for tarefa in pendentes:
            print(i, ". ", tarefa)
            i = i + 1
        try:
            numero = int(input("Digite o número da tarefa que deseja editar: "))
            if numero >= 1 and numero <= len(pendentes):
                novo_texto = input("Digite o novo texto: ")
                if novo_texto.strip():
                    pendentes[numero - 1] = novo_texto
                    print("Tarefa atualizada com sucesso!")
                else:
                    print("Texto da tarefa não pode ser vazio.")
            else:
                print("Número inválido!")
        except:
            print("Entrada inválida! Digite um número.")

def excluir_tarefa():
    if len(pendentes) == 0:
        print("Nenhuma tarefa pendente para excluir.")
    else:
        i = 1
        for tarefa in pendentes:
            print(i, ". ", tarefa)
            i = i + 1
        try:
            numero = int(input("Digite o número da tarefa que deseja excluir: "))
            if numero >= 1 and numero <= len(pendentes):
                pendentes.pop(numero - 1)
                print("Tarefa excluída com sucesso!")
            else:
                print("Número inválido!")
        except:
            print("Entrada inválida! Digite um número.")

menu()
