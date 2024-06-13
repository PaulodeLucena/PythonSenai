print('Calculo de IMC')

peso = float(input('\nDigite seu peso em kg: '))
altura = float(input('\nDigite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'\nO seu IMC foi {imc:.2f}')

if imc < 18.5:
    print('\nVocê está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Seu peso está normal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
else:
    print('Você está obeso')

