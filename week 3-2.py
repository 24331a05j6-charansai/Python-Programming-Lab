import numpy as np
a = np.ndarray(shape=(3, 3), dtype=int)
a[:] = [[10, 20, 30], [40, 50, 60],   [70, 80, 90]]         
print("The elements of matrix 1:\n", a)
print("Dimension of matrix 1 is:", a.ndim)
b = np.ndarray(shape=(3, 3), dtype=int)
b[:] = [[100, 120, 140],[160, 180, 200], [130, 150, 190]]          
print("The elements of matrix 2:\n", b)
print("Dimension of matrix 2 is:", b.ndim)
print("Addition of two matrices is:\n", np.add(a, b))
print("Subtraction of two matrices is:\n", np.subtract(a, b))
print("Multiplication of two matrices is:\n", np.dot(a, b))
print("Division of two matrices is:\n", np.divide(a, b))
