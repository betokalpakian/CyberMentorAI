def main():
    usuarios = [
        {"nome": "Roberto", "email": "roberto@gmail.com"},
        {"nome": "ANA", "email": "ana@gmail.com"},
        {"nome": "Carlos", "email": "carlos@outlook.com"},
        {"nome": "ana", "email": "ana@gmail.com"},
        {"nome": "ROBERTO", "email": "roberto@gmail.com"},
    ]

    nomes_unicos = {
        usuario["nome"].lower()
        for usuario in usuarios
    }

    emails_unicos = {
        usuario["email"].lower()
        for usuario in usuarios
    }

    dominios = {
        email.split("@")[1]
        for email in emails_unicos
    }

    print("Nomes únicos:")
    for nome in sorted(nomes_unicos):
        print(f"- {nome}")

    print("\nE-mails únicos:")
    for email in sorted(emails_unicos):
        print(f"- {email}")

    print("\nDomínios encontrados:")
    for dominio in sorted(dominios):
        print(f"- {dominio}")


if __name__ == "__main__":
    main()