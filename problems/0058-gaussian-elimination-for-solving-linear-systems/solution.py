import numpy as np

def gaussian_elimination(A, b):
    # Lấy kích thước của hệ phương trình
    n = len(b)
    
    # Tạo bản sao và ép kiểu float để tránh thay đổi biến gốc và lỗi chia số nguyên
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    
    # --- Bước 1 & 2: Partial Pivoting và Forward Elimination ---
    for k in range(n):
        # Tìm chỉ số của hàng có phần tử trị tuyệt đối lớn nhất ở cột k (từ hàng k trở xuống)
        max_row_index = np.argmax(np.abs(A[k:n, k])) + k
        
        # Hoán vị hàng k và hàng max_row_index trong ma trận A và vector b
        A[[k, max_row_index]] = A[[max_row_index, k]]
        b[[k, max_row_index]] = b[[max_row_index, k]]
        
        # Khử các phần tử dưới đường chéo chính
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            # Cập nhật toàn bộ hàng i của A và b
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]
            
    # --- Bước 3: Backward Substitution ---
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # Tính tổng của các tích A[i, j] * x[j] cho các j > i
        # np.dot giúp nhân vô hướng 2 mảng cực kỳ nhanh
        sum_ax = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - sum_ax) / A[i, i]
        
    # Làm tròn nhẹ để tránh các sai số dấu phẩy động siêu nhỏ (tùy chọn)
    return np.round(x, 8).tolist()
