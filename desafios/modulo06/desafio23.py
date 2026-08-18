import json

ARQUIVO = "mini_projetos/modulo06/usuario.json"


def carregar_usuario():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuario(usuario):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuario,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def main():
    usuario = carregar_usuario()

    print("\n--- USUÁRIO ATUAL ---")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")

    nova_profissao = input("\nNova profissão: ").strip()

    if not nova_profissao:
        print("Erro: profissão inválida.")
        return

    usuario["profissao"] = nova_profissao

    salvar_usuario(usuario)

    print("\n--- USUÁRIO ATUALIZADO ---")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")


if __name__ == "__main__":
    main()