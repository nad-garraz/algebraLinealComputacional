import numpy as np
import matplotlib.pyplot as plt

# Nuestra Matriz
M = np.array([[0.5,0.5],[0.5,0.5]]) 

# Genero 15 puntos aleatorios
# de distancia 1 al origen. También  15 puntos
# a distancia 3 del origen.

V = np.random.rand(2, 15) - 0.5
V_uni = V/np.linalg.norm(V, axis = 0)
V_3 = 3*V/np.linalg.norm(V, axis = 0)

# Multiplico la matriz por todos esos vectoes
# para ver el efecto
MV_uni = M @ V_uni
MV_3 = M @ V_3

# Ploteo dos figuras, una para radio 1 y otra para radio 3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(V_uni[0], V_uni[1], label="v_uni")
ax1.scatter(MV_uni[0], MV_uni[1], label="Av_uni")
ax1.legend()
ax1.set_aspect('equal') # aspect ratio para que se vea cuadradito
ax2.set_title('Puntos que distan 1 del origen y su transformación con A')

ax2.scatter(V_3[0], V_3[1], label="v_3")
ax2.scatter(MV_3[0], MV_3[1], label="Av_3")
ax2.legend()
ax2.set_aspect('equal') # aspect ratio para que se vea cuadradito
ax2.set_title('Puntos que distan 3 del origen y su transformación con A')

# plt.tight_layout()
plt.show()
