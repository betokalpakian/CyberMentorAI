def obter_idade():
    while True:
        try:
            idade = int(input("Idade: "))

            if 0 <= idade <= 120:
                return idade

            print("Digite uma idade entre 0 e 120.")

        except ValueError:
            print("Digite apenas números.")

idade = obter_idade()

print(f"Idade válida: {idade}")