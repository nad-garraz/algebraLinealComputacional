import numpy as np

# Matriz del ejercicio
A = np.array([[1-1j, 2], [1j, -1 + 1j]])
b = [0, 0]

print(A)

# Resuelvo el sistema A x = b, y lo devuelvo en
# las variables con los nombres adecuados
alpha, beta = np.linalg.solve(A, b)

print(f"alpha = {alpha}\nbeta = {beta}")
