import json
import os

arquivo = "tarefas.json"

if os.path.exists(arquivo):
    with open(arquivo, "r") as f:
        tarefas = json.load(f)
else:
    tarefas = []

def salvar():
    with open(arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (YYYY-MM-DD): ")
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar()
    print("Tarefa adicionada!")

def listar_tarefas():
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x["prazo"])
    for i, tarefa in enumerate(tarefas_ordenadas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - {status}")

def marcar_concluida():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar()
        print("Tarefa marcada como concluída!")

while True:
    print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Marcar como Concluída\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")