import tkinter as interface
import Aula10.aula.janela2 as janela2
import Aula10.aula.janela3 as janela3



def abrirNovaJanela():
    janela.destroy()
    janela3.iniciarJanela()

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry('300x600')
    janela.title('Janela 1')

    botaoAbrirJanela2 = interface.Button(janela, text='Abrir janela 3', command=abrirNovaJanela)
    botaoAbrirJanela2.pack()


    janela.mainloop()

if __name__ == '__main__':
    iniciarJanela()