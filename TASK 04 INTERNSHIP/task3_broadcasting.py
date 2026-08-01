import numpy as np

# Example 1: Add a scalar to an array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

print("\nAdding 5 to each element:")
print(arr + 5)

# Example 2: Add a 1D array to each row of a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("\n2D Matrix:")
print(matrix)

print("\n1D Vector:")
print(vector)

print("\nBroadcasting Result (Matrix + Vector):")
print(matrix + vector)

# Example 3: Multiply every element by 2
print("\nMultiply Matrix by 2:")
print(matrix * 2)