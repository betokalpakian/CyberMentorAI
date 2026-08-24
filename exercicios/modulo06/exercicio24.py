import json

usuarios = [
    {
        "nome":"Roberto",
        "idade":39,
        "profissao":"Desenvolvedor Python",
    },
    {
        "nome":"Ana",
        "idade":30,
        "profissao":"Analista",
    },
]

with open(
    "mini_projetos/modulo06/usuarios.json",
    "w",
    encoding="utf-8",
) as arquivo:
   json.dump(
    usuarios,
    arquivo,
    indent=4,
    ensure_ascii=False,
)

print("Usuários salvos com sucesso!")

