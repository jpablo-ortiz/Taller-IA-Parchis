from components.gui_components import (Cuadros_Partida, Div_Cuadros,
                                       Pintar_Flechas)


def Cuadro_Color(x, y, color, tortab):
    # desfase para las celdas
    d = 40
    tortab.up()
    tortab.end_fill()
    tortab.color("black", color)
    tortab.goto(x-d, y)
    tortab.down()
    tortab.begin_fill()
    tortab.goto(x-(2*d), y)
    tortab.goto(x-(2*d), y-d)
    tortab.goto(x-d,     y-d)
    tortab.goto(x-d,     y)
    tortab.end_fill()

def pintar_pantalla_inicial(tortab):
    # desfase para las celdas
    d = 40
    Pintar_Flechas(-90,0,(-60,60),180,90,(-260-d-d,60),'red', tortab)			#Pinta la flecha Roja
    Pintar_Flechas(180,-90,(60,60),90,0,(60,260+d+d),'blue', tortab)			#Pinta la flecha Verde
    Pintar_Flechas(90,180,(60,-60),0,-90,(260+d+d,-60),'yellow', tortab)			#Pinta la flecha Azul
    Pintar_Flechas(0,90,(-60,-60),-90,180,(-60,-260-d-d),'green', tortab)		#Pinta la flecha Amarilla

    Cuadro_Color(-140, 60, 'gray', tortab)
    Cuadro_Color(260, -20, 'gray', tortab)
    Cuadro_Color(100, 220, 'gray', tortab)
    Cuadro_Color(20, -180, 'gray', tortab)

    Cuadro_Color(-300, 20, 'gray', tortab)
    Cuadro_Color(420, 20, 'gray', tortab)
    Cuadro_Color(60, 380, 'gray', tortab)
    Cuadro_Color(60, -340, 'gray', tortab)

    tortab.color('black')

    Div_Cuadros((-380,60),90,-90, tortab)
    Div_Cuadros((-340,60),90,-90, tortab)
    Div_Cuadros((-300,60),90,-90, tortab)						#Divide en cuadritos el lado Rojo
    Div_Cuadros((-260,60),90,-90, tortab)
    Div_Cuadros((-220,60),90,-90, tortab)
    Div_Cuadros((-180,60),90,-90, tortab)
    Div_Cuadros((-140,60),90,-90, tortab)
    Div_Cuadros((-100,60),90,-90, tortab)

    Cuadro_Color(-140, -20, 'red', tortab)
    Cuadro_Color(-260, 60, 'white', tortab)

    Div_Cuadros((380,-60),90,90, tortab)
    Div_Cuadros((340,-60),90,90, tortab)
    Div_Cuadros((300,-60),90,90, tortab)						#Divide en cuadritos el lado Azul
    Div_Cuadros((260,-60),90,90, tortab)
    Div_Cuadros((220,-60),90,90, tortab)
    Div_Cuadros((180,-60),90,90, tortab)
    Div_Cuadros((140,-60),90,90, tortab)
    Div_Cuadros((100,-60),90,90, tortab)

    Cuadro_Color(260, 60, 'yellow', tortab)
    Cuadro_Color(380,-20, 'white', tortab)

    Div_Cuadros((60,380),90,180, tortab)
    Div_Cuadros((60,340),90,180, tortab)
    Div_Cuadros((60,300),90,180, tortab)						#Divide en cuadritos el lado Amarillo
    Div_Cuadros((60,260),90,180, tortab)
    Div_Cuadros((60,220),90,180, tortab)
    Div_Cuadros((60,180),90,180, tortab)
    Div_Cuadros((60,140),90,180, tortab)
    Div_Cuadros((60,100),90,180, tortab)

    Cuadro_Color(20, 220, 'blue', tortab)
    Cuadro_Color(100, 340, 'white', tortab)

    Div_Cuadros((-60,-380),90,0, tortab)
    Div_Cuadros((-60,-340),90,0, tortab)
    Div_Cuadros((-60,-300),90,0, tortab)			                        #Divide en cuadritos el lado Verde
    Div_Cuadros((-60,-260),90,0, tortab)
    Div_Cuadros((-60,-220),90,0, tortab)
    Div_Cuadros((-60,-180),90,0, tortab)
    Div_Cuadros((-60,-140),90,0, tortab)
    Div_Cuadros((-60,-100),90,0, tortab)

    Cuadro_Color(100, -180, 'green', tortab)
    Cuadro_Color(20, -300, 'white', tortab)

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

    tortab.color('black','blue')					        #Creacion de los cuadros de colores
    Cuadros_Partida((-340,100),0, tortab)
    tortab.color('black','green')
    Cuadros_Partida((340,-100),180, tortab)
    tortab.color('black','yellow')
    Cuadros_Partida((100,340),-90, tortab)
    tortab.color('black','red')
    Cuadros_Partida((-100,-340),90, tortab)
    tortab.hideturtle()
