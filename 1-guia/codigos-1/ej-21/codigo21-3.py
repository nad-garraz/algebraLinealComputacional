import numpy as np

# Ingresar matriz
A = np.array([[3, 2], [3, 6], [-6, -8]])
tamanio = A.shape
print(f"A=\n{A}\nCantidad de filas: {tamanio[0]}\nCantidad de columnas: {tamanio[1]}")

# Oneliner falopa listas por comprensión.
resultado = sum([sum(fila) for fila in A]);

if (resultado > 0):
    respuesta = True
else:
    respuesta = False

print(f"Ganan los positivos? Respuesta: {respuesta}")
