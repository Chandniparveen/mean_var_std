import numpy as np
def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix_3 = np.array(lst).reshape(3, 3)
    
    calculations = {
        'mean': [matrix_3.mean(axis=0).tolist(), matrix_3.mean(axis=1).tolist(), matrix_3.mean().tolist()],
        'variance': [matrix_3.var(axis=0).tolist(), matrix_3.var(axis=1).tolist(), matrix_3.var().tolist()],
        'standard deviation': [matrix_3.std(axis=0).tolist(), matrix_3.std(axis=1).tolist(), matrix_3.std().tolist()],
        'max': [matrix_3.max(axis=0).tolist(), matrix_3.max(axis=1).tolist(), matrix_3.max().tolist()],
        'min': [matrix_3.min(axis=0).tolist(), matrix_3.min(axis=1).tolist(), matrix_3.min().tolist()],
        'sum': [matrix_3.sum(axis=0).tolist(), matrix_3.sum(axis=1).tolist(), matrix_3.sum().tolist()]
    }
    
    return calculations

print(calculate([0, 1, 2, 3, 4, 5,6,7, 8]))
