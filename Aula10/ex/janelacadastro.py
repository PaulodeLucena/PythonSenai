import tkinter as interface
from tkinter import messagebox

def encerrar():
    messagebox.showinfo('Cadastro','O Cadastro foi enviado com sucesso')
    janela.destroy()   

def informacoesUsuario():
    global janela
    janela = interface.Tk();
    janela.geometry('300x200')
    janela.title('Cadastro')

    frameCadastro = interface.Frame(janela)
    frameCadastro.pack()

    lblNome = interface.Label(frameCadastro, text='Nome:')
    lblNome.grid(row=0, column=0, pady=5)
    txtNome = interface.Entry(frameCadastro)
    txtNome.grid(row=0, column=1, pady=5)

    lblEmail = interface.Label(frameCadastro, text='Email:')
    lblEmail.grid(row=1, column=0, pady=5)
    txtEmail = interface.Entry(frameCadastro)
    txtEmail.grid(row=1, column=1, pady=5)

    lblCpf = interface.Label(frameCadastro, text='CPF:')
    lblCpf.grid(row=2, column=0, pady=5)
    txtCpf = interface.Entry(frameCadastro)
    txtCpf.grid(row=2, column=1, pady=5)

    lblRg = interface.Label(frameCadastro, text='RG:')
    lblRg.grid(row=3, column=0, pady=5)
    txtRg = interface.Entry(frameCadastro)
    txtRg.grid(row=3, column=1, pady=5)

    lblNomeMae = interface.Label(frameCadastro, text='Nome da Mãe:')
    lblNomeMae.grid(row=4, column=0, pady=5)
    txtNomeMae = interface.Entry(frameCadastro)
    txtNomeMae.grid(row=4, column=1, pady=5)

    frameBtn = interface.Frame(janela)
    frameBtn.pack()

    btnEnviar = interface.Button(frameBtn, text='Enviar', command=encerrar)
    btnEnviar.grid(pady=5)

    janela.mainloop()

if __name__ == '__main__':
    informacoesUsuario()