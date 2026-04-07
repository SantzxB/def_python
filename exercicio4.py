import os

os.system("cls||clear")

def num(numero):
    if numero > 0 :
            print(f"O número {numero} é positivo")
    else:
            print(f"O número {numero} é negativo")

numero = int(input("Digite um númer (negativo ou positivo): "))
num(numero)
