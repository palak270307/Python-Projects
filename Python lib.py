import numpy as np
# a=np.array([1,2,3,4])
# print(a)

# b=np.array([[1,2,3,4],[1,2,3,4]])
# print(b)

# print(type(a))
# print(type(b))

# print(a.shape)
# print(b.shape)

# np.zeros(5) 
# np.ones(5)
# np.full((2,3),5)
# np.arange(0,10)
# np.linspace(0,10,5)

## Exercise 1 ##
# a=np.array([10,20,30,40,50])
# print(a)
# print(type(a))

# b=np.array([[1,2],[3,4],[5,6]])
# print(b)
# print(b.shape)
# print(type(b))
# print(np.zeros(4))
# print(np.arange(5,16,1))

## Exercise 2 ##
# a = np.array([5, 10, 15, 20, 25, 30])
# print(a[0])
# print(a[-1])
# print(a[0:5])

# b = np.array([[10, 20, 30],
#                 [40, 50, 60],
#                 [70, 80, 90]])
# print(b[1,1])
# print(b[1])
# print(b[0:,2])

## Exercise 3 ##
# x = np.array([5, 10, 15])
# y = np.array([2, 4, 6])
# print(x+y)
# print(y-x)
# print(x*y)
# print(x/y)
# print(np.sum(x))
# print(np.mean(x))
# print(np.max(x))
# print(np.min(x))

## Exercise 4 ##
# print(np.random.rand(5))
# print(np.random.rand(3,3))
# print(np.random.randint(10,50,4))
# np.random.seed(1)
# print(np.random.rand(3))

## Exercise 5 ##
# a = np.array([10,20,30,40,50,60])
# print(a.reshape(2,3))

# b = np.array([[1,2,3],
#                 [4,5,6]])
# print(b.flatten())

# c = np.array([1,2,3,4,5,6,7,8])
# print(c.reshape(4,2))

## Exercise 6 ##
# a = np.array([5, 12, 18, 25, 30, 40])
# print(a[a>20])
# print(a[(a>10) & (a<30)])

# b = np.array([[10, 15, 20],
#                 [25, 30, 35]])
# print(b[b>20])
# print(b[b<30])

## Exercise 7 ##
x = np.array([10,20,30])
y = np.array([40,50,60])
print(np.vstack((x,y)))
print(np.hstack((x,y)))
print(np.column_stack((x,y)))  ##bascically we did transpose

m1 = np.array([[1,2],
               [3,4]])

m2 = np.array([[5,6],
               [7,8]])
print(np.vstack((m1,m2)))
print(np.hstack((m1,m2)))