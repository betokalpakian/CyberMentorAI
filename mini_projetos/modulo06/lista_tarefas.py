[15:33, 29/07/2026] Roberto Kalpakian: tarefas = [
    "Estudar Python",
    "Treinar Git",
    "Fazer exercícios"
]

tarefas.remove("Treinar Git")

for numero, tarefa in enumerate(tarefas, start=1):
    print(f"{numero}. {tarefa}")
[15:34, 29/07/2026] Roberto Kalpakian: def mostrar_tarefas(tarefas):
    print("\n===== MINHAS TAREFAS =====")

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero}. {tarefa}")

    print(f"\nTotal de tarefas: {len(tarefas)}")


def main():
    tarefas = [
        "Estudar Python",
        "Fazer exercícios",
        "Atualizar GitHub",
        "Ler documentação",
    ]

    mostrar_tarefas(tarefas)


if __name__ == "__main__":
    main()