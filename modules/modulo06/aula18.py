nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
profissao = input("Digite sua profissão:")

pessoa = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao
}

print("\n==== Cadastro ====")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Profissão:", pessoa["profissao"])