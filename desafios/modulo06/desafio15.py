matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma = 0

for linha in matriz:
    for numero in linha:
        print(numero)
        soma += numero

print(f"Soma: {soma}")