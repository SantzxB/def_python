import os
import time
os.system("cls||clear")

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_negativos = 0 
quantidade_positivos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
quantidadades_num = 5

num = []
num_pares = []
num_impares = []
# Variáveis para armazenar os números
for i in range(quantidadades_num):
    numero = int(input(f"Digite o {i+1}º número: "))
    num.append(numero)

# Processando cada número
for numero in num:
    if numero % 2 == 0:
        num_pares.append(numero)
        quantidade_pares += 1
        soma_pares += numero

    else:
        num_impares.append(numero)
        quantidade_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
        
    if numero < 0:
        quantidade_negativos += 1

maior_numero = max(num)
menor_numero = min(num)

# Calculando as médias
mediageral = sum(num) / len(num)
soma_geral += numero
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0 
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0  else 0


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidades de números inseridos: {quantidadades_num}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média de números pares: {media_pares} | Média de números impares: {media_impares}")
print(f"Média dos números inseridos: {mediageral}")

tempo = 2
for numero in sorted(num, reverse=True):
    print(numero)
    time.sleep(tempo)
    tempo -= 0.3  
    if tempo <= 0:
        tempo = 0.1
