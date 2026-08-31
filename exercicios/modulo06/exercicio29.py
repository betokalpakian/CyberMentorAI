class Usuario:
    def __init__(self,nome,idade):
        self.nome = nome
        self._idade = idade

usuario = Usuario("Roberto",39)

print(usuario.nome)
print(usuario._idade)