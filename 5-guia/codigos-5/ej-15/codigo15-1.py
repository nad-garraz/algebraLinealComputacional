import numpy as np

A = np.array([[1, 4, 0], [-4, -1, 0], [0, 0, 2]])
U = np.array([[1, -1, 0], [-1, -1, 0], [0, 0, np.sqrt(2)]])
V = np.array([[1, 1, 0], [1, -1, 0], [0, 0, np.sqrt(2)]])
S = np.array([[5, 0, 0], [0, 3, 0], [0, 0, 2]])
S_1 = np.array([[5, 0, 0], [0, 3, 0], [0, 0, 0]])
S_2 = np.array([[5, 0, 0], [0, 0, 0], [0, 0, 0]])
H = np.transpose(A) @ A

# print(np.linalg.eig(H))
# avas = np.linalg.eig(H)
print(U @ S_1 @ np.transpose(V))
print(U @ S_2 @ np.transpose(V))
# print(U @ S @ np.transpose(V))
