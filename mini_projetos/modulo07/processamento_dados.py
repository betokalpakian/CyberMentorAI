def main():
    usuarios = [
        {"nome": "Roberto", "idade": 39},
        {"nome": "Ana", "idade": 25},
        {"nome": "Carlos", "idade": 17},
        {"nome": "Maria", "idade": 32},
        {"nome": "João", "idade": 15},
    ]

    maiores_de_idade = filter(
        lambda usuario: usuario["idade"] >= 18,
        usuarios
    )

    nomes = map(
        lambda usuario: usuario["nome"],
        maiores_de_idade
    )

    nomes = list(nomes)

    print("Usuários maiores de idade:")

    for nome in nomes:
        print(f"- {nome}")


if __name__ == "__main__":
    main()