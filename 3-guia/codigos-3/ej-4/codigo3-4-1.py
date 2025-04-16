"""
Eliminacion Gausianna
"""

import numpy as np


def elim_gaussiana(A):
    m = A.shape[0]
    n = A.shape[1]
    Ac = A.copy()

    if m != n:
        print("Matriz no cuadrada")
        return


    for i in range(0, n - 1):
        divisor = Ac[i][i]
        for j in range(i, n - 1):
            coef = Ac[j + 1][i] / divisor
            Ac[j + 1][i:] = np.subtract(Ac[j + 1][i:], coef * Ac[i][i:])
            Ac[j + 1][i] = coef


    L = np.tril(Ac, -1) + np.eye(A.shape[0])
    U = np.triu(Ac)

    return L, U

def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n, n)), -1)
    B[:n, n - 1] = 1
    print(f"Matriz B = \n{B}\n")

    L, U = elim_gaussiana(B)

    print(f"Matriz L = \n{L}\n")
    print(f"Matriz U = \n{U}\n")
    print("B = LU? ", "Sí!" if np.allclose(np.linalg.norm(B - L @ U, 1), 0) else "No!")
    print("Norma infinito de U: ", np.max(np.sum(np.abs(U), axis=1)))


if __name__ == "__main__":
    main()
