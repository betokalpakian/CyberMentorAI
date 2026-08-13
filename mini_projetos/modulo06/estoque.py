def mostrar_produtos(produtos):
    print("\n===== ESTOQUE =====")

    for produto in produtos:
        print(
            f"{produto['nome']} | "
            f"R$ {produto['preco']:.2f} | "
            f"Estoque: {produto['estoque']}"
        )


def mostrar_estoque_baixo(produtos):
    print("\n===== ESTOQUE BAIXO =====")

    for produto in produtos:
        if produto["estoque"] < 10:
            print(
                f"{produto['nome']} - "
                f"{produto['estoque']} unidades"
            )


def main():
    produtos = [
        {"nome": "Notebook", "preco": 3500.00, "estoque": 5},
        {"nome": "Mouse", "preco": 80.00, "estoque": 20},
        {"nome": "Teclado", "preco": 150.00, "estoque": 8},
        {"nome": "Monitor", "preco": 1200.00, "estoque": 3},
    ]

    mostrar_produtos(produtos)
    mostrar_estoque_baixo(produtos)


if __name__ == "__main__":
    main()