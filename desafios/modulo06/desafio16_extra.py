países = (
    "Brasil",
    "Argentina",
    "Itália",
    "Japão",
    "Canadá",
)

país = input("Digite um país:")

if país in países:
    print("País encontrado.")
    print("Posição:", países.index(país))
else:
    print("País não encontrado.")