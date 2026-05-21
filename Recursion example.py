name = input("Enter your name: ")

count = 0
def to_greet(name):
    global count  # here global is used becoz nmae is defined outside the function

    if count == 5:
        return
    count += 1
    print("Hello \t" + name)
    to_greet(name)

to_greet(name)    