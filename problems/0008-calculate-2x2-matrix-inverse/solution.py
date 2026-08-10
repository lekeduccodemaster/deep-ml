import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    try:
        matrix = np.array(matrix)
        matrix_inv = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "None"
    return matrix_inv
    pass