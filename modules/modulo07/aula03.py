def main():
    numeros = [1,2,3,4,5]

    quadrados = {
        numero ** 2
        for numero in numeros
    }

    print("Quadrados:")
    print(quadrados)

if __name__ == "__main__":
    main()