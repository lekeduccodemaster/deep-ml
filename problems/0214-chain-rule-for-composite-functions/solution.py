import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    # Your code here
    dx = 1
    # Đổi 0 thành -1 để vòng lặp chạy đến hết index 0 của mảng
    for i in range(len(functions) - 1, -1, -1):
        if functions[i] == 'square':
            dx = (2 * x) * dx
            gx = x**2
            x = gx 

        elif functions[i] == 'sin':
            dx = math.cos(x) * dx
            gx = math.sin(x)
            x = gx 

        elif functions[i] == 'exp':
            dx = math.exp(x) * dx
            gx = math.exp(x)
            x = gx

        else:
            dx = (1 / x) * dx 
            gx = math.log(x)
            x = gx 
            
    return dx
    pass