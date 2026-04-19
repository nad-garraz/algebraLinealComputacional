import numpy as np

def Lyb(matriz, resultado):
    y = np.zeros((len(matriz), 1))
    y[0] = resultado[0]
    for i in range(1, len(matriz)):
        y[i] = resultado[i] - matriz[i] @ y
    return y
