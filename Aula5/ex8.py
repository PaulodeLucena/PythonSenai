print("Digite apenas número positivos 0 é neutro")

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

contador = 0 
maior = 0

if n1 > n2:
    contador = n2
    maior = n1
elif n2 > n1:
    contador = n1
    maior = n2
else:
    print('Os número são iguais')

if contador > 0:
    while contador <= maior:
        print(contador)
        contador += 1
