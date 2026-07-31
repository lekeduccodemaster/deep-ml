import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	# Your code here
	matrix = []
	if degree < 0:
		return matrix
	for i in range(len(data)):
		tmp = []
		tmp.append(1.0)
		x = data[i]
		for j in range(0, degree):
			tmp.append(tmp[-1] * x)
		matrix.append(tmp)
	return matrix
	pass