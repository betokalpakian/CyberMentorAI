produtos = [
    {"nome":"Notebook", "preco": 3500.00},
    {"nome":"Mouse", "preco": 80.00},
    {"nome":"Teclado", "preco": 150.00},
    {"nome":"Monitor", "preco": 1200.00}
]

produto_mais_caro = max(
    produtos,
    key=lambda produto: produto["preco"]
)

produto_mais_caro = max(
    produtos,
    key=lambda produto: produto["preco"]
)

print(f"Produto mais caro:", produto_mais_caro["nome"])
print(f"Preço: R$ {produto_mais_caro["preco"]:.2f}") 