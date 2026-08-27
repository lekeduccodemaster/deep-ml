import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]
    dct = {}
    dct['mean'] = np.mean(data)
    dct['median'] = np.median(data)
    dct['mode'] = mode
    dct['variance'] = np.var(data)
    dct['standard_deviation'] = np.std(data)
    dct['25th_percentile'] =  np.percentile(data, 25)
    dct['50th_percentile'] =  np.percentile(data, 50)
    dct['75th_percentile'] =  np.percentile(data, 75)
    dct['interquartile_range'] = dct['75th_percentile'] - dct['25th_percentile'] 
    return dct
    pass