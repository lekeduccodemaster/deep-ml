def determinant_3x3(mx: list[list[int|float]]) -> float:
	a1 = mx[0][0] * mx[1][1] * mx[2][2] + mx[1][0] * mx[2][1] * mx[0][2] + mx[0][1] * mx[1][2] * mx[2][0]
	a2 = mx[0][2] * mx[1][1] * mx[2][0] + mx[0][1] * mx[1][0] * mx[2][2] + mx[1][2] * mx[2][1] * mx[0][0]
	return a1-a2

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	i = 0
	det = 0
	for j in range(0, 4):
		mu = []
		for u in range(0, 4):
			if u == i:
				continue
			mv = [] 
			for v in range(0, 4):
				if v != j:
					mv.append(matrix[u][v])
			mu.append(mv)
		res = (matrix[i][j] * determinant_3x3(mu))
		if j == 0 or j == 2:
			det += res
		else:
			det -= res
	return det
	pass