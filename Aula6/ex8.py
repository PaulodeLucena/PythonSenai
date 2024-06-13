homens = []
mulheres = []

for i in range(1, 4):
    mulheres_nome = str(input(f'Digite o nome da {i}° mulher: '))
    mulheres.append(mulheres_nome)

for i in range(1, 4):
    homens_nome = str(input(f'Digite o nome {i}° do homem: '))
    homens.append(homens_nome)

for i in range(1, 4):
    print(f'A {i}° dupla é {homens[i]} e {mulheres[i]}')
