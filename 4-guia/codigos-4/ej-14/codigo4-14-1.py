import numpy as np
# Matriz de Markov P
A = np.array(
    [[0.25, 0.5, 0.5, 0.5],
     [0.25, 0.5, 0, 0],
     [0.25, 0, 0.5, 0],
     [0.25, 0, 0, 0.5]]
)

print(np.linalg.eig(A)[0]) # autovalores --> [-0.25  1.    0.5   0.5 ]
print(np.linalg.eig(A)[1]) # autovectores:
                           # [-8.66e-01  7.55e-01 -1.81e-16  0.00e+00]
                           # [ 2.88e-01  3.77e-01 -8.16e-01  0.00e+00]
                           # [ 2.88e-01  3.77e-01  4.08e-01 -7.07e-01]
                           # [ 2.88e-01  3.77e-01  4.08e-01  7.07e-01]
