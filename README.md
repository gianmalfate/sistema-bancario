# Sistema Bancário Simplificado
Este é um sistema bancário simplificado desenvolvido em Python. Ele permite criar clientes e contas bancárias, realizar transações como depósitos e saques, e exibir extratos de transações.

## Funcionalidades
- Criação de Clientes: Cadastro de clientes do tipo Pessoa Física com CPF, nome completo, data de nascimento e endereço.
- Criação de Contas Correntes: Geração de contas bancárias associadas a clientes, com um limite de saque e número de saques diários.
- Depósito: Função para adicionar fundos à conta.
- Saque: Função para retirar fundos da conta, respeitando limites estabelecidos.
- Extrato: Exibição do histórico de transações realizadas, como depósitos e saques.
- Limite de Saques: O sistema limita a quantidade de saques diários para contas correntes.

## Estrutura de Classes
- Cliente: Representa um cliente, contendo endereço e contas associadas.
- PessoaFisica: Subclasse de Cliente, representa uma pessoa física com CPF, nome e data de nascimento.
- Conta: Representa uma conta bancária com número, agência, saldo e histórico de transações.
- ContaCorrente: Subclasse de Conta, implementa um limite de saque e limite de saques diários.
- Transacao: Classe abstrata que define o modelo de uma transação, que pode ser implementada como depósito ou saque.
- Deposito: Subclasse de Transacao, para operações de depósito.
- Saque: Subclasse de Transacao, para operações de saque.
- Historico: Armazena e gerencia o histórico de transações para cada conta.

## Requisitos
- Python 3.x
- Não há bibliotecas externas necessárias

## Como Executar
Clone o repositório:
```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
Execute o sistema:
```
python main.py
```

## Menu de Operações
- Depositar: Informe o CPF e o valor para realizar o depósito.
- Sacar: Informe o CPF, selecione a conta (se houver mais de uma), e o valor do saque.
- Extrato: Exibe o histórico de transações e saldo atual da conta.
- Novo Usuário: Cria um novo cliente.
- Nova Conta: Cria uma nova conta corrente associada a um cliente existente.
- Listar Contas: Exibe todas as contas cadastradas.
- Sair: Encerra o programa.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Autor
Giancarlo Malfate Caprino

## Licença
Este projeto é licenciado sob a MIT License.
