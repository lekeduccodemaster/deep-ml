def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    mn = min(x)
    mx = max(x)
    x2 = x
    for i in range(len(x)):
        x2[i] = (x2[i] - mn) / (mx - mn)
    return x2
    pass