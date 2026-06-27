import numpy as np

## Exercise 1 ##
# a=[5,10,15,20,25,30,35,40]
# print(np.max(a))
# print(np.min(a))

# b=[2,4,4,6,8,8,10]
# print(np.unique(b))

# c=[45,12,89,33,21]
# print(np.sort(c))

# d=[5,15,25,35,45]
# print(np.clip(d,10,30))

# print(np.linspace(0,50,6))

## Exercise 2##
# a=np.array([5, 10, 15, 20, 25, 30])
# print(a[a>15])
# print(a[(a>10)&(a<25)])
# a[a>20] = 0
# print(a)

# b=np.array([[12, 45, 33],
#             [20, 55, 18],
#             [40, 22, 60]])
# print(b[b>30])

## Exercise 3 ##
# a=np.array([2, 4, 6, 8])
# print(a+10)

# c = np.array([1, 2, 3])
# d = np.array([10, 20, 30])
# print(c+d)

# e=np.array([[1,2,3],
#            [4,5,6]])
# vec=np.array([10,20,30])
# print(e+vec)

# f=np.array([[5,10,15],
#  [20,25,30]])
# scale=np.array([2,3,4])
# print(f*scale)

## Exercise 4 ##
# A =np.array([[2,3],
#      [4,5]])

# B = np.array([[1,2],
#      [3,4]])
# print(A@B)

# C = np.array([[1,2,3],
#      [4,5,6]])
# V = np.array([10,20,30])
# print(C@V)

## Exercise 5 ##
# A =np.array([[2,4,6],
#      [1,3,5]])
# print(np.transpose(A))
# print(np.sum(A, axis=0))
# print(np.sum(A, axis=1))

## Exercise 6 ##

a = np.array([5,10,15,20])
b = np.array([1,2,3,4])
print(a+b)
mul_result = a * b
print(mul_result)
print(a*b)
print(a**2)
print(np.sum(mul_result))