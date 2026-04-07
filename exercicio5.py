import os

os.system("cls||clear")

def calcular_media(n1, n2):
    media = n1 + n2 / 2
    return media

def verificar_resultados(media):
    if media >= 7:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado!"
    return resultado

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

media = calcular_media(n1, n2)
resultado = verificar_resultados(media)

print(f"Média: {media}")
print(f"Resultado: {resultado}")
