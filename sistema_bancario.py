menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\n================ Operação falhou! ================")
            print("O valor informado é inválido.")
            print("Verifique e Tente novamente")
            print("==========================================")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n================ Operação falhou! ================")
            print("Você não tem saldo suficiente.")
            print("Verifique e Tente novamente")
            print("==========================================")
            
        elif excedeu_limite:
            print("\n================ Operação falhou! ================")
            print("O valor do saque excede o limite.")
            print("Verifique e Tente novamente")
            print("==========================================")
        

        elif excedeu_saques:
            print("\n================ Operação falhou! ================")
            print("Número máximo de saques excedido.")
            print("Verifique e Tente novamente")
            print("==========================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\n================ Operação falhou! ================")
            print("O valor informado é inválido.")
            print("Verifique e Tente novamente")
            print("==========================================")


    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")