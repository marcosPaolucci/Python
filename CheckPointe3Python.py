class Conta:
    def __init__(self, numero_conta, nome_titular, saldo=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

    def mostrar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

    def salvar_dados(self, arquivo):
        with open(arquivo, 'a') as f:
            f.write(f'{self.numero_conta},{self.nome_titular},{self.saldo}\n')

    @staticmethod
    def carregar_dados(arquivo):
        contas = []
        with open(arquivo, 'r') as f:
            for linha in f:
                numero_conta, nome_titular, saldo = linha.strip().split(',')
                contas.append(Conta(numero_conta, nome_titular, float(saldo)))
        return contas

class ContaCorrente(Conta):
    def __init__(self, numero_conta, nome_titular, saldo=0, taxa_operacao=2.5):
        super().__init__(numero_conta, nome_titular, saldo)
        self.taxa_operacao = taxa_operacao

    def sacar(self, valor):
        total_saque = valor + self.taxa_operacao
        if total_saque <= self.saldo:
            self.saldo -= total_saque
            print(f'Saque de R${valor:.2f} e taxa de operação de R${self.taxa_operacao:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, nome_titular, saldo=0, taxa_juros=0.02):
        super().__init__(numero_conta, nome_titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f'Juros de R${juros:.2f} aplicados. Saldo atualizado: R${self.saldo:.2f}')


#Menu Iterativo:
def criar_conta(contas):
    tipo = input('Tipo de conta (1- Corrente, 2- Poupança): ')
    numero_conta = input('Número da conta: ')
    nome_titular = input('Nome do titular: ')
    saldo = float(input('Saldo inicial: '))
    
    if tipo == '1':
        conta = ContaCorrente(numero_conta, nome_titular, saldo)
    elif tipo == '2':
        conta = ContaPoupanca(numero_conta, nome_titular, saldo)
    else:
        print('Tipo de conta inválido.')
        return

    contas.append(conta)
    print('Conta criada com sucesso!')

def encontrar_conta(contas, numero_conta):
    for conta in contas:
        if conta.numero_conta == numero_conta:
            return conta
    return None

def realizar_deposito(contas):
    numero_conta = input('Número da conta: ')
    conta = encontrar_conta(contas, numero_conta)
    if conta:
        valor = float(input('Valor do depósito: '))
        conta.depositar(valor)
    else:
        print('Conta não encontrada.')

def realizar_saque(contas):
    numero_conta = input('Número da conta: ')
    conta = encontrar_conta(contas, numero_conta)
    if conta:
        valor = float(input('Valor do saque: '))
        conta.sacar(valor)
    else:
        print('Conta não encontrada.')

def mostrar_saldo(contas):
    numero_conta = input('Número da conta: ')
    conta = encontrar_conta(contas, numero_conta)
    if conta:
        conta.mostrar_saldo()
    else:
        print('Conta não encontrada.')

def salvar_dados(contas, arquivo):
    with open(arquivo, 'w') as f:
        for conta in contas:
            f.write(f'{conta.numero_conta},{conta.nome_titular},{conta.saldo}\n')
    print('Dados salvos com sucesso.')

def carregar_dados(arquivo):
    contas = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                numero_conta, nome_titular, saldo = linha.strip().split(',')
                saldo = float(saldo)
                if numero_conta.startswith('CC'):
                    conta = ContaCorrente(numero_conta, nome_titular, saldo)
                else:
                    conta = ContaPoupanca(numero_conta, nome_titular, saldo)
                contas.append(conta)
    except FileNotFoundError:
        pass
    return contas

#Menu Principal
def menu():
    contas = carregar_dados('contas.txt')
    while True:
        print('Menu:')
        print('1. Criar conta')
        print('2. Realizar depósito')
        print('3. Realizar saque')
        print('4. Mostrar saldo')
        print('5. Salvar dados')
        print('6. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            criar_conta(contas)
        elif opcao == '2':
            realizar_deposito(contas)
        elif opcao == '3':
            realizar_saque(contas)
        elif opcao == '4':
            mostrar_saldo(contas)
        elif opcao == '5':
            salvar_dados(contas, 'contas.txt')
        elif opcao == '6':
            salvar_dados(contas, 'contas.txt')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    menu()
