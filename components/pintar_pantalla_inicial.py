from components.gui_components import (Cuadros_Partida, Div_Cuadros,
                                       Pintar_Flechas)


def pintar_pantalla_inicial(tortab):
    Pintar_Flechas(-90,0,(-60,60),180,90,(-260,60),'red', tortab)			#Pinta la flecha Roja
    Pintar_Flechas(180,-90,(60,60),90,0,(60,260),'green', tortab)			#Pinta la flecha Verde
    Pintar_Flechas(90,180,(60,-60),0,-90,(260,-60),'blue', tortab)			#Pinta la flecha Azul
    Pintar_Flechas(0,90,(-60,-60),-90,180,(-60,-260),'yellow', tortab)		#Pinta la flecha Amarilla
                    
    tortab.color('black')
    Div_Cuadros((-300,60),90,-90, tortab)						#Divide en cuadritos el lado Rojo
    Div_Cuadros((-260,60),90,-90, tortab)
    Div_Cuadros((-220,60),90,-90, tortab)
    Div_Cuadros((-180,60),90,-90, tortab)
    Div_Cuadros((-140,60),90,-90, tortab)
    Div_Cuadros((-100,60),90,-90, tortab)
    Div_Cuadros((300,-60),90,90, tortab)						#Divide en cuadritos el lado Azul
    Div_Cuadros((260,-60),90,90, tortab)
    Div_Cuadros((220,-60),90,90, tortab)
    Div_Cuadros((180,-60),90,90, tortab)
    Div_Cuadros((140,-60),90,90, tortab)
    Div_Cuadros((100,-60),90,90, tortab)
    Div_Cuadros((60,300),90,180, tortab)						#Divide en cuadritos el lado Amarillo
    Div_Cuadros((60,260),90,180, tortab)
    Div_Cuadros((60,220),90,180, tortab)
    Div_Cuadros((60,180),90,180, tortab)
    Div_Cuadros((60,140),90,180, tortab)
    Div_Cuadros((60,100),90,180, tortab)
    Div_Cuadros((-60,-300),90,0, tortab)			                        #Divide en cuadritos el lado Verde
    Div_Cuadros((-60,-260),90,0, tortab)
    Div_Cuadros((-60,-220),90,0, tortab)
    Div_Cuadros((-60,-180),90,0, tortab)
    Div_Cuadros((-60,-140),90,0, tortab)
    Div_Cuadros((-60,-100),90,0, tortab)	

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

    tortab.color('black','red')					        #Creacion de los cuadros de colores
    Cuadros_Partida((-300,100),0, tortab)
    tortab.color('black','blue')
    Cuadros_Partida((300,-100),180, tortab)
    tortab.color('black','green')
    Cuadros_Partida((100,300),-90, tortab)
    tortab.color('black','yellow')
    Cuadros_Partida((-100,-300),90, tortab)
    tortab.hideturtle()
