precos = [100,250,500,750,1000]

precos_altos = filter(
    lambda preco:preco > 500,
    precos
)

precos_com_desconto = map(
    lambda preco: preco * 0.90,
    precos_altos
)

resultado = list(precos_com_desconto)

print(resultado)