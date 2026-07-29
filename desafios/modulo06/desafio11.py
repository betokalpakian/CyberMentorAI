filmes = [
    "Matrix",
    "Interestelar",
    "Gladiador",
    "Avatar",
    "O Poderoso Chefão"
]

filmes.append("Batman")

filmes.remove("Avatar")

for filme in filmes:
    print(filme)

print(f"Total: {len(filmes)}")