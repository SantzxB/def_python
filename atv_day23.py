import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- FUNÇÕES ---------------- #

def calcular_vr(valor_vr):
    return valor_vr * 0.20

def calcular_vt(salario, deseja_vt):
    return salario * 0.06 if deseja_vt.lower() == "s" else 0.0

def calcular_dependentes(qtd):
    return qtd * 150.0

def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09
    elif salario <= 4190.83:
        return salario * 0.12
    elif salario <= 8157.41:
        return salario * 0.14
    else:
        return 951.62  # teto

def calcular_irrf(salario):
    if salario <= 2428.80:
        return 0.0
    elif salario <= 2826.65:
        return salario * 0.075
    elif salario <= 3751.05:
        return salario * 0.15
    elif salario <= 4664.68:
        return salario * 0.225
    else:
        return salario * 0.275

# ---------------- PROGRAMA PRINCIPAL ---------------- #

limpar_tela()

matricula = input("Digite sua matrícula: ")
senha = input("Digite sua senha: ")

print("\nAcesso permitido!\n")

salario_base = float(input("Digite seu salário base: R$ "))
vale_refeicao = float(input("Digite o valor do vale refeição: R$ "))
qtd_dependentes = int(input("Quantidade de dependentes: "))
vale_transporte = input("Deseja vale transporte? (s/n): ")

# Cálculos
desconto_vr = calcular_vr(vale_refeicao)
desconto_vt = calcular_vt(salario_base, vale_transporte)
desconto_dep = calcular_dependentes(qtd_dependentes)

inss = calcular_inss(salario_base)
irrf = calcular_irrf(salario_base)

total_descontos = desconto_vr + desconto_vt + desconto_dep + inss + irrf
salario_liquido = salario_base - total_descontos

limpar_tela()

# ---------------- RESULTADO ---------------- #

print("----- RESUMO DA FOLHA -----\n")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
print(f"Desconto Dependentes: R$ {desconto_dep:.2f}")

print("\nTotal de Descontos: R$ {:.2f}".format(total_descontos))
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
