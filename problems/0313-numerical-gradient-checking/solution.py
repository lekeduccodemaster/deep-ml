import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    h = epsilon
    grad = [0.0] * len(x)
    for i in range(len(x)):
        original_xi = x[i]
        x[i] = original_xi + h
        fxh = f(x) 

        x[i] = original_xi - h
        fx = f(x) 

        grad[i] = (fxh - fx) / (2 * h)
    analytical_grad = np.array(analytical_grad)
    grad = np.array(grad)
    tmp = analytical_grad - grad 
    p = np.linalg.norm(tmp)
    q = np.linalg.norm(grad) + np.linalg.norm(analytical_grad)
    if abs(q) <= epsilon:
        return 0.0
    p = p/q
    return (grad, p)

    pass