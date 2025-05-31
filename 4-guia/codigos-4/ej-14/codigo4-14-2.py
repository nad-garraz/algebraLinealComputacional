import numpy as np

A = np.array(
    # Matriz de Markov P
    [[0.25, 0.5, 0.5, 0.5],
     [0.25, 0.5, 0, 0],
     [0.25, 0, 0.5, 0],
     [0.25, 0, 0, 0.5]]
)

# No importa el estado inicial, de donde partas, siempre llegás al equilibrio
v = np.array([20, 0, 0, 0]) # Estado inicial
#v = np.array([5, 5, 5, 5])

hasta_estado = 10
for i in range(hasta_estado + 1):
    print(f"v{i}: {v}")
    if i <= hasta_estado:
        v = A @ v # Estado siguiente
