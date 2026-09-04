class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")


class Cliente(Usuario):
    def __init__(self, nome, email, telefone):
        super().__init__(nome, email)
        self.telefone = telefone

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Telefone: {self.telefone}")


class Administrador(Usuario):
    def __init__(self,nome, email, nivel):
        super().__init__(nome, email)
        self.nivel = nivel

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Nível: {self.nivel}")


def main():
    cliente = Cliente(
        "Roberto",
        "roberto@email.com",
        "21999999999",
    )

    administrador = Administrador(
        "Ana",
        "ana@email.com",
        "Administrador",
    )

    print("=== CLIENTE ===")
    cliente.mostrar_dados()

    print("\n=== ADMINISTRADOR ===")
    administrador.mostrar_dados()


if __name__ == "__main__":
    main()