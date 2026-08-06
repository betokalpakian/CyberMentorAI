frutas = ["Maçã","Banana","Laranja"]

fruta = input("Digite a fruta que deseja remover:")

if fruta in frutas:
    frutas.remove(fruta)
    print("Fruta removida com sucesso!")
else:
    print("Essa fruta não está na lista.")

print("\nLista atual.")

for item in frutas:
    print(item) 