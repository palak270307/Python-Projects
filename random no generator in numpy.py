import numpy as np

# rng = np.random.default_rng()
# # print(rng.integers(low=1, high=101,size=5))
# print(rng.integers(low=1, high=101,size=(3,4)))

# rng = np.random.default_rng()
# array =np.array([10,20,30,40,50,60,70,80,90,100])
# rng.shuffle(array)
# print("Shuffled Array:\n", array)

rng = np.random.default_rng()
subjects = np.array(["Mathematics", "Physics", "Chemistry", "Biology", "English"])
subject = rng.choice(subjects,size=1)
print("Randomly Selected Subject:", subject)