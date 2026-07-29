def analisar_frase(frase: str) -> None:
    frase = frase.strip()

    if not frase:
        print("Você precisa digitar uma frase.")
        return

    palavras = frase.split()

    quantidade_vogais = sum(1 for letra in frase.lower() if letra in "aeiou")
    quantidade_consoantes = sum(
        1 for letra in frase.lower()
        if letra.isalpha() and letra not in "aeiou"
    )
    quantidade_espacos = frase.count(" ")

    print("\n===== ANÁLISE DA FRASE =====")
    print(f"Frase..................: {frase}")
    print(f"Maiúsculas.............: {frase.upper()}")
    print(f"Minúsculas.............: {frase.lower()}")
    print(f"Caracteres.............: {len(frase)}")
    print(f"Palavras...............: {len(palavras)}")
    print(f"Primeira palavra.......: {palavras[0]}")
    print(f"Última palavra.........: {palavras[-1]}")
    print(f"Frase invertida........: {frase[::-1]}")
    print(f"Quantidade de vogais...: {quantidade_vogais}")
    print(f"Quantidade consoantes..: {quantidade_consoantes}")
    print(f"Quantidade de espaços..: {quantidade_espacos}")


def main():
    frase = input("Digite uma frase: ")
    analisar_frase(frase)


if __name__ == "__main__":
    main()