import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

# Indexing
print("\nFirst Element:", arr[0])
print("Last Element:", arr[-1])

# Slicing
print("\nElements from index 1 to 4:")
print(arr[1:5])

# Create a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(matrix)

# Accessing elements in 2D array
print("\nElement at Row 1, Column 2:", matrix[0, 1])

# Reshaping
new_array = np.arange(1, 13)
reshaped = new_array.reshape(3, 4)

print("\nOriginal Array:")
print(new_array)

print("\nReshaped Array (3x4):")
print(reshaped)

# Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray A:", a)
print("Array B:", b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)

print("\nSquare of A:")
print(a ** 2)