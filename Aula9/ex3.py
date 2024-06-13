import tkinter as interface

janela = interface.Tk()
janela.title('Layout Simples com Frame e Grid')
janela.geometry('250x150')

frameWelcome = interface.Frame(janela)
frameWelcome.pack()


lblWelcome = interface.Label(frameWelcome, text='Bem-vindo ao Layout Simples!')
lblWelcome.grid(row=0,column=0, padx=5, pady=5)

btnClick = interface.Button(frameWelcome, text='Clique Aqui')
btnClick.grid(row=2,column=0, padx=5, pady=5)

txtEntry = interface.Entry(frameWelcome)
txtEntry.grid(row=3,column=0)

btnClear = interface.Button(frameWelcome, text='Limpar')
btnClear.grid(row=3,column=1)











janela.mainloop()