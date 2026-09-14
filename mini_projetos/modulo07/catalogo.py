def main():
    produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 120},
        {"nome": "Teclado", "preco": 250},
        {"nome": "Monitor", "preco": 1800},
        {"nome": "SSD", "preco": 650},
    ]

    catalogo = {
        produto["nome"]: produto["preco"]
        for produto in produtos
    }

    produtos_caros = {
        nome: preco
        for nome, preco in catalogo.items()
        if preco > 500
    }

    print("Catálogo completo:")

    for nome, preco in catalogo.items():
        print(f"{nome}: R$ {preco:.2f}")

    print("\nProdutos acima de R$ 500:")

    for nome, preco in produtos_caros.items():
        print(f"{nome}: R$ {preco:.2f}")


if __name__ == "__main__":
    main()