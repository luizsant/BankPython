print('''
### BEM VINDO AO BANCO CHOMPIRAS S/A ###
''')

value = 10.50
saqueNumber = 0
operacoes = []

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
        if not operacoes:
            print("Nenhuma operação foi realizada.")
        else:
            print("Histórico de operações:")
            for operacao in operacoes:
                print(operacao)
    elif option == 2:
        cash = float(input('Digite o valor que você quer depositar: '))
        if cash > 0:
            value += cash
            operacoes.append(f'Depósito: R${cash:.2f}')
            print(f'Seu novo saldo é R${value:.2f}')
        else:
            print('Operação encerrada.')
    elif option == 3:
        if saqueNumber < 3:
            cash = float(input('Digite o valor que você quer sacar: '))
            if 0 < cash <= value and cash <= 500:
                value -= cash
                saqueNumber += 1
                operacoes.append(f'Saque: R${cash:.2f}')
                print(f'Seu novo saldo é R${value:.2f}')
                print(f'Saques restantes para hoje: {3 - saqueNumber}')
            else:
                print('Valor acima do limite de R$500,00 ou saldo insuficiente.')
        else:
            print('Você excedeu seu limite diário de saques')
    elif option == 4:
        print(f'Seu saldo é de R${value:.2f}')
    elif option == 5:
        print('Obrigado por usar o Banco Chompiras. Até logo!')
        break
    else:
        print('Opção inválida.')
