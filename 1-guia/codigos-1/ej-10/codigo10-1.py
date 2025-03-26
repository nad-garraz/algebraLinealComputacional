import numpy as np

# Matriz del ejercicio

A = [[1, 4, -1, 3], [2, 1, -3, 1], [0, 2, 1, -5, 1]]
b = [0, 0, 0, 0]

print(A)

# Resuelvo el sistema A x = b, y lo devuelvo en
# las variables con los nombres adecuados
a1, b1, c1 = np.linalg.solve(A, b)
