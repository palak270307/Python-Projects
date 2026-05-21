# import numpy as np

# radii = np.array([1,2,3,4])
# areas = np.pi *radii ** 2
# print("Radii:", radii)
# print("Areas:", areas)

import numpy as np
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
# areas = array1 * array2
# print("Area Of rectangles.", areas)

# scores = np.array([90, 85, 78, 92, 88])
# average_score = np.mean(scores)
# average_score = np.median(scores)
# average_score = np.std(scores)

# print("average score:", average_score)
# print(scores > average_score)
# print(scores> 80)

array1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
array2 = np.array([[7],[8],[9]])

print(array1.shape)
print(array2.shape)
print("Array1 * Array2:\n", array1 * array2)  # Broadcasting in action