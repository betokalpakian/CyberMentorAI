class Usuario:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not 0 <= valor <= 120:
            raise ValueError("Idade inválida.")

        self._idade = valor

    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, valor):
        if not valor.strip():
            raise ValueError(
                "A profissão não pode ficar vazia."
            )

        self._profissao = valor

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Profissão: {self.profissao}")


def main():
    usuario = Usuario(
        "Roberto",
        39,
        "Desenvolvedor Python",
    )

    usuario.mostrar_dados()

    usuario.idade = 40
    usuario.profissao = "Analista de Segurança"

    print("\nDepois da atualização:")

    usuario.mostrar_dados()


if __name__ == "__main__":
    main()