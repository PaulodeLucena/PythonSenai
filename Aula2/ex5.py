id = int(input('Digite o ID desejado \n 1 - Playstation 5  \n 2 - Iphone 15 \n 3 - Monitor Gamer \n 4 - Notebook Asus \n 5 - Mouse Gamer \n ID:'))

precoplay = 3999.99 - (3999.99 * 0.20)
precoiphone = 4999.99 - (4999.99 * 0.30)
precomonitor = 899.99 - (899.99 * 0.15)
preconote = 2989.99 - (2989.99 * 0.1)
precomouse = 89.99 - (89.99 * 0.05)


if id == 1:
    print(f'O produdo escolhido foi o Playsatation 5, seu valor é 3999.99, com o desconto de 20%, o preço fica:{precoplay:.2f}')
elif id == 2:
    print(f'O produdo escolhido foi o Iphone 15, seu valor é 4999.99, com o desconto de 30%, o preço fica:{precoiphone:.2f}')
elif id == 3:
    print(f'O produdo escolhido foi o Monitor Gamer, seu valor é 899.99, com o desconto de 15%, o preço fica:{precomonitor:.2f}')
elif id == 4:
    print(f'O produdo escolhido foi o Notebook Asus, seu valor é 2989.99, com o desconto de 10%, o preço fica:{preconote:.2f}')
elif id == 5:
    print(f'O produdo escolhido foi o Mouse Gamer, seu valor é 89.90, com o desconto de 5%, o preço fica:{precomouse:.2f}')
else:
    print('Você digitou um id incorreto, por gentileza, na proxime, digite um valor correot (1 até 5)')
