class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto = Produto(
    "Notebook",
    3500,
)

print(produto.nome)
print(produto.preco)
