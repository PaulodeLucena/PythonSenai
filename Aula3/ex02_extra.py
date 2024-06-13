print('Produto mais barato')

produto1 = float(input('\nInforme o preço do produto 1: '))
produto2 = float(input('\nInforme o preço do produto 2: '))
produto3 = float(input('\nInforme o preço do produto 3: '))

if produto1 < produto2 and produto1 < produto3:
    print('O produto 1 é o mais barato, compre ele.')
elif produto2 < produto1 and produto2 < produto3:
    print('O produto 2 é o mais barato, compre ele.')
elif produto3 < produto1 and produto3 < produto2:
    print('O produto 3 é o mais barato, compre ele.')
else:
    if produto1 == produto2 and produto1 < produto3:
        print('Produto 1 e produto 2 tem os mesmo valor e são mais baratos que o produto 3, compre qualquer um dos dois')
    elif produto1 == produto3 and produto1 < produto2:
        print('Produto 1 e produto 3 tem os mesmo valor e são mais baratos que o produto 2, compre qualquer um dos dois')
    elif produto2 == produto3 and produto2 < produto1:
        print('Produto 2 e produto 3 tem os mesmo valor e são mais baratos que o produto 1, compre qualquer um dos dois')
    else:
        print('Todos os produtos tem o mesmo valor, leve o que preferir.')
