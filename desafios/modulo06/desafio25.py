def obter_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo não pode ficar vazio.")

def obter_idade():
    while True:
        try:
            idade = int(input("Idade."))

            if 0 <= idade <= 120:
                return idade

            print("Digite uma idade entre 0 e 120.")

        except ValueError:
            print("Digite apenas números.")

nome = obter_texto("Nome")
idade = obter_idade()
profissao = obter_texto("Profissão:")
 