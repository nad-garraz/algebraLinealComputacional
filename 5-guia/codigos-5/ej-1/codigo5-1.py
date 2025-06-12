import numpy as np

A = np.array([[13, 8, 8], [-1, 7, -2], [-1, -2, 7]])
U = np.array([[-2/np.sqrt(5), -2/(3*np.sqrt(5)), 1/3], [1/np.sqrt(5), -4/(3*np.sqrt(5)), 2/3], [0, 5/(3*np.sqrt(5)), 2/3]])
U2 =np.array([[-6, -2, np.sqrt(5)],
                [3, -4, 2*np.sqrt(5)],
              [0, 5, 2*np.sqrt(5)]])
T = np.array([[9,0,-9/np.sqrt(5)],[0,9,-9/np.sqrt(5)],[0,0,9]])
v = np.array([1/3,2/3,2/3])
v1 = np.array([-2/(3*np.sqrt(5)),-4/(3*np.sqrt(5)),5/(3*np.sqrt(5))])

print( (1/45) * np.transpose(U2) @ A @ U2)
# print(U @ T @ np.transpose(U))
print((np.transpose(U) @ A @ v1))
# print(np.linalg.eig(A)[0])
