import numpy as np
import math 

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    n = len(X_train)
    m = len(X_train[0])
    X_test_scaled = X_test.astype(float)
    for i in range(m):
        mean = 0
        std = 0
        for j in range(n):
            mean += X_train[j][i]
        mean /= n 
        for j in range(n):
            std += ((X_train[j][i] - mean) ** 2)
        if std == 0:
            std = 1
        else:
            std /= n
            std = math.sqrt(std)
        for j in range(len(X_test)):
            X_test_scaled[j][i] = (X_test_scaled[j][i] - mean) / std 
    return X_test_scaled
    pass
