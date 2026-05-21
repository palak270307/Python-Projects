import numpy as np
marks = np.array([[47,70,93],[88,95,100],[76,85,90],[45,55,65],[90,92,94]])
good_scores = marks[marks > 80]

high_scores = np.where(marks > 80, marks, 0)
print("High Scores with condition:\n", high_scores)
print("Good Scores:\n", good_scores)

