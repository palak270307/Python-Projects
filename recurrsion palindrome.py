num = input("Enter a string: ")
def rec_palindrome(num):
    if len(num) <= 1:
        return True
    if num[0] == num[-1]:
        return rec_palindrome(num[1:-1])
    return False
print(rec_palindrome(num))