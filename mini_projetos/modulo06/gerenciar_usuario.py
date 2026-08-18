import json
from pathlib import Path


ARQUIVO = Path("mini_projetos/modulo06/usuario.json")


def carregar_usuario():
    if not ARQUIVO.exists():
        return None

    with ARQUIVO.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuario(usuario):
    with ARQUIVO.open("w", encoding="utf-8") as arquivo:
        json.dump(
            usuario,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def mostrar_usuario(usuario):
    print("\n--- DADOS DO USUÁRIO ---")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")


def alterar_nome(usuario):
    nome = input("Novo nome: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    usuario["nome"] = nome
    print("Nome atualizado!")


def alterar_idade(usuario):
    try:
        idade = int(input("Nova idade: "))

        if idade <= 0:
            print("Idade inválida.")
            return

        usuario["idade"] = idade
        print("Idade atualizada!")

    except ValueError:
        print("Digite uma idade válida.")


def alterar_profissao(usuario):
    profissao = input("Nova profissão: ").strip()

    if not profissao:
        print("Profissão inválida.")
        return

    usuario["profissao"] = profissao
    print("Profissão atualizada!")


def mostrar_menu():
    print("""
================================
      GERENCIADOR DE USUÁRIO
================================

1 - Visualizar usuário
2 - Alterar nome
3 - Alterar idade
4 - Alterar profissão
5 - Salvar
6 - Sair
""")


def main():
    usuario = carregar_usuario()

    if usuario is None:
        print("Arquivo de usuário não encontrado.")
        return

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_usuario(usuario)

        elif opcao == "2":
            alterar_nome(usuario)

        elif opcao == "3":
            alterar_idade(usuario)

        elif opcao == "4":
            alterar_profissao(usuario)

        elif opcao == "5":
            salvar_usuario(usuario)
            print("Dados salvos com sucesso!")

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()