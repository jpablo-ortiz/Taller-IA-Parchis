class Nodo():
    def __init__(self, padre, estado, accion):
        self.padre = padre
        self.estado = estado
        self.accion = accion

class FronteraPila():
    def __init__(self):
        self.frontera = []

    def agregar(self, nodo):
        self.frontera.append(nodo)

    def estaVacia(self):
        return len(self.frontera) == 0

    def eliminar(self):
        if self.estaVacia():
            raise("Frontera Vacía")
        else:
            nodo = self.frontera[-1]
            self.frontera = self.frontera[:-1]
            return nodo

    def contieneEstado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class FronteraCola(FronteraPila):
    def eliminar(self):
        if self.estaVacia():
            raise("Frontera Vacía")
        else:
            nodo = self.frontera[0]
            self.frontera = self.frontera[1:]
            return nodo


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
