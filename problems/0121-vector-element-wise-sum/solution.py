import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	a = np.array(a)
	b = np.array(b)
	try:
		c = a + b 
		return c
	except Exception:
		return -1
	pass