import numpy as np

# Ingresar matriz
A = np.array([[3, 2], [0, 1], [6, 8]])
tamanio = A.shape
print(f"A=\n{A}\nCantidad de filas: {tamanio[0]}\nCantidad de columnas: {tamanio[1]}")

# método de numpy
print(f"Forma Numpy: tr(A) = {np.trace(A)}")

# ====================METODO 2====================
# A manopla
contar_hasta = min(A.shape[0], A.shape[1])
elemento = 0
traza = 0

while elemento < contar_hasta:
    traza += A[elemento][elemento]
    elemento += 1

print(f"Forma a manopla: tr(A) = {traza}")
