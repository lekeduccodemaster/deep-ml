import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	n = len(X)
	x_mean = np.mean(X, axis = 0)
	x_center = X - x_mean 
	std_x = np.std(X, axis=0, ddof=1)
	if Y is None:
		cov = (x_center.T @ x_center) / (n - 1)
		tmp = np.outer(std_x, std_x)
	else:
		std_y = np.std(Y, axis=0, ddof=1)
		y_mean = np.mean(Y, axis = 0)
		y_center = Y - y_mean 
		cov = (x_center.T @ y_center) / (n - 1)
		tmp = np.outer(std_x, std_y)
	return cov/tmp
	pass