class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <0:
            raise ValueError(
                "O depósito não pode ser negativo."
            )

        self.saldo += valor

conta = Conta("Roberto",100)

conta.depositar(50)

print(conta.saldo)