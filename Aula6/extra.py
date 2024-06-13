import random

computador = random.randint(0, 100)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 100.\nSerá que você consegue adivinhar qual foi ? ')

acertou = False
palpites: int = 0
while not acertou:
    jogador = int(input('tente acerta! escolha um número:'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')

print(f"Acertou!! Você conseguiu depois de {palpites} tentativa(s)")
