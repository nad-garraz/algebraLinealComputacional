import numpy as np

c_BE = np.array([[-1,-1,1], [1,0,1], [0,1,1]])

c_EB = np.linalg.inv(c_BE)

P = np.array([[-1,-1,0], [1,0,0], [0,1,0]])
p_ee = P@c_EB
p_bb = c_EB@P

# print(c_BE)
# print(c_EB)
print(p_bb)
# print(f"pop: {p_ee@p_ee}")
print(f"popbb: {p_bb@p_bb}")
