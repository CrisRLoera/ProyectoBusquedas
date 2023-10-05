import math

# Una clase para representar los estados en las listas
class Estado:
    def __init__(self, nombre, padre, g, f):
        self.nombre = nombre
        self.padre = padre
        self.g = g
        self.f = f

# Esta función devuelve los hijos de un estado
def get_hijos(estado, grafo):
    return grafo[estado]

# Esta función devuelve el mejor estado en la lista
def siguiente(abiertos):
    v_mejor = -10.0
    mejor = Estado("", "", 0.0, 0.0)
    ind_mejor = -1
    for indi, esta in enumerate(abiertos):
        if esta.f >= v_mejor:
            v_mejor = esta.f
            mejor = esta
            ind_mejor = indi
    n_abiertos = abiertos[:ind_mejor] + abiertos[ind_mejor + 1:]
    return mejor, n_abiertos

# Esta función indica si un estado es parte de una lista
def es_miembro(nodo, lista):
    inde = -1
    miembro = False
    for indi, dato in enumerate(lista):
        if dato.nombre == nodo:
            inde = indi
            miembro = True
            break
    return miembro, inde

# Esta función expande un estado
def expandir(actual, meta, problema, dlrs, abiertos, cerrados):
    n_abiertos = abiertos.copy()
    n_cerrados = cerrados.copy()
    hijos = get_hijos(actual.nombre, problema)
    for hijo in hijos:
        g_hijo = actual.g + dlrs[actual.nombre][hijo]
        h_hijo = dlrs[hijo][meta]
        f_hijo = g_hijo + h_hijo
        en_cerr, _ = es_miembro(hijo, n_cerrados)
        if not en_cerr:
            en_abi, ind_abi = es_miembro(hijo, n_abiertos)
            if en_abi:
                ori = n_abiertos[ind_abi]
                if f_hijo > ori.f:
                    n_abiertos[ind_abi] = Estado(hijo, actual.nombre, g_hijo, f_hijo)
            else:
                n_abiertos.append(Estado(hijo, actual.nombre, g_hijo, f_hijo))
    n_cerrados.append(actual)
    return n_abiertos, n_cerrados

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

# Esta función forma el camino a partir de cerrados
def get_camino(ini, meta, cerrados):
    resp = []
    actual = meta
    listo = False
    while not listo:
        for nodo in cerrados:
            if nodo.nombre == actual:
                resp = [nodo.nombre] + resp
                actual = nodo.padre
                break
        if actual == ini:
            listo = True
            resp = [actual] + resp
    return resp

# El punto de entrada al programa
if __name__ == "__main__":
    # El grafo del problema
    problema = {
        "H": ["E", "B", "F"],
        "E": ["H", "A", "C"],
        "B": ["H", "F"],
        "F": ["H", "B", "G"],
        "A": ["E", "G"],
        "C": ["E", "D", "I"],
        "G": ["F", "A", "J"],
        "D": ["C", "J"],
        "I": ["C", "J"],
        "J": ["I", "D", "G"]
    }

    # Las distancias entre estados
    dlrs = {
        "A": {"A": 0, "B": 1.8, "C": 2.5, "D": 2.8, "E": 4.5, "F": 5.0, "G": 3.0, "H": 5.5, "I":5.8, "J":6.4},
        "B": {"A": 1.8, "B": 0, "C": 4.4, "D": 5.6, "E": 3.5, "F": 2.3, "G": 4.5, "H": 3.2, "I":8.6, "J":10.8},
        "C": {"A": 2.5, "B": 4.4, "C": 0, "D": 3.8, "E": 3.4, "F": 8.0, "G": 6.3, "H": 7.7, "I":4.0, "J":9.5},
        "D": {"A": 2.8, "B": 5.6, "C": 3.8, "D": 0, "E": 7.7, "F": 8.0, "G": 2.8, "H": 10.0, "I":3.0, "J":4.6},
        "E": {"A": 4.5, "B": 3.5, "C": 3.4, "D": 7.7, "E": 0, "F": 6.7, "G": 6.8, "H": 4.0, "I":8.7, "J":13.5},
        "F": {"A": 5.0, "B": 2.3, "C": 8.0, "D": 8.0, "E": 6.7, "F":0, "G": 5.3, "H": 3.5, "I":11.8, "J":12.3},
        "G": {"A": 3.0, "B": 4.5, "C": 6.3, "D": 2.8, "E": 6.8, "F": 5.3, "G": 0, "H": 6.6, "I":7.5, "J":6.8},
        "H": {"A": 5.5, "B": 3.2, "C": 7.7, "D": 10.0, "E": 4.0, "F": 3.5, "G": 6.6, "H": 0, "I":12.5, "J":15.2},
        "I": {"A": 5.8, "B": 8.6, "C": 4.0, "D": 3.0, "E": 8.7, "F": 11.8, "G": 7.5, "H": 12.5, "I":0, "J":6.4},
        "J": {"A": 6.4, "B": 10.8, "C": 9.5, "D": 4.6, "E": 13.5, "F": 12.3, "G": 6.8, "H": 15.2, "I":6.4, "J":0}
    }




    print("Búsqueda A*!!!")
    cerrados = a_star("H", "J", problema, dlrs)
    soln = get_camino("H", "J", cerrados)
    print(soln)
