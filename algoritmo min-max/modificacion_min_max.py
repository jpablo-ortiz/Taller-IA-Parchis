from copy import deepcopy

# Variables globales
seguros = [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68]

def copiar(estado):
    return {
        1: { # Jugador 1
            1: { # Ficha 1
                'tipo': estado[1][1]['tipo'],
                'casilla': estado[1][1]['casilla']
            },
            2: { # Ficha 2
                'tipo': estado[1][2]['tipo'],
                'casilla': estado[1][2]['casilla']
            }
        },
        2: { # Jugador 2
            1: { # Ficha 1    
                'tipo': estado[2][1]['tipo'],
                'casilla': estado[2][1]['casilla']
            },
            2: { # Ficha 2
                'tipo': estado[2][2]['tipo'],
                'casilla': estado[2][2]['casilla']
            }
        }
    }

class Jugador():
    def __init__(self, id, casilla_inicio, casilla_fin, nombre = None):
        self.id = id
        self.casilla_inicio = casilla_inicio
        self.casilla_fin = casilla_fin
        self.nombre = nombre

class Nodo():
    def __init__(self, padre, estado, accion, utilidad):
        self.padre = padre
        self.estado = estado
        self.accion = accion
        self.utilidad = utilidad
    
    def generar_acciones(self, jugador: Jugador, mover=None):
        acciones = []
        if mover is None:
            for i in range(6):
                for j in range(2):
                    acciones.append(
                        {
                            "jugador": jugador.id,
                            "mover":   i + 1,
                            "ficha":   j + 1
                        }
                    )
            return acciones
        else:
            for j in range(2):
                acciones.append(
                    {
                        "jugador": jugador.id,
                        "mover":   mover,
                        "ficha":   j + 1
                    }
                )
            return acciones

    def verificar_y_dar_nodos(self, acciones, jugador: Jugador):
        nodos = []
        for accion in acciones:

            # ============ Variables necesarias ============
            #estado_n = self.estado.copy()
            # Copiar correctamente estado
            estado_n = copiar(self.estado)
            enemigo = 1 if accion["jugador"] == 2 else 2   

            if self.estado[accion["jugador"]][accion["ficha"]]['tipo'] == 'tablero':

                # ============ Variables necesarias ============

                casilla_actual = self.estado[accion["jugador"]][accion["ficha"]]['casilla']
                movimientos = accion["mover"]
                casilla_final = (casilla_actual + movimientos) % 68
                if casilla_final == 0:
                    casilla_final = 68

                # ============ Verificación de acciones infactibles ============
                jugador.casilla_inicio
                if jugador.casilla_fin == 68 and jugador.casilla_inicio == 5: # inicio y fin amarillo calculo distinto
                    if 0 < casilla_final <= 5:
                        continue
                elif jugador.casilla_fin < casilla_final <= jugador.casilla_inicio: # El resto este calculo
                    continue # No se puede mover a una casilla antes de la inicial

                # ============ Creación nodo hijo con nuevo estado ============

                # Si en la anterior acción la ficha estaba antes del fin y ahora está después, significa que pasa a estar en pasillo
                if (self.padre.estado[accion["jugador"]][accion["ficha"]]["tipo"] == 'tablero' 
                    and self.padre.estado[accion["jugador"]][accion["ficha"]]["casilla"] <= jugador.casilla_fin 
                    and self.estado[accion["jugador"]][accion["ficha"]]["casilla"] > jugador.casilla_fin):

                    # Cambiar tipo a pasillo y la casilla pasa a rango de 1 a 8
                    estado_n[accion["jugador"]][accion["ficha"]]['tipo'] = 'pasillo'
                    estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = casilla_final - jugador.casilla_fin

                else: # Movimiento dentro del tablero
                    # Cambiar la casilla actual de la ficha
                    estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = casilla_final

                    # R1, R2. Verificar si se come alguna ficha del enemigo
                    for i in range(2):
                        if estado_n[enemigo][i+1]['casilla'] == casilla_final and casilla_final not in seguros:
                            estado_n[enemigo][1]['tipo'] = 'casa'
                            estado_n[enemigo][1]['casilla'] = 0

            elif self.estado[accion["jugador"]][accion["ficha"]]['tipo'] == 'pasillo':

                # ============ Variables necesarias ============

                casilla_actual = self.estado[accion["jugador"]][accion["ficha"]]['casilla']
                movimientos = accion["mover"]
                casilla_final = casilla_actual + movimientos

                # ============ Creación nodo hijo con nuevo estado ============

                if casilla_final < 8:
                    estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = casilla_final
                elif casilla_final == 8:
                    estado_n[accion["jugador"]][accion["ficha"]]['tipo'] = 'meta'
                    estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = 0
                else: # R5. Si se mueve más de la 8va casilla se devuelve la cantidad de casillas que se pasó
                    estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = 8 - (casilla_final - 8)

            elif self.estado[accion["jugador"]][accion["ficha"]]['tipo'] == 'casa':

                # ============ Verificación de acciones infactibles ============

                # R3. Regla para sacar ficha de casa
                if accion["mover"] != 5:
                    continue # No se puede sacar una ficha de la casa al menos que el dado sea 5
                
                # ============ Creación nodo hijo con nuevo estado ============
                estado_n[accion["jugador"]][accion["ficha"]]['tipo'] = 'tablero'
                estado_n[accion["jugador"]][accion["ficha"]]['casilla'] = jugador.casilla_inicio

            nodos.append(Nodo(self, estado_n, accion, 0))

        return nodos

    def obtener_nodos_hijos(self, jugador: Jugador, mover=None):
        acciones = self.generar_acciones(jugador, mover)
        nodos = self.verificar_y_dar_nodos(acciones, jugador)
        return nodos

    def evaluar_utilidad(self, jugador: Jugador):
        utilidad = 0
        enemigo = 1 if jugador.id == 2 else 2   

        # Verificación Fichas Jugador
        for ficha in range(2):

            if self.estado[jugador.id][ficha+1]['tipo'] == 'casa':
                # Si la ficha está en casa -1
                utilidad += -1

            elif self.estado[jugador.id][ficha+1]['tipo'] == 'pasillo':
                # Si la ficha está en pasillo 2
                utilidad += 2

            elif self.estado[jugador.id][ficha+1]['tipo'] == 'tablero':

                # Si la ficha está en el tablero
                utilidad += 1

                # Entre más casillas se mueva más puntos
                utilidad += self.accion['mover']

                # 1. Ficha en seguro +10
                if self.estado[jugador.id][ficha+1]['casilla'] in seguros:
                    utilidad += 16

                # 2. Si la ficha no está en seguro mirar las fichas enemigas que estén a 6 o menos casillas de distancia (-8 x ficha enemiga)
                if self.estado[jugador.id][ficha+1]['casilla'] not in seguros:
                        for ficha_enemiga in range(2):
                            if self.estado[enemigo][ficha+1]['tipo'] == 'tablero':
                                if self.estado[jugador.id][ficha+1]['casilla'] > 6:
                                    if 0 < self.estado[jugador.id][ficha+1]['casilla'] - self.estado[enemigo][ficha_enemiga+1]['casilla'] <= 6:
                                        utilidad += -10
                                else:
                                    if self.estado[enemigo][ficha_enemiga+1]['casilla'] >= 68 - (self.estado[jugador.id][ficha+1]['casilla'] - 6):
                                        utilidad += -10
                                    if self.estado[enemigo][ficha_enemiga+1]['casilla'] <= self.estado[jugador.id][ficha+1]['casilla']:
                                        utilidad += -10

                # 3. Si estoy en un seguro y hay una ficha enemiga en la misma casilla (-5 x ficha enemiga)
                if self.estado[jugador.id][ficha+1]['casilla'] in seguros:
                    for ficha_enemiga in range(2):
                        if self.estado[enemigo][ficha+1]['tipo'] == 'tablero':
                            if self.estado[jugador.id][ficha+1]['casilla'] == self.estado[enemigo][ficha_enemiga+1]['casilla']:
                                utilidad += -5

                # 4. Clasificación de aumento de las piezas atacadas y disminución de las piezas atacantes
                # Esto es si no alcanzamos seguro
                # TODO: si hay tiempo
                #if self.estado[jugador.id][ficha+1]['casilla'] not in seguros:

                # TODO: dudoso esta penalización
                # 5. Penalización fichas rezagadas
                #if self.padre.estado[jugador.id][ficha+1]['tipo'] == 'tablero':
                #    utilidad += 1 - ((self.estado[jugador.id][ficha+1]['casilla'] - self.padre.estado[jugador.id][ficha+1]['casilla']) / 8)
                
                # 6. Si se come una pieza enemiga +27
                for ficha_enemiga in range(2):
                    if self.estado[enemigo][ficha_enemiga+1]['tipo'] == 'tablero' and self.estado[jugador.id][ficha+1]['casilla'] not in seguros:
                        if self.estado[jugador.id][ficha+1]['casilla'] == self.estado[enemigo][ficha_enemiga+1]['casilla']:
                            utilidad += 30

                # 7. Fichas enemigas por delante y por detrás al momento de sacar una ficha de la casa
                if self.padre.estado[jugador.id][ficha+1]['tipo'] == 'casa' and self.estado[jugador.id][ficha+1]['tipo'] == 'tablero':
                                        
                    enemigos_delante = 0
                    enemigos_detras = 0

                    for ficha_enemiga in range(2):
                        if self.estado[enemigo][ficha+1]['tipo'] == 'tablero':

                            # Para revisar los de atrás
                            if self.estado[jugador.id][ficha+1]['casilla'] > 8:
                                if 0 < self.estado[jugador.id][ficha+1]['casilla'] - self.estado[enemigo][ficha_enemiga+1]['casilla'] <= 8:
                                    enemigos_detras += 1
                            else:
                                if self.estado[enemigo][ficha_enemiga+1]['casilla'] >= 68 - (self.estado[jugador.id][ficha+1]['casilla'] - 8):
                                    enemigos_detras += 1
                                elif self.estado[enemigo][ficha_enemiga+1]['casilla'] <= self.estado[jugador.id][ficha+1]['casilla']:
                                    enemigos_detras += 1

                            # Para revisar los de delante
                            if self.estado[jugador.id][ficha+1]['casilla'] < 60:
                                if 0 < self.estado[enemigo][ficha_enemiga+1]['casilla'] - self.estado[jugador.id][ficha+1]['casilla'] <= 8:
                                    enemigos_delante += 1
                            else:
                                if 60 <= self.estado[enemigo][ficha_enemiga+1]['casilla'] <= 68:
                                    enemigos_delante += 1
                                elif 0 <= self.estado[enemigo][ficha_enemiga+1]['casilla'] <= (self.estado[jugador.id][ficha+1]['casilla'] + 8) % 68:
                                    enemigos_delante += 1

                    utilidad += 5*(enemigos_delante) - 10*(enemigos_detras)

        self.utilidad = utilidad
        return utilidad

