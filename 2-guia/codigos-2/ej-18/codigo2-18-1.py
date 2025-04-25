import numpy as np
import matplotlib.pyplot as plt

# Nuestra Matriz de 3 x 3
A = np.array([[0.1, 3, 9], [0.01, 0.1, 0.1], [89, 0.1, 0]])

s_k = 0
sucesion = [s_k]
x_k = np.array([0, 0, 0])

for k in range(1, 101):
    x = np.random.rand(3, 1) - 0.5
    # Vectores en r 3 con  de norma = 1
    x_k = x / np.linalg.norm(x, axis=0)

    Ax_k = A @ x_k
    norma_Ax_k = np.linalg.norm(Ax_k, axis=0)
    s_k = max(s_k, norma_Ax_k)
    sucesion.append(s_k)


# Printeo el resultado
for i in range(0, 100):
    print(f"término k = {i} --> {sucesion[i]}")

# Ploteo dos figuras, una para radio 1 y otra para radio 3
fig, ax1 = plt.subplots(1)

ax1.scatter(V_uni[0], V_uni[1], label="v_uni")
ax1.scatter(MV_uni[0], MV_uni[1], label="Av_uni")
ax1.legend()
ax1.set_aspect('equal') # aspect ratio para que se vea cuadradito
ax2.set_title('Puntos que distan 1 del origen y su transformación con A')


# plt.tight_layout()
plt.show()
