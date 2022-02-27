import turtle
from random import *
from tkinter import *

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

        #---------PINTAR FLECHAS----------#
        def Pintar_Flechas(sa,sb,gt,sc,sd,gt1,col):   # ----->>>> Funcion para pintar las flechas en el tablero
                tortab.up()
                tortab.goto(gt1)
                tortab.down()
                tortab.color(col)
                tortab.begin_fill()
                tortab.seth(sa)
                tortab.fd(80)
                tortab.seth(sb)
                tortab.fd(200)
                tortab.seth(sa)
                tortab.fd(40)
                tortab.goto(0,0)
                tortab.goto(gt)
                tortab.seth(sa)
                tortab.fd(40)
                tortab.seth(sc)
                tortab.fd(160)
                tortab.seth(sd)
                tortab.fd(40)
                tortab.seth(sc)
                tortab.fd(40)
                tortab.end_fill()

        Pintar_Flechas(-90,0,(-60,60),180,90,(-260,60),'red')			#Pinta la flecha Roja
        Pintar_Flechas(180,-90,(60,60),90,0,(60,260),'green')			#Pinta la flecha Verde
        Pintar_Flechas(90,180,(60,-60),0,-90,(260,-60),'blue')			#Pinta la flecha Azul
        Pintar_Flechas(0,90,(-60,-60),-90,180,(-60,-260),'yellow')		#Pinta la flecha Amarilla

        #---------DIVIDIR CUADROS----------#
        def Div_Cuadros(IrA,a,b):                       # ----->>>> Funcion para dividir en cuadros al tablero
                tortab.up()
                tortab.goto(IrA)
                tortab.down()
                tortab.seth(b)
                i = 0
                while i < 4:
                        tortab.fd(40)
                        tortab.lt(a)
                        i += 1
                tortab.seth(b)
                tortab.fd(40)
                i = 0
                while i < 4:
                        tortab.fd(40)
                        tortab.lt(a)
                        i += 1
                tortab.seth(b)
                tortab.fd(40)
                i = 0
                while i < 4:
                        tortab.fd(40)
                        tortab.lt(a)
                        i += 1
                        
        tortab.color('black')
        Div_Cuadros((-300,60),90,-90)						#Divide en cuadritos el lado Rojo
        Div_Cuadros((-260,60),90,-90)
        Div_Cuadros((-220,60),90,-90)
        Div_Cuadros((-180,60),90,-90)
        Div_Cuadros((-140,60),90,-90)
        Div_Cuadros((-100,60),90,-90)
        Div_Cuadros((300,-60),90,90)						#Divide en cuadritos el lado Azul
        Div_Cuadros((260,-60),90,90)
        Div_Cuadros((220,-60),90,90)
        Div_Cuadros((180,-60),90,90)
        Div_Cuadros((140,-60),90,90)
        Div_Cuadros((100,-60),90,90)
        Div_Cuadros((60,300),90,180)						#Divide en cuadritos el lado Amarillo
        Div_Cuadros((60,260),90,180)
        Div_Cuadros((60,220),90,180)
        Div_Cuadros((60,180),90,180)
        Div_Cuadros((60,140),90,180)
        Div_Cuadros((60,100),90,180)
        Div_Cuadros((-60,-300),90,0)			                        #Divide en cuadritos el lado Verde
        Div_Cuadros((-60,-260),90,0)
        Div_Cuadros((-60,-220),90,0)
        Div_Cuadros((-60,-180),90,0)
        Div_Cuadros((-60,-140),90,0)
        Div_Cuadros((-60,-100),90,0)	

        #---------DIVIDIR TRIANGULOS----------#
        tortab.up()				                                #Divide los triangulos del centro
        tortab.goto(-60,60)
        tortab.down()
        tortab.goto(60,-60)
        tortab.up()
        tortab.goto(60,60)
        tortab.down()
        tortab.goto(-60,-60)

        tortab.up()
        tortab.end_fill()
        tortab.color("black", "white")
        tortab.goto(20, 20)
        tortab.down()
        tortab.begin_fill()
        tortab.goto(-20, 20)
        tortab.goto(-20, -20)
        tortab.goto(20, -20)
        tortab.goto(20, 20)
        tortab.end_fill()

        #---------CREAR CUADROS DE PARTIDA----------#
        def Cuadros_Partida(IrA,a):			# ----->>>> Funcion que crea las bases cuadradas de cada pieza							
                tortab.begin_fill()
                tortab.up()
                tortab.goto(IrA)
                tortab.down()
                tortab.seth(a)
                tortab.fd(80)
                tortab.lt(90)
                tortab.fd(80)
                tortab.lt(90)
                tortab.fd(80)
                tortab.lt(90)
                tortab.fd(80)
                tortab.end_fill()

        tortab.color('black','red')					        #Creacion de los cuadros de colores
        Cuadros_Partida((-300,100),0)
        tortab.color('black','blue')
        Cuadros_Partida((300,-100),180)
        tortab.color('black','green')
        Cuadros_Partida((100,300),-90)
        tortab.color('black','yellow')
        Cuadros_Partida((-100,-300),90)
        tortab.hideturtle()

        #-------DADO-----#
        def DADO(dado, color):
                tortab.begin_fill()
                tortab.up()
                tortab.goto(20, 20)
                tortab.color("black", "white")
                tortab.down()
                tortab.goto(-20, 20)
                tortab.goto(-20, -20)
                tortab.goto(20, -20)
                tortab.goto(20, 20)
                tortab.end_fill()
                tortab.color("black" , color)
                def uno():
                        tortab.up()
                        tortab.goto(0, -1)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                def dos():
                        tortab.up()
                        tortab.goto(-7, 7)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                        tortab.up()
                        tortab.goto(7, -9)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                def cuatro():
                        tortab.up()
                        tortab.goto(7, 7)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                        tortab.up()
                        tortab.goto(-7, -9)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                        dos()
                def seis():
                        tortab.up()
                        tortab.goto(7, -1)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                        tortab.up()
                        tortab.goto(-7, -1)
                        tortab.down()
                        tortab.begin_fill()
                        tortab.circle(2)
                        tortab.end_fill()
                        cuatro()
                if dado == 6:
                        seis()
                elif dado == 5:
                        cuatro()
                        uno()
                elif dado == 4:
                        cuatro()
                elif dado == 3:
                        dos()
                        uno()
                elif dado == 2:
                        dos()
                elif dado == 1:
                        uno()
                        
        #----------MOVER PIEZA---------#
        def MoverPieza(x, y, dado, color, Ganador):            # ----->>>> Funcion que determina donde quedara la pieza, segun el numero del dado
                while dado != 0:
                        #-------------Jugador rojo (1) -Entrada por su color- -------#
                        if x == -240 and y == 30 and color == "red" and dado != 0:
                                y = -10
                                dado -= 1
                        if x < 0 and x >= -240 and y == -10 and color =="red" and dado != 0:
                                x += 40
                                dado -= 1
                                if x == -40 and y == -10 and color == "red" and dado == 0:
                                        return 1, "red"
                                elif x == -40 and y == -10 and color == "red" and dado != 0:
                                        while dado != 0:
                                                x -= 40
                                                dado -= 1

                        #-------------Jugador azul (2) -Entrada por su color- -------#                    
                        if x == 240 and y == -50 and color == "blue" and dado != 0:
                                y = -10
                                dado -= 1
                        if x > 0 and x <= 240 and y == -10 and color =="blue" and dado != 0:
                                x -= 40
                                dado -= 1
                                if x == 40 and y == -10 and color == "blue" and dado == 0:
                                        return 2, "blue"
                                elif x == 40 and y == -10 and color == "blue" and dado != 0:
                                        while dado != 0:
                                                x += 40
                                                dado -= 1

                        #-------------Jugador amarillo (3) -Entrada por su color- -------#
                        if x == -40 and y == -250 and color == "yellow" and dado != 0:
                                x = 0
                                dado -= 1
                        if y < 0 and x == 0 and y >= -250 and color =="yellow" and dado != 0:
                                y += 40
                                dado -= 1
                                if x == 0 and y == -50 and color == "yellow" and dado == 0:
                                        return 3, "yellow"
                                elif x == 0 and y == -50 and color == "yellow" and dado != 0:
                                        while dado != 0:
                                                y -= 40
                                                dado -= 1
                                                
                        #-------------Jugador verde (4) -Entrada por su color- -------#
                        if x == 40 and y == 230 and color == "green" and dado != 0:
                                x = 0
                                dado -= 1
                        if y > 0 and x == 0 and y <= 230 and color =="green" and dado != 0:
                                y -= 40
                                dado -= 1
                                if x == 0 and y == 30 and color == "green" and dado == 0:
                                        return 4, "green"
                                elif x == 0 and y == 30 and color == "green" and dado != 0:
                                        while dado != 0:
                                                y += 40
                                                dado -= 1
                                                
                        if x <= 0 and y <= 0:                 # ----->>>> Cada 'if' que tenga un 'and' es una esquina (aun que tambien hay coordenadas con numeros '0').
                                if x == -280 and y == -50:    # ----->>>> Si se esta en un eje 'x' que cumple alguna condicional, la pieza sube o baja (depende de 'x') por 
                                        x += 40                     #>>>> el eje 'y', hasta llegar a un eje 'y' que cumpla una condicional. Si esto ocurre, la pieza se
                                        dado -= 1                   #>>>> mueve por el eje 'x'. Es un ciclo. Por cada movimiento, el dado se resta en 1, hasta llegar a '0'.
                                elif x == -40 and y == -50:
                                        y -= 40
                                        dado -= 1
                                elif x == -40 and y == -290:  # ----->>>> Los 'or' son coordenadas que no corresponden a esquinas, los cuales siempre se cumplen. A menos que
                                        x += 40                     #>>>> se encuentre una esquina, en cuyo caso, la pieza cambia su movimiento del eje 'x' al 'y' y 'y' al 'x'.
                                        dado -= 1
                                elif x == 0 and y == -290:
                                        x += 40
                                        dado -= 1
                                elif x == -280 or x == -40:
                                        y -= 40
                                        dado -= 1
                                elif y == -50 or y == -290:
                                        x += 40
                                        dado -= 1
                        elif x <= 0 and y >= 0:
                                if x == -280 and y == 30:
                                        y -= 40
                                        dado -= 1
                                elif x == -40 and y == 270:
                                        y -= 40
                                        dado -= 1
                                elif x == -40 and y == 30:
                                        x -= 40
                                        dado -= 1
                                elif x == -280 and y == 0:
                                        x -= 40
                                        dado -= 1
                                elif x == -280 or x == -40:
                                        y -= 40
                                        dado -= 1
                                elif y == 30 or y == 270:
                                        x -= 40
                                        dado -= 1
                        elif x >= 0 and y <= 0:
                                if x == 40 and y == -290:
                                        y += 40
                                        dado -= 1
                                elif x == 40 and y == -50:
                                        x += 40
                                        dado -= 1
                                elif x == 280 and y == -50:
                                        y += 40
                                        dado -= 1
                                elif x == 280 and y == 0:
                                        y += 40
                                        dado -= 1
                                elif x == 280 or x == 40:
                                        y += 40
                                        dado -= 1
                                elif y == -50 or y == -290:
                                        x += 40
                                        dado -= 1
                        elif x >= 0 and y >= 0:
                                if x == 280 and y == 30:
                                        x -= 40
                                        dado -= 1
                                elif x == 40 and y == 30:
                                        y += 40
                                        dado -= 1
                                elif x == 40 and y == 270:
                                        x -= 40
                                        dado -= 1
                                elif x == 0 and y == 270:
                                        x -= 40
                                        dado -= 1
                                elif x == 280 or x == 40:
                                        y += 40
                                        dado -= 1
                                elif y == 30 or y == 270:
                                        x -= 40
                                        dado -= 1
                tortab.begin_fill()                     # ----->>>> Cuando el dado llega a '0', se dibuja la pieza en la coordenada que ha caido
                tortab.up()		
                tortab.goto(x, y)        
                tortab.color("black", color)
                tortab.down()
                tortab.circle(10)
                tortab.end_fill()
                return x, y                             # ----->>>> retorna x, y para sobreescribir la pieza que se esta moviendo

        #---------SOBRE-ESCRIBIR TRIANGULOS--------#
        def Sobre_Escribir(x, y):                       # ----->>>> Funcion para sobreescribe los triangulos
                if x > 0:                                     #>>>> Si una pieza esta en un triangulo (los del centro), estos se limpian para no dejar rastro de la pieza
                        tortab.up()                           #>>>> que estaba en esa posicion.
                        tortab.color("black", "blue")
                        tortab.begin_fill()
                        tortab.goto(60, -60)
                        tortab.down()
                        tortab.goto(60, 60)
                        tortab.goto(20, 20)
                        tortab.goto(20, -20)
                        tortab.goto(60, -60)
                        tortab.end_fill()
                if x < 0:
                        tortab.up()
                        tortab.color("black", "red")
                        tortab.begin_fill()
                        tortab.goto(-60, -60)
                        tortab.down()
                        tortab.goto(-60, 60)
                        tortab.goto(-20, 20)
                        tortab.goto(-20, -20)
                        tortab.goto(-60, -60)
                        tortab.end_fill()
                if y > 0:
                        tortab.up()
                        tortab.color("black", "green")
                        tortab.begin_fill()
                        tortab.goto(60, 60)
                        tortab.down()
                        tortab.goto(-60, 60)
                        tortab.goto(-20, 20)
                        tortab.goto(20, 20)
                        tortab.goto(60, 60)
                        tortab.end_fill()
                if y < 0:
                        tortab.up()
                        tortab.color("black", "yellow")
                        tortab.begin_fill()
                        tortab.goto(-60, -60)
                        tortab.down()
                        tortab.goto(60, -60)
                        tortab.goto(20, -20)
                        tortab.goto(-20, -20)
                        tortab.goto(-60, -60)
                        tortab.end_fill()
                        
        #---------BORRAR PIEZA ANTERIOR----------#
        def Borrar_Pieza(Px, Py):
                color1 = "white"
                color2 = "white"        #-----------------------------------------------Coordenadas de cuadros de colores--------------------------------------------------
                if (Px == -250 and Py == 30) or (Px == -250 and Py == -10) or (Px == -210 and Py == -10) or (Px == -170 and Py == -10) or (Px == -130 and Py == -10) or (Px == -90 and Py == -10):
                        color1 = "red"
                        color2 = "red"
                elif (Px == 230 and Py == -50) or (Px == 230 and Py == -10) or (Px == 190 and Py == -10) or (Px == 150 and Py == -10) or (Px == 110 and Py == -10) or (Px == 70 and Py == -10):
                        color1 = "blue"
                        color2 = "blue"
                elif (Px == -50 and Py == -250) or (Px == -10 and Py == -250) or (Px == -10 and Py == -210) or (Px == -10 and Py == -170) or (Px == -10 and Py == -130) or (Px == -10 and Py == -90):
                        color1 = "yellow"
                        color2 = "yellow"
                elif (Px == -10 and Py == 70) or (Px == -10 and Py == 110) or (Px == -10 and Py == 150) or (Px == -10 and Py == 190) or (Px == -10 and Py == 230) or (Px == 30 and Py == 230):
                        color1 = "green"
                        color2 = "green"
                tortab.begin_fill()
                tortab.up()		
                tortab.goto(Px, Py)
                tortab.color(color1, color2)
                tortab.down()
                
                i = 0
                while i < 4:            #------>>>> Sobre-escribe el cuadro (lo "borra")
                        tortab.fd(20)
                        tortab.lt(90)
                        i += 1
                tortab.end_fill()
                
                if Px == 30 and Py == 30:     #------>>>> Si cae en los triangulos, estos tambien se limpian cuando la pieza no esta. (vuelven a como deberian estar).
                        Sobre_Escribir(Px, Py)
                elif Px == -50 and Py == 30:
                        Sobre_Escribir(Px, Py)
                elif Px == -50 and Py == -50:
                        Sobre_Escribir(Px, Py)
                elif Px == 30 and Py == -50:
                        Sobre_Escribir(Px, Py)

        #-----FUNCION PARA MARCAR AL GANADOR------#
        def Marcar_Ganador(x, y):
                tortab.up()		
                tortab.goto(x, y - 6)        
                tortab.color("white")
                tortab.down()
                tortab.circle(16)
                tortab.end_fill()

        #-----FUNCION PONER FICHA EN EL TRIANGULO GANADOR-----#
        def Poner_pieza_triangulo(centro, color):
                tortab.begin_fill()
                tortab.up()		
                tortab.goto(centro)        
                tortab.color("black", color)
                tortab.down()
                tortab.circle(10)
                tortab.end_fill() 
        def PintarFichas(centro, color):         # ----->>>> Crea las fichas, segun el numero de jugadores. Todas son circulares (pero de diferentes colores).
                tortab.begin_fill()
                tortab.up()		
                tortab.goto(centro)
                tortab.color("black", color)
                tortab.down()
                tortab.circle(10)                # ----->>>> Diametro 20
                tortab.end_fill()
        if jugador > 1:
                PintarFichas((-280, 70), "red")
                PintarFichas((280, -90), "blue")
        if jugador > 2:
                PintarFichas((-80, -290), "yellow")
        if jugador > 3:
                PintarFichas((80, 270), "green")
        #---------SEGUNDA PARTE DEL MENU DE INICIO---------#
        lista_r = [-280, 70]
        lista_b = [280, -90]
        lista_y = [-80, -290]
        lista_g = [80, 270]
        players = [1, 1]
        players[-1] = jugador
        def Jugar(players, lista_r, lista_b, lista_y, lista_g):
            Ganador = "a"
            if players[-2] == players[-1] + 1:        #------>>>> Condicional para no crear mas jugadores que el usuario pide
                players[-2] = 1                                                                    #------>>>> Si es 'l', se tira dado
            dado = randint(1, 6)                                                      #------>>>> Numero obtenido
            if players[-2] == 1:                                       #------>>>> Turno del primer jugador
                    DADO(dado, "red")
                    Borrar_Pieza(lista_r[-2] - 10, lista_r[-1])                    #------>>>> Borra la pieza actual, para dejar la pieza en la siguiente posicion (segun el dado).
                    x, y = MoverPieza(lista_r[-2], lista_r[-1], dado, "red", Ganador)       #------>>>> Mueve pieza a la siguiente posicion (segun dado)
                    if x == 1 and y == "red":
                            color = "red"
                            Ganador = "Roja"
                            players[-2] = 10
                            x, y = -40, -10
                            Poner_pieza_triangulo((x, y), "red")
                            Marcar_Ganador(x, y)
                            return
                    lista_r[-2], lista_r[-1] = x, y                                #------>>>> Sobre escribe la posicion de la pieza actual, por la que se obtuvo con el dado
                    if dado == 6:                                #------>>>> Si sale 6, se repite turno
                            players[-2] = 0
                    if lista_r[-2] == lista_b[-2] and lista_r[-1] == lista_b[-1]:                    #------>>>> Si la posicion obtenida esta siendo usada por otra pieza, esta vuelve a la base
                            lista_b[-2], lista_b[-1] = 280, -90
                            PintarFichas((lista_b[-2], lista_b[-1]), "blue")       #------>>>> Funcion que devuelve la pieza comida a base
                    elif lista_r[-2] == lista_y[-2] and lista_r[-1] == lista_y[-1]:                      #------>>>> lo mismo
                            lista_y[-2], lista_y[-1] = -80, -290
                            PintarFichas((lista_y[-2], lista_y[-1]), "yellow")
                    elif lista_r[-2] == lista_g[-2] and lista_r[-1] == lista_g[-1]:                      #------>>>> lo mismo
                            lista_g[-2], lista_g[-1] = 80, 270
                            PintarFichas((lista_g[-2], lista_g[-1]), "green")
            if players[-2] == 2:                                       #------>>>>                -Turno del segundo jugador-
                    DADO(dado, "blue")
                    Borrar_Pieza(lista_b[-2] - 10, lista_b[-1])
                    x, y = MoverPieza(lista_b[-2], lista_b[-1], dado, "blue", Ganador)
                    if x == 2 and y == "blue":
                            color = "blue"
                            Ganador = "Azul"
                            players[-2] = 10
                            x, y = 40, -10
                            Poner_pieza_triangulo((x, y), "blue")
                            Marcar_Ganador(x, y)
                            return
                    lista_b[-2], lista_b[-1] = x, y
                    if dado == 6:                                #------>>>> ACA SE REPITE EXACTAMENTE LO QUE SE HA HECHO
                        players[-2] = 1
                    if lista_b[-2] == lista_r[-2] and lista_b[-1] == lista_r[-1]:                    #------>>>> ANTERIORMENTE, SOLO QUE PARA EL SEGUNDO JUGADOR.
                            lista_r[-2], lista_r[-1] = -280, 70
                            PintarFichas((lista_r[-2], lista_r[-1]), "red")
                    elif lista_b[-2] == lista_y[-2] and lista_b[-1] == lista_y[-1]:
                            lista_y[-2], lista_y[-1] = -80, -290
                            PintarFichas((lista_y[-2], lista_y[-1]), "yellow")
                    elif lista_b[-2] == lista_g[-2] and lista_b[-1] == lista_g[-1]:
                            lista_g[-2], lista_g[-1] = 80, 270
                            PintarFichas((lista_g[-2], lista_g[-1]), "green")
            if players[-2] == 3:                                       #------>>>>                 -Turno del tercer jugador-
                    DADO(dado, "yellow") 
                    Borrar_Pieza(lista_y[-2] - 10, lista_y[-1])
                    x, y = MoverPieza(lista_y[-2], lista_y[-1], dado, "yellow", Ganador)
                    if x == 3 and y == "yellow":
                            color = "yellow"
                            Ganador = "Amarilla"
                            players[-2] = 10
                            x, y = 0, -50
                            Poner_pieza_triangulo((x, y), "yellow")
                            Marcar_Ganador(x, y)
                            return
                    lista_y[-2], lista_y[-1] = x, y
                    if dado == 6:
                            players[-2] = 2
                    if lista_y[-2] == lista_b[-2] and lista_y[-1] == lista_b[-1]:
                            lista_b[-2], lista_b[-1] = 280, -90
                            PintarFichas((lista_b[-2], lista_b[-1]), "blue")
                    elif lista_y[-2] == lista_r[-2] and lista_y[-1] == lista_r[-1]:
                            lista_r[-2], lista_r[-1] = -280, 70
                            PintarFichas((lista_r[-2], lista_r[-1]), "red")
                    elif lista_y[-2] == lista_g[-2] and lista_y[-1] == lista_g[-1]:
                            lista_g[-2], lista_g[-1] = 80, 270
                            PintarFichas((lista_g[-2], lista_g[-1]), "green")
            if players[-2] == 4:                                       #------>>>>                 -Turno del cuarto jugador-
                    DADO(dado, "green")
                    Borrar_Pieza(lista_g[-2] - 10, lista_g[-1])
                    x, y = MoverPieza(lista_g[-2], lista_g[-1], dado, "green", Ganador)
                    if x == 4 and y == "green":
                            color = "green"
                            Ganador = "Verde"
                            players[-2] = 10
                            x, y = 0, 30
                            Poner_pieza_triangulo((x, y), "green")
                            Marcar_Ganador(x, y)
                            return
                    lista_g[-2], lista_g[-1] = x, y
                    if dado == 6:
                            players[-2] = 3
                    if lista_g[-2] == lista_b[-2] and lista_g[-1] == lista_b[-1]:
                            lista_b[-2], lista_b[-1] = 280, -90
                            PintarFichas((lista_b[-2], lista_b[-1]), "blue")
                    elif lista_g[-2] == lista_y[-2] and lista_g[-1] == lista_y[-1]:
                            lista_y[-2], lista_y[-1] = -80, -290
                            PintarFichas((lista_y[-2], lista_y[-1]), "yellow")
                    elif lista_g[-2] == lista_r[-2] and lista_r[-1] == lista_g[-1]:
                            lista_r[-2], lista_r[-1] = -280, 70
                            PintarFichas((lista_r[-2], lista_r[-1]), "red")
            players[-2] = players[-2] + 1
            
        def MonitorBotones():
            def FunBotons():
                Jugar(players, lista_r, lista_b, lista_y, lista_g)
            return FunBotons

        boton = Button(window, relief = RIDGE, width = 30, height = 20, text = "Click!", command = MonitorBotones())
        boton.config(bg = "black", fg = "white")
        boton.grid(row = 0, column = 0)
            
jugador = [0,1]
def jugador2():
        jugador[-1] = 2
        Maxixd(jugador[-1])
def jugador3():
        jugador[-1] = 3
        Maxixd(jugador[-1])
def jugador4():
        jugador[-1] = 4
        Maxixd(jugador[-1])
        
filemenu.add_command(label = "2 players", command = jugador2)
filemenu.add_command(label = "3 players", command = jugador3)
filemenu.add_command(label = "4 players", command = jugador4)

helpmenu = Menu(menu)
menu.add_cascade(label="Reglas", menu=helpmenu)
helpmenu.add_command(label="1. Numero 6 repite jugada")
helpmenu.add_command(label="2. Caer en una ficha lo envia a base")
helpmenu.add_command(label="3. Para ganar, se debe caer justo en la meta")

window.title('Ludo   by: Foji')
window.mainloop()
