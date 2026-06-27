# num = int(input())

# if num > 13:
#     print("Number is greater than  13")
# elif num==13:
#     print("Number is equal to 13")   
# else:
#     print("Number is smaller than 13")

# num = int(input())
# if num >= 0:
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Negative")


# x = int(input("Enter your age:"))
# if x >= 18:
#     print("You're eligible to vote")

# else:
#     print("You're not eligible to vote")

# n = int(input("Enter a number:"))

# for i in range(1,n-1):
#     print(i)

# for i in range(1,n*1):
#     print(i)    

# for i in range(1,n*2):
#     print(i)

# n = input("Enter your Favourite Flower: ")
# for i in n:
#     print(i)

# i = 0
# while (i < 7):
#     i += 1
#     print("Helloooooo")
 

# n = int(input("Enter a number:"))
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end=" ")

#         print("")


# for i in range(1, 6):
#     print("*" * i)

        
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
