import numpy as np

def simulate_dice_sum(num_rolls, seed=0):
    #empirical probability
    rng = np.random.RandomState(seed)
    dice1 = rng.randint(low = 1, high = 7, size = num_rolls)
    dice2 = rng.randint(low = 1, high = 7, size = num_rolls)
    rolls_sum = dice1 + dice2
    counts = np.bincount(rolls_sum, minlength=13)[2:]
    empirical_result = counts / num_rolls
    #theoretical probability
    theoretical_result = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], dtype = float)
    theoretical_result = theoretical_result / 36.0
    return (empirical_result, theoretical_result)