import numpy as np
import matplotlib.pyplot as plt

A = np.array( [
            [20 - 4 * np.sqrt(5), 20 + 4 * np.sqrt(5), 20 + 2 * np.sqrt(5)],
            [40 + 2 * np.sqrt(5), 20 - 2 * np.sqrt(5), 40 + np.sqrt(5)]
            ])
#
total_puntos = 500

V = np.random.rand(3, total_puntos) - 0.5  # circunferencia unitaria
V_uni = V / np.linalg.norm(V, axis=0)
AV_uni = A @ V_uni
# print(AV_uni)

## TikZ-----------------------------------------------
np.savetxt(
    f"../../ejercicios-5/dataFiles/17-ej-data/circulo.data",
    np.transpose([V_uni[0], V_uni[1], V_uni[2]]),
    fmt="%.2e",
    header="circulo y producto por matriz",
    comments="# SVD circulo unitario",
)
np.savetxt(  # matriz A
    f"../../ejercicios-5/dataFiles/17-ej-data/matrizDotCirculo.data",
    np.transpose([AV_uni[0], AV_uni[1], np.zeros(total_puntos)]),
    fmt="%.2e",
    header="circulo y producto por matriz",
    comments="# SVD Matriz por circulo unitario",
)
## -----------------------------------------------
fig, ax1 = plt.subplots(1, 1, figsize=(12, 5))
ax1.scatter(V_uni[0], V_uni[1], V_uni[2], label="v_uni")
ax1.scatter(AV_uni[0], AV_uni[1], label="Av_uni")
ax1.legend()
ax1.grid()
ax1.set_aspect("equal")  # aspect ratio para que se vea cuadradito
plt.show()
