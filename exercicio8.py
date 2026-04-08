import os 

os.system("cls||clear")

def idade(a, b):
    
    return  a - b
    
ano = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026

tempo = idade(ano_atual, ano)

print(f"Idade: {tempo}")
