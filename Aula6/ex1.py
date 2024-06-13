palavra = str(input('Digite uma palavra: '))
vogais = 0

for l in palavra:
    if l.lower() in 'aeiou':
        vogais += 1

print(f'A quantidade de vogais é {vogais}')