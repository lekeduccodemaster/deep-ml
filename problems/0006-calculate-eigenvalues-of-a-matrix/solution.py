import math
def calculate_eigenvalues(mx: list[list[float|int]]) -> list[float]:
	tr = mx[0][0] + mx[1][1]
	det = mx[0][0] * mx[1][1] - mx[0][1] * mx[1][0]
	delta = tr * tr - 4 * det 
	eigenvalues = []
	if delta > 0:
		a = (tr - math.sqrt(delta)) / 2
		b = (tr + math.sqrt(delta)) / 2
		eigenvalues.append(a)
		eigenvalues.append(b)
	elif delta == 0:
		a = tr / 2
		eigenvalues.append(a)
	eigenvalues.sort()
	eigenvalues.reverse()
	return eigenvalues