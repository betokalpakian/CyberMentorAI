class Usuario:
    def __init__(self, nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

usuarios = [
    Usuario(
        "Roberto",
        39,
        "Desenvolvedor Python",
    ),
    Usuario(
        "Ana",
        30,
        "Analista",
    ),
    Usuario(
        "Carlos",
        28,
        "Analista de Segurança",
    ),
]

for usuario in usuarios:
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"Profissão: {usuario.profissao}")
    print()