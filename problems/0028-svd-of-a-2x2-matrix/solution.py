import numpy as np

def eigenvalues_2x2(A: np.ndarray) -> np.ndarray:
    """
    Compute the eigenvalues of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        eigenvalues: 1D array of eigenvalues
    """
    # Your code here
    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]
    
    # Characteristic polynomial: λ^2 - (a+d)λ + (ad - bc) = 0
    trace = a + d
    determinant = a * d - b * c
    
    # Calculate eigenvalues using the quadratic formula
    discriminant = trace**2 - 4 * determinant
    if discriminant < 0:
        raise ValueError("Matrix has complex eigenvalues.")
    
    lambda1 = (trace + np.sqrt(discriminant)) / 2
    lambda2 = (trace - np.sqrt(discriminant)) / 2
    
    return np.array([lambda1, lambda2])

def get_eigenvector(B: np.ndarray, lambda_val: float) -> np.ndarray:
    """
    Tính vector riêng chuẩn hóa cho một trị riêng cụ thể của ma trận 2x2.
    """
    m11 = B[0, 0] - lambda_val
    m12 = B[0, 1]
    
    # Xử lý trường hợp ma trận đường chéo (m12 rất nhỏ, gần bằng 0)
    if abs(m12) < 1e-10:
        if abs(m11) < 1e-10:
            return np.array([1.0, 0.0])
        else:
            return np.array([0.0, 1.0])
            
    # Công thức tìm vector: m11*x + m12*y = 0 => x = m12, y = -m11
    u = np.array([m12, -m11])
    
    # Chuẩn hóa vector (chia cho độ dài của nó)
    norm = np.sqrt(u[0]**2 + u[1]**2)
    return u / norm

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # Your code here
    B = A @ A.T
    eigenvals = eigenvalues_2x2(B)
    s = np.sqrt(eigenvals)
    # 2. Tìm ma trận U (chứa các vector riêng của B)
    u1 = get_eigenvector(B, eigenvals[0])
    u2 = get_eigenvector(B, eigenvals[1])
    
    # Ma trận U được tạo bằng cách xếp u1 và u2 thành các cột
    # np.column_stack ghép 2 mảng 1D thành các cột của mảng 2D
    U = np.column_stack((u1, u2))

    # 3. Tìm ma trận V (chứa các vector suy biến phải)
    
    # Xử lý v1: Áp dụng công thức v = (1/s) * A^T * u
    # Cần kiểm tra s > 0 để tránh lỗi chia cho 0
    if s[0] > 1e-10:
        v1 = (1 / s[0]) * (A.T @ u1)
    else:
        v1 = np.array([1.0, 0.0]) # Mặc định nếu ma trận suy biến hoàn toàn
        
    # Xử lý v2 tương tự
    if s[1] > 1e-10:
        v2 = (1 / s[1]) * (A.T @ u2)
    else:
        # Trong trường hợp s2 = 0, ta không thể chia được.
        # Nhưng theo tính chất trực giao, v2 phải vuông góc với v1.
        v2 = np.array([-v1[1], v1[0]])
        
    # Ghép v1, v2 thành các cột của ma trận V
    V = np.column_stack((v1, v2))
    V = V.T  # Chuyển vị để V có dạng đúng
    return U, s, V
    

#U, s, V = svd_2x2(np.array([[-10, 8], [10, -1]]))
#result = U @ np.diag(s) @ V
#print(svd_2x2(np.array([[-10, 8], [10, -1]])))