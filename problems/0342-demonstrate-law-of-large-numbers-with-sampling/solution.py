import numpy as np
import math

def law_of_large_numbers(n_samples: int, population_mean: float, population_std: float) -> float:
    """
    Demonstrate the Law of Large Numbers by computing the sample mean.
    
    Args:
        n_samples: Total number of samples to draw from the distribution
        population_mean: The true mean of the population distribution
        population_std: The true standard deviation of the population distribution
    
    Returns:
        The sample mean
    """
    data = np.random.normal(loc=population_mean, scale=population_std, size=n_samples)
    # Your code here
    return np.mean(data)
    pass