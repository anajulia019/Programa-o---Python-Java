import json
import os

arquivo = "contatos.json"

if os.path.exists(arquivo):
    with open(arquivo, "r") as f:
        contatos = json.load(f)
else:
    contatos = []

def salvar():
    with open(arquivo, "w") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar()
    print("Contato adicionado!")

def buscar_contato():
    nome = input("Nome para buscar: ")
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            return
    print("Contato não encontrado.")

while True:
    print("\n1. Adicionar Contato\n2. Buscar Contato\n3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")