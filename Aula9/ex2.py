import tkinter as interface
from tkinter import *

janela = interface.Tk()
janela.geometry('260x170')
janela.title('Exercício 2 - Formulário')


frameMenu = interface.Frame(janela)
frameMenu.pack()

frameBotao = interface.Frame(janela)
frameBotao.pack()

labelNome = interface.Label(frameMenu, text='Nome: ')
labelNome.grid(row=0,column=0, padx=5, pady=5)
inputNome = interface.Entry(frameMenu)
inputNome.grid(row=0,column=1,padx=5, pady=5)

labelEmail = interface.Label(frameMenu, text='Email: ')
labelEmail.grid(row=1,column=0, padx=5, pady=5)
inputEmail = interface.Entry(frameMenu)
inputEmail.grid(row=1,column=1,padx=5, pady=5)

labelAge = interface.Label(frameMenu, text='Idade: ')
labelAge.grid(row=2,column=0, padx=5, pady=5)
inputAge = interface.Entry(frameMenu)
inputAge.grid(row=2,column=1,padx=5, pady=5)

labelTel = interface.Label(frameMenu, text='Telefone: ')
labelTel.grid(row=3,column=0, padx=5, pady=5)
inputTel = interface.Entry(frameMenu)
inputTel.grid(row=3,column=1,padx=5, pady=5)

btnCad = interface.Button(frameBotao, text='Cadastrar')
btnCad.grid(row=4, column=1, padx=10, pady=5)

janela.mainloop()