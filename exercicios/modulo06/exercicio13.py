produtos = ["Arroz","Feijão","Leite","Café"]

produto = input("Produto para remover:")

if produto in produtos:
    produtos.remove(produto)
    print("Produto removido.")
else:
    print("Produto não encontrado.")

print("\nProdutos")

for item in produtos:
    print(item)