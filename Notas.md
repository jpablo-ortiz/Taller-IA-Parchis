# Representación del estado del juego parchis

- Tablero para cada jugador desde la celda 1 hasta la 68 (1-68)
- 1 Pasillo para cada jugador (va para después de terminar el tablero general) (1-8 la 8 es la meta)
- 1 Celda de inicio para cada jugador
- 1 Celda de fin del tablero para cada jugador (no la del pasillo)
- 2 fichas para cada jugador
- 1 dado para tirar
- Seguros en las celdas 5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68

## Estados

~~~
estado = {
    1: { # Jugador 1
        1: { # Ficha 1
            'tipo': 'tablero', # tablero, pasillo, casa, meta
            'casilla': 1, # numero de casilla 1-68 o 1-8
        },
        2: { # Ficha 2
            'tipo': 'tablero', # tablero, pasillo, casa, meta
            'casilla': 1, # numero de casilla 1-68 o 1-8
        }
    },
    2: { # Jugador 2
        1: { # Ficha 1    
            'tipo': 'tablero', # tablero, pasillo, casa, meta
            'casilla': 1, # numero de casilla 1-68 o 1-8
        },
        2: { # Ficha 2
            'tipo': 'tablero', # tablero, pasillo, casa, meta
            'casilla': 1,# numero de casilla 1-68 o 1-8
        }
    }
}

~~~

## Acciones

~~~
jugador = 1  # 1 -> '1 - MAX', 2 -> '2 - MIN'
mover   = 1  # 1 - 6 casillas
ficha   = 1  # 1 - 2 ficha

accion = {
    "jugador": jugador,
    "mover":   mover,
    "ficha":   ficha,
}
~~~

## Constantes
~~~
celda_inicio_1 = 5  # Amarillo
celda_fin_1    = 68 # Amarillo

celda_inicio_2 = 22 # Azul
celda_fin_2    = 17 # Azul

seguros = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68]
~~~
# Reglas

https://enszink.blogspot.com/2019/03/luisa-parchis.html

# Reglas aplicadas
1. Si una ficha cae en una casilla blanca y numerada ocupada por una ficha de otro color (siempre hacia delante), se la comerá. La ficha comida irá a su casa original (de su mismo color).
2. En las salidas y en los seguros no es posible comer y por tanto pueden estar dos fichas de colores diferentes.
3. El jugador que saca un 5 con el dado puede sacar ficha de su casa a la casilla de salida.
4. #TODO - Al sacar 5 en la primera jugada, se ponen 2 fichas en la salida.
5. Cuando un jugador tiene una ficha o todas sus fichas en el pasillo de meta o en meta , y no saca la puntuación exacta para introducir alguna ficha en meta, se deberá "rebotar" con una ficha de las que queden por llegar a meta. El "rebote" consiste en contar la tirada del dado hasta la meta y luego retroceder por las casillas del pasillo de meta hasta completar el valor del dado.

## Reglas desconocidas
- Se emplean las palabras comer o capturar cuando una ficha ocupa la posición de una ficha contraria, moviéndose esta última a su casa.
- Se avanzarán 20 casillas en el caso de comer una ficha distinta a la tuya
- Antes de comenzar la partida Los jugadores lanzarán el dado y quien obtenga la mayor puntuación será quien comience la partida.
- La partida se desarrolla por turnos. Cada jugador lanzará el dado una sola vez en cada turno. Una vez jugado su turno, si sacó un 6, el jugador repetirá el turno.
- Una ficha debe rebotar, es decir, retroceder en el caso de que al tirar los dados se encuentre con una casilla en la que ya existan 2 fichas formando una barrera o puente; salvo el caso especial de que, al obtener un 5, haya fichas contrarias en la salida del jugador que saca ficha. Sólo la casa y la meta pueden contener 3 o 4 fichas. Esta regla prevalece sobre otras. 
- El jugador que saca un 5 con el dado puede sacar ficha de su casa a la casilla de salida. Si esto no fuera posible porque ya hay dos fichas de su mismo color en la salida o porque ya no dispone de más fichas para sacar, tendrá que mover 5 casillas con otra ficha. Al sacar 5 en la primera jugada, se ponen 2 fichas en la salida. Si se da el caso de que 2 fichas de otro color se encuentran en la casilla de salida de otra, y esta otra saca un 5, una de las dos anteriores (la que esté más tiempo) deberá ser devuelta a su casa permitiendo que quien ha sacado un 5 pueda poner su ficha.
- El jugador que saque un 6 avanzará una de sus fichas seis casillas si tiene fichas en su casa. En el caso de que no tenga fichas en casa se contará 12 (esta es la regla más comúnmente seguida, aunque tiene alguna variante).
- El jugador que saque un 6 podrá repetir turno. Si saca otro 6 podrá volver a repetir.
- Si saca un 6 en la tercera tirada, la última ficha que movió volverá a casa,exceptuando si la última ficha que movió ya estaba en el color de su meta, en este caso la ficha permanecerá en en su lugar y pasará el turno al siguiente jugador.