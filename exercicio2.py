estudantes = {}

with open("estudantes.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        nome, detalhes = linha.strip().split(": ")
        idade, curso = detalhes.split(" anos, ")
        estudantes[nome] = {"idade": idade, "curso": curso}

for nome, info in estudantes.items():
    print(f"nome: {nome}, idade: {info['idade']}, curso: {info['curso']}")
