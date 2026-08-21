import numpy as np
import math

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        mx = 0
        for elements in arr:
            mx = mx + abs(elements)
        return mx
    elif norm_type == "l2":
        mx = 0
        for elements in arr:
            mx = mx + elements**2
        return math.sqrt(mx)
    else:
        mx = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                mx += arr[i][j]*arr[i][j]
        return math.sqrt(mx)
    pass