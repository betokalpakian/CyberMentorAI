class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if valor <0:
            raise ValueError(
                "O saldo não pode ser negativo."
            )

        self._saldo = valor

conta = Conta("Roberto",1000)

print(conta.saldo)

conta.saldo = 1500

print(conta.saldo)
    