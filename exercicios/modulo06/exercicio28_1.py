class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def atualizar_preco(self,novo_preco):
        if novo_preco < 0:
            raise ValueError(
                "O preço não pode ser negativo."
            )
        
        self.preco = novo_preco

produto = Produto("Notebook",3500)

produto.atualizar_preco(3800)

print(produto.preco)