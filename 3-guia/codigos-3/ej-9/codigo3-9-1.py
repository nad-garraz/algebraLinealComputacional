import numpy as np

L_tilde = np.array([[1,0,0],[0.5,1,0],[-.5, 1.5, 1]])
U = np.array([[4,2,-2],[0,4,6],[0, 0, 1]])

print(f"L_tilde U=\n{L_tilde@U}")
#    [ 4 2 -2]
#  = [ 2 5  5]
#    [-2 5 11]
