import json

ARQUIVO = "mini_projetos/modulo06/usuarios.json"


def carregar_usuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Erro: arquivo JSON inválido.")
        return []


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False,
        )


def buscar_usuario(usuarios, nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            return usuario

    return None


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


def cadastrar_usuario(usuarios):
    nome = input("Nome: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    if buscar_usuario(usuarios, nome):
        print("Esse usuário já existe.")
        return

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        return

    profissao = input("Profissão: ").strip()

    if not profissao:
        print("Profissão inválida.")
        return

    usuario = {
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")


def atualizar_profissao(usuarios):
    nome = input("Nome do usuário: ").strip()

    usuario = buscar_usuario(usuarios, nome)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    profissao = input("Nova profissão: ").strip()

    if not profissao:
        print("Profissão inválida.")
        return

    usuario["profissao"] = profissao

    salvar_usuarios(usuarios)

    print("Profissão atualizada!")


def excluir_usuario(usuarios):
    nome = input("Nome do usuário: ").strip()

    usuario = buscar_usuario(usuarios, nome)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    usuarios.remove(usuario)
    salvar_usuarios(usuarios)

    print("Usuário excluído!")


def main():
    usuarios = carregar_usuarios()

    while True:
        print("\n===== SISTEMA DE USUÁRIOS =====")
        print("1 - Listar usuários")
        print("2 - Cadastrar usuário")
        print("3 - Buscar usuário")
        print("4 - Atualizar profissão")
        print("5 - Excluir usuário")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_usuarios(usuarios)

        elif opcao == "2":
            cadastrar_usuario(usuarios)

        elif opcao == "3":
            nome = input("Nome: ").strip()
            usuario = buscar_usuario(usuarios, nome)

            if usuario:
                print(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            atualizar_profissao(usuarios)

        elif opcao == "5":
            excluir_usuario(usuarios)

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()