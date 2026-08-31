class Usuario:
    def __init__(self, nome, idade, profissao):
        if not nome.strip():
            raise ValueError(
                "O nome não pode ficar vazio."
            )

        if not 0 <= idade <= 120:
            raise ValueError(
                "A idade deve estar entre 0 e 120."
            )

        if not profissao.strip():
            raise ValueError(
                "A profissão não pode ficar vazia."
            )

        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def atualizar_idade(self, nova_idade):
        if not 0 <= nova_idade <= 120:
            raise ValueError(
                "A idade deve estar entre 0 e 120."
            )

        self.idade = nova_idade

    def atualizar_profissao(self, nova_profissao):
        if not nova_profissao.strip():
            raise ValueError(
                "A profissão não pode ficar vazia."
            )

        self.profissao = nova_profissao

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

    usuario.atualizar_idade(40)
    usuario.atualizar_profissao(
        "Analista de Segurança"
    )

    usuario.mostrar_dados()


if __name__ == "__main__":
    main()