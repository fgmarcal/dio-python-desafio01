menu = """
    Selecione uma opção:
    [d] = depósito
    [s] = saque
    [e] = extrato
    [q] = fechar
"""
saldo_em_conta = 0
deposito = 0
saque = 0
extrato = []
SAQUES_DIARIOS = 3

while True:

    option = input(menu + " ")
    
    if option == 'q':
        break
    elif option == 'd':
        valor_dep = float(input("Informe o valor do depósito: "))
        print(f"Confirma depósito R$ {valor_dep:.2f}")
        saldo_em_conta += valor_dep
        deposito += 1
        extrato.append(f"dep. efet. R$ {valor_dep:.2f}")
    elif option == 's':
        if saque < SAQUES_DIARIOS:
            valor_saque = float(input("Informe o valor do saque: "))
            if valor_saque > saldo_em_conta:
                print(f"Saldo insuficiente para saque. Saldo atual R$ {saldo_em_conta:.2f}")
            else:
                saldo_em_conta -= valor_saque
                print(f"Saque efetuado! R$ {valor_saque:.2f}")
                saque += 1
                extrato.append(f"saq. efet. R$ {valor_saque:.2f}")
        else:
            print("Excedeu a quantidade diária de saques.")
    elif option == 'e':
        print("EXTRATO".center(20, "="))
        print("Sem movimentação." if not extrato else "")
        for line in extrato:
            print(line)
        print(f"\nSaldo atual = R${saldo_em_conta:.2f}")
    else:
        print("Opção inválida")
