class Usuario:
    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Profissão: {self.profissao}")

usuario = Usuario(
    "Roberto",
    39,
    "Desenvolvedor Python",
    )

usuario.mostrar_dados()