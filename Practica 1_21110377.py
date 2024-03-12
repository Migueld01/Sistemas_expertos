
def busqueda(nodo, grafo, vis):
    vis.add(nodo)
    orden = [nodo]

    for a in grafo[nodo]:
        if a not in vis:
            orden.extend(busqueda(a, grafo, vis))

    return orden

def bus_profundidad(E, ni):
    grafo = {}
    
    for u, v in E:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)

    vis = set()
    vertices= busqueda(ni, grafo, vis)

    return vertices

E = [('a', 'b'), ('a', 'c'), ('a', 'g'), ('b', 'a'), ('b', 'd'), ('c', 'a'),
     ('c', 'd'), ('c', 'e'), ('d', 'b'), ('d', 'c'), ('d', 'f'), ('e', 'c'),
     ('e', 'f'), ('e', 'g'), ('f', 'd'), ('f', 'e'), ('f', 'h'), ('g', 'a'),
     ('g', 'e'), ('h', 'f')]

vertices = bus_profundidad(E, 'a')
print(vertices)
