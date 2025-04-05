import numpy as np

epsilon = np.finfo(float).eps

print(f"epsilon = {epsilon}")   # epsilon = 2.220446049250313e-16

p = 100
q = 1e-15

calculo1 = (p + q) + q 
calculo2 = ((p + q) + q) + q
calculo3 = p + 2*q
calculo4 = p + 3*q


print(f"p = {p}\nq = {q}")
print(f"(p + q) + q = {calculo1}")
print(f"((p + q) + q) + q = {calculo2}")
print(f"p + 2q = {calculo3}")
print(f"p + 3q = {calculo4}")
