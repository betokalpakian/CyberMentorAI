configuracoes = (
    "Python",
    "Git",
    "GitHub",
    "Vs Code"
)

print("==== AMBIENTE DE DESENVOLVIMENTO ====")

for numero, ferramenta in enumerate(configuracoes,
start=1):
    print(f"{numero} - {ferramenta}")

print(f"\nTotal de ferramentas: {len(configuracoes)}")