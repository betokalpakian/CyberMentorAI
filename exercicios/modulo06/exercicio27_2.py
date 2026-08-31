class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Roberto",39)
pessoa2 = Pessoa("Ana",30)

print(pessoa1.nome)
print(pessoa2.nome)