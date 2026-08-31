class Usuario:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Profissão: {self.profissao}")

    def atualizar_profissao(self, nova_profissao):
        if not nova_profissao:
            print("Profissão inválida.")
            return

        self.profissao = nova_profissao
        print("Profissão atualizada!")


def main():
    usuario = Usuario(
        "Roberto",
        39,
        "Desenvolvedor Python",
    )

    usuario.mostrar_dados()

    print("\nAtualizando profissão...")

    usuario.atualizar_profissao(
        "Analista de Segurança"
    )

    print()
    usuario.mostrar_dados()


if __name__ == "__main__":
    main()