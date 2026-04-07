import os

os.system("cls||clear")

def tabuada(numero):
    for i in range(1,11):
        print(f" {numero} x {i} = {numero * i }")

numero = int(input("Digite um número para tabuada: "))

tabuada(numero)
