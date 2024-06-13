import tkinter as interface

janela = interface.Tk()
janela.title('Exercício 1 - Calculadora')
janela.geometry('500x300')

qtdlinha = 4
qtdcoluna = 4

lista_botoes = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-','0','.','+','=']

index = 0

# for botao in lista_botoes:
#     print(f'{index} > {botao}')
#     index += 1


frameInput = interface.Frame(janela)
frameInput.pack()

InputNumber = interface.Entry(frameInput, font=35)
InputNumber.pack(pady=20)

frameMenu = interface.Frame(janela)
frameMenu.pack()

indiceTextoBotao = 0
for linha in range(qtdlinha):
    for coluna in range(qtdcoluna):
        textoBotao = lista_botoes[indiceTextoBotao]
        btn = interface.Button(frameMenu, text=textoBotao)
        btn.grid(row=linha, column=coluna)
        indiceTextoBotao +=1
        print(f'linha {linha}, coluna {coluna}')




janela.mainloop()