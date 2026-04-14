import os

os.system("cls||clear")

def imc (peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso - consulte um médico para avaliação"
    
    elif 18.5 <= imc < 25:
        return "Peso normal - mantenha um estilo de vida saudável"
    
    elif 25 <= imc < 30:
        return "Sobrepeso - considere uma dieta equilibrada e exercícios físicos regulares"
    
    elif imc >= 30 and imc < 35:
        return "Obesidade Grau 1 - Procure orientação de um profissional de saúde para avaliação e plano de ação"
    

    elif imc >= 35 and imc < 40:
        return "Obesidade Grau 2 - consulte um médico para avaliação e considere mudanças no estilo de vida"
    
    else:
        return "Obesidade Grau 3 - Procure ajuda médica imediatamente para avaliação e tratamento adequado"

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

calculo_imc = imc(peso, altura)
classificacao = classificar_imc(calculo_imc)

print(f"IMC: {calculo_imc:.2f}")
print(f"Classificação: {classificacao}")
