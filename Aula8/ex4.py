import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.geometry('600x400')
janela.title('Calculadora de IMC')

def calculoIMC():
    peso = float(txt_peso.get())
    altura = float(txt_altura.get())
    imc = peso / (altura ** 2)
    messagebox.showinfo('IMC', f'Seu IMC é {imc:.2f}')

lbl_peso = interface.Label(janela, text='Digite seu peso')
lbl_peso.pack()

txt_peso = interface.Entry(janela)
txt_peso.pack()

lbl_altura = interface.Label(janela, text='Digite sua altura (em metros)')
lbl_altura.pack()

txt_altura = interface.Entry(janela)
txt_altura.pack()

btn_Verifica = interface.Button(janela, text='Fazer o calculo de imc', command=calculoIMC)
btn_Verifica.pack()

janela.mainloop()