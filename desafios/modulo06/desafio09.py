def analisar_frase(frase: str) -> None:
    frase = frase.strip()

    if not frase:
        print("Você precisa digitar uma frase.")
        return

    palavras = frase.split()

    print("\n===== ANÁLISE DA FRASE =====")
    print(f"Primeira palavra.......: {palavras[0]}")
    print(f"Última palavra.........: {palavras[-1]}")
    print(f"Frase invertida........: {frase[::-1]}")
    print(f"Quantidade caracteres..: {len(frase)}")
    print(f"Quantidade palavras....: {len(palavras)}")


def main():
    frase = input("Digite uma frase: ")
    analisar_frase(frase)


if _name_ == "_main_":
    main()