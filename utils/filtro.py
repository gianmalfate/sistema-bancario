def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def filtrar_contas_por_cpf(cpf, clientes):
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\nCliente não encontrado!")
        return None

    if not cliente.contas:
        print("\nCliente não possui contas!")
        return None
    
    return cliente.contas


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    else:
        if len(cliente.contas) == 1:
            return cliente.contas[0]
        else:
            numero_conta = int(input("\nQual o número da conta: "))
            for conta in cliente.contas:
                if conta.numero == numero_conta:
                    return conta
            print("Conta não encontrada.")
            return None