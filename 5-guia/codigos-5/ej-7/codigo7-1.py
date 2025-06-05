import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4, 0], [3, 5]])
A_inv = 0.05 * np.array([[5, 0], [-3, 4]]) 
# H = np.transpose(A) @ A
# # H2 = A @ np.transpose(A)
#
# print(np.linalg.eig(H))
#
# print(1 / np.sqrt(2))
# print("============")
# v = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
# v2 = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
# print(A @ v2)

# Nuestra Matriz
V = np.random.rand(2, 200) - 0.5 # circunferencia unitaria
V_uni = V / np.linalg.norm(V, axis=0)
AV_uni = A @ V_uni
A_invV_uni = A_inv @ V_uni
print(np.linalg.svd(A_inv))

## Genero data para poder hacer el gráfico en TiKz
## -----------------------------------------------
# np.savetxt(
#     f"../../ejercicios-5/dataFiles/7-ej-data/item-circulo.data",
#     np.transpose([V_uni[0], V_uni[1]]),
#     fmt="%.10e",
#     header="circulo y producto por matriz",
#     comments="# SVD circulo unitario",
# )
#
# np.savetxt( # matriz A
#     f"../../ejercicios-5/dataFiles/7-ej-data/item-matrizDotCirculo.data",
#     np.transpose([AV_uni[0], AV_uni[1]]),
#     fmt="%.10e",
#     header="circulo y producto por matriz",
#     comments="# SVD Matriz por circulo unitario",
# )
# np.savetxt( # matriz A inversa
#     f"../../ejercicios-5/dataFiles/7-ej-data/item-matrizInvDotCirculo.data",
#     np.transpose([A_invV_uni[0], A_invV_uni[1]]),
#     fmt="%.10e",
#     header="circulo y producto por matriz inversa",
#     comments="# SVD Matriz inversa por circulo unitario",
# )
## -----------------------------------------------

# Ploteo dos figuras, una para radio 1 y otra para radio 3
fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
ax1.scatter(V_uni[0], V_uni[1], label="v_uni")
ax1.scatter(AV_uni[0], AV_uni[1], label="Av_uni")
ax1.legend()
ax1.grid()
ax1.set_aspect("equal")  # aspect ratio para que se vea cuadradito
plt.show()
