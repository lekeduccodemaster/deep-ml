import numpy as np
import math

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    for element in vectors:
        ck = False
        for i in range(len(element)):
            if element[i] != 0:
                ck = True
                break
        if ck == False:
            return False
    vectors.sort()
    com = 1
    for element in vectors:
        com = math.lcm(com, element[0])
    for i in range(len(vectors)):
        if vectors[i][0] != 0:
            scalar = com / vectors[i][0]
        else:
            scalar = 1
        for j in range(len(vectors[i])):
            vectors[i][j] *= scalar
    for j in range(1, len(vectors)):
        for i in range(0, j):
            if vectors[i] == vectors[j]:
                return False 
    return True
    pass