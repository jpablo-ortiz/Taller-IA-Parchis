from components.gui_components import DADO
from algoritmo_min_max import dar_siguiente_paso


#----------MOVER PIEZA---------#
def MoverPieza(x, y, dado, color, Ganador ,tortab):            # ----->>>> Funcion que determina donde quedara la pieza, segun el numero del dado
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
def Sobre_Escribir(x, y, tortab):                       # ----->>>> Funcion para sobreescribe los triangulos
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
def Borrar_Pieza(Px, Py, tortab):
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
def Marcar_Ganador(x, y, tortab):
        tortab.up()
        tortab.goto(x, y - 6)
        tortab.color("white")
        tortab.down()
        tortab.circle(16)
        tortab.end_fill()

#-----FUNCION PONER FICHA EN EL TRIANGULO GANADOR-----#
def Poner_pieza_triangulo(centro, color, tortab):
        tortab.begin_fill()
        tortab.up()
        tortab.goto(centro)
        tortab.color("black", color)
        tortab.down()
        tortab.circle(10)
        tortab.end_fill()

def PintarFichas(centro, color, tortab):         # ----->>>> Crea las fichas, segun el numero de jugadores. Todas son circulares (pero de diferentes colores).
        tortab.begin_fill()
        tortab.up()
        tortab.goto(centro)
        tortab.color("black", color)
        tortab.down()
        tortab.circle(10)                # ----->>>> Diametro 20
        tortab.end_fill()

def Jugar(players, lista_r, lista_b, lista_y, lista_g, tortab):
        Ganador = "a"
        if players[-2] == players[-1] + 1:        #------>>>> Condicional para no crear mas jugadores que el usuario pide
            players[-2] = 1                       #------>>>> Si es 'l', se tira dado
        dado = dar_siguiente_paso(jugador=players[-2])               #------>>>> Numero obtenido
        if players[-2] == 1:                                       #------>>>> Turno del primer jugador
                DADO(dado, "red", tortab)
                Borrar_Pieza(lista_r[-2] - 10, lista_r[-1], tortab)        #------>>>> Borra la pieza actual, para dejar la pieza en la siguiente posicion (segun el dado).
                x, y = MoverPieza(lista_r[-2], lista_r[-1], dado, "red", Ganador, tortab)       #------>>>> Mueve pieza a la siguiente posicion (segun dado)
                if x == 1 and y == "red":
                        color = "red"
                        Ganador = "Roja"
                        players[-2] = 10
                        x, y = -40, -10
                        Poner_pieza_triangulo((x, y), "red", tortab)
                        Marcar_Ganador(x, y, tortab)
                        return
                lista_r[-2], lista_r[-1] = x, y              #------>>>> Sobre escribe la posicion de la pieza actual, por la que se obtuvo con el dado
                if dado == 6:                                #------>>>> Si sale 6, se repite turno
                        players[-2] = 0
                if lista_r[-2] == lista_b[-2] and lista_r[-1] == lista_b[-1]:      #------>>>> Si la posicion obtenida esta siendo usada por otra pieza, esta vuelve a la base
                        lista_b[-2], lista_b[-1] = 280, -90
                        PintarFichas((lista_b[-2], lista_b[-1]), "blue", tortab)           #------>>>> Funcion que devuelve la pieza comida a base
                elif lista_r[-2] == lista_y[-2] and lista_r[-1] == lista_y[-1]:                      #------>>>> lo mismo
                        lista_y[-2], lista_y[-1] = -80, -290
                        PintarFichas((lista_y[-2], lista_y[-1]), "yellow", tortab)
                elif lista_r[-2] == lista_g[-2] and lista_r[-1] == lista_g[-1]:                      #------>>>> lo mismo
                        lista_g[-2], lista_g[-1] = 80, 270
                        PintarFichas((lista_g[-2], lista_g[-1]), "green", tortab)
        if players[-2] == 2:                                       #------>>>>                -Turno del segundo jugador-
                DADO(dado, "blue", tortab)
                Borrar_Pieza(lista_b[-2] - 10, lista_b[-1], tortab)
                x, y = MoverPieza(lista_b[-2], lista_b[-1], dado, "blue", Ganador, tortab)
                if x == 2 and y == "blue":
                        color = "blue"
                        Ganador = "Azul"
                        players[-2] = 10
                        x, y = 40, -10
                        Poner_pieza_triangulo((x, y), "blue", tortab)
                        Marcar_Ganador(x, y, tortab)
                        return
                lista_b[-2], lista_b[-1] = x, y
                if dado == 6:                                #------>>>> ACA SE REPITE EXACTAMENTE LO QUE SE HA HECHO
                    players[-2] = 1
                if lista_b[-2] == lista_r[-2] and lista_b[-1] == lista_r[-1]:                    #------>>>> ANTERIORMENTE, SOLO QUE PARA EL SEGUNDO JUGADOR.
                        lista_r[-2], lista_r[-1] = -280, 70
                        PintarFichas((lista_r[-2], lista_r[-1]), "red", tortab)
                elif lista_b[-2] == lista_y[-2] and lista_b[-1] == lista_y[-1]:
                        lista_y[-2], lista_y[-1] = -80, -290
                        PintarFichas((lista_y[-2], lista_y[-1]), "yellow", tortab)
                elif lista_b[-2] == lista_g[-2] and lista_b[-1] == lista_g[-1]:
                        lista_g[-2], lista_g[-1] = 80, 270
                        PintarFichas((lista_g[-2], lista_g[-1]), "green", tortab)
        players[-2] = players[-2] + 1

