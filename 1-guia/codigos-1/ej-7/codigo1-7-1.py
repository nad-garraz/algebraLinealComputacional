import numpy as np

# Matriz del ejercicio
A = np.array([[1,0,-3],[1,1,-1],[1,0,-1]])
b = [0, 0, 0]

# Resuelvo el sistema A x = b, y lo devuelvo en
x, y, z = np.linalg.solve(A, b)

print(f"x = {x}\ny = {y}\nz = {z}")
