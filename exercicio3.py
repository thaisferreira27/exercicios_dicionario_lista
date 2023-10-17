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


estudantes = carregar_estudantes()


nome_alterar = input("digite o nome do estudante que deseja atualizar: ")

if nome_alterar in estudantes:
    nova_idade = input("digite a nova idade do estudante: ")
    novo_curso = input("digite o novo curso do estudante: ")

    # Atualizar informações do estudante
    estudantes[nome_alterar]["idade"] = nova_idade
    estudantes[nome_alterar]["curso"] = novo_curso


    salvar_estudantes(estudantes)
    print("as informações do estudante foram atualizadas com sucesso.")
else:
    print("o estudante não foi encontrado.")