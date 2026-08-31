class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self,valor):
        if not isinstance(valor,(int,float)):
            raise TypeError(
                "O salário não pode ser negativo."
            )

        self._salario = valor

funcionario = Funcionario(
    "Roberto",
    5000,
)

print(funcionario.salario)

funcionario.salario = 5500

print(funcionario.salario)

