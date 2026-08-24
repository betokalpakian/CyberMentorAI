import json

ARQUIVO = "mini_projetos/modulo06/usuarios.json"

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    usuarios=json.load(arquivo)

for usuario in usuarios:
    print(usuario["nome"])