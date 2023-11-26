import re

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not all(x.isalpha() or x.isspace() for x in valor):
            raise ValueError("Nome inválido.")
        self._nome = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not self.validar_cpf(valor):
            raise ValueError("CPF inválido.")
        self._cpf = self.formatar_cpf(valor)

    @staticmethod
    def validar_cpf(cpf):
        # Simplificado: Adicione aqui sua lógica de validação de CPF
        return bool(re.match(r'^\d{11}$', cpf))

    @staticmethod
    def formatar_cpf(cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

class Banco:
    def __init__(self):
        self.clientes = []
        self.operacoes = []
        self.saldo = 0.0
        self.saqueNumber = 0

    def cadastrar_cliente(self, nome, cpf):
        try:
            cliente = Cliente(nome, cpf)
            self.clientes.append(cliente)
            print("Cliente cadastrado com sucesso.")
        except ValueError as e:
            print(e)

    def excluir_cliente(self, cpf):
        cpf_formatado = Cliente.formatar_cpf(cpf)
        self.clientes = [cliente for cliente in self.clientes if cliente.cpf != cpf_formatado]
        print("Cliente excluído com sucesso.")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f'Depósito: R${valor:.2f}')
            print(f'Seu novo saldo é R${self.saldo:.2f}')
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if self.saqueNumber < 3 and 0 < valor <= self.saldo and valor <= 500:
            self.saldo -= valor
            self.saqueNumber += 1
            self.operacoes.append(f'Saque: R${valor:.2f}')
            print(f'Seu novo saldo é R${self.saldo:.2f}')
            print(f'Saques restantes para hoje: {3 - self.saqueNumber}')
        else:
            print('Valor inválido ou limite de saques diários excedido.')

    def extrato(self):
        if not self.operacoes:
            print("Nenhuma operação foi realizada.")
        else:
            print("Histórico de operações:")
            for operacao in self.operacoes:
                print(operacao)

    def saldo_atual(self):
        print(f'Seu saldo é de R${self.saldo:.2f}')

banco = Banco()

while True:
    option = int(input('''
Digite a opção desejada:
1. Extrato
2. Depósito
3. Saque
4. Saldo
5. Cadastrar Cliente
6. Excluir Cliente
7. Sair

-> Opção: 
'''))

    if option == 1:
        banco.extrato()
    elif option == 2:
        valor = float(input('Digite o valor que você quer depositar: '))
        banco.deposito(valor)
    elif option == 3:
        valor = float(input('Digite o valor que você quer sacar: '))
        banco.saque(valor)
    elif option == 4:
        banco.saldo_atual()
    elif option == 5:
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente (apenas números): ")
        banco.cadastrar_cliente(nome, cpf)
    elif option == 6:
        cpf = input("Digite o CPF do cliente a ser excluído (apenas números): ")
        banco.excluir_cliente(cpf)
    elif option == 7:
        print('Obrigado por usar o Banco Chompiras. Até logo!')
        break
    else:
        print('Opção inválida.')
