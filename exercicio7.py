def carregar_estudantes():
    try:
        with open("estudantes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            estudantes = {}
            for linha in linhas:
                nome, detalhes = linha.strip().split(": ")
                idade, curso = detalhes.split(" anos, ")
                estudantes[nome] = {"idade": idade, "curso": curso}
            return estudantes
    except FileNotFoundError:
        return {}

# carrega os estudantes do arquivo
estudantes = carregar_estudantes()

# conta quantos estudantes estão matriculados em cada curso
contagem_cursos = {}
for info in estudantes.values():
    curso = info["curso"]
    contagem_cursos[curso] = contagem_cursos.get(curso, 0) + 1

# mostra a contagem de estudantes por curso
print("contagem de estudantes por curso:")
for curso, quantidade in contagem_cursos.items():
    print(f"{curso}: {quantidade} estudante(s)")