import os

#Função sem parâmetros e sem retorno.
def logo():
    os.system("cls||clear")
    print("=========")
    print("  SENAI  ")
    print("=========")

#Função com parâmetros e com retorno.
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    multiplicacao = a * b
    print(f"Multiplicação: {multiplicacao}")


def dividir(a, b):
    divisao = a / b
    print(f"Divisão: {divisao:.2f}")


logo()
print("= Solicitando Dados=")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)


logo()
print("= Exibindo Dados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
multiplicar(n1, n2)
dividir(n1, n2)
