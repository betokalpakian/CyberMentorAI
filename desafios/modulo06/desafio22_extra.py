import json

CAMINHO = "mini_projetos/modulo06/usuario.json"

def carregar_usuario():
    with open(CAMINHO, "r",encoding="utf-8") as arquivo: 
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

    print("\n====CADASTRO====")
    print("1 - Alterar nome")
    print("2 - Alterar idade")
    print("3 - Alterar profissão")
    print("4 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        usuario["nome"] = input("Digite o novo nome: ").strip()

    elif opcao == "2":
        usuario["idade"] = int(input("Nova idade: "))

    elif opcao == "3":
        usuario["profissao"] = input("Nova profissão:").strip()

    elif opcao == "4":
        print("Programa encerrado.")
        return 

    salvar_usuario(usuario)

    print("Dados atualizados com sucesso!")

if __name__ == "__main__":
    main()