try:
    numero = int(input("Digite um número: "))
    print(f"Número: {numero}")

except ValueError:
    print("Digite um número válido.")