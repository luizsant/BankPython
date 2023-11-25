class Banco:
    def __init__(self):
        self.saldo = 10.50
        self.saqueNumber = 0
        self.operacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f'Depósito: R${valor:.2f}')
            return f'Seu novo saldo é R${self.saldo:.2f}'
        else:
            return 'Operação encerrada.'

    def sacar(self, valor):
        if self.saqueNumber < 3:
            if 0 < valor <= self.saldo and valor <= 500:
                self.saldo -= valor
                self.saqueNumber += 1
                self.operacoes.append(f'Saque: R${valor:.2f}')
                return f'Seu novo saldo é R${self.saldo:.2f}\nSaques restantes para hoje: {3 - self.saqueNumber}'
            else:
                return 'Valor acima do limite de R$500,00 ou saldo insuficiente.'
        else:
            return 'Você excedeu seu limite diário de saques.'

    def extrato(self):
        if not self.operacoes:
            return "Nenhuma operação foi realizada."
        else:
            return "Histórico de operações:\n" + "\n".join(self.operacoes)

    def consultar_saldo(self):
        return f'Seu saldo é de R${self.saldo:.2f}'


def main():
    banco = Banco()
    print('### BEM VINDO AO BANCO CHOMPIRAS S/A ###')

    while True:
        option = int(input('''
Digite a opção desejada:
1. Extrato
2. Depósito
3. Saque
4. Saldo
5. Sair

-> Opção: 
'''))

        if option == 1:
            print(banco.extrato())
        elif option == 2:
            valor = float(input('Digite o valor que você quer depositar: '))
            print(banco.depositar(valor))
        elif option == 3:
            valor = float(input('Digite o valor que você quer sacar: '))
            print(banco.sacar(valor))
        elif option == 4:
            print(banco.consultar_saldo())
        elif option == 5:
            print('Obrigado por usar o Banco Chompiras. Até logo!')
            break
        else:
            print('Opção inválida.')


if __name__ == "__main__":
    main()
