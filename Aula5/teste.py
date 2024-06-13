conta = input('Digite o número da sua conta: ')
senha = input('Digite a sua senha de 4 dígitos: ')
saldo = 0

while conta != '1234' and senha != '4321':
    conta = input('Digite o número da sua conta: ')
    senha = input('Digite a sua senha de 4 dígitos: ')


print('\nOpções disponíveis:')
print('1 - Verificar saldo')
print('2 - Depositar dinheiro na conta')
print('3 - Retirar dinheiro da conta')
print('0 - Sair do sistema')

opcao = input('Escolha uma opção: ')


while opcao > 0: 
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