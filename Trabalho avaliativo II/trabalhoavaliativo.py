pendentes = []
concluidas = []
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
            opcao = int(input("Escolha uma opção:"))
            break
        except ValueError: 
            print("Entrada invalida! tente um numero.")
    
    if opcao == 1:
        print("Voce selecionou: [1] Adicionar nova tarefa")
        tarefanova = input("Digite uma nova tarefa:")
        if tarefanova in pendentes:
            resposta = input("Essa tarefa ja está na lista, deseja adicionar mesmo assim?:").upper()
            if resposta == "SIM":
                    pendentes.append(tarefanova)
                    print("Tarefa:", tarefanova, "adicionada com sucesso.")
            else:
                print("A tarefa nao será adicionada!")
        else:
            print("Tarefa:", tarefanova, "adicionada com sucesso.")
            pendentes.append(tarefanova)
    elif opcao == 2:
        print("Voce selecionou: [2] Listar tarefas")
        if len(pendentes) > 0:
            print("As tarefas pendentes são:")
            for i in range (len(pendentes)):
                print("Tarefa", i + 1,pendentes[i], "pendente!")
        else:
            print("Voce não tem tarefas pendentes.")
        if len(concluidas) > 0:
            print("As tarefas concluidas são:")
            for i in range (len(concluidas)):
                print("Tarefa", i + 1,concluidas[i], "concluida!")
        else:
            print("Voce não tem tarefas concluidas.")
    elif opcao == 3:
        if len(pendentes) > 0:
            for i in range (len(pendentes)):
                print("Tarefa", i + 1,pendentes[i])
            indice = int(input("Digite o numero da atividade concluida:"))
            while indice <= 0 or indice > len(pendentes):
                print("Digite um numero de um item que esteja na lista!")
                indice = int(input("Digite o numero da atividade concluida:"))
            tarefaconcluida = pendentes[indice - 1]
            concluidas.append(pendentes[indice - 1])
            pendentes.pop(indice - 1)
            print("A tarefa:", tarefaconcluida, "foi concluida com sucesso!")
        else:
            print("Voce ainda nao tem atividades pendentes a ser concluidas!")
    
    elif opcao == 4:
        if len(pendentes) > 0:
            for i in range (len(pendentes)):
                print("Tarefa", i + 1,pendentes[i])
            indice = int(input("Qual tarefa deseja alterar?:"))
            while indice <= 0 or indice > len(pendentes):
                print("Digite um numero de um item que esteja na lista!")
                indice = int(input("Qual tarefa deseja editar?:"))
            tarefaantiga = pendentes[indice - 1]
            tarefanova = input("Digite a tarefa nova para ser editada:")
            pendentes[indice - 1] = tarefanova
            print("Tarefa:", tarefaantiga, "editada para:", tarefanova, "com sucesso!")

    elif opcao == 5:
        if len(pendentes) > 0:
            for i in range (len(pendentes)):
                print("Tarefa", i + 1,pendentes[i])
            indice = int(input("Qual tarefa deseja excluir?:"))
            while indice <= 0 or indice > len(pendentes):
                print("Digite um numero de um item que esteja na lista!")
                indice = int(input("Qual tarefa deseja excluir?:"))
            tarefaexcluida = pendentes[indice - 1]
            pendentes.pop(indice - 1)
            print("A tarefa:", tarefaexcluida, "foi excluida com sucesso!")
    elif opcao == 6:
        print("Voce saiu...")

    
