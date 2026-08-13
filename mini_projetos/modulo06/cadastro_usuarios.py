def mostrar_usuario(usuario):
    print("\n===== USUÁRIO =====")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")

    endereco = usuario["endereco"]

    print(f"Cidade: {endereco['cidade']}")
    print(f"Estado: {endereco['estado']}")


def main():
    usuarios = {
        "usuario1": {
            "nome": "Ana",
            "idade": 30,
            "profissao": "Designer",
            "endereco": {
                "cidade": "Rio de Janeiro",
                "estado": "RJ",
            },
        },
        "usuario2": {
            "nome": "Carlos",
            "idade": 25,
            "profissao": "Programador",
            "endereco": {
                "cidade": "São Paulo",
                "estado": "SP",
            },
        },
    }

    for usuario in usuarios.values():
        mostrar_usuario(usuario)


if __name__ == "__main__":
    main()