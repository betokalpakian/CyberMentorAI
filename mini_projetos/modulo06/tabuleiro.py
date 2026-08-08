def mostrar_tabuleiro(tabuleiro):
    print("\n===== TABULEIRO =====")

    for linha in tabuleiro:
        print(" | ".join(linha))


def main():
    tabuleiro = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"],
    ]

    mostrar_tabuleiro(tabuleiro)


if __name__ == "__main__":
    main()