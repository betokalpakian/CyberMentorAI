pessoa = {
    "nome": input("Nome:"),
    "idade": int(input("Idade:")),
    "profissao": input("Profissão:")
}

print("\n==== CADASTRO ====")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("\n1 - Alterar nome")
print("2 - Alterar idade")
print("3 - Alterar profissão")

opcao = input("Escolha:")

if opcao == "1":
    pessoa["nome"] = input("Novo nome:")

elif opcao == "2":
    pessoa["idade"] = int(input("Nova idade:"))

elif opcao == "3":
    pessoa["profissao"] = input("Nova profissão:")

else: 
    print("Opção inválida!")

print("\n==== CADASTRO ATUALIZADO  ====")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")