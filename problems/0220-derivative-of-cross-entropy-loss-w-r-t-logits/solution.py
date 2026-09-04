import math 
def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	sm = 0
	for i in range(len(logits)):
		sm += math.exp(logits[i])
	s = []
	for i in range(len(logits)):
		tmp = math.exp(logits[i])
		s.append(tmp / sm) 
	s[target] -= 1
	return s
	pass