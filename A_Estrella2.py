import heapq

def a_star_search(graph, dlrs, start, goal):
    # Inicialización de variables
    open_set = [(0, start)]  # Cola de prioridad con el nodo inicial y su costo estimado
    came_from = {}  # Diccionario para rastrear el camino
    g_score = {node: float('inf') for node in graph}  # Costo real desde el inicio hasta el nodo actual
    g_score[start] = 0

    # Función heurística (valor h) basada en dlrs
    def heuristic(node):
        return dlrs[node][goal]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruir y devolver el camino si se alcanza el objetivo
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + dlrs[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                # Se encontró un camino mejor
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))

    # No se encontró un camino
    return None

# Definir el grafo del problema
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

# Ejemplo de uso
estado_inicial = "H"
estado_objetivo = "J"
camino = a_star_search(problema, dlrs, estado_inicial, estado_objetivo)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino desde {} hasta {}".format(estado_inicial, estado_objetivo))
