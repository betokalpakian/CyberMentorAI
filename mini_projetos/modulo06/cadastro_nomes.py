def cadastrar_nomes():
    nomes = []

    for i in range(5):
        nome = input(f"Digite o {i + 1}º nome: ").strip()

        if nome:
            nomes.append(nome)

    return nomes


def mostrar_nomes(nomes):
    print("\n===== NOMES CADASTRADOS =====")

    for indice, nome in enumerate(nomes, start=1):
        print(f"{indice}. {nome}")

    print(f"\nTotal de nomes: {len(nomes)}")


def main():
    nomes = cadastrar_nomes()
    mostrar_nomes(nomes)


if __name__ == "__main__":
    main()