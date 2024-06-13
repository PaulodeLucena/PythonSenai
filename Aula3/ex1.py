print('Cadastro de produtos')

nomeprod = str(input('\nDigite o nome do produto: '))
categoria = str(input('\nDigite a categoria do produto (Informática, VideoGame ou Smarthphone): ')).lower()
custo = float(input('\nDigite o valor do produto: R$'))

if categoria == 'informatica' or categoria == 'informática':
    custo = custo * 1.30
    print(f'O produto {nomeprod}, que é da categoria {categoria} custa R${custo:.2f} já com acrescimo')
elif categoria == 'smarthphone':
    custo = custo * 1.15
    print(f'O produto {nomeprod}, que é da categoria {categoria} custa R${custo:.2f} já com acrescimo')
elif categoria == 'videogame':
    custo = custo * 1.20
    print(f'O produto {nomeprod}, que é da categoria {categoria} custa R${custo:.2f} já com acrescimo')
else:
    print('A categoria foi digitada incorretamente.')

