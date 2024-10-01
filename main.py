from sistema_bancario.utils.menu import menu
from sistema_bancario.transacao.operacoes import depositar, sacar, exibir_extrato
from sistema_bancario.utils.helpers import criar_cliente, criar_conta
from sistema_bancario.utils.helpers import listar_contas



def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            print("\nDepósito")
            depositar(clientes)

        elif opcao == "2":
            print("\nSaque")
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            print("\nNovo usuário")
            criar_cliente(clientes)

        elif opcao == "5":
            print("\nNova conta")
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            print("\nListar contas")
            cpf = input("Informe o CPF do usuário (somente número): ")
            listar_contas(contas, clientes, cpf)

        elif opcao == "7":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


main()