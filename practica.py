def dijkstra(w, a, z):
    L = {vertex: float('inf') for vertex in w}
    L[a] = 0

    T = set(w)
    prev = {vertex: None for vertex in w}

    while T:
        v = min(T, key=lambda vertex: L[vertex])
        T.remove(v)

        for x in w[v]:
            if L[x] > L[v] + w[v][x]:
                L[x] = L[v] + w[v][x]
                prev[x] = v

    # Construir la ruta
    path = []
    current = z
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return L[z], path

w = {
    'casa': {'periferico': 2, 'zapopan': 1},
    'periferico': {'casa': 2, 'acueducto': 10, 'mercado del mar': 2, 'patria': 4},
    'acueducto': {'periferico': 2, 'patria': 3, 'ceti': 1},
    'mercado del mar': {'periferico': 2, 'patria': 4, 'zapopan': 3},
    'patria': {'periferico': 4, 'acueducto': 3, 'mercado del mar': 4, 'americas': 7},
    'zapopan': {'casa': 1, 'mercado del mar': 3, 'americas': 5},
    'americas': {'patria': 7, 'zapopan': 5, 'ceti': 6},
    'ceti': {'acueducto': 1, 'americas': 6}
}

a = 'casa'
z = 'ceti'
longitud, ruta = dijkstra(w, a, z)

print(f"La ruta más corta para llegar de casa al ceti es: {ruta}")

