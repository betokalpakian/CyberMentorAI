import json

pessoa = {
    "nome": "Roberto",
    "idade": 39,
    "linguagem": "Python"
}

dados_json = json.dumps(
    pessoa,
    indent=4
)

print(dados_json)