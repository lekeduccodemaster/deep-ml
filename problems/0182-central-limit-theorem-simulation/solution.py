import numpy as np
import math

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    np.random.seed(seed)
    # Your implementation here
    res = {}
    try:
        if distribution == 'exponential':
            ex = np.random.exponential(1.0, size=(runs, n))
            mu = 1.0
            sigma = 1.0 
            sample_means = np.mean(ex, axis = 1)
            z = (sample_means - mu) / (sigma / math.sqrt(n))
            res['mean'] = np.mean(z)
            res['std'] = np.std(z)
        elif distribution == 'uniform':
            ex = np.random.uniform(0, 1, size=(runs, n))
            mu = 0.5
            sigma = math.sqrt(1/12)
            sample_means = np.mean(ex, axis = 1)
            z = (sample_means - mu) / (sigma / math.sqrt(n))
            res['mean'] = np.mean(z)
            res['std'] = np.std(z)
        elif distribution == 'bernoulli':
            ex = (np.random.rand(runs, n) < 0.3).astype(float) 
            mu = 0.3 
            sigma = math.sqrt(0.3 * 0.7) 
            sample_means = np.mean(ex, axis = 1)
            z = (sample_means - mu) / (sigma / math.sqrt(n))
            res['mean'] = np.mean(z)
            res['std'] = np.std(z)
        return res
    except:
        raise ValueError
    pass