def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m = len(matrix)
	n = len(matrix[0])
	res = []
	if mode == 'column':
		for j in range(n):
			sum = 0
			for i in range(m):
				sum += matrix[i][j]
			res.append(sum / m)
	else:
		for i in range(m):
			sum = 0
			for j in range(n):
				sum += matrix[i][j]
			res.append(sum / n)
	return res