def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))

            if idade < 0:
                print("A idade não pode ser negativa.")
                continue

            return idade

        except ValueError:
            print("Digite apenas números.")

idade = obter_idade()

print("Idade cadastrada: {idade}")