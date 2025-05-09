import numpy as np

L_tilde = np.array([[1,0,0],[0.5,1,0],[-.5, 1.5, 1]])
D_sqrt = np.array([[2,0,0],[0,2,0],[0, 0, 1]])
L_chole = L_tilde @ D_sqrt

print(f"A=LL_traspuesta=\n{L_chole@np.transpose(L_chole)}")
#    [4 2 -2]
# = [2 5  5]
#   [-2 5 11]
