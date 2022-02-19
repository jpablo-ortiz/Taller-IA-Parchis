import turtle
from tkinter import *

from acciones_parchis import Jugar, PintarFichas
from components.gui_components import DADO
from components.pintar_pantalla_inicial import pintar_pantalla_inicial

window = Tk()
menu = Menu(window)
window.config(menu = menu)
window.config(width = 220, height = 310)
filemenu = Menu(menu)
menu.add_cascade(label = "New Game", menu = filemenu)

#--------PINTAR FICHAS--------#
def Maxixd(jugador):
        game = turtle.Screen()
        tortab = turtle.Turtle()
        tortab.shape ('turtle')
        game.screensize(620,620)
        tortab.speed(0)

        #---------PINTAR TABLERO--------#
        pintar_pantalla_inicial(tortab)

        if jugador > 1:
                PintarFichas((-280, 70), "red", tortab)
                PintarFichas((280, -90), "blue", tortab)

        #---------SEGUNDA PARTE DEL MENU DE INICIO---------#
        lista_r = [-280, 70]
        lista_b = [280, -90]
        lista_y = [-80, -290]
        lista_g = [80, 270]
        players = [1, 1]
        players[-1] = jugador
    
        def MonitorBotones():
            def FunBotons():
                Jugar(players, lista_r, lista_b, lista_y, lista_g, tortab)
            return FunBotons

        boton = Button(window, relief = RIDGE, width = 30, height = 20, text = "Click!", command = MonitorBotones())
        boton.config(bg = "black", fg = "white")
        boton.grid(row = 0, column = 0)
            
jugador = [0,1]
def jugador2():
        jugador[-1] = 2
        Maxixd(jugador[-1])

filemenu.add_command(label = "2 players", command = jugador2)

helpmenu = Menu(menu)
menu.add_cascade(label="Reglas", menu=helpmenu)
helpmenu.add_command(label="1. Numero 6 repite jugada")
helpmenu.add_command(label="2. Caer en una ficha lo envia a base")
helpmenu.add_command(label="3. Para ganar, se debe caer justo en la meta")

window.title('Taller Min Max')
window.mainloop()
