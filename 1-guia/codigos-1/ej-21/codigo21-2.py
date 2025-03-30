import numpy as np

# Ingresar matriz
A = [[3, 2], [0, 1], [6, 8]]
cantidad_filas = len(A)
cantidad_columnas = len(A[0])
print(
    f"A=\n{A}\nCantidad de filas: {cantidad_filas}\nCantidad de columnas: {cantidad_columnas}"
)

# ====================METODO 1====================
# inicializo los índices
fila = 0
columna = 0
suma_elementos = 0

while fila < cantidad_filas:
    while columna < cantidad_columnas:
        suma_elementos += A[fila][columna]
        columna += 1  # actualizo las columnas
    columna = 0  # reseteo las columnas
    fila += 1  # actualizo las filas

print(f"Suma de elementos a manopla: {suma_elementos}")

# ====================METODO 2====================
# Con listas por comprensión. Oneliner falopa,
suma_total_oneliner = sum([sum(fila) for fila in A])
print(f"Suma de elementos oneliner: {suma_total_oneliner}")
