import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g = 0
    dg = 0
    for i in range(len(g_coeffs)):
        index = len(g_coeffs) - i - 1
        g += g_coeffs[i] * x**index 
        dg += g_coeffs[i] * index * x**max(0,index-1)
    h = 0
    dh = 0
    for i in range(len(h_coeffs)):
        index = len(h_coeffs) - i - 1
        h += h_coeffs[i] * x**index 
        dh += h_coeffs[i] * index * x**max(0,index-1)
    return (dg * h - dh * g) / (h**2)
    pass