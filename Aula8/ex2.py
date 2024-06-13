import tkinter as interface
from tkinter import messagebox
import time

def apresentarMensagem():
    nome = txt_Nome.get()
    idade = int(txt_idade.get())
    email = txt_Email.get()
    messagebox.showinfo('Cadastro usuário', f'Seu nome é {nome}\nVocê tem {idade} anos\nSeu e-mail é {email}')

janela = interface.Tk()
janela.geometry('600x400')
janela.title('Aplicativo')

lbl_Nome = interface.Label(janela, text='Digite seu nome')
lbl_Nome.pack()

txt_Nome = interface.Entry(janela)
txt_Nome.pack()

lbl_idade = interface.Label(janela, text='Digite sua idade')
lbl_idade.pack()

txt_idade = interface.Entry(janela)
txt_idade.pack()

lbl_Email = interface.Label(janela, text='Digite seu e-mail')
lbl_Email.pack()

txt_Email = interface.Entry(janela)
txt_Email.pack()

btn_SalvarDados = interface.Button(janela, text='Cadastra usuário', command=apresentarMensagem)
btn_SalvarDados.pack()


janela.mainloop()