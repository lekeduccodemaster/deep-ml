import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]):
    try:
        T = np.array(T)
        S = np.array(S)
        A = np.array(A)
        T_inv = np.linalg.inv(T)
        S_inv = np.linalg.inv(S)
        A_dash = A @ S  
        A_dash = T_inv @ A_dash
    except np.linalg.LinAlgError:
        return -1
    return A_dash