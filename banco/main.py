menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu)

    if op == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Operação falhou. O valor informado é inválido.")
    
    elif op == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou. Você excedeu seu limite.")

        elif excedeu_saque:
            print("Operação falhou. Numero de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou. O valor informado é inválido.")
    
    elif op == "e":
        print("\n---- EXTRATO ----")
        print("Não foram relizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------")
    elif op == "q":
        break

    else:
        print("Opção Inválida. Insira o valor novamente.")
