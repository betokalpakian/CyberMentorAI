def buscar_usuario(usuarios,nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            return usuario

    return None
    