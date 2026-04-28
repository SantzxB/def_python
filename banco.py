import os
os.system("cls||clear")

user_name =  []
saldo = 0 

def menu():
    
    print("""               OPÇÃO         
                1           SACAR
                2         DEPOSITAR
                3           SALDO
                4           SAIR
                
""")
def opcao(op):
        global saldo
        
        if op == "1":
            try:
                saque = int(input("Digite o valor à sacar:  "))
                if saque <= 0:
                    print("Valor inválido!")
                elif saque > saldo:
                    print("Saldo insuficiente!")
                else:
                    saldo -= saque
                    print("Saque Realizado com sucesso.")
            except:
                print("Entrade Inválida!")

        elif op == "2":
            try:
                deposito = int(input("Qual Valor à depositar: "))
                if deposito <= 0:
                    print("Valor indisponível para depósito")
                else:
                    saldo += deposito
                print("Depósito realizado com sucesso")
            except:
                print("Entrada Inválida!")
        
        elif op == "3":
            
            print(f"Olá {name_user}, esse é seu saldo:      ")
            print(f"       {saldo:.2f}     ")

        elif op == "4":
            print("Voltando para tela inicial...")
            
            
            return False
        
        else:
            print("Opção inválida!")
            return True


print("Bem-Vindo ao Banco Digital CodBank")
print()
name_user = input("Digite seu nome completo: ").strip().title()
user_name.append(name_user)
print()
while True:
    menu()
    print()
    op = input("ESCOLHA A OPÇÃO:")

    opcao(op)

