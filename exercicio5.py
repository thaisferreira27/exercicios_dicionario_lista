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


def salvar_estudantes(estudantes):
    with open("estudantes.txt", "w") as arquivo:
        for nome, info in estudantes.items():
            arquivo.write(f"{nome}: {info['idade']} anos, {info['curso']}\n")


def remover_estudante(estudantes, nome):
    if nome in estudantes:
        del estudantes[nome]
        return True
    else:
        return False


estudantes = carregar_estudantes()


remover_nome = input("digite o nome do estudante que deseja remover: ")

if remover_estudante(estudantes, remover_nome):
    salvar_estudantes(estudantes)
    print(f"estudante '{remover_nome}' removido com sucesso.")
else:
    print("estudante não encontrado.")