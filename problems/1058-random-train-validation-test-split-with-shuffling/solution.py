import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n = len(data)
    rows = np.random.default_rng(seed).permutation(n)
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)
    train = []
    for i in range(train_end):
        train.append(data[rows[i]])
    train = np.array(train)
    validation = []
    for i in range(train_end, validation_end):
        validation.append(data[rows[i]])
    validation = np.array(validation)
    test = []
    for i in range(validation_end, n):
        test.append(data[rows[i]])
    test = np.array(test)
    return train, validation, test
    pass