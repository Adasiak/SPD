def jackson_algorithm(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v, graph[u][v]))

    edges.sort(key=lambda e: e[2]) # sortujemy krawędzie według kosztu

    mst = set() # minimalne drzewo rozpinające

    parent = {} # słownik przechowujący rodzica każdego wierzchołka

    def find_parent(node):
        if parent[node] == node:
            return node
        parent[node] = find_parent(parent[node])
        return parent[node]

    for node in graph:
        parent[node] = node # każdy wierzchołek zaczyna jako własny rodzic

    for edge in edges:
        u, v, cost = edge
        if find_parent(u) != find_parent(v): # jeżeli wierzchołki nie są w tym samym zbiorze
            mst.add(edge) # dodajemy krawędź do drzewa rozpinającego
            parent[find_parent(u)] = find_parent(v) # łączymy wierzchołki w jeden zbiór

    return mst

graph1 = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

print(jackson_algorithm(graph1))

import random

n = 10 # liczba wierzchołków
m = 15 # liczba krawędzi

graph2 = {}

for i in range(n):
    graph2[i] = {}

for j in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    cost = random.randint(1, 10)
    graph2[u][v] = cost
    graph2[v][u] = cost

print(jackson_algorithm(graph2))
