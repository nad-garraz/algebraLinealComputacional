import numpy as np

# Quiero darle el input n y p y que devuelva la matriz
# de transición del proceso.


def generar_matriz_transicion(n, p):
    orden_matriz = n + 2
    matriz_transicion = np.zeros((orden_matriz, orden_matriz))
    matriz_transicion[0][0] = 1
    matriz_transicion[orden_matriz - 1][orden_matriz - 1] = 1

    for col in range(1, orden_matriz - 1):
        row = col - 1
        matriz_transicion[row][col] = 1 - p
        matriz_transicion[row + 2][col] = p
                                               # [1  0.5  0    0    0    0    0]
    return matriz_transicion                   # [0  0    0.5  0    0    0    0]
                                               # [0  0.5  0    0.5  0    0    0]
print(generar_matriz_transicion(5, 0.5)) # ->  # [0  0    0.5  0    0.5  0    0]
                                               # [0  0    0    0.5  0    0.5  0]
                                               # [0  0    0    0    0.5  0    0]
                                               # [0  0    0    0    0    0.5  1]
