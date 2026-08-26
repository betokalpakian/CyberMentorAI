try:
    idade=int(input("Digite sua idade:"))
    print(f"idade informada: {idade}")

except ValueError:
    print("Digite uma idade válida.")

    