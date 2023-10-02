import heapq

def primero_mejor(grafo, inicio, meta):
    visitados = set()
    priority_queue = [(0, inicio, [inicio])]
    
    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        
        if node not in visitados:
            visitados.add(node)
            print(f"Visitando nodo: {node}")
            
            if node == meta:
                print("Camino: ", ' -> '.join(path))
                return True
            
            neighbors = grafo.get(node, {})
            for neighbor, weight in sorted(neighbors.items(), key=lambda x: x[1]):
                if neighbor not in visitados:
                    new_path = path + [neighbor]
                    priority = weight  # Utilizamos el peso del enlace como valor heurístico
                    heapq.heappush(priority_queue, (priority, neighbor, new_path))
    
    print("No se encontró el objetivo")
    return False

# Grafo
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


nodo_inicial = 'H'
nodo_meta = 'J'

primero_mejor(grafo, nodo_inicial, nodo_meta)
