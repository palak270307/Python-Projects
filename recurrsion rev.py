num=list(input("Enter a string: "))
def rev(num,left,right):
    if left >= right:
        return num
    num[left], num[right] = num[right], num[left]
    return rev(num, left + 1, right - 1)
# call the function with proper indices
print(rev(num, 0, len(num) - 1))