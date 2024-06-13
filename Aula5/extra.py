conta_correta = '1234'
senha_correta = '4321'

while True:
    conta = input('Digite o número da sua conta: ')
    senha = input('Digite a sua senha de 4 dígitos: ')

    if conta == conta_correta and senha == senha_correta:
        saldo = 0
        break
    else:
        print('Conta ou senha incorretos. Tente novamente.')

while True:
    print('\nOpções disponíveis:')
    print('1 - Verificar saldo')
    print('2 - Depositar dinheiro na conta')
    print('3 - Retirar dinheiro da conta')
    print('0 - Sair do sistema')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'Seu saldo é: {saldo:.2f}')
    elif opcao == '2':
        valor_deposito = float(input('Digite o valor do deposito: '))
        saldo += valor_deposito
        print('Depósito realizado.')
    elif opcao == '3':
        valor_retirada = float(input('Digite o valor da retirada: '))
        if valor_retirada <= saldo:
            saldo -= valor_retirada
            print('Retirada realizada.')
        else:
            print('Saldo insuficiente')
    elif opcao == '0':
        print('Saindo do sistema.')
        break
    else:
        print('Opção inválida.')
