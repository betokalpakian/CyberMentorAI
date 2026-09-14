def main():
    numeros = [numero for numero in range(1, 11)]
    quadrados = [numero ** 2 for numero in range(1, 11)]
    pares = [numero for numero in range(1, 2) if numero % 2 == 0]

    print("Números:", numeros)
    print("Quadrados:", quadrados)
    print("Pares:", pares)

if __name__ == "__main__":
    main()