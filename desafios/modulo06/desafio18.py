nome = input("Nome do produto:")
preco = float(input("Preço:"))
estoque = int(input("Quantidade em estoque:"))

produto = {
    "nome": nome,
    "preco": preco,
    "estoque": estoque
}

print("\n==== Produto ====")
print("Nome:", produto["nome"])
print("Preço:", produto["preco"])
print("Estoque:", produto["estoque"])

novo_estoque = int(input("\nNova quantidade em estoque:"))

produto["estoque"] = novo_estoque

print("\n==== Atualizado ====")
print("Nome:", produto["nome"])
print("Preço:", produto["preco"])
print("Estoque:", produto["estoque"])