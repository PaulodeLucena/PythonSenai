import time

contagem = int(input('Digite um número: '))

for n in range(contagem, 0, -1):
    time.sleep(1)
    print(n)