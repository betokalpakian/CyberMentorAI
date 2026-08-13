import json

pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "Progrmador"
}

dados_json = json.dumps(pessoa, indent=4)

print(dados_json)