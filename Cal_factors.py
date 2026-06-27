# def cal_factors(n):
#     result =[]
#     for i in range(1,n+1):
#         if n%i == 0:
#             result.append(i)
#     return result

# n =  int(input("Enter a number: "))
# print(cal_factors(n))

def cal_factors(n):
    from math import sqrt
    result=[]
    for i in range(1, int(sqrt(n)+ 1)):
        if n%i == 0:
            result.append(i)
            if n//i != i:
                result.append(n//i)
                result.sort()
    return result

n =  int(input("Enter a number: "))
print(cal_factors(n))

# def cal_factors(n):
#     result =[]
#     for i in range(1,n//2 + 1):
#         if n%i == 0:
#             result.append(i)
#             result.append(n)
#     return result

# n =  int(input("Enter a number: "))
# print(cal_factors(n))
