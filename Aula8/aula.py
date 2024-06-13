import tkinter as interface
from tkinter import messagebox

def apresentarMensagem():
    nome = txt_Nome.get()
    idade = int(txt_idade.get())
    messagebox.showinfo('Titulo', f'Seu nome é {nome} e você tem {idade} anos')
    
def fecharJanela():
    yesOrNo = messagebox.askquestion('Finalizar programa', 'Deseja finalizar?')
    if yesOrNo == 'yes':
        janela.destroy()

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

btn_SalvarDados = interface.Button(janela, text='Salvar dados', command=apresentarMensagem)
btn_SalvarDados.pack()

btn_FecharJanela = interface.Button(janela, text='Finalizar', command=fecharJanela)
btn_FecharJanela.pack()

janela.mainloop()