# n = int(input('digite um numero: '))

# for i in range(n + 1):
#     print(f'{i}')


palavra = input("Digite uma palavra: ")

# Inicializa uma string vazia para armazenar a palavra invertida
palavra_invertida = ""

# Loop for para inverter a palavra
for letra in palavra:
    # Adiciona cada letra no início da palavra_invertida
    palavra_invertida = letra + palavra_invertida

# Imprime a palavra invertida
print("A palavra invertida é:", palavra_invertida)
