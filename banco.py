from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

# Global variable - Lista de contas
contas: List[Conta] = []


# Definir função main
def main() -> None:
    menu()


# Definir menu
def menu() -> None:
    # Estruturar função menu com as opções
    print('=============================')
    print('========== ATM ==============')
    print('======== Pur Bank ===========')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    # Definir variável das opções
    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


# Definir criar conta
def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('Email do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: (dd/mm/yyyy)')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('---------------------')
    print(conta)
    sleep(2)
    menu()


# Definir efetuar saque
def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')

    else:
        print(f'Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


# Definir efetuar depósito
def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')

    else:
        print(f'Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


# Definir efetuar transferência
def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)

            else:
                print(f'A conta destino com número {numero_d} não foi encontrada.')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')

    else:
        print(f'Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


# Definir listar contas
def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('-------------------------------')
            sleep(1)
    else:
        print(f'Não existem contas cadastradas.')
    sleep(2)
    menu()


# Definir buscar contas por número
def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


# Definir função main
if __name__ == '__main__':
    main()







