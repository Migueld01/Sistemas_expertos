from collections import deque

def busca_ancho(ni, grafo):
    anterior = set()
    orden = []

    queue = deque([ni])

    while queue:
        nodo = queue.popleft()
        if nodo not in anterior:
            anterior.add(nodo)
            orden.append(nodo)

            for vecino in grafo[nodo]:
                if vecino not in anterior:
                    queue.append(vecino)

    return orden

def bus_ancho(E, ni):
    grafo = {}
    
    for u, v in E:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)

    vertice = busca_ancho(ni, grafo)

    return vertice

E = [('a', 'b'), ('a', 'c'), ('a', 'g'), ('b', 'a'), ('b', 'd'), ('c', 'a'),
     ('c', 'd'), ('c', 'e'), ('d', 'b'), ('d', 'c'), ('d', 'f'), ('e', 'c'),
     ('e', 'f'), ('e', 'g'), ('f', 'd'), ('f', 'e'), ('f', 'h'), ('g', 'a'),
     ('g', 'e'), ('h', 'f')]

vertice = bus_ancho(E, 'a')
print(vertice)