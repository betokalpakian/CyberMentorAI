import json

CAMINHO = "mini_projetos/modulo06/usuario.json"

def carregar_usuario():
    with open(CAMINHO, "r") as arquivo:
        return json.load(arquivo)

def salvar_usuario(usuario):
    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuario, 
            arquivo, 
            indent=4,
            ensure_ascii=False
            )

def main():
    usuario = carregar_usuario()

    print(f"Nome: {usuario['nome']}")
    print(f"Profissão atual: {usuario['profissao']}")

    nova_profissao = input("Digite a nova profissão:").strip()
    
    usuario["profissao"] = nova_profissao
    
    salvar_usuario(usuario)
    
    print("Profissão atualizada com sucesso!")

if __name__ == "__main__":
    main()