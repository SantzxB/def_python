import os 
from datetime import date   
os.system("cls||clear")


def idade(tempo):
    ano_atual = date.today().year
    return ano_atual - tempo
    
    
ano = int(input("Digite seu ano de nascimento: "))

calcular_idade = idade(ano)

print(f"Idade: {calcular_idade}")
