def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    cnta = 0
    for first, second in data:
      if first == x:
        cnta += 1
    cntb = 0
    for first, second in data:
      if first == x and second == y:
        cntb += 1
    if cnta > 0: 
      return cntb / cnta
    else:
      return 0.0
    pass