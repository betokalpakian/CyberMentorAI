import json


def cadastrar_usuario():
    usuario = {
        "nome": input("Nome: ").strip(),
        "idade": int(input("Idade: ")),
        "profissao": input("Profissão: ").strip(),
    }

    return usuario


def salvar_usuario(usuario):
    with open(
        "mini_projetos/modulo06/usuario.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(usuario, arquivo, indent=4, ensure_ascii=False)


def main():
    usuario = cadastrar_usuario()
    salvar_usuario(usuario)

    print("\nUsuário salvo com sucesso!")


if __name__ == "__main__":
    main()