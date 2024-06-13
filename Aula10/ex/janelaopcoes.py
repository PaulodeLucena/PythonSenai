import tkinter as interface
import janelacadastro
from tkinter import messagebox

def sistema():
    messagebox.showerror('Erro', 'Essa função ainda não foi criada')

def cadastro():
    janela.destroy()
    janelacadastro.informacoesUsuario()

def fechar():
    janela.destroy()

def opcoes():
    global janela
    janela = interface.Tk()
    janela.geometry('650x500')
    janela.title('Pagina de opções')

    frameBotoes = interface.Frame(janela)
    frameBotoes.pack()

    btnCadastro = interface.Button(frameBotoes, text='Cadastro', command=cadastro, font=10, width=50, height=5)
    btnCadastro.grid(row=0, column=0, pady=10, padx=10)

    btnSistema = interface.Button(frameBotoes, text='Sistema', command=sistema, font=10, width=50, height=5)
    btnSistema.grid(row=1, column=0, pady=10, padx=10)

    btnSair = interface.Button(frameBotoes, text='Sair', command=fechar, font=10, width=50, height=5)
    btnSair.grid(row=2, column=0, pady=10, padx=10)

    janela.mainloop()

if __name__ == '__main__':
    opcoes()