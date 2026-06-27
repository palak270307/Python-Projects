import matplotlib.pyplot as plt
import pandas as pd

# Line Graphs
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
# plt.plot(x,y)
# plt.show()
# plt.title("Line Graph")
# plt.show()
# plt.xlabel("X axis")
# plt.show()
# plt.ylabel("Y axis")
# plt.show()
# plt.plot(x,y,color="red",marker="o",linestyle="dashed")
# plt.show()

# Bar Graphs
names = ["A", "B", "C"]
marks = [85, 90, 78]
# plt.bar(names, marks)
# plt.title("Student Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()

# Pie Charts
labels = ["Python", "Java", "C++"]
sizes = [50, 30, 20]
# plt.pie(sizes,labels=labels,autopct="%1.1f%%")
# plt.title("Programming Languages")
# plt.show()

subjects=["Science","Maths","English","Social Studies","Hindi","Marathi"]
marks=[19,20,19,19,18,18]
# plt.pie(marks,labels=subjects,startangle=90,autopct="%1.1f%%",explode=[0.1,0,0,0,0,0])
# plt.title("Subject-wise Marks")
# plt.show()

# Histogram
data = [10, 20, 20, 30, 30, 30, 40]
# plt.hist(data, bins=5, edgecolor="black")
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# Scatter Plot
x = [1,2,3,4]
y = [10,15,13,17]
# plt.scatter(x,y,color="Blue",marker="x")
# plt.title("Scatter Plot")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.show()

plt.plot([1,2,3], [10,20,30], label="Line 1")
plt.plot([1,2,3], [30,20,10], label="Line 2")
# plt.legend()
# plt.title("Multiple Lines")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.show()

# plt.subplot(1, 2, 1)
# plt.plot([1,2,3], [10,20,30])

# plt.subplot(1, 2, 2)
# plt.plot([1,2,3], [30,20,10])

# plt.show()

plt.plot(x, y)
plt.grid()
plt.show()