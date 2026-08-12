nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")

pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print("\n==== Cadastro ====")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])