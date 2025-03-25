import numpy as np
import matplotlib.pyplot as plt

# Matriz del ejercicio

A = [[1, 1, 1], [4, 2, 1], [9, 3, 1]]
b = [1, 2, 0]

# Resuelvo el sistema A x = b, y lo devuelvo en
# las variables con los nombres adecuados
a, b, c = np.linalg.solve(A, b)

xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])

x = np.linspace(0, 4, 100)  # genera100 puntos equiespaciados entre 0 y 4.

f = lambda t: a * t**2 + b * t + c

plt.plot(xx, yy, "*")
plt.plot(x, f(x))
plt.show()
