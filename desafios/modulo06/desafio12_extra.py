nome = []

for i in range(5):
    nome: input("Digite um nome: ")
    nomes.append(nome)

pesquisa = input("\nDigite o nome que deseja procurar:")

if pesquisa in nomes:
    print("Nome encontrado.")
else:
    print("Nome não encontrado.")