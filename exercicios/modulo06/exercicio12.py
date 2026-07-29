cidades = []

for i in range(5):
    cidade = input("Digite o nome de uma cidade: ")
    cidades.append(cidade)

print("Cidades cadastradas:")

for cidade in cidades:
    print(cidade)