import numpy as np

def matrixmul(A: list[list[int|float]], B: list[list[int|float]]):
    ma = len(A)
    na = len(A[0])
    mb = len(B)
    nb = len(B[0])
    if na != mb:
        return -1
    C = np.zeros((ma, nb))
    for i in range(ma):
        for j in range(nb):
            sum_val = 0  # Đổi tên biến sum thành sum_val để tránh trùng từ khóa sum của Python
            for t in range(na):
                sum_val += A[i][t] * B[t][j]
            C[i][j] = sum_val
    return C 

