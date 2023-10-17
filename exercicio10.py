import csv

def adicionar_produto(compras, produto, preco):
    compras[produto] = preco

def atualizar_preco(compras, produto, novo_preco):
    if produto in compras:
        compras[produto] = novo_preco
        print(f"preço do produto '{produto}' atualizado para {novo_preco:.2f} reais.")
    else:
        print(f"produto '{produto}' não encontrado.")

def calcular_valor_total(compras):
    valor_total = sum(compras.values())
    return valor_total

def exportar_para_csv(compras, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Produto', 'Preço'])

        for produto, preco in compras.items():
            escritor.writerow([produto, preco])

def main():
    compras = {}

    # menu
    while True:
        print("1. adicionar produto")
        print("2. atualizar produto")
        print("3. calcular valor total")
        print("4. fazer um arquivo csv")
        print("5. parar/sair ")

        escolha = input("escolha uma opção: ")

        if escolha == '1':
            produto = input("digite o nome do produto: ")
            preco = float(input("digite o preço do produto: R$"))
            adicionar_produto(compras, produto, preco)
            print(f"produto '{produto}' adicionado com sucesso.")
        elif escolha == '2':
            produto = input("digite o nome do produto que deseja atualizar: ")
            novo_preco = float(input("digite o novo preço: R$"))
            atualizar_preco(compras, produto, novo_preco)
        elif escolha == '3':
            valor_total = calcular_valor_total(compras)
            print(f"valor total das compras: {valor_total:.2f} reais")
        elif escolha == '4':
            nome_arquivo = input("digite o nome do arquivo CSV para exportar: ")
            nome_arquivo = f"{nome_arquivo}.csv"
            exportar_para_csv(compras, nome_arquivo)
            print(f"dicionário de compras exportado para '{nome_arquivo}'")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()