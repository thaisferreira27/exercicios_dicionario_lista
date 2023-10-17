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


estudantes = carregar_estudantes()


pesquisar_nome = input("digite o nome do estudante que deseja pesquisar: ")

if pesquisar_nome in estudantes:
    info = estudantes[pesquisar_nome]
    print(f"Nome: {pesquisar_nome}, Idade: {info['idade']}, Curso: {info['curso']}")
else:
    print("estudante não encontrado.")