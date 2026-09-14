def main():
    numeros = [1,2,3,4,5]

    quadrados = {
        numero: numero ** 2 
        for numero in numeros
    }

    print("Dicionário de quadrados:")
    print(quadrados)
    
    numeros = [1,2,3,4,5,6]

    pares = {
        numero: numero **2 
        for numero in numeros 
        if numero % 2 == 0
    }

    print("\nDicionário números pares:")
    print(pares)

if __name__ == "__main__":
    main()