dias_semana = (
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo"
)

print("Primeiro:", dias_semana[0])
print("Último:", dias_semana[-1])
print("Quantidade:", len(dias_semana))

dia = input("Digite um dia:").lower()

if dia in dias_semana:
    print("Dia encontrado.")
else:
    print("Dia não encontrado.")