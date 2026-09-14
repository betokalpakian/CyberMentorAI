produtos = {
    "Notebook": 3500,
    "Mouse": 120,
    "Monitor": 1800,
    "Teclado": 250,
}

promocoes = {
    nome: preco * 0.90
    for nome, preco in produtos.items()
    if preco > 500
}

print(promocoes)