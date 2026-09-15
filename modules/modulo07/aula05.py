def main():
    nomes = [
        "Roberto",
        "Ana",
        "Carlos",
        "Maria",
    ]

    idades = [
        39,
        25,
        32,
        28,
    ]

    print("Lista de usuários:")

    for numero, (nome,idade) in enumerate(
        zip(nomes,idades),
        start=1
    ):
        print(f"{numero} - {nome} - {idade} anos")

if __name__ == "__main__":
    main()