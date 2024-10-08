menu = """

========MENU========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
====================
=> 
"""


saldo = 0
limite = 500
extrato = ""  
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        # Depósito
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")

    elif opcao == "2":
        # Saque
        if numero_saques < LIMITES_SAQUES:
            valor = float(input("Informe o valor do saque: R$ "))
            if valor > saldo:
                print("Você está sem saldo!")
            elif valor > limite:
                print("O limite por saque é de R$ 500.00")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Valor inválido!")
        else:
            print("Limite de saques diários atingido!")

    elif opcao == "3":
        # Extrato
        print("\n========== EXTRATO ==========")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================")
        
    elif opcao == "4":
        # Sair  
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")
