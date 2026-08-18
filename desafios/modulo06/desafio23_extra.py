import json
from pathlib import Path


ARQUIVO = Path("mini_projetos/modulo06/usuario.json")


def carregar_usuario():
    if not ARQUIVO.exists():
        print("Arquivo não encontrado.")
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


def main():
    usuario = carregar_usuario()

    if usuario is None:
        return

    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")

    nova_profissao = input("\nNova profissão: ").strip()

    if not nova_profissao:
        print("Profissão inválida.")
        return

    usuario["profissao"] = nova_profissao

    salvar_usuario(usuario)

    print("Usuário atualizado com sucesso!")


if __name__ == "__main__":
    main()