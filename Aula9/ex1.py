import tkinter as interface

janela = interface.Tk()
janela.title('Exercício 1 - Calculadora')
janela.geometry('500x300')

frameInput = interface.Frame(janela)
frameInput.pack()

InputNumber = interface.Entry(frameInput, font=35)
InputNumber.pack(pady=20)

frameMenu = interface.Frame(janela)
frameMenu.pack()

btn7 = interface.Button(frameMenu, text='7', font=30, width=1)
btn7.grid(row=1, column=1, padx=20, pady=10)

btn8 = interface.Button(frameMenu, text='8', font=30, width=1)
btn8.grid(row=1, column=2, padx=20, pady=10)

btn9 = interface.Button(frameMenu, text='9', font=30, width=1)
btn9.grid(row=1, column=3, padx=20, pady=10)

btnBarra = interface.Button(frameMenu, text='/', font=30, width=1)
btnBarra.grid(row=1, column=4, padx=20, pady=10)
#----------------------------------------------------------
btn4 = interface.Button(frameMenu, text='4', font=30, width=1)
btn4.grid(row=2, column=1, padx=20, pady=10)

btn5 = interface.Button(frameMenu, text='5', font=30, width=1)
btn5.grid(row=2, column=2, padx=20, pady=10)

btn6 = interface.Button(frameMenu, text='6', font=30, width=1)
btn6.grid(row=2, column=3, padx=20, pady=10)

btnAsterisco = interface.Button(frameMenu, text='*', font=30, width=1)
btnAsterisco.grid(row=2, column=4, padx=20, pady=10)
#----------------------------------------------------------
btn1 = interface.Button(frameMenu, text='1', font=30, width=1)
btn1.grid(row=3, column=1, padx=20, pady=10)

btn2 = interface.Button(frameMenu, text='2', font=30, width=1)
btn2.grid(row=3, column=2, padx=20, pady=10)

btn3 = interface.Button(frameMenu, text='3', font=30, width=1)
btn3.grid(row=3, column=3, padx=20, pady=10)

btnMenos = interface.Button(frameMenu, text='-', font=30, width=1)
btnMenos.grid(row=3, column=4, padx=20, pady=10)
#----------------------------------------------------------
btn0 = interface.Button(frameMenu, text='0', font=30, width=1)
btn0.grid(row=4, column=1, padx=20, pady=10)

btnPonto = interface.Button(frameMenu, text='.', font=30, width=1)
btnPonto.grid(row=4, column=2, padx=20, pady=10)

btnigual = interface.Button(frameMenu, text='=', font=30, width=1)
btnigual.grid(row=4, column=3, padx=20, pady=10)

btnMais = interface.Button(frameMenu, text='+', font=30, width=1)
btnMais.grid(row=4, column=4, padx=20, pady=10)

janela.mainloop()