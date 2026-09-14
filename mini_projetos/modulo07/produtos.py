def main():
    produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 100},
        {"nome": "Teclado", "preco": 250},
        {"nome": "Monitor", "preco": 1200},
        {"nome": "Headset", "preco": 350},
    ]

    nomes = [produto["nome"] for produto in produtos]

    precos = [produto["preco"] for produto in produtos]

    produtos_caros = [
        produto["nome"]
        for produto in produtos
        if produto["preco"] > 500
    ]

    produtos_baratos = [
        produto["nome"]
        for produto in produtos
        if produto["preco"] <= 500
    ]

    precos_com_desconto = [
        produto["preco"] * 0.90
        for produto in produtos
    ]

    print("Produtos:")
    print(nomes)

    print("\nPreços:")
    print(precos)

    print("\nProdutos acima de R$ 500:")
    print(produtos_caros)

    print("\nProdutos até R$ 500:")
    print(produtos_baratos)

    print("\nPreços com 10% de desconto:")
    print(precos_com_desconto)


if __name__ == "__main__":
    main()