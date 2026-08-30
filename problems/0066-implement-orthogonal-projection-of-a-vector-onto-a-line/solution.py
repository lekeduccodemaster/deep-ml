import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	n = len(v)
	tu = 0
	mau = 0
	for i in range(n):
		tu += v[i] * L[i]
		mau += L[i] * L[i]
	scalar = tu / mau 
	L = np.array(L)
	return scalar * L
	pass
