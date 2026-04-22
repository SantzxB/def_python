import os

os.system("cls||clear1")

# Vetores
avioes = [0] * 4
assentos = [0] * 4

# Lista de reservas
reservas = []
LIMITE_RESERVAS = 20


def menu():
    print("\n--- SWEET FLIGHT ---")
    print("1. Cadastrar aviões")
    print("2. Cadastrar assentos")
    print("3. Reservar passagem")
    print("4. Consultar por avião")
    print("5. Consultar por passageiro")
    print("6. Sair")


while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    
    if opcao == 1:
        for i in range(4):
            avioes[i] = int(input(f"Digite o número do avião {i+1}: "))

    
    elif opcao == 2:
        for i in range(4):
            assentos[i] = int(input(f"Assentos disponíveis para avião {avioes[i]}: "))

    #Reserva
    elif opcao == 3:
        if len(reservas) >= LIMITE_RESERVAS:
            print("Limite de reservas atingido!")
            continue

        numero = int(input("Digite o número do avião: "))

        if numero not in avioes:
            print("Este avião não existe!")
            continue

        indice = avioes.index(numero)

        if assentos[indice] <= 0:
            print("Não há assentos disponíveis para este avião!")
            continue

        nome = input("Digite o nome do passageiro: ")

        reservas.append({
            "numero_aviao": numero,
            "nome_passageiro": nome
        })

        assentos[indice] -= 1
        print("Reserva realizada com sucesso!")

    # Opção 4 - Consulta por avião
    elif opcao == 4:
        numero = int(input("Digite o número do avião: "))

        if numero not in avioes:
            print("Este avião não existe!")
            continue

        encontrou = False
        for r in reservas:
            if r["numero_aviao"] == numero:
                print("Passageiro:", r["nome_passageiro"])
                encontrou = True

        if not encontrou:
            print("Não há reservas realizadas para este avião!")

    # Opção 5 - Consulta por passageiro
    elif opcao == 5:
        nome = input("Digite o nome do passageiro: ")

        encontrou = False
        for r in reservas:
            if r["nome_passageiro"].lower() == nome.lower():
                print("Avião:", r["numero_aviao"])
                encontrou = True

        if not encontrou:
            print("Não há reservas realizadas para este passageiro!")

    # Opção 6 - Sair
    elif opcao == 6:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
