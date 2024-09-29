import textwrap


# Mensagem de boas-vindas ao usuário
print("Seja bem-vindo ao Banco!")


def menu():
    # Função que exibe o menu de opções para o usuário
    menu = """
    Selecione a opcao desejada:
    -------------------------------------
    |       [1] Depositar               |
    |       [2] Sacar                   |
    |       [3] Extrato                 |
    |       [4] Criar usuário           |
    |       [5] Criar conta             |
    |       [6] Listar conta            |
    |       [7] Sair                    |
    -------------------------------------
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    # Função que realiza um depósito na conta
    if valor > 0:
        saldo += valor  # Atualiza o saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona a movimentação ao extrato
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato  # Retorna o saldo e o extrato atualizados


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Função que realiza um saque na conta
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")

    elif valor > limite:
        print("Operação falhou! Valor acima do limite máximo.")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")

    elif valor > 0:
        saldo -= valor  # Atualiza o saldo
        extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona a movimentação ao extrato
        numero_saques += 1  # Incrementa o contador de saques
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato  # Retorna o saldo e o extrato atualizados


def exibir_extrato(saldo, /, *, extrato):
    # Função que exibe o extrato da conta
    print("\n--------------EXTRATO--------------")
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("-----------------------------------")


def criar_usuario(usuarios):
    # Função que cria um novo usuário
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)  # Filtra o usuário pelo CPF

    if usuario:
        print("\nJá existe um usuário com esse CPF.")  # Verifica se o CPF já está cadastrado
        return
    
    else:
        # Coleta as informações do novo usuário
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
        print("Endereço")
        logradouro = input("Informe logradouro: ")
        numero = input("Informe número: ")
        bairro = input("Informe bairro: ")
        cidade = input("Informe cidade: ")
        estado = input("Informe estado: ")
        
        # Adiciona o novo usuário à lista de usuários
        usuarios.append({
            "nome": nome, 
            "data_nascimento": data_nascimento, 
            "cpf": cpf, 
            "endereco": {
                "logradouro": logradouro,
                "nro": numero,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            }
        })
        print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    # Função que filtra o usuário com base no CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None  # Retorna o usuário ou None


def criar_conta(contas, numero_conta, AGENCIA, usuarios):
    # Função que cria uma nova conta para um usuário existente
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)  # Filtra o usuário pelo CPF

    if usuario:
        # Adiciona a nova conta à lista de contas
        contas.append({
            "agencia": AGENCIA,
            "nro": numero_conta,
            "usuario": usuario
        })
        print("Conta criada com sucesso!")

    else:
        print("Usuário não encontrado, a conta não pode ser criada.")


def listar_contas(contas, cpf=None):
    # Função que lista as contas existentes, podendo filtrar por CPF
    if cpf:
        contas_filtradas = [conta for conta in contas if conta['usuario']['cpf'] == cpf]  # Filtra por CPF

    else:
        # Se o CPF não for informado, lista todas as contas e ordena pelo nome do titular
        contas_filtradas = sorted(contas, key=lambda conta: conta['usuario']['nome'])
    # Exibe as contas filtradas
    
    if contas_filtradas:

        for conta in contas_filtradas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['nro']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

    else:
        print("Nenhuma conta encontrada para o CPF informado." if cpf else "Nenhuma conta cadastrada.")


def main():
    # Função principal que controla o fluxo do programa
    LIMITE_SAQUES = 3  # Limite de saques diários
    AGENCIA = "0001"  # Número da agência

    saldo = 0  # Inicializa o saldo
    limite = 500  # Limite para saques
    extrato = ""  # Inicializa o extrato
    numero_saques = 0  # Contador de saques
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    while True:
        opcao = menu()  # Exibe o menu e captura a opção escolhida

        if opcao == "1":
            print("Depósito")
            valor = float(input("Informe o valor que deseja depositar: "))  # Captura o valor do depósito
            saldo, extrato = depositar(saldo, valor, extrato)  # Realiza o depósito

        elif opcao == "2":
            print("Saque")
            valor = float(input("Informe o valor que deseja sacar: "))  # Captura o valor do saque
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)  # Realiza o saque

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)  # Exibe o extrato

        elif opcao == "4":
            print("Criar usuário")
            criar_usuario(usuarios)  # Cria um novo usuário

        elif opcao == "5":
            print("Criar conta")
            numero_conta = len(contas) + 1  # Gera um novo número de conta
            criar_conta(contas, numero_conta, AGENCIA, usuarios)  # Cria uma nova conta

        elif opcao == "6":
            print("Listar contas")
            cpf = input("Informe o CPF do usuário (somente número): ")  # Captura o CPF para listar contas
            listar_contas(contas, cpf)  # Lista as contas

        elif opcao == "7":
            break  # Encerra o programa
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro para opções inválidas

# Chama a função principal para iniciar o programa
main()