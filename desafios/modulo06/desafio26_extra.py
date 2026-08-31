usuarios = [
    {
        "nome": "Roberto",
        "idade": 39,
        "profissao": "Desenvolvedor Python",
    },
    {
        "nome": "Ana",
        "idade": 30,
        "profissao": "Analista",
    },
]


def buscar_usuario(usuarios, nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            return usuario

    return None


def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(
            f"{usuario['nome']} | "
            f"{usuario['idade']} anos | "
            f"{usuario['profissao']}"
        )


def atualizar_profissao(usuario):
    profissao = input("Nova profissão: ").strip()

    if not profissao:
        print("Profissão inválida.")
        return

    usuario["profissao"] = profissao
    print("Usuário atualizado!")


def excluir_usuario(usuarios, nome):
    usuario = buscar_usuario(usuarios, nome)

    if usuario is None:
        return False

    usuarios.remove(usuario)
    return True


while True:
    print("\n1 - Buscar")
    print("2 - Atualizar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        nome = input("Nome: ").strip()
        usuario = buscar_usuario(usuarios, nome)

        if usuario:
            print(usuario)
        else:
            print("Usuário não encontrado.")

    elif opcao == "2":
        nome = input("Nome: ").strip()
        usuario = buscar_usuario(usuarios, nome)

        if usuario:
            atualizar_profissao(usuario)
        else:
            print("Usuário não encontrado.")

    elif opcao == "3":
        nome = input("Nome: ").strip()

        if excluir_usuario(usuarios, nome):
            print("Usuário excluído.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "4":
        listar_usuarios(usuarios)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")