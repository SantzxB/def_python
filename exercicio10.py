import os

os.system("cls||clear")

vetor= []
quantidade_notas = 3

def nota(a, b, c):
    media =  (a + b + c) / 2
    return media


for i in range (quantidade_notas):
    note = int(input(f"Digite sua {i + 1 }ª nota: "))
    vetor.append(note)

media = sum(vetor) / quantidade_notas

print(f"Média: {media}")
