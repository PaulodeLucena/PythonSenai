import tkinter as interface
from tkinter import messagebox

def adicao():
        n1 = float(txt_n1.get())
        n2 = float(txt_n2.get())
        resultado = n1 + n2
        print('s')
        lbl_Resultado.config(text=f"Resultado: {resultado}")
        messagebox.showinfo("Resultado", f"O resultado da adição é: {resultado}")

def subtracao():
        n1 = float(txt_n1.get())
        n2 = float(txt_n2.get())
        resultado = n1 - n2
        messagebox.showinfo("Resultado", f"O resultado da subtração é: {resultado}")

def multiplicacao():
        n1 = float(txt_n1.get())
        n2 = float(txt_n2.get())
        resultado = n1 * n2
        messagebox.showinfo("Resultado", f"O resultado da multiplicação é: {resultado}")

def divisao():
        n1 = float(txt_n1.get())
        n2 = float(txt_n2.get())
        if n2 == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
        else:
            resultado = n1 / n2
            messagebox.showinfo("Resultado", f"O resultado da divisão é: {resultado}")

janela = interface.Tk()
janela.geometry('600x400')
janela.title('Calculadora')

lbl_n1 = interface.Label(janela, text='Digite o primeiro numero: ')
lbl_n1.pack()

txt_n1 = interface.Entry(janela)
txt_n1.pack()

lbl_n2 = interface.Label(janela, text='Digite o segundo numero: ')
lbl_n2.pack()

txt_n2 = interface.Entry(janela)
txt_n2.pack()

btn_Soma = interface.Button(janela, text='+', command=adicao)
btn_Soma.pack(pady=4)

btn_Sub = interface.Button(janela, text='-', command=subtracao)
btn_Sub.pack(pady=4)

btn_Mult = interface.Button(janela, text='x', command=multiplicacao)
btn_Mult.pack(pady=4)

btn_Div = interface.Button(janela, text='/', command=divisao)
btn_Div.pack(pady=4)

lbl_Resultado = interface.Label(janela,text='resultado: ', font=15)
lbl_Resultado.pack()

janela.mainloop()


#btn_Sete = interface.Button(janela, text="7")
# btn_Sete.pack

# btn_Oito = interface.Button(janela, text="8")
# btn_Oito.pack

# btn_Nove= interface.Button(janela, text="9")
# btn_Nove.pack

# btn_Divisao= interface.Button(janela, text="/")
# btn_Divisao.pack

# btn_Quatro = interface.Button(janela, text="4")
# btn_Quatro.pack

# btn_Cinco = interface.Button(janela, text="5")
# btn_Cinco.pack

# btn_Seis = interface.Button(janela, text="6")
# btn_Seis.pack

# btn_Multiplicacao = interface.Button(janela, text="X")
# btn_Multiplicacao.pack

# btn_Um= interface.Button(janela, text="1")
# btn_Um.pack

# btn_Dois= interface.Button(janela, text="2")
# btn_Dois.pack

# btn_Tres= interface.Button(janela, text="3")
# btn_Tres.pack

# btn_Subtracao= interface.Button(janela, text="-")
# btn_Subtracao.pack

# btn_Zero= interface.Button(janela, text="0")
# btn_Zero.pack

# btn_Ponto= interface.Button(janela, text=".")
# btn_Ponto.pack

# btn_Igual= interface.Button(janela, text="=")
# btn_Igual.pack

# btn_Soma= interface.Button(janela, text="+")
# btn_Soma.pack

