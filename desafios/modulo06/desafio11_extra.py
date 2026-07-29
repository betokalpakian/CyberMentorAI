tarefas = [
    "Estudar Python",
    "Treinar Git",
    "Fazer exercícios"
]

tarefas.remove("Treinar Git")

for numero, tarefa in enumerate(tarefas, start=1):
    print(f"{numero}. {tarefa}")