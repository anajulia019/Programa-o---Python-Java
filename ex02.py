import json
import os

arquivo = "estoque.json"

if os.path.exists(arquivo):
    with open(arquivo, "r") as f:
        estoque = json.load(f)
else:
    estoque = []

def salvar():
    with open(arquivo, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar()
    print("Produto adicionado!")

def listar_produtos():
    total = 0
    for produto in estoque:
        print(f"{produto['nome']} - {produto['quantidade']} unidades - R${produto['preco']:.2f} cada")
        total += produto['quantidade'] * produto['preco']
    print(f"Valor total do estoque: R${total:.2f}")

while True:
    print("\n1. Adicionar Produto\n2. Listar Produtos\n3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")