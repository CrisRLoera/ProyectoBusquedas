import heapq


def astar(grafo, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in grafo}
    g_score[start] = 0
    f_score = {node: float('inf') for node in grafo}
    f_score[start] = 0  
   
    nodos_recorridos = []


    while open_set:
        _, current = heapq.heappop(open_set)
        nodos_recorridos.append(current)


        if current == goal:
            return reconstruct_path(came_from, current), nodos_recorridos


        for neighbor, cost in grafo[current].items():
            tentative_g_score = g_score[current] + cost


            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))


    return None, nodos_recorridos


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))


grafo = {
    'H': {'E': 4.0, 'B': 3.2, 'F': 3.5},
    'E': {'H': 4.0, 'A': 4.5, 'C': 3.4},
    'B': {'H': 3.2, 'F': 2.3},
    'F': {'H': 3.5, 'B': 2.3, 'G': 5.3},
    'A': {'E': 4.5, 'G': 3.0},
    'C': {'E': 3.4, 'D': 3.8, 'I': 4.0},
    'G': {'F': 5.3, 'A': 3.0, 'J': 6.8},
    'D': {'C': 3.8, 'J': 4.6},
    'I': {'C': 4.0, 'J': 6.4},
    'J': {'I': 6.4, 'D': 4.6, 'G': 6.8}
}


ini = input("Introduce el nodo inicial: ").upper()
meta = input("Introduce el nodo objetivo: ").upper()
camino, nodos_recorridos = astar(grafo, ini, meta)


if camino:
    print(f"Nodos recorridos: {nodos_recorridos}")
    print(f"Camino de {ini} a {meta}: {camino}")
else:
    print(f"No se encontró un camino de {ini} a {meta}.")
