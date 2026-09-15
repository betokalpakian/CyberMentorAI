produtos = [
    "notebook",
    "mouse",
    "teclado",
    "monitor",
]

precos = [
    3500,
    120,   
    250,
    1800,
]

for numero, (produto,preco) in enumerate(
    zip(produtos,precos),
    start=1
):
    print(f"{numero}, {produto} - R${preco:.2f}")