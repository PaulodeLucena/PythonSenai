contador = 0
soma = 0

while contador <= 4:
    n = int(input('Digite um numero: '))
    soma += n
    contador +=1

media = soma / contador
print(f'O valor da soma é: {soma} e média foi {media:.2f}') 
