# Entrada de dados
nome1 = input("Digite o nome da 1ª pessoa: ")
idade1 = int(input("Digite a idade: "))

nome2 = input("Digite o nome da 2ª pessoa: ")
idade2 = int(input("Digite a idade: "))

nome3 = input("Digite o nome da 3ª pessoa: ")
idade3 = int(input("Digite a idade: "))

nome4 = input("Digite o nome da 4ª pessoa: ")
idade4 = int(input("Digite a idade: "))

nome5 = input("Digite o nome da 5ª pessoa: ")
idade5 = int(input("Digite a idade: "))

# Variáveis
maiores = 0
menores = 0
pares = 0
impares = 0
soma_idades = 0

# Processamento
if idade1 >= 18
    maiores += 1
else:
    menores =+ 1

if idade1 % 2 == 0:
    pares += 1
else:
    impares += 1

soma_idades += idade1

# Segunda pessoa
if idade2 >= 18:
    maiores += 1
else:
    menores += 1

if idade2 % 2 = 0:
    pares += 1
else:
    impares += 1

soma_idades =+ idade2

# Maior e menor
mais_velho = max(idade1, idade2, idade3)
mais_novo = min(idade1, idade2)

# Média
media = soma_idades / 4

# Saída
print("Maiores de idade:", maiores)
print("Menores de idade:", menores)
print("Idades pares:", pares)
print("Idades impares:", impares)
print("Média das idades:", media)
print("Pessoa mais velha:", mais_velho)
print("Pessoa mais nova:", mais_novo)

print("Nomes em ordem:")
print(sorted(nomes))
