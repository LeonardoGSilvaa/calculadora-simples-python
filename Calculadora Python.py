from tkinter import *

# Cores

cor1 = "#fcba03"  # Amarelo
cor2 = "#111211"  # Preto
cor3 = "#3cf0ba"  # Azul Esverdeado
cor4 = "#ffffff"  # Branco
cor5 = "#d4d4d4"  # Cinza

principal = Tk()

principal.title('***Calculadora***')
principal.geometry("235x312+1016+162")  # Largura x Altura + dist Esquerda + dist Topo
principal.wm_resizable(width=False, height=False)
principal.config(bg=cor1)

# Frames
frame_tela = Frame(principal, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(principal, width=235, height=268)
frame_body.grid(row=1, column=0)

# Variavel para todos os valores
valores = ''


# Funções

def clique_esq_mouse(retorno):
    print(f'X: {retorno.x} | Y: {retorno.y} Geo: {principal.geometry()}')


def entrar_valores(event):  # Lógica

    global valores
    valores = valores + str(event)

    # Valor para a tela
    valor_texto.set(valores)


def calcular():  # Função para calcular
    global valores
    resultado = eval(valores)

    valor_texto.set(str(resultado))


def limpar_tela():
    global valores
    valores = ""
    valor_texto.set("")


# Label

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font='Ivy 18 italic', bg=cor3)  # para mostrar o resultado no visor
app_label.place(x=0, y=0)

# Botões

b_clear = Button(frame_body, command=limpar_tela, text="C", width=12, height=2, bg=cor5, font='Ivy 13 bold',
                 relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=1)
b_2 = Button(frame_body, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=117, y=1)
b_3 = Button(frame_body, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor1, fg=cor4,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=175, y=1)
b_4 = Button(frame_body, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=54)
b_5 = Button(frame_body, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=54)
b_6 = Button(frame_body, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=117, y=54)
b_7 = Button(frame_body, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor1, fg=cor4,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_7.place(x=175, y=54)
b_8 = Button(frame_body, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)
b_9 = Button(frame_body, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=106)
b_10 = Button(frame_body, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor5,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_10.place(x=117, y=106)
b_11 = Button(frame_body, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor1, fg=cor4,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_11.place(x=175, y=106)
b_12 = Button(frame_body, command=lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor5, font='Ivy 13 bold',
              relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=158)
b_13 = Button(frame_body, command=lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor5, font='Ivy 13 bold',
              relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=158)
b_14 = Button(frame_body, command=lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor5, font='Ivy 13 bold',
              relief=RAISED, overrelief=RIDGE)
b_14.place(x=117, y=158)
b_15 = Button(frame_body, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor1, fg=cor4,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_15.place(x=175, y=158)
b_16 = Button(frame_body, command=lambda: entrar_valores('0'), text="0", width=12, height=2, bg=cor5,
              font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=210)
b_17 = Button(frame_body, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor5, font='Ivy 13 bold',
              relief=RAISED, overrelief=RIDGE)
b_17.place(x=117, y=210)
b_18 = Button(frame_body, command=calcular, text="=", width=5, height=2, bg=cor1, fg=cor4, font='Ivy 13 bold',
              relief=RAISED, overrelief=RIDGE)
b_18.place(x=175, y=210)

# Eventos

principal.bind("<Button-1>", clique_esq_mouse)

principal.mainloop()