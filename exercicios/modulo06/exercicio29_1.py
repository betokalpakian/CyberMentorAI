class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor):
        if not isinstance(valor,(int,float)):
            raise TypeError(
                "O preço deve ser um número."

            )
        
        if valor <0:
            raise ValueError(
                "O preço não pode ser negativo."
            )

        self._preco = valor

produto = Produto("Notebook", 3500)

print(produto.preco)
    
produto.preco = 3800

print(produto.preco)