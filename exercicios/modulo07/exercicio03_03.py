emails = [
    "ana@gmail.com",
    "joao@gmail.com",
    "maria@outlook.com",
    "carlos@gmail.com",
    "maria@outlook.com",
]

dominios = {
    email.split("@")[1]
    for email in emails
}

print(dominios)