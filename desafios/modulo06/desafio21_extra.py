import json

dados_json = '{"nome": "Ana", "idade": 30}'

pessoa = json.loads(dados_json)

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])