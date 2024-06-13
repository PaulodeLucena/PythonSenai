palavra = input("Digite uma palavra: ")
contador = 0 
vogais = 0

tamanho_palavra = len(palavra)

while tamanho_palavra > contador:
    if palavra[contador].lower() in 'aeiou':
        vogais += 1 
    contador +=1
  
print(f'A quantidade de vogais é {vogais}')

