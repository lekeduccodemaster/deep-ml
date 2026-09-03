import math
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	dct = {}
	# Your code here
	sm_x = 1/(1 + math.exp(-x))
	dct['sigmoid'] = sm_x * (1 - sm_x)
	tnh = 1 - math.tanh(x)**2
	dct['tanh'] = tnh 
	if x <= 0:
		rl = 0
	else:
		rl = 1
	dct['relu'] = rl 
	return dct
	pass