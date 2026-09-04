class Veículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veículo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Portas: {self.portas}")

carro = Carro(
    "Toyota",
    "Corolla",
    4,
)

carro.mostrar_dados()