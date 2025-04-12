import numpy as np
import matplotlib.pyplot as plt  # librería para graficar.

# ...
# Acá , crear la matriz y resolver el sistema para calcularl a , b y c.
# ...

xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])

x = np.linspace(0, 4, 100)  # genera100 puntos equiespaciados entre 0 y 4.
f = lambda t: a * t**2 + b * t + c  # esto genera una función f de t.
plt.plot(xx, yy, "*")
plt.plot(x, f(x))
plt.show()
