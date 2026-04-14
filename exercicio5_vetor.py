import os

os.system("cls")
vetor = []

def calcular_media(vetor):
    media = sum(vetor) / len(vetor)
    return media

def verificar_media(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado




for i in range(2):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    vetor.append(nota)

media =  calcular_media(vetor)
resultado = verificar_media(media)

print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")
