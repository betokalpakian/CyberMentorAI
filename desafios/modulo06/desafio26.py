usuarios = [
    {
        "nome":"Roberto",
        "idade":39,
        "profissao":"Desenvolvedor Python",
    },
    {
        "nome":"Ana",
        "idade":30,
        "profissao":"Analista",
    },
]

def buscar_usuario(usuarios,nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            return usuario

    return None

def atualizar_profissao(usuario,profissao):
    usuario["profissao"] = profissao

def excluir_usuario(usuarios,nome):
    usuario = buscar_usuario(usuarios, nome)

    if usuario is None:
        return False

    usuarios.remove(usuario)
    return True

usuario = buscar_usuario(usuarios, "Roberto")

if usuario:
    atualizar_profissao(usuario,"Analista de Segurança")
    print("Usuário atualizado!")

if excluir_usuario(usuarios,"Ana"):
    print("Ana foi excluída.")

print("\nUsuários.")
for usuario in usuarios:
    print(usuario)

        