numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("\nLista original:", numeros)

print("Crescente:", sorted(numeros))
print("Decrescente:", sorted(numeros, reverse=True))

print("Maior:", max(numeros))
print("Menor:", min(numeros))