def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade:"))

        except ValueError:
            print("Erro: digite apenas números.")
            continue

        if idade <= 0 or idade > 120:
            print("Erro: idade deve estar entre 0 e 120.")
            continue

        return idade

idade = obter_idade()

print(f"Idade válida: {idade}")