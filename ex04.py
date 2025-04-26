usuarios = {
    "admin": {"senha": "1234", "saldo": 0, "transacoes": []}
}

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        print("Login bem-sucedido!")
        menu_banco(usuario)
    else:
        print("Usuário ou senha incorretos!")

def menu_banco(usuario):
    while True:
        print("\n1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: "))
            usuarios[usuario]["saldo"] += valor
            usuarios[usuario]["transacoes"].append(f"Depósito de R${valor:.2f}")
        elif opcao == "2":
            valor = float(input("Valor do saque: "))
            if valor <= usuarios[usuario]["saldo"]:
                usuarios[usuario]["saldo"] -= valor
                usuarios[usuario]["transacoes"].append(f"Saque de R${valor:.2f}")
            else:
                print("Saldo insuficiente!")
        elif opcao == "3":
            print(f"Saldo: R${usuarios[usuario]['saldo']:.2f}")
            print("Transações:")
            for t in usuarios[usuario]["transacoes"]:
                print(t)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

while True:
    print("\n--- Sistema Bancário ---")
    login()