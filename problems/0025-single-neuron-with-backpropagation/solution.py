import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	mse_values = []
	n_samples = len(features)
	for _ in range(epochs):
		z = np.dot(features, initial_weights) + initial_bias
		a = 1 / (1 + np.exp(-z))
		mse = np.mean((a - labels) ** 2)

		mse_values.append(round(mse, 4))
		# 1. Đạo hàm của Loss theo a: dL/da = 2 * (a - y) 
		# (Lưu ý: Công thức gốc có chia cho N, nhưng ta sẽ để dành việc chia N ở bước tính dw và db cho gọn)
		dL_da = 2 * (a - labels)

		# 2. Đạo hàm của a theo z (Hàm Sigmoid): da/dz = a * (1 - a)
		da_dz = a * (1 - a)

		# 3. Gom lại theo quy tắc chuỗi: dz = dL/da * da/dz
		dz = dL_da * da_dz

		# 4. Tìm đạo hàm của trọng số (dw) và bias (db) tính trung bình cho toàn batch
		dw = np.dot(features.T, dz) / n_samples
		db = np.sum(dz) / n_samples

		initial_weights -= learning_rate * dw
		initial_bias -= learning_rate * db

	updated_weights = np.round(initial_weights, 4)
	updated_bias = np.round(initial_bias, 4)
	return updated_weights, updated_bias, mse_values