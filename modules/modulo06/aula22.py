import json

caminho = "mini_projetos/modulo06/usuario.json"

with open(caminho,"r",encoding="utf-8") as arquivo:
    usuario = json.load(arquivo)

usuario["profissao"] = "Desenvolvedor Python"
    json.dump(
        usuario,
        arquivo,
        indent=4,
        ensure_ascii=False
    )

print("Dados atualizados com sucesso!")
