import json 

usuario = {
    "nome": "Ana",
    "idade": 28,
    "profissao": "Designer"
}

caminho = "exercicios/modulo06/usuario.json"

with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(
        usuario, 
        arquivo, 
        indent=4, 
        ensure_ascii=False
    )

usuario["profissao"] = "Desenvolvedor"

with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(
        usuario, 
        arquivo, 
        indent=4, 
        ensure_ascii=False
    )   

print(usuario)