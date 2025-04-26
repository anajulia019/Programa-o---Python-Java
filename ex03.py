assentos = ["Livre"] * 10

def mostrar_assentos():
    for i, status in enumerate(assentos):
        print(f"Assento {i+1}: {status}")

def reservar_assento():
    mostrar_assentos()
    numero = int(input("Número do assento para reservar: ")) - 1
    if 0 <= numero < len(assentos) and assentos[numero] == "Livre":
        assentos[numero] = "Reservado"
        print("Assento reservado!")
    else:
        print("Assento inválido ou já reservado!")

def cancelar_reserva():
    mostrar_assentos()
    numero = int(input("Número do assento para cancelar reserva: ")) - 1
    if 0 <= numero < len(assentos) and assentos[numero] == "Reservado":
        assentos[numero] = "Livre"
        print("Reserva cancelada!")
    else:
        print("Assento inválido ou não reservado!")

while True:
    print("\n1. Mostrar Assentos\n2. Reservar Assento\n3. Cancelar Reserva\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_assentos()
    elif opcao == "2":
        reservar_assento()
    elif opcao == "3":
        cancelar_reserva()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")