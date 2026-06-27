def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num*factorial(num - 1)

n = int(input("Enter a number to compute its factorial: "))
print(factorial(n))