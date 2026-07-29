def mostrar_lista(lista):
    print("\nLISTA DE COMPRAS")
    print("-" * 20)

    for item in lista:
        print(f"- {item}")

    print("-" * 20)
    print(f"Total de itens: {len(lista)}")


def main():
    compras = [
        "Arroz",
        "Feijão",
        "Macarrão",
        "Leite",
        "Café",
    ]

    mostrar_lista(compras)


if __name__ == "__main__":
    main()