def listar(tarefas):
    print("\n===== TAREFAS =====")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def main():
    tarefas = []

    while True:
        print("\n1 - Adicionar")
        print("2 - Remover")
        print("3 - Listar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            tarefas.append(input("Nova tarefa: ").strip())

        elif opcao == "2":
            tarefa = input("Qual tarefa deseja remover? ").strip()

            if tarefa in tarefas:
                tarefas.remove(tarefa)
                print("Tarefa removida.")
            else:
                print("Tarefa não encontrada.")

        elif opcao == "3":
            listar(tarefas)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()