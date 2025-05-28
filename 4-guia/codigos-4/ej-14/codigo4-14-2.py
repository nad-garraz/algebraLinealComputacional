import numpy as np

A = np.array(
    # Matriz de Markov P
    [[0.25, 0.5, 0.5, 0.5],
     [0.25, 0.5, 0, 0],
     [0.25, 0, 0.5, 0],
     [0.25, 0, 0, 0.5]]
)

v = np.array([20, 0, 0, 0])
k = 10 
for i in range(10):
    print(f"v{i}: {v}")
    if i <= 10:
        v = A @ v