class Problema:
    def __init__(self, raiz, jugador_max: Jugador, jugador_min: Jugador, jugador_inicial: bool = None):
        self.raiz = raiz
        self.jugador_max = jugador_max
        self.jugador_min = jugador_min
        if jugador_inicial == None:
            self.jugador_inicial = self.jugador_max
        else:
            self.jugador_inicial = self.jugador_max if jugador_inicial else self.jugador_min

    def es_objetivo(self, nodo: Nodo):
        if nodo.estado[1][1]['tipo'] == 'meta' and nodo.estado[1][2]['tipo'] == 'meta':
            return True	
        else:
            return False

    def __str__(self) -> str:
        return 'Problema - Raiz: {} - Jugador Max: {} - Jugador Min: {} - Jugador Inicial: {}'.format(self.raiz, self.jugador_max, self.jugador_min, self.jugador_inicial)

# ===============================================================
# --------------------- Funciones Min Max -----------------------
# ===============================================================

def MAX(problema: Problema, nodo: Nodo, profundidad: int | None):
    if problema.es_objetivo(nodo) or (profundidad != None and profundidad == 0):
        #return nodo.evaluar_utilidad(problema.jugador_max)
        nodo.evaluar_utilidad(problema.jugador_max)
        return nodo

    mayor_utilidad = float("-inf")
    mejor_nodo = None

    for nodo_hijo in nodo.obtener_nodos_hijos(problema.jugador_max): # -> 2 - MIN
        nodo = MIN(problema, nodo_hijo, profundidad-1 if profundidad != None else None)
        if nodo.utilidad > mayor_utilidad:
            mayor_utilidad = nodo.utilidad
            mejor_nodo = nodo
    
    return mejor_nodo

