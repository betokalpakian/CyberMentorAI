nomes = [
    "Roberto",
    "Ana",
    "Carlos",
    "Ana",
    "ROBERTO",
    "Carlos",
]

nomes_unicos = {
    nome.lower()
    for nome in nomes
}

print(nomes_unicos)