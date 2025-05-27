import numpy as np
# Matriz de Markov P
A = np.array(
    [[0.25, 0.25, 0.25, 0.25],
     [0.25, 0.75, 0, 0],
     [0.25, 0, 0.75, 0],
     [0.25, 0, 0, 0.75]]
)
print(np.linalg.eig(A)[0]) # autovalores --> [0 1 0.75 0.75]
