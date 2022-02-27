#---------PINTAR FLECHAS----------#
def Pintar_Flechas(sa,sb,gt,sc,sd,gt1,col, tortab):   # ----->>>> Funcion para pintar las flechas en el tablero
    tortab.up()
    tortab.goto(gt1)
    tortab.down()
    tortab.color(col)
    tortab.begin_fill()
    tortab.seth(sa)
    tortab.fd(80)
    tortab.seth(sb)
    #tortab.fd(200)
    #tortab.fd(240)
    tortab.fd(280)
    tortab.seth(sa)
    tortab.fd(40)
    tortab.goto(0,0)
    tortab.goto(gt)
    tortab.seth(sa)
    tortab.fd(40)
    tortab.seth(sc)
    #tortab.fd(160)
    #tortab.fd(200)
    tortab.fd(240)
    tortab.seth(sd)
    tortab.fd(40)
    tortab.seth(sc)
    tortab.fd(40)
    tortab.end_fill()


#---------DIVIDIR CUADROS----------#
def Div_Cuadros(IrA,a,b, tortab):                       # ----->>>> Funcion para dividir en cuadros al tablero
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

#---------CREAR CUADROS DE PARTIDA----------#
def Cuadros_Partida(IrA,a, tortab):			# ----->>>> Funcion que crea las bases cuadradas de cada pieza
    tortab.begin_fill()
    tortab.up()
    tortab.goto(IrA)
    tortab.down()
    tortab.seth(a)
    tortab.fd(240)
    tortab.lt(90)
    tortab.fd(240)
    tortab.lt(90)
    tortab.fd(240)
    tortab.lt(90)
    tortab.fd(240)
    tortab.end_fill()

#-------DADO-----#
def DADO(dado, color, tortab):
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
