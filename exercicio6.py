def carregar_estudantes():
    try:
        with open("estudantes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            estudantes = {}
            for linha in linhas:
                nome, detalhes = linha.strip().split(": ")
                idade, curso = detalhes.split(" anos, ")
                estudantes[nome] = {"idade": int(idade), "curso": curso}
            return estudantes
    except FileNotFoundError:
        return {}

# carrega estudantes do arquivo
estudantes = carregar_estudantes()

# calcula a idade média dos estudantes
idades = [info["idade"] for info in estudantes.values()]
idade_media = sum(idades) / len(idades)

print(f"a idade média dos estudantes é: {idade_media:.2f} anos")