def MIN(problema: Problema, nodo: Nodo, profundidad: int | None):
    if problema.es_objetivo(nodo) or (profundidad != None and profundidad == 0):
        #return nodo.evaluar_utilidad(problema.jugador_max)
        nodo.evaluar_utilidad(problema.jugador_min)
        return nodo

    menor_utilidad = float("inf")
    mejor_nodo = None

    for nodo_hijo in nodo.obtener_nodos_hijos(problema.jugador_min): # -> 1 - MÁX
        nodo = MAX(problema, nodo_hijo, profundidad-1 if profundidad != None else None)
        if nodo.utilidad < menor_utilidad:
            menor_utilidad = nodo.utilidad
            mejor_nodo = nodo

    return mejor_nodo

def MINMAX(problema: Problema, profundidad = None, mover = None) -> Nodo:
    nodo_inicial: Nodo = problema.raiz
    mejor_nodo: Nodo = None
    mayor_utilidad = float("-inf")
    menor_utilidad = float("inf")

    # Los nodos hijos son nodos que al realizar una acción, se obtiene un nuevo estado
    if problema.jugador_inicial == problema.jugador_max:
        for nodo_hijo in nodo_inicial.obtener_nodos_hijos(problema.jugador_max, mover):
            nodo_hijo = MIN(problema, nodo_hijo, profundidad)
            if nodo_hijo.utilidad > mayor_utilidad:
                mayor_utilidad = nodo_hijo.utilidad
                mejor_nodo = nodo_hijo
    else:
        for nodo_hijo in nodo_inicial.obtener_nodos_hijos(problema.jugador_min, mover):
            nodo_hijo = MAX(problema, nodo_hijo, profundidad)
            if nodo_hijo.utilidad < menor_utilidad:
                menor_utilidad = nodo_hijo.utilidad
                mejor_nodo = nodo_hijo
    return mejor_nodo