def main():
    nomes = [
        "Roberto",
        "Ana",
        "Carlos",
        "Maria",
        "João",
    ]

    idades = [
        39,
        25,
        17,
        32,
        15,
    ]

    cidades = [
        "Rio de Janeiro",
        "São Paulo",
        "Curitiba",
        "Belo Horizonte",
        "Salvador",
    ]

    print("=== RELATÓRIO DE USUÁRIOS ===")

    for numero, (nome, idade, cidade) in enumerate(
        zip(nomes, idades, cidades),
        start=1
    ):
        status = "Maior de idade" if idade >= 18 else "Menor de idade"

        print(
            f"{numero}. {nome} | "
            f"{idade} anos | "
            f"{cidade} | "
            f"{status}"
        )


if __name__ == "__main__":
    main()