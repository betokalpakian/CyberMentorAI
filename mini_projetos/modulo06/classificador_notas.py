notas = []

for i in range(5):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

print("\n===== RELATÓRIO =====")
print("Notas:", notas)
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Notas em ordem:", sorted(notas))
print("Média:", sum(notas) / len(notas))