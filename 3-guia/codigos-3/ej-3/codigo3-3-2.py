def Uxy(matriz, resultado):
    dim = len(matriz)
    x = np.zeros((dim, 1))
    x[dim - 1] = resultado[dim - 1] / matriz[dim - 1][dim - 1]
    for i in range(dim - 2, -1, -1):
        x[i] = (resultado[i] - matriz[i] @ x) / matriz[i][i]
    return x
