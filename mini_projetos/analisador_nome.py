def analisar_nome(nome: str) -> None:
    nome = nome.strip()

    quantidade_letras = len(nome.replace(" ", ""))
    quantidade_espacos = nome.count(" ")
    quantidade_vogais = sum(1 for letra in nome.lower() if letra in "aeiou")

    print("\n===== ANÁLISE DO NOME =====")
    print(f"Nome................: {nome}")
    print(f"Maiúsculas..........: {nome.upper()}")
    print(f"Minúsculas..........: {nome.lower()}")
    print(f"Quantidade de letras: {quantidade_letras}")
    print(f"Primeira letra......: {nome[0]}")
    print(f"Última letra........: {nome[-1]}")
    print(f"Vogais..............: {quantidade_vogais}")
    print(f"Espaços.............: {quantidade_espacos}")


def main():
    nome = input("Digite seu nome completo: ")

    if not nome.strip():
        print("Nome inválido.")
        return

    analisar_nome(nome)


if _name_ == "_main_":
    main()