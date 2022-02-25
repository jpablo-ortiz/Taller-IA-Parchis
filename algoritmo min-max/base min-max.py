# Diseño del algorítmo min-máx
class Problema:
    def __init__(self, jugador_max, jugador_min, raiz):
        self.raiz = raiz
        self.jugador_max = jugador_max
        self.jugador_min = jugador_min
    
    def resultado(self, estado, accion):
        # TODO: Implementar
        # Dar resultado del nuevo estado dados el estado actual y la acción
        pass

def generar_acciones(estado):
    # TODO: Generar acciones posibles
    return []

def verificar_acciones(acciones):
    # TODO: Verificar acciones
    return []

def MIN(problema: Problema, estado):
    if problema.es_objetivo(estado):
        return problema.utilidad(estado)

    menor_utilidad = float("inf")

    for accion in verificar_acciones(generar_acciones(estado)):
        resultado = problema.resultado(estado, accion)
        utilidad = MAX(problema, resultado)
        if utilidad < menor_utilidad:
            menor_utilidad = utilidad

    return menor_utilidad


def MAX(problema: Problema, estado):
    if problema.es_objetivo(estado):
        return problema.utilidad(estado)

    mayor_utilidad = float("-inf")

    for accion in verificar_acciones(generar_acciones(estado)):
        resultado = problema.resultado(estado, accion)
        utilidad = MIN(problema, resultado)

        if utilidad > mayor_utilidad:
            mayor_utilidad = utilidad
    
    return mayor_utilidad


def MINMAX(problema: Problema):
    mejor_accion = None
    mejor_utilidad = 0
    inicial = problema.nodo_raiz.estado

    for accion in verificar_acciones(generar_acciones(inicial)):
        resultado = problema.resultado(inicial, accion)
        utilidad = MIN(problema, resultado)

        if utilidad > mejor_utilidad:
            mejor_accion = accion
            mejor_utilidad = utilidad

    return mejor_accion
