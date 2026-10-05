import numpy as np
from collections import Counter
import math

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    if strategy == 'most_frequent':
        nmx = max(y_train)
        dem = [0] * (nmx + 1)
        for i in range(len(y_train)):
            dem[y_train[i]] += 1
        res = 0
        kq = 0 # Khởi tạo kq để tránh lỗi nếu y_train rỗng
        for i in range(nmx + 1):
            if dem[i] > res:
                res = dem[i]
                kq = i 
        return [kq] * n_test
        
    elif strategy == 'constant':
        return [constant] * n_test
        
    elif strategy == 'uniform':
        unique_y_train = list(set(y_train))
        k = len(unique_y_train)
        arr = [0] * n_test
        for i in range(n_test):
            arr[i] = y_train[i % k]
        return arr
        
    else: # Nhánh xử lý cho "stratified"
        n_train = len(y_train)
        classes = sorted(list(set(y_train)))
        
        allocations = {}
        fractional_parts = {}
        allocated_total = 0
        
        # Bước 1 & 2: Tính tỷ lệ và phân bổ phần nguyên
        for c in classes:
            count_c = y_train.count(c)
            f_c = count_c / n_train
            
            exact_alloc = n_test * f_c
            base_alloc = math.floor(exact_alloc) 
            
            allocations[c] = base_alloc
            fractional_parts[c] = exact_alloc - base_alloc
            allocated_total += base_alloc
            
        # Bước 3: Xác định số lượng còn thiếu và phân bổ dựa trên phần thập phân
        remaining = n_test - allocated_total
        
        # Sắp xếp để ưu tiên: phần thập phân lớn nhất -> nhãn lớp nhỏ nhất
        sorted_classes = sorted(classes, key=lambda c: (-fractional_parts[c], c))
        
        for i in range(remaining):
            c = sorted_classes[i]
            allocations[c] += 1
            
        # Bước 4: Tạo list kết quả theo đúng thứ tự nhãn
        predictions = []
        for c in classes:
            predictions.extend([c] * allocations[c])
            
        return predictions