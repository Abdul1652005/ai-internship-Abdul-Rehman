import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 1. Dot Product
dot_product = np.dot(A, B)
print("\nDot Product:")
print(dot_product)

# 2. Matrix Multiplication
matrix_product = A @ B
print("\nMatrix Multiplication:")
print(matrix_product)

# 3. Transpose
transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)

# 4. Inverse
inverse_A = np.linalg.inv(A)
print("\nInverse of Matrix A:")
print(inverse_A)