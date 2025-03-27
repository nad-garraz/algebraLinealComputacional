import numpy as np

# Matriz del ejercicio
A = np.array([[-1,2,1],[1,0,-1],[1,1,3]])
b = [1, 1, 0]

# Resuelvo el sistema A x = b, y lo devuelvo en
# las variables con los nombres adecuados
a, b, c = np.linalg.solve(A, b)

print(f"a = {a}\nb = {b}\nc = {c}")
