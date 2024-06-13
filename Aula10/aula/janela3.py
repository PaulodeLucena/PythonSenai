import tkinter as interface
import Aula10.aula.janela1 as janela1


def abrirNovaJanela():
    janela.destroy()
    janela1.iniciarJanela()

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry('300x600')
    janela.title('Janela 3')

    txtNome = interface.Entry()
    txtNome.pack()

    botaoAbrirJanela2 = interface.Button(janela, text='Voltar', command=abrirNovaJanela)
    botaoAbrirJanela2.pack()



    janela.mainloop()

if __name__ == '__main__':
    iniciarJanela()


    