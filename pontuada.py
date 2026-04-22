import os


def limpar_tela():
    os.system("cls||clear")

avioes = [0] * 4
assentos = [0] * 4
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
    limpar_tela()
    menu()
    opcao = int(input("Escolha uma opção: "))

    
    if opcao == 1:
        for i in range(4):
            avioes[i] = int(input(f"Digite o número do avião {i+1}: "))

    
    elif opcao == 2:
        for i in range(4):
            assentos[i] = int(input(f"Assentos do avião {avioes[i]}: "))

    
    elif opcao == 3:
        if len(reservas) >= LIMITE_RESERVAS:
            print("Limite de reservas atingido!")
            continue

        numero = int(input("Número do avião: "))

        if numero not in avioes:
            print("Este avião não existe!")
            continue

        indice = avioes.index(numero)

        if assentos[indice] <= 0:
            print("Não há assentos disponíveis para este avião!")
            continue

        nome = input("Nome do passageiro: ")

        reservas.append({
            "numero_aviao": numero,
            "nome_passageiro": nome
        })

        assentos[indice] -= 1
        print("Reserva realizada com sucesso!")

    
    elif opcao == 4:
        numero = int(input("Número do avião: "))

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

    elif opcao == 5:
        nome = input("Nome do passageiro: ").lower()

        for r in reservas:
            if r["nome_passageiro"].lower() == nome:
                print("Avião:", r["numero_aviao"])
                break
        else:
            print("Não há reservas realizadas para este passageiro!")

    elif opcao == 6:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
