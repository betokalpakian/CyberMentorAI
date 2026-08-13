produtos = [
    {"nome":"Notebook","estoque":5},
    {"nome": "Mouse","estoque":20},
    {"nome":"Teclado","estoque":8},
    {"nome":"Monitor","estoque":3},
    {"nome":"Webcam","estoque":15}
]

print("Produtos com estoque baixo.")

for produto in produtos:
    if produto["estoque"] < 10:
        print(f"{produto['nome']} - Estoque: {produto['estoque']}")  