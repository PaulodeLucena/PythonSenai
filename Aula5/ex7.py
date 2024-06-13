print('Calculadora')

while True:
    id = int(input('\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Sair\nEscolha uma opção:'))

    n1 = float(input('\nDigite um numero: '))
    n2 = float(input('Digite outro numero: '))

    if id == 0:
        print('Obrigado por usar a calculadora')
        break
    elif id == 1:
        conta = n1 + n2
        print(f'A conta dos números é: {conta:.2f}') 
    elif id == 2:
        conta = n1 - n2
        print(f'A conta dos números é: {conta:.2f}')
    elif id == 3:
        conta = n1 * n2
        print(f'A conta dos números é: {conta:.2f}')
    elif id == 4:
        if n2 <= 0:
            print('Não é possível fazer divisão por 0')
        else:   
            conta = n1 / n2
            print(f'A conta dos números é: {conta:.2f}')
    else:
        print('\n Não foi possível fazer um calculo pois a opção selecionada está incorreta, tente selecionar outra opção.')
