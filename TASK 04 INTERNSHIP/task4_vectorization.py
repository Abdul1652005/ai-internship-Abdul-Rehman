import numpy as np
import time

# Create a large NumPy array
arr = np.arange(1, 1000001)

# -------------------------------
# Traditional Loop
# -------------------------------
start = time.time()

result_loop = []
for i in arr:
    result_loop.append(i * 2)

end = time.time()

print("Loop Time:")
print(end - start, "seconds")

# -------------------------------
# Vectorized Operation
# -------------------------------
start = time.time()

result_vector = arr * 2

end = time.time()

print("\nVectorized Operation Time:")
print(end - start, "seconds")

# Display first 10 elements
print("\nFirst 10 Elements (Loop):")
print(result_loop[:10])

print("\nFirst 10 Elements (Vectorized):")
print(result_vector[:10])