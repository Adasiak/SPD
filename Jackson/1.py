from queue import Queue

def jackson_algorithm(graph):
    # Inicjalizujemy zbiory S i T
    S = set()
    T = set(graph.keys())

    # Sprawdzamy, czy graf jest spójny
    if not is_connected(graph):
        return None

    # Dopóki T nie jest pusty
    while T:
        # Wybieramy wierzchołek z T o najmniejszym stopniu
        v = min(T, key=lambda x: len(graph[x]))

        # Usuwamy wybrany wierzchołek z T
        T.remove(v)

        # Dodajemy wybrany wierzchołek do S
        S.add(v)

        # Szukamy krawędzi z S do T
        queue = Queue()
        queue.put(v)
        while not queue.empty():
            u = queue.get()
            for w in graph[u]:
                if w in T:
                    T.remove(w)
                    S.add(w)
                    queue.put(w)

    # Zwracamy nacięcie minimalne
    return S

def is_connected(graph):
    # Sprawdzamy, czy graf jest spójny
    if not graph:
        return False
    visited = set()
    queue = Queue()
    queue.put(next(iter(graph)))
    while not queue.empty():
        u = queue.get()
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                queue.put(v)
    return len(visited) == len(graph)

graph1 = {
    0: set(range(1, 6)),
    1: set(range(6, 11)),
    2: set(range(11, 16)),
    3: set(range(16, 21)),
    4: set(range(21, 26)),
    5: set(range(26, 31)),
}

graph2 = {
    0: {1, 4},
    1: {0, 2},
    2: {1, 3},
    3: {2, 4},
    4: {0, 3},
}

print(jackson_algorithm(graph1))