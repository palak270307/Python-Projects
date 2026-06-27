import random
print("Enter your list of tasks(comma-seperated):  ")
# Asks the user to type their tasks separated by commas (,)
user_input= input("👉 ")

#Splits the input string into a list using commas.
tasks = user_input.split(",") 
print("Enter the no. of tasks you can do: ")
n = int(input())

#Removes extra spaces around each task (strip()).
#Ignores empty entries (in case user adds extra commas)
tasks = [task.strip() for task in user_input.split(",") if task.strip()]

# Creates a dictionary task is a key and value is r.v btw 0.6 to 0.95.
probabilities = {task: round(random.uniform(0.6, 0.95), 2) for task in tasks}


def prob_tasks(tasks,n):
    if n > len(tasks):
        return 1
    return n/len(tasks)
print("The probability of doing any task is :", prob_tasks(tasks,n))

print("\n📊 Estimated Effectiveness Probabilities:")
for task, prob in probabilities.items():
    emoji = "✅" if prob > 0.8 else "⚠️"
    print(f"{emoji} {task}: {prob*100}%")

    # prob of completing any task in that function.
    print(f"Probability of completing {task}: {prob_tasks([task], n)}")
    print()