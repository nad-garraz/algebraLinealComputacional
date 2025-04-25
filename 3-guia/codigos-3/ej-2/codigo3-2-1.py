import numpy as np
import scipy

# Matriz A
A = np.array([[1, -1, 0, 1], [0, 1, 4, 0], [2, -1, 0, -2], [-3, 3, 0, -1]])
L = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [2, 1, 1, 0], [-3, 0, 0, 1]])
U = np.array([[1, -1, 0, 1], [0, 1, 4, 0], [0, 0, -4, -4], [0, 0, 0, 2]])
b = np.array([[1],[-7],[-5],[1]])

print(f"A =\n {A}")
print(f"L =\n {L}")
print(f"U =\n {U}")

print(f"\nA == LU --> {np.array_equal(A,L @ U)}")
print(f"Ax = b  -->  x = {np.transpose(np.linalg.solve(A,b))}")
