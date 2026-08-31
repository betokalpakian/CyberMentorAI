class Usuario:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

usuario = Usuario("Roberto", 39)

usuario.mostrar_dados()