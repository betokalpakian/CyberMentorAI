import json

ARQUIVO = "mini_projetos/modulo06/usuarios.json"


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False,
        )


def cadastrar_usuario(usuarios):
    usuario = {
        "nome": input("Nome: ").strip(),
        "idade": int(input("Idade: ")),
        "profissao": input("Profissão: ").strip(),
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")


def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(
            f"{usuario['nome']} | "
            f"{usuario['idade']} anos | "
            f"{usuario['profissao']}"
        )


def main():
    usuarios = carregar_usuarios()

    while True:
        print("\n1 - Listar usuários")
        print("2 - Cadastrar usuário")
        print("3 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar_usuarios(usuarios)

        elif opcao == "2":
            cadastrar_usuario(usuarios)

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()