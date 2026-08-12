produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 10
}

print("Produto:", produto["nome"])
print("Preço:", produto["preco"])
print("Estoque:", produto["estoque"])

produto["preco"] = 3299.00
produto["estoque"] = 1

print("nDados atualizados:")
print("Produto:", produto["nome"])
print("Preço:", produto["preco"])
print("Estoque:", produto["estoque"])