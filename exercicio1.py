estudantes = {}

nome = input("digite o nome do estudante: ")
idade = input("digite a idade do estudante: ")
curso = input("digite o curso do estudante: ")

estudantes[nome] = {"idade": idade, "curso": curso}

with open("estudantes.txt", "w") as arquivo:
    for nome, info in estudantes.items():
        arquivo.write(f"{nome}: {info['idade']} anos, {info['curso']}\n")