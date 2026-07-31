def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	x = len(a)
	y = len(a[0])
	z = len(b)
	c = []
	if(y != z):
		return -1
	for i in range(x):
		sum = 0
		for j in range(y):
			sum += a[i][j] * b[j]
		c.append(sum)
	return c
	pass