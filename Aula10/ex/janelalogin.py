import tkinter as interface
import janelaopcoes
from tkinter import messagebox
 
erro = 0

def usuarioSenha():
    usuario = str(txtUsuario.get())
    senha = str(txtSenha.get())
    global erro
    if usuario == 'admin' and senha == '4321':
        messagebox.showinfo('Valida', 'Login efetuado com sucesso')
        janela.destroy()
        janelaopcoes.opcoes()
    elif usuario != 'admin' or senha != '4321':
        messagebox.showwarning('Errou', 'Senha errada, tente novamente, caso erre a senha 3 vez o programa será encerrado.')
        erro += 1
        print(erro)
        if erro >= 3:
            messagebox.showwarning('Erro', 'Por motivos de segurança o programa será encerrado')
            janela.destroy()   
    else:
        messagebox.showwarning('Valida', 'Houve algum erro inesperado, reinicie o programa')

def login():
    global janela
    janela = interface.Tk()
    janela.geometry('300x200')
    janela.title('Pagina de login')

    frameLogin = interface.Frame(janela)
    frameLogin.pack()

    lblUsuario = interface.Label(frameLogin, text='Usuário')
    lblUsuario.grid()
    global txtUsuario
    txtUsuario = interface.Entry(frameLogin)
    txtUsuario.grid()
#--------------------------------------------------------------
    lblSenha = interface.Label(frameLogin, text='Senha')
    lblSenha.grid()
    global txtSenha
    txtSenha = interface.Entry(frameLogin)
    txtSenha.grid()

    botaoAbrirJanelaopcoes = interface.Button(frameLogin, text='Entrar', command=usuarioSenha)
    botaoAbrirJanelaopcoes.grid(padx=10, pady=10)

    janela.mainloop()



if __name__ == '__main__':
    login()