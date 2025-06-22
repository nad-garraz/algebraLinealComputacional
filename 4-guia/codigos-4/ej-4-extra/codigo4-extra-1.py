import numpy as np

A = np.array([[0.8, 0.1, 0.3], [0.2, 0.8, 0.3], [0, 0.1, 0.4]])

v_0 = np.array([0.3, 0.34, 0.36])

v_eq = np.array([-0.59473674,  0.79410449, -0.47596315])
v_eq = np.abs(v_eq / np.sum(np.abs(v_eq)))

print(f"El eq: {v_eq}")
print(f"El A @ eq: {A @ v_eq}")
# v_eq = np.abs(v_eq / np.linalg.norm([-0.59473674,  0.79410449, -0.47596315],1))

print(f"El 13 de agosto: {A @ v_0}")
print(f"El 22 de octubre: {A @ A @ v_0}")

print(f"El eq normalizado: {v_eq}")
print(f"El eq: {A @ v_eq}")
print(f"Autovalores de a: {np.linalg.eig(A)}")
