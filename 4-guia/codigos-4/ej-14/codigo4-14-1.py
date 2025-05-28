import numpy as np
# Matriz de Markov P
A = np.array(
    [[0.25, 0.5, 0.5, 0.5],
     [0.25, 0.5, 0, 0],
     [0.25, 0, 0.5, 0],
     [0.25, 0, 0, 0.5]]
)

print(np.linalg.eig(A)[0]) # autovalores --> [-0.25  1.    0.5   0.5 ]
print(np.linalg.eig(A)[1]) # autovectores
