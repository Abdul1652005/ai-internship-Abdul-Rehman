import numpy as np

# 1. One-Dimensional Array
array1 = np.array([10, 20, 30, 40, 50])
print("One-Dimensional Array:")
print(array1)

# 2. Two-Dimensional Array
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\nTwo-Dimensional Array:")
print(array2)

# 3. Array of Zeros
zeros = np.zeros((2, 3))
print("\nArray of Zeros:")
print(zeros)

# 4. Array of Ones
ones = np.ones((3, 2))
print("\nArray of Ones:")
print(ones)

# 5. Identity Matrix
identity = np.eye(3)
print("\nIdentity Matrix:")
print(identity)

# 6. Array using arange()
arange_array = np.arange(1, 11)
print("\nArray using arange():")
print(arange_array)

# 7. Array using linspace()
linspace_array = np.linspace(0, 1, 5)
print("\nArray using linspace():")
print(linspace_array)

# 8. Random Array
random_array = np.random.randint(1, 100, (3, 3))
print("\nRandom Array:")
print(random_array)