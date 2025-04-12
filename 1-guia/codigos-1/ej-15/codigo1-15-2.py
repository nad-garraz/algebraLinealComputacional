import numpy as np

# Matriz del ejercicio
A = np.array([[-1,2,1],[1,0,-1],[1,1,3]])
b = [1, 1, 0]

a1, b1, c1 = np.linalg.solve(A, b)
print(f"a1 = {a1}\nb1 = {b1}\nc1 = {c1}\n")

b = [0, 1, 1]
a2, b2, c2 = np.linalg.solve(A, b)
print(f"a2 = {a2}\nb2 = {b2}\nc2 = {c2}\n")

b = [1, 0, 1]
a3, b3, c3 = np.linalg.solve(A, b)
print(f"a3 = {a3}\nb3 = {b3}\nc3 = {c3}\n")

