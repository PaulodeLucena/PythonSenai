import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.geometry('600x400')
janela.title('Verificador de maioridade')

def verificaMaior():
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo('Janela de validação', f'Sua idade é {idade}, você é maior de idade.')
    else:
        messagebox.showwarning('Janela de validação', f'Sua idade é {idade}, você é menor de idade.')

lbl_idade = interface.Label(janela, text='Digite sua idade')
lbl_idade.pack()

txt_idade = interface.Entry(janela)
txt_idade.pack()

btn_Verifica = interface.Button(janela, text='Validar se é maior de idade', command=verificaMaior)
btn_Verifica.pack()

janela.mainloop()