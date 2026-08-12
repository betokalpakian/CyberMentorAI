def cadastrar_pessoa():
    print("\n===== NOVO CADASTRO =====")

    pessoa = {
        "nome": input("Nome: ").strip(),
        "idade": int(input("Idade: ")),
        "profissao": input("Profissão: ").strip(),
    }

    return pessoa


def mostrar_pessoa(pessoa):
    print("\n===== DADOS =====")

    for chave, valor in pessoa.items():
        print(f"{chave.capitalize()}: {valor}")


def atualizar_pessoa(pessoa):
    print("\n1 - Nome")
    print("2 - Idade")
    print("3 - Profissão")

    opcao = input("O que deseja alterar? ")

    if opcao == "1":
        pessoa["nome"] = input("Novo nome: ").strip()

    elif opcao == "2":
        pessoa["idade"] = int(input("Nova idade: "))

    elif opcao == "3":
        pessoa["profissao"] = input("Nova profissão: ")

    else:
        print("Opção inválida.")


def main():
    pessoa = cadastrar_pessoa()

    mostrar_pessoa(pessoa)

    atualizar_pessoa(pessoa)

    mostrar_pessoa(pessoa)


if __name__ == "__main__":
    main()