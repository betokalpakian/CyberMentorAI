def excluir_usuario(usuarios,nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            usuarios.remove(usuario)
            return true

    return False