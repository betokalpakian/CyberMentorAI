def mostrar_cores(cores):
    print("\nLista de cores:")

    for indice, cor in enumerate(cores, start=1):
        print(f"{indice}. {cor}")


def main():
    cores = ["Azul", "Verde", "Vermelho"]

    cores.append("Amarelo")

    mostrar_cores(cores)


if __name__ == "__main__":
    main()