class Animal:
    def __init__(self, nome):
        self.nome = nome
        
class Cachorro(Animal):
    def latir(self):
        print("Au au!")

cachorro = Cachorro("Rex")

print(cachorro.nome)

cachorro.latir()