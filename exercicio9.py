import os

os.system("cls||clear")

list = []

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def multiplicar(a,b):
    multiplicacao = a * b
    print(f"Multiplicação: {multiplicacao}")
    return a * b

def dividir(a,b):
    divisao = a / b
    print(f"Divisão: {divisao:.2f}")

for i in range (2):
    numb = int(input(f"Digite o {i + 1}º número que deseja: "))
    list.append(numb)

soma = somar(list[0], list [1])
subtracao = subtrair(list[0], list[1])



print("= Exibindo Dados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
multiplicar(list[0], list[1])
dividir(list[0], list[1])
