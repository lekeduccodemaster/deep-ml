import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Jacobian matrix using numerical differentiation.
    """
    # 1. Chuyển x thành Numpy array để an toàn cho mọi phép toán bên trong hàm f
    x_arr = np.array(x, dtype=float)
    
    # 2. Đánh giá hàm f tại điểm x và chuyển kết quả thành Numpy array
    f_x = np.array(f(x_arr))
    
    n = len(x_arr)
    m = len(f_x) 
    
    # 3. Khởi tạo ma trận Jacobian chứa toàn số 0 với kích thước m x n
    J = np.zeros((m, n))
    
    # 4. Tính toán sai phân
    for j in range(n):
        x_plus_h = x_arr.copy()
        x_plus_h[j] += h
        
        # Đánh giá hàm tại x + h
        f_x_plus_h = np.array(f(x_plus_h))
        
        # Tính đạo hàm riêng và gán trực tiếp vào cột j của ma trận J
        # Numpy cho phép trừ 2 mảng trực tiếp thay vì phải lặp qua từng phần tử
        J[:, j] = (f_x_plus_h - f_x) / h
        
    # 5. Làm tròn và chuyển đổi lại thành list of lists theo yêu cầu của Type Hint
    return np.round(J, 4).tolist()