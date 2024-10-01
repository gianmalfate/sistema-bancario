import textwrap

def menu():
    menu = """
    Selecione a opcao desejada:
    -------------------------------------
    |       [1] Depositar               |
    |       [2] Sacar                   |
    |       [3] Extrato                 |
    |       [4] Novo usuário            |
    |       [5] Nova conta              |
    |       [6] Listar contas           |
    |       [7] Sair                    |
    -------------------------------------
    => """
    return input(textwrap.dedent(menu))