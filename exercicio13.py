import os

os.system("cls||clear")

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
nome_completos = []
sobrenomes = []
idades = []
alturas = []
pesos = []

def imc(peso, altura):
    return peso / (altura ** 2)

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif  18.5 <= imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif  35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    sobrenome = str(input("Digite o sobrenome do usuário: "))
    nome_completo = (f"{nome} {sobrenome}")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    nome_completos.append(nome_completo)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"{i+1}º Usuário:")
    print("Nome:", nomes[i])
    print("Nome completo:", nome_completos[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC: {imc(pesos[i], alturas[i]):.2f}")
    print(f"Classificação do IMC: {classificacao_imc(imc(pesos[i], alturas[i]))}")
    print() 
    
