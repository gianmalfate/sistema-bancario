import textwrap
from cliente.pessoa_fisica import PessoaFisica
from conta.conta_corrente import ContaCorrente
from utils.filtro import filtrar_cliente, filtrar_contas_por_cpf

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    print("Endereço")
    logradouro = input("Informe logradouro: ")
    numero = input("Informe número: ")
    bairro = input("Informe bairro: ")
    cidade = input("Informe cidade: ")
    estado = input("Informe estado: ")
    endereco = [logradouro, numero, bairro, cidade, estado]
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")


def listar_contas(contas, clientes, cpf=None):
    if cpf:
        contas = filtrar_contas_por_cpf(cpf, clientes)

    if contas != None:
        for conta in contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))