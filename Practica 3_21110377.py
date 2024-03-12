
def reinas(fila):
    def conflicto(k):
        for i in range(1, k):
            if fila[i] == fila[k] or abs(fila[i] - fila[k]) == abs(i - k):
                return True
        return False

    k = 1  
    fila[1] = 0 
    while k > 0:
        fila[k] = fila[k] + 1  
        while fila[k] <= 4 and conflicto(k):
            fila[k] = fila[k] + 1  
        if fila[k] <= 4:
            if k == 4:
                return True  
            else:  
                k = k + 1
                if k <= 4:
                    fila[k] = 0  
        else:  
            k = k - 1

    return False  


fila = [0, 0, 0, 0, 0]  
solucion = reinas(fila)

if solucion:
    print("posicion de la primera reina, fila 1, columna", fila[1],
          "\nposicion de la segunda reina, fila 2, columna", fila[2],
          "\nposicion de la tercera reina, fila 3, columna", fila[3],
          "\nposicion de la cuarta reina, fila 4, columna", fila[4]) 
else:
    print("No hay solución")
"""
    [ ,X, , ] 2
    [ , , ,X] 4
    [X, , , ] 1
    [ , ,X, ] 3
"""
