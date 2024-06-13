print('Maior número')

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
    print('O número 1 é maior')
elif n2 > n1 and n2 > n3:
    print('O segundo número é maior')
elif n3 > n1 and n3 > n2:
    print('O terceiro número é maior')
else:
    print('Não existe número maior, dois ou mais número são iguais')
    