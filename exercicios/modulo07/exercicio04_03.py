numeros = [5,10,15,20,25,30]

maiores = filter(
    lambda numero: numero > 10,
    numeros     
)

dobrados = map(
    lambda numero: numero * 2,
    maiores
)

resultado = list(dobrados)

print(resultado)
