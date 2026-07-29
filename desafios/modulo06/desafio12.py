filmes = []

for i in range(5):
    filme = input("Digite um filme:")
    filmes.append(filme)

print("\nLista de filmes.")

for filme in filmes:
    print(filme)

print(f"\nTotal: {len(filmes)}")