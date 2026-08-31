class Funcionario:
    def __init__(self,nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

funcionario = Funcionario(
    "Roberto",
    "Desenvolvedor Python",
    5000,
)

print(funcionario.nome)
print(funcionario.cargo)
print(funcionario.salario)