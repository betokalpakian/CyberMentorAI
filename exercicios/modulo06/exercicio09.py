def analisar_nome(nome: str) -> None:
    nome = nome.strip()

    print(f"Primeira letra : {nome[0]}")
    print(f"Última letra   : {nome[-1]}")
    print(f"Início         : {nome[:3]}")
    print(f"Final          : {nome[-3:]}")
    print(f"Invertido      : {nome[::-1]}")


def main():
    nome = input("Digite seu nome: ")

    if not nome.strip():
        print("Nome inválido.")
        return

    analisar_nome(nome)


if _name_ == "_main_":
    main()