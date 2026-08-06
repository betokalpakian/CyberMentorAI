tarefas = []

while True:
    print("\n1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Nova tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        tarefa = input("Tarefa para remover: ")

        if tarefa in tarefas:
            tarefas.remove(tarefa)
        else:
            print("Tarefa não encontrada.")

    elif opcao == "3":
        print("\nLista de tarefas:")

        for tarefa in tarefas:
            print("-", tarefa)

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")