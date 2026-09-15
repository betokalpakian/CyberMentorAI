nomes = [
    "Roberto",
    "Ana",
    "Carlos",
]

cidades = [
    "Rio de Janeiro",
    "São Paulo",
    "Curitiba",
]

for nome, cidade in zip(nomes, cidades):
    print(f"{nome} mora em {cidade}")