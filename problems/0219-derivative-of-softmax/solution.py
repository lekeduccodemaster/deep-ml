import numpy as np
import math
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	n = len(x)
	sm = 0
	for i in range(len(x)):
		sm += math.exp(x[i])
	s = []
	for i in range(len(x)):
		tmp = math.exp(x[i]) / sm
		s.append(tmp)
	matrix = np.zeros((n, n), dtype=float)
	for i in range(n):
		for j in range(n):
			if i != j:
				matrix[i][j] = -s[i] * s[j]
			else:
				matrix[i][j] = s[i] * (1 - s[i])
	return matrix
	pass