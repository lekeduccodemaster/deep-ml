import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	res = np.linalg.det(matrix)
	n = len(matrix)
	sum = 0
	for i in range(n):
		sum += matrix[i][i]
	return (res, sum)
	pass