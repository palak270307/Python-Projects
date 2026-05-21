import numpy as np

marks = np.array([
    [78, 85, 90],
    [60, 70, 75],
    [88, 92, 95],
    [45, 50, 55],
    [72, 80, 68]
])
# Calculate the average marks for each student
avg_marks=(np.mean(marks,axis=1))
print("Average marks for each student:\n",avg_marks)
 # Calculate the average marks for each subject
avg_subject_marks=(np.mean(marks,axis=0))
print("Average marks for each subject:\n",avg_subject_marks)
# Calculate highest total scorer
total_marks=(np.sum(marks,axis=1))
highest_scorer=(np.argmax(total_marks))    #argmax returns the index of the maximum value in the array, which corresponds to the student with the highest total marks.
print("Highest total scorer:\n",highest_scorer)
#Students scoring greater than 200
std_abv_200=(total_marks[total_marks>200])
print("Students scoring greater than 200:\n",std_abv_200)
print(np.where(total_marks>200))
#Add 5 grace marks to everyone
grace_marks=total_marks + 5
print("Total marks after adding grace marks:\n",grace_marks)