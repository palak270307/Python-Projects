def check_palindrome(n):
    result = 0
    num = n
    while num > 0:
        ld = num % 10
        result = (result * 10) + ld 
        num = num // 10
    return result == n

n = int(input("Enter a number: "))
print(check_palindrome(n))
