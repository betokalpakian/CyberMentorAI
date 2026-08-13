import json

nome = input("Nome: ")
idade = int(input("Idade: "))
profissao = input("Profissão: ")

pessoa = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao
}

dados_json = json.dumps(pessoa, indent=4)

print("\n===== JSON =====")
print(dados_json)