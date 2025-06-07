import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4, 14], [8, -19], [20, -10]])
At = np.transpose(A)
H = np.transpose(A) @ A
#
# print(np.linalg.eig(H))
# print(np.linalg.svd(A))
#
V = np.random.rand(2, 500) - 0.5  # circunferencia unitaria
V_uni = V / np.linalg.norm(V, axis=0)
AV_uni = A @ V_uni
print(AV_uni)
## TikZ-----------------------------------------------
np.savetxt(
    f"../../ejercicios-5/dataFiles/9-ej-data/circulo.data",
    np.transpose([V_uni[0], V_uni[1], np.zeros(500)]),
    fmt="%.10e",
    header="circulo y producto por matriz",
    comments="# SVD circulo unitario",
)
np.savetxt(  # matriz A
    f"../../ejercicios-5/dataFiles/9-ej-data/matrizDotCirculo.data",
    np.transpose([AV_uni[0], AV_uni[1], AV_uni[2]]),
    fmt="%.10e",
    header="circulo y producto por matriz",
    comments="# SVD Matriz por circulo unitario",
)
## -----------------------------------------------
# Ploteo dos figuras, una para radio 1 y otra para radio 3
fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
ax1.scatter(V_uni[0], V_uni[1], label="v_uni")
ax1.scatter(AV_uni[0], AV_uni[1], label="Av_uni")
ax1.legend()
ax1.grid()
ax1.set_aspect("equal")  # aspect ratio para que se vea cuadradito
# plt.show()
