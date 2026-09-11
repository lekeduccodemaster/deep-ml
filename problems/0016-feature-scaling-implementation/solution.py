import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mu = np.mean(data, axis = 0)
	sigma = np.std(data, axis = 0)
	standardized_data = (data - mu) / sigma 
	inda = np.argmin(np.sum(data, axis=1))
	indb = np.argmax(np.sum(data, axis=1))
	normalized_data = (data - data[inda]) / (data[indb] - data[inda])
	return standardized_data, normalized_data