nomes = ["Ana","Carlos","João","Maria","Pedro"]

nome = input("Nome:")

if nome in nomes: 
    nomes.remove(nome)
    print("Nome removido.")
else:
    print("Nome não encontrado.")

print("\nLista atual:")

for item in nomes:
    print(item)