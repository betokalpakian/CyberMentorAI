nome = input("Digite seu nome completo: ")strip()

print(f"Nome:{nome}")
print(F"Caracteres:{len(nome)}")
print(f"Palavras:{len(nome.split())}")
print(f"Primeira letra do nome:{nome[0]}")
print(f"Última letra do nome:{nome[-1]}")
