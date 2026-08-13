aluno = {
    "nome": "Carlos",
    "idade": 22,
    "curso": "Python",
    "endereco": {
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "cep": "20000-000"
    }
}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])
print("Cidade:", aluno["endereco"]["cidade"])
print("Estado:", aluno["endereco"]["estado"])
print("CEP:", aluno["endereco"]["cep"])