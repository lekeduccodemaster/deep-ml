import numpy as np
import math
def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	res = {}
	s = 0
	for elements in gradient:
		s += elements**2
	s = math.sqrt(s)
	res['magnitude'] = s
	direction = []
	for elements in gradient:
		if s!=0:
			tmp = abs(elements/s)
			direction.append(tmp)
		else:
			direction.append(0)
	res['direction'] = direction
	des = []
	for i in range(len(direction)):
		if gradient[i] > 0:
			des.append(-1 * direction[i])
		else:
			des.append(direction[i])
	res['descent_direction'] = des
	return res
	pass