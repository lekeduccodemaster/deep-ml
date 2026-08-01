import numpy as np
import math

def swap(A: np.ndarray, u, v):
    m = len(A)
    n = len(A[0])
    tmp = []
    for i in range(n):
        tmp.append(A[u][i])
    for i in range(n):
        A[u][i] = A[v][i]
    for i in range(n):
        A[v][i] = tmp[i]

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    A = A.astype(float)
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    m = len(A)
    n = len(A[0])
    current_pivot_row = 0
    for i in range(n):
        mx = tol
        pos = -1
        for j in range(current_pivot_row, m):
            if abs(A[j][i]) > mx:
                mx = abs(A[j][i])
                pos = j
        if pos == -1:
            continue
        swap(A, current_pivot_row, pos)
        for j in range(current_pivot_row + 1, m):
            if A[current_pivot_row][i] != 0:
                cst = A[j][i] / A[current_pivot_row][i] 
                for k in range(n):
                    A[j][k] = A[j][k] - cst * A[current_pivot_row][k]
        current_pivot_row += 1
    return current_pivot_row
    pass