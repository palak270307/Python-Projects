def count_digits(n):
    count = 0
    num = n
    while num > 0:
        count += 1
        num = num // 10
    return count

n = int(input("Enter a number: "))
print(count_digits(n))