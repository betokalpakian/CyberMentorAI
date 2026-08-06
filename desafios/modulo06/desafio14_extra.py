nomes = []

for i in range(10):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

print("\nOrdem alfabética:")
for nome in sorted(nomes):
    print(nome)

print("\nOrdem inversa:")
for nome in sorted(nomes, reverse=True):
    print(nome)