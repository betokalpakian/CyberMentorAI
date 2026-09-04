class Usuario:
    def __init__(self,nome):
        self.nome = nome

class Cliente(Usuario):
    def __init__(self,nome,email):
        super().__init__(nome)
        self.email = email

cliente = Cliente (
    "Roberto",
    "betoviannna@gmail.com",
)

print(cliente.nome)
print(cliente.email)
