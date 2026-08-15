def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	sum_e = 0
	for i in range(len(priors)):
		sum_e += (priors[i] * likelihoods[i])
	result = []
	for i in range(len(priors)):
		perc = (priors[i] * likelihoods[i]) / sum_e
		result.append(perc)
	return result
	pass