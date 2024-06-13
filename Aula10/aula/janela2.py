import tkinter as interface
import Aula10.aula.janela3 as janela3

def iniciarJanela():
    janela = interface.Tk()
    janela.geometry('300x600')
    janela.title('Janela 2')

    botaoAbrirJanela2 = interface.Button(janela, text='Abrir janela 3', command=janela3)
    botaoAbrirJanela2.pack()
    

    janela.mainloop()

if __name__ == '__main__':
    iniciarJanela()