numeros = [5,12,8,20,15,3]

maiores = list(
    filter(
        lambda numero: numero > 10,
        numeros
    )
)

print(maiores)