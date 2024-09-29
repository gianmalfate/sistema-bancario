# Exibe mensagem de boas-vindas
print("Seja bem vindo ao Banco!")

# Menu de opções para o usuário
menu = """
Selecione a opcao desejada:
-------------------------------------
|       [1] Depositar               |
|       [2] Sacar                   |
|       [3] Extrato                 |
|       [4] Sair                    |
-------------------------------------
=> """

# Constantes e variáveis iniciais
LIMITE_SAQUES = 3
saldo = 0
limite = 500
extrato = ""
numero_saques = 0

# Loop principal do programa
while True:
    opcao = input(menu)  # Solicita ao usuário uma opção do menu
    
    # Opção para depósito
    if opcao == "1":
        print("Depósito")
        valor = float(input("Informe o valor que deseja depositar: "))  # Solicita valor para depósito
        if valor > 0:
            saldo += valor  # Atualiza saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # Opção para saque
    elif opcao == "2":
        print("Saque")
        valor = float(input("Informe o valor que deseja sacar: "))  # Solicita valor para saque
        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("Operação falhou! Valor acima do limite máximo.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor  # Atualiza saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa contagem de saques
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção para exibir o extrato
    elif opcao == "3":
        print("\n--------------EXTRATO--------------")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)  # Exibe extrato
        print(f"Saldo: R$ {saldo:.2f}")

    # Opção para sair
    elif opcao == "4":
        break  # Encerra o loop
    
    # Tratamento de operações inválidas
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
