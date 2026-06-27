import numpy as np

# 1. Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Perform mathematical operations
print("Array + 10:", arr + 10)       # Add 10 to each element
print("Array squared:", arr ** 2)    # Square each element

# 3. Useful functions
print("Mean:", np.mean(arr))         # Average of elements
print("Sum:", np.sum(arr))           # Sum of elements
print("Standard Deviation:", np.std(arr))  # Spread of values

# 4. Multi-dimensional arrays
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)
print("Transpose:\n", matrix.T)      # Flip rows & columns
