pesopeixe = float(input('digite o peso do peixe: '))

calculopeso = (pesopeixe - 50) * 4

if pesopeixe <= 50:
    print('Peso do peixe está dentro do regulamento, tudo ok')
else:
    print(f'O peso do peixe foi {pesopeixe:.2f} então você pagará uma multa de R${calculopeso:.2f}')