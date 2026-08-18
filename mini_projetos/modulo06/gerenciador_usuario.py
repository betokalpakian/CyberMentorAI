import json

CAMINHO = "mini_projetos/modulo06/usuario.json"

def carregar_usuario():
    with open(CAMINHO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_usuario(usuario):
    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuario, 
            arquivo, 
            indent=4,
            ensure_ascii=False
       )

def exibir_usuario(usuario):
    print("\n====USUÁRIO====")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")

def main():
    usuario = carregar_usuario()

    exibir_usuario(usuario)

    print("\nQual informação deseja alterar?")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Profissão")
    print("4 - Cancelar")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        usuario["nome"] = input("Novo nome: ").strip()

    elif opcao == "2": 
        usuario["idade"] = int(input("Nova idade:"))

    elif opcao == "3":
        usuario["profissao"] = input("Nova profissão:").strip()
    
    elif opcao =="4":
        print("Operação cancelada.")
        return

    else: 
        print("Operação inválida.")
        return

    salvar_usuario(usuario)

    print("\nUsuário atualizado com sucesso!")
    exibir_usuario(usuario)

if __name__=="__main__":
    main()