def mostra_produto(produto):
    print("\n==== Produto ====")

    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

def main():
    produto = {
        "nome": "Notebook",
        "preco": 3500.00,
        "estoque": 10
    }

    mostra_produto(produto)

if __name__ == "__main__":
    main()