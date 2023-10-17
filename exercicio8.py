contatos = {}

def adicionar_contato(nome, telefone):
    contatos[nome] = telefone

def visualizar_contatos():
    for nome, telefone in contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

def atualizar_contato(nome, novo_telefone):
    if nome in contatos:
        contatos[nome] = novo_telefone
        print("contato atualizado com sucesso.")
    else:
        print("contato não encontrado.")

def excluir_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print("contato excluído com sucesso.")
    else:
        print("contato não encontrado.")

# menu principal
while True:
    print("1. adicionar Contato")
    print("2. visualizar Contatos")
    print("3. atualizar Contato")
    print("4. excluir Contato")
    print("5. sair")
    
    escolha = input("escolha uma opção: ")

    if escolha == "1":
        nome = input("digite o nome do contato: ")
        telefone = input("digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif escolha == "2":
        visualizar_contatos()
    elif escolha == "3":
        nome = input("digite o nome do contato que deseja atualizar: ")
        novo_telefone = input("digite o novo telefone: ")
        atualizar_contato(nome, novo_telefone)
    elif escolha == "4":
        nome = input("digite o nome do contato que deseja excluir: ")
        excluir_contato(nome)
    elif escolha == "5":
        break
    else:
        print("opção inválida. escolha uma opção válida.")

# Salvar contatos em um arquivo
with open("contatos.txt", "w") as arquivo:
    for nome, telefone in contatos.items():
        arquivo.write(f"{nome}: {telefone}\n")

print("contatos salvos com sucesso.")