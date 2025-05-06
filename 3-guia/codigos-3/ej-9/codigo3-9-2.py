import numpy as np

L_tilde = np.array([[1,0,0],[0.5,1,0],[-.5, 1.5, 1]])
D = np.array([[4,0,0],[0,4,0],[0, 0, 1]])

print(f"D L_tilde_traspuesta=\n{D@np.transpose(L_tilde)}")   
#   [4 2 -2]
# = [0 4 6]                                                                
#   [0 0 1]
