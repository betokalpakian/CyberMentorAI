usuarios = {
    "usuario1": {
        "nome": "Ana",
        "idade": 30,
        "profissao": "Designer",
        "endereco": {
            "cidade": "Rio de Janeiro",
            "estado": "RJ"
        }
    },
    "usuario2": {
        "nome": "Carlos",
        "idade": 25,
        "profissao": "Programador",
        "endereco": {
            "cidade": "São Paulo",
            "estado": "SP"
        }
    },
    "usuario3": {
        "nome": "Maria",
        "idade": 35,
        "profissao": "Professora",
        "endereco": {
            "cidade": "Belo Horizonte",
            "estado": "MG"
        }
    }
}

for identificador, usuario in usuarios.items():
    print("\n===== USUÁRIO =====")
    print("ID:", identificador)
    print("Nome:", usuario["nome"])
    print("Idade:", usuario["idade"])
    print("Profissão:", usuario["profissao"])
    print("Cidade:", usuario["endereco"]["cidade"])
    print("Estado:", usuario["endereco"]["estado"])