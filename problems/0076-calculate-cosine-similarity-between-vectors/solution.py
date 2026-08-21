import numpy as np
import math
def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	len_v1 = 0
	for elements in v1:
		len_v1 += elements**2
	len_v1 = math.sqrt(len_v1)
	len_v2 = 0
	for elements in v2:
		len_v2 += elements**2
	len_v2 = math.sqrt(len_v2)
	ans = len_v1 * len_v2 
	tu = 0
	for i in range(len(v1)):
		tu += v1[i] * v2[i]
	return tu/ans
	pass