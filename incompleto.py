import os

os.system("cls||clear")
total_assentos = 20
vetor_aviao = []
vetor_assentos = [4]
numero_avioes = [4]
nome_passageiro = []

def logo_sweet():
    os.system("cls||clear")

    print("              SWEET FLIGHT           ")

logo_sweet()
print(""" Número do Avião
                1
                2
                3
                4

""")

numero_aviao = str(input("Digite o número do avião que deseja embarcar: "))
numero_avioes.append(numero_aviao)
assento = str(input("Digite o número de assentos que deseja reservar:"))
vetor_assentos.append(assento)


match numero_aviao:
    case "1":
        
        print(f"Assentos disponíveis {assentos_disponiveis}")

    case "2":
        print(f"Assentos disponíveis {vetor_assentos - total_assentos}")
    case "3":
        print(f"Assentos disponíveis {vetor_assentos - total_assentos}")
    case "4":
        print(f"Assentos disponíveis {vetor_assentos- total_assentos}")
    case _:
        print("Este Avião não existe!")


