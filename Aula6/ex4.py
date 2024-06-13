palavra = str(input('Digite uma palavra: '))
invertida = ''

for l in palavra:
    invertida = l + invertida

if palavra == invertida:
    print(f'A palavra é um palindromo')
else:
    print('A palavra não é um palindromo')

print(f'Invertida: {invertida}')