import math

# Una clase para representar los estados en las listas
class Estado:
    def __init__(self, nombre, padre, g, f):
        self.nombre = nombre
        self.padre = padre
        self.g = g
        self.f = f

# Esta función devuelve a los hijos de un estado
def get_hijos(estado, grafo):
    return grafo[estado]

# Esta función devuelve el mejor estado en la lista
def siguiente(abiertos):
    mejor = None
    vmejor = math.inf
    indMejor = -1
    for indi, esta in enumerate(abiertos):
        if esta.f <= vmejor:
            vmejor = esta.f
            mejor = esta
            indMejor = indi
    if mejor:
        nAbiertos = abiertos[:indMejor] + abiertos[indMejor + 1:]
    else:
        nAbiertos = abiertos
    return mejor, nAbiertos

# Esta función indica si un estado es parte de una lista
def es_miembro(nodo, lista):
    for indi, dato in enumerate(lista):
        if dato.nombre == nodo:
            return True, indi
    return False, -1

# Esta función expande un estado
def expandir(actual, meta, problema, dlrs, abiertos, cerrados):
    nAbiertos = abiertos
    nCerrados = cerrados
    hijos = get_hijos(actual.nombre, problema)
    for hijo in hijos:
        gHijo = actual.g + dlrs[actual.nombre][hijo]
        hHijo = dlrs[hijo][meta]
        fHijo = gHijo + hHijo
        enCerr, _ = es_miembro(hijo, nCerrados)
        if not enCerr:
            enAbi, indAbi = es_miembro(hijo, nAbiertos)
            if enAbi:
                ori = nAbiertos[indAbi]
                if fHijo < ori.f:
                    nAbiertos[indAbi] = Estado(hijo, actual.nombre, gHijo, fHijo)
            else:
                nAbiertos.append(Estado(hijo, actual.nombre, gHijo, fHijo))
    nCerrados.append(actual)
    return nAbiertos, nCerrados

# Esta función implementa la búsqueda primero por lo mejor
def a_star(ini, meta, problema, dlrs):
    actual = Estado(ini, ini, 0, dlrs[ini][meta])
    abiertos = [actual]
    cerrados = []
    listo = False
    while not listo:
        actual, abiertos = siguiente(abiertos)
        if actual.nombre == meta:
            listo = True
            cerrados.append(actual)
        else:
            abiertos, cerrados = expandir(actual, meta, problema, dlrs, abiertos, cerrados)
    return cerrados

# Esta función forma el camino a partir de Cerrados
def get_camino(ini, meta, cerrados):
    resp = []
    actual = meta
    listo = False
    while not listo:
        for nodo in cerrados:
            if nodo.nombre == actual:
                resp.insert(0, nodo.nombre)
                actual = nodo.padre
                break
        if actual == ini:
            listo = True
            resp.insert(0, actual)
    return resp

# El punto de entrada al programa
if __name__ == "__main__":
    # El grafo del problema
    problema = {
        "A": ["B", "C", "D"],
        "B": ["A", "C", "E"],
        "C": ["A", "B", "D", "E"],
        "D": ["A", "C", "F"],
        "E": ["B", "C", "F"],
        "F": ["D", "E"]
    }

    # Las distancias entre estados
    dlrs = {
        "A": {"A": 0, "B": 5, "C": 8, "D": 6, "E": 13, "F": 18},
        "B": {"A": 5, "B": 0, "C": 6, "D": 10, "E": 5, "F": 15},
        "C": {"A": 8, "B": 6, "C": 0, "D": 7, "E": 7, "F": 14},
        "D": {"A": 6, "B": 10, "C": 7, "D": 0, "E": 12, "F": 10},
        "E": {"A": 13, "B": 5, "C": 7, "D": 12, "E": 0, "F": 8},
        "F": {"A": 18, "B": 15, "C": 14, "D": 10, "E": 8, "F": 0}
    }

    print("Busqueda A*!!!")
    cerrados = a_star("A", "F", problema, dlrs)
    soln = get_camino("A", "F", cerrados)
    print(soln)
