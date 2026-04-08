import os

os.system("cls||clear")


def promocao(a, b):
    return a * b

preco = int(input("Digite o valor do produto que deseja: "))

if preco > 100:
    valor_novo = 1.20

else:
    valor_novo = 1.10

preco_final = promocao(preco, valor_novo)
print(f"Valor à pagar é : {preco_final}")
