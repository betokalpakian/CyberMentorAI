produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 100},
    {"nome": "Teclado", "preco": 250},
    {"nome": "Monitor", "preco": 1200},
]

produtos_caros = [
    produto["nome"]
    for produto in produtos
    if produto["preco"] > 500
]

print(produtos_caros)