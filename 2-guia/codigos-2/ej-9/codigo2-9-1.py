import numpy as np

epsilon = 0.001

# La matriz a resolver A:
A = np.array([[1, 2, 1],\
              [2, 3 - epsilon, 2 + epsilon],\
              [0, 1 + epsilon, epsilon]])
b = np.array([0,0.1,0.1])

# Que lo resuelva python
x, y, z = np.linalg.solve(A, b)          # x = -100.0000000000055   
print(f"x = {x}\ny = {y}\nz = {z}")      # y = -5.50397778192042e-15
                                         # z = 100.00000000000551   

# Solución mantisa 3 floating point corroboración:
X = np.array([-200, -0.1, 200])
print(f"Corroborar cuentas de punto flotante\nA X = {A @ X}")  
        #A X = [-0.2    -0.0999  0.0999]

# Solución exacta a mano corroboración:
X = np.array([-100, 0, 100])
print(f"Corroborar las cuentas horribles esas\nA X = {A @ X}")
        # A X = [0.  0.1 0.1]
