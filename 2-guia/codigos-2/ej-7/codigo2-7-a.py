import numpy as np

epsilon = np.finfo(float).eps

print(f"epsilon = {epsilon}")   # epsilon = 2.220446049250313e-16

p = 1e34 # p = 10000000000000000000000000000000000
q = 1

calculo = p + q - p # calculo = 0

print(f"p = {p}\nq = {q}\np + q - p = {calculo}")
