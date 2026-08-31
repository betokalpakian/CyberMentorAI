class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError(
                "O depósito deve ser maior que zero."
            )

        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError(
                "O saque deve ser maior que zero."
            )

        if valor > self.saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self.saldo -= valor


conta = Conta("Roberto", 500)

conta.depositar(100)
conta.sacar(200)

print(conta.saldo)