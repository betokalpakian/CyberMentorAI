import json

ARQUIVO = "mini_projetos/modulo06/usuario.json"

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    usuario = json.load(arquivo)

usuario["profissao"] = "Desenvolvedor Python"

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(
        usuario,
        arquivo,
        indent=4,
        ensure_ascii=False
    )

print("Dados atualizados com sucesso!